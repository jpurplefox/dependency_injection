from django.urls import path

from pokemon.views import can_learn

urlpatterns = [
    path('<str:pokemon>/can_learn', can_learn)
]
