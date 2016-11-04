from rest_framework import routers
from django.conf.urls import include, url

from cookbook.apis.views import RecipeViewSet, IngredientViewSet
from cookbook.views import recipes_list
router = routers.SimpleRouter()
router.register(r'recipe', RecipeViewSet)
router.register(r'ingredient', IngredientViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls, app_name='api', namespace='v1')),
    url(r'^recipes-list/$', recipes_list, name='recipes-list')
]
