from dependency_injector.wiring import inject, Provide
from django.http import JsonResponse

from pokemon.containers import Container


@inject
def can_learn(request, pokemon_name, api_integration=Provide[Container.api_integration]):
    move_name = request.GET.get('move')

    pokemon = api_integration.get_pokemon(pokemon_name)

    return JsonResponse({'can_learn': pokemon.can_learn(move_name)})
