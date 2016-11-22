from rest_framework import serializers

from ..models import DIFICULT_CHOICES, Recipe, Ingredient, UsedIngredient
from django.template.defaultfilters import slugify


class b64Image(serializers.ImageField):
    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(b64Image, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension
        return extension


class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    note = serializers.CharField(required=False)
    added_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        ingredient, _ = Ingredient.objects.get_or_create(
            slug=slugify(validated_data.get('name')),
            defaults=validated_data)
        return ingredient


class UsedIngredientSerializer(serializers.Serializer):
    ingredient = IngredientSerializer()
    used = serializers.FloatField()
    unit = serializers.CharField()


class RecipeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    cook_time = serializers.TimeField()
    dificult = serializers.ChoiceField(choices=DIFICULT_CHOICES)
    ingredients = UsedIngredientSerializer(many=True)
    directions = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    pk = serializers.IntegerField(read_only=True)
    image = b64Image(max_length=None, use_url=True)

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients', None)

        recipe = Recipe.objects.create(**validated_data)
        for used_ingredient in ingredients:
            ingredient = used_ingredient.get('ingredient')
            ing_name = ingredient.get('name')
            ing, _ = Ingredient.objects.get_or_create(slug=slugify(ing_name), defaults={"name": ing_name, "note": ingredient.get('note')})
            used_ing = UsedIngredient.objects.create(ingredient=ing, used=used_ingredient.get('used'), unit=used_ingredient.get('unit'))
            recipe.ingredients.add(used_ing)
        return recipe
