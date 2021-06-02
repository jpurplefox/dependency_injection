import requests

from django.http import JsonResponse


def can_learn(request, pokemon):
    move_name = request.GET.get('move')

    response = requests.get('https://pokeapi.co/api/v2/pokemon/squirtle')
    data = response.json()

    for move in data['moves']:
        if move['move']['name'] == move_name:
            can_learn = True
            break
    else:
        can_learn = False

    return JsonResponse({'can_learn': can_learn})
