import json

from django.test import RequestFactory, TestCase

from pokemon.views import can_learn


class CanLearnTestCase(TestCase):
    def test_squirtle_can_learn_bubble(self):
        request = RequestFactory().get('/pokemon/squirtle/can_learn', {'move': 'bubble'})

        response = can_learn(request, 'squirtle')
        data = json.loads(response.content)

        self.assertTrue(data['can_learn'])
