import json

from django.test import RequestFactory, TestCase
from django.urls import resolve

from pokemon import container
from pokemon.integrations import Pokemon
from pokemon.views import can_learn


class FakeAPIIntegration:
    def __init__(self, pokemons):
        self.pokemons = pokemons

    def get_pokemon(self, pokemon):
        try:
            return self.pokemons[pokemon]
        except KeyError:
            raise Pokemon.DoesNotExist()


class CanLearnTestCase(TestCase):
    def setUp(self):
        pokemons = {
            'squirtle': Pokemon(moves_can_learn=['bubble']),
            'charmander': Pokemon(moves_can_learn=['ember'])
        }
        self.fake_integration = FakeAPIIntegration(pokemons)

    def test_squirtle_can_learn_bubble(self):
        request = RequestFactory().get('/pokemon/squirtle/can_learn', {'move': 'bubble'})

        with container.api_integration.override(self.fake_integration):
            response = can_learn(request, 'squirtle')
        data = json.loads(response.content)

        self.assertTrue(data['can_learn'])

    def test_squirtle_cannot_learn_ember(self):
        request = RequestFactory().get('/pokemon/squirtle/can_learn', {'move': 'ember'})

        with container.api_integration.override(self.fake_integration):
            response = can_learn(request, 'squirtle')
        data = json.loads(response.content)

        self.assertFalse(data['can_learn'])

    def test_charmander_can_learn_ember(self):
        request = RequestFactory().get('/pokemon/charmander/can_learn', {'move': 'ember'})

        with container.api_integration.override(self.fake_integration):
            response = can_learn(request, 'charmander')
        data = json.loads(response.content)

        self.assertTrue(data['can_learn'])

    def test_unown_king_does_not_exist(self):
        request = RequestFactory().get('/pokemon/unown_king/can_learn', {'move': 'ember'})

        with container.api_integration.override(self.fake_integration):
            response = can_learn(request, 'unown_king')

        self.assertTrue(response.status_code, 404)

    def test_resolve_url_returns_can_learn_view(self):
        match = resolve('/pokemon/squirtle/can_learn')

        self.assertEqual(match.func, can_learn)
