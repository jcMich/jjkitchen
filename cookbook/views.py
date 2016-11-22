from django.views.generic import TemplateView


class RecipeListView(TemplateView):
    template_name = 'cookbook/recipes-list.html'


class RecipeDetailView(TemplateView):
    template_name = "cookbook/recipe-detail.html"


recipes_list = RecipeListView.as_view()
recipe_detail = RecipeDetailView.as_view()
