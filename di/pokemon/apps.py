from django.apps import AppConfig

from pokemon import container, views


class PokemonConfig(AppConfig):
    name = 'pokemon'

    def ready(self):
        container.wire(modules=[views])
