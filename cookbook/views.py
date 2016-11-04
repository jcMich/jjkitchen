from django.views.generic import TemplateView


class RecipeListView(TemplateView):
    template_name = 'cookbook/recipes-list.html'

recipes_list = RecipeListView.as_view()
