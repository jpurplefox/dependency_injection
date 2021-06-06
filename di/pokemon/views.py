from django.http import JsonResponse


def can_learn(request, pokemon, api_integration):
    move_name = request.GET.get('move')

    can_learn = api_integration.can_learn(pokemon, move_name)

    return JsonResponse({'can_learn': can_learn})
