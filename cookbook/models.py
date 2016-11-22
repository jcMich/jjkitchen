from django.db import models
from django.utils.translation import ugettext_lazy as _

EASY_DIFICULT = 'E'
MEDIUM_DIFICULT = 'M'
HIGHT_DIFICULT = 'D'

DIFICULT_CHOICES = (
    (EASY_DIFICULT, _("Easy")),
    (MEDIUM_DIFICULT, _("Medium")),
    (HIGHT_DIFICULT, _("Difucult"))
)


class Ingredient(models.Model):
    slug = models.SlugField(max_length=100, unique=True, primary_key=True)

    name = models.CharField(max_length=100)
    note = models.CharField(max_length=500, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UsedIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    used = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredient.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes')

    cook_time = models.TimeField(null=True, blank=True)
    dificult = models.CharField(max_length=1, choices=DIFICULT_CHOICES, default=MEDIUM_DIFICULT)

    ingredients = models.ManyToManyField(UsedIngredient)
    directions = models.TextField()

    # marcar como cocinada el dia de elaboracion no el dia de alta de la receta
    cook_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
