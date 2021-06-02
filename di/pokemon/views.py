from django.http import JsonResponse


def can_learn(request, pokemon):
    return JsonResponse({'can_learn': True})
