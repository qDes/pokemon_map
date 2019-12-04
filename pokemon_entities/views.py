import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import Pokemon

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        for pokemon_entity in pokemon.entity.all():
            add_pokemon(folium_map,
                        pokemon_entity.lat,
                        pokemon_entity.lon,
                        pokemon_entity.pokemon.title,
                        request.build_absolute_uri(pokemon_entity.pokemon.image.url))
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Покемон не найден </h1>")
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon.entity.all():
        add_pokemon(folium_map,
                    pokemon_entity.lat,
                    pokemon_entity.lon,
                    pokemon_entity.pokemon.title,
                    request.build_absolute_uri(pokemon_entity.pokemon.image.url))
    pokemon_render = {
                "pokemon_id": pokemon.id,
                "title_ru": pokemon.title,
                "title_en": pokemon.title_en,
                "title_jp": pokemon.title_jp,
                "img_url": request.build_absolute_uri(pokemon.image.url),
                "description": pokemon.description,
              }
    if pokemon.next_evolution:
        pokemon_render['next_evolution'] = {
                    "title_ru": pokemon.next_evolution.title,
                    "pokemon_id": pokemon.next_evolution.id,
                    "img_url": request.build_absolute_uri(
                        pokemon.next_evolution.image.url),
                     }
    try:
        previous_pokemon = pokemon.previous.get()
        pokemon_render['previous_evolution'] = {
                    "title_ru": previous_pokemon.title,
                    "pokemon_id": previous_pokemon.id,
                    "img_url": request.build_absolute_uri(
                        previous_pokemon.image.url),
                }
    except ObjectDoesNotExist:
        pass
    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon_render})
