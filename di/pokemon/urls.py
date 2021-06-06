from functools import partial

from django.urls import path

from pokemon.views import can_learn
from pokemon.integrations import APIIntegration

def inject_api_integration(func):
    api_integration = APIIntegration()
    return partial(func, api_integration=api_integration)

urlpatterns = [
    path('<str:pokemon>/can_learn', inject_api_integration(can_learn))
]
