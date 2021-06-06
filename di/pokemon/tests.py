import json

from django.test import RequestFactory, TestCase
from django.urls import resolve

from pokemon.views import can_learn


class FakeAPIIntegration:
    def __init__(self, pokemons):
        self.pokemons = pokemons

    def can_learn(self, pokemon, move_name):
        return move_name in self.pokemons.get(pokemon, [])


class CanLearnTestCase(TestCase):
    def setUp(self):
        pokemons = {
            'squirtle': ['bubble'],
            'charmander': ['ember']
        }
        self.fake_integration = FakeAPIIntegration(pokemons)

    def test_squirtle_can_learn_bubble(self):
        request = RequestFactory().get('/pokemon/squirtle/can_learn', {'move': 'bubble'})

        response = can_learn(request, 'squirtle', self.fake_integration)
        data = json.loads(response.content)

        self.assertTrue(data['can_learn'])

    def test_squirtle_cannot_learn_ember(self):
        request = RequestFactory().get('/pokemon/squirtle/can_learn', {'move': 'ember'})

        response = can_learn(request, 'squirtle', self.fake_integration)
        data = json.loads(response.content)

        self.assertFalse(data['can_learn'])

    def test_charmander_can_learn_ember(self):
        request = RequestFactory().get('/pokemon/charmander/can_learn', {'move': 'ember'})

        response = can_learn(request, 'charmander', self.fake_integration)
        data = json.loads(response.content)

        self.assertTrue(data['can_learn'])

    def test_resolve_url_returns_can_learn_view(self):
        match = resolve('/pokemon/squirtle/can_learn')

        self.assertEqual(match.func.func, can_learn)
