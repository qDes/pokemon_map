from django.db import models

# your models here
class PokemonEntity(models.Model):
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)


class Pokemon(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='pokemons', null=True)
    coordinate = models.ForeignKey(PokemonEntity, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}"



