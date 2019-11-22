from django.db import models

# your models here

class Pokemon(models.Model):
    title = models.TextField(blank=True)
    title_en = models.TextField(blank=True)
    title_jp = models.TextField(blank=True)
    image = models.ImageField(upload_to='pokemons', null=True)
    description = models.TextField(blank=True) 
    next_evolution = models.ForeignKey('self', 
                                       on_delete=models.SET_NULL,
                                       related_name='previous',
                                       null=True,
                                       blank=True)
    
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    defence = models.IntegerField(null=True)
    stamina = models.IntegerField(null=True)
