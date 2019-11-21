from django.db import models

# your models here

class Pokemon(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='pokemons', null=True)
    
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
