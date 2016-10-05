from rest_framework import mixins, viewsets, permissions

from .serializers import RecipeSerializer, IngredientSerializer
from ..models import Recipe, Ingredient


class IngredientViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = IngredientSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Ingredient.objects.all()


class RecipeViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = RecipeSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Recipe.objects.all()
