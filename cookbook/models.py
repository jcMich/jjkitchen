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

KILO_UNIT = 'KG'
GRAMO_UNIT = 'GR'
LITRO_UNIT = 'LT'
PIZCA_UNIT = 'PZ'
TROZO_UNIT = 'TR'
HOJAS_UNIT = 'HJ'
RAMA_UNIT = 'RM'
CUADRO_UNIT = 'CD'
PIEZA_UNIT = 'PZ'
UNIDAD_UNIT = "UN"

UNIT_CHOICES = (
    (KILO_UNIT, "Kilo"),
    (GRAMO_UNIT, "Gramo"),
    (LITRO_UNIT, "Litro"),
    (PIZCA_UNIT, "Pizca"),
    (TROZO_UNIT, "Trozo"),
    (HOJAS_UNIT, "Hoja"),
    (RAMA_UNIT, "Rama"),
    (CUADRO_UNIT, "Cuadro"),
    (PIEZA_UNIT, "Pieza"),
    (UNIDAD_UNIT, "Unidad")
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
    unit = models.CharField(max_length=1, choices=UNIT_CHOICES)

    def __str__(self):
        return self.ingredient.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='/')

    cook_time = models.TimeField(null=True, blank=True)
    dificult = models.CharField(max_length=1, choices=DIFICULT_CHOICES, default=MEDIUM_DIFICULT)

    ingredients = models.ManyToManyField(UsedIngredient)
    directions = models.TextField()

    # marcar como cocinada el dia de elaboracion no el dia de alta de la receta
    cook_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
