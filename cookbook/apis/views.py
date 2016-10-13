from rest_framework import mixins, viewsets, permissions

from .serializers import RecipeSerializer, IngredientSerializer
from ..models import Recipe, Ingredient

ACCESS_CONTROL_ALLOW_HEADERS = 'Authorization,Content-Type'
ACCESS_CONTROL_ALLOW_METHODS = 'GET, POST, PUT, PATCH, HEAD, OPTIONS, DELETE'


class CORSAccessControlMixin(object):
    is_options_method_open = True

    def dispatch(self, request, *args, **kwargs):
        response = super(CORSAccessControlMixin, self).dispatch(request, *args, **kwargs)
        try:
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Headers'] = ACCESS_CONTROL_ALLOW_HEADERS
            response['Access-Control-Allow-Methods'] = ACCESS_CONTROL_ALLOW_METHODS
        except TypeError:
            pass
        return response


class IngredientViewSet(CORSAccessControlMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = IngredientSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Ingredient.objects.all()


class RecipeViewSet(CORSAccessControlMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = RecipeSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Recipe.objects.all()
