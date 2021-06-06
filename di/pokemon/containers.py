from dependency_injector import containers, providers

from pokemon.integrations import APIIntegration


class Container(containers.DeclarativeContainer):
    api_integration = providers.Factory(APIIntegration)
