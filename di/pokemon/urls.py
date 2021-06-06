from functools import partial

from django.urls import path

from pokemon.views import can_learn

urlpatterns = [
    path('<str:pokemon_name>/can_learn', can_learn)
]
