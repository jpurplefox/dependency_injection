from dependency_injector.wiring import inject, Provide
from django.http import JsonResponse

from pokemon.containers import Container
from pokemon.integrations import Pokemon


@inject
def can_learn(request, pokemon_name, api_integration=Provide[Container.api_integration]):
    move_name = request.GET.get('move')

    try:
        pokemon = api_integration.get_pokemon(pokemon_name)
    except Pokemon.DoesNotExist:
        return JsonResponse({}, status=404)

    return JsonResponse({'can_learn': pokemon.can_learn(move_name)})
