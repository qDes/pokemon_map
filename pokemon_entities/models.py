from django.db import models


class Pokemon(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    title_en = models.CharField(default='', blank=True,
                                max_length=100,
                                verbose_name="Название EN")
    title_jp = models.CharField(default='', blank=True,
                                max_length=100,
                                verbose_name="Название JP")
    image = models.ImageField(upload_to='pokemons',
                              verbose_name="Изображение")
    description = models.TextField(default='', blank=True,
                                   verbose_name="Описание")
    next_evolution = models.ForeignKey('self',
                                       on_delete=models.SET_NULL,
                                       related_name='previous',
                                       null=True,
                                       blank=True,
                                       verbose_name="Эволюция")

    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                related_name="entities",
                                verbose_name="Покемон")
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(null=True, blank=True,
                                       verbose_name="Появился в")
    disappeared_at = models.DateTimeField(null=True, blank=True,
                                          verbose_name="Исчезнет в")
    level = models.IntegerField(null=True, blank=True,
                                verbose_name="Уровень")
    health = models.IntegerField(null=True, blank=True,
                                 verbose_name="Здоровье")
    strength = models.IntegerField(null=True, blank=True,
                                   verbose_name="Сила")
    defence = models.IntegerField(null=True, blank=True,
                                  verbose_name="Защита")
    stamina = models.IntegerField(null=True, blank=True,
                                  verbose_name="Стамина")
