from rest_framework import serializers

from ..models import DIFICULT_CHOICES, Recipe, Ingredient, UsedIngredient, UNIT_CHOICES
from django.template.defaultfilters import slugify


class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    note = serializers.CharField(required=False)
    added_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        ingredient, _ = Ingredient.objects.get_or_create(
            slug=slugify(validated_data.get('name')),
            defaults=validated_data)
        return ingredient


class UserIngredientSerializer(serializers.Serializer):
    ingredient = IngredientSerializer()
    used = serializers.FloatField()
    unit = serializers.ChoiceField(choices=UNIT_CHOICES)


class RecipeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    cook_time = serializers.TimeField()
    dificult = serializers.ChoiceField(choices=DIFICULT_CHOICES)
    ingredients = UserIngredientSerializer(many=True)
    directions = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

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
