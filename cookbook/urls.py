from rest_framework import routers
from django.conf.urls import include, url

from cookbook.apis.views import RecipeViewSet, IngredientViewSet

router = routers.SimpleRouter()
router.register(r'recipe', RecipeViewSet)
router.register(r'ingredient', IngredientViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls, app_name='api', namespace='v1')),
]
