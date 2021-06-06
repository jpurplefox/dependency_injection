from django.http import JsonResponse

from pokemon.integrations import APIIntegration


def can_learn(request, pokemon):
    move_name = request.GET.get('move')

    integration = APIIntegration()
    can_learn = integration.can_learn(pokemon, move_name)

    return JsonResponse({'can_learn': can_learn})
