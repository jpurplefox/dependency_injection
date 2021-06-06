import requests


class Pokemon:
    class DoesNotExist(Exception):
        pass

    def __init__(self, moves_can_learn):
        self.moves_can_learn = moves_can_learn

    def can_learn(self, move_name):
        return move_name in self.moves_can_learn


class APIIntegration:
    def get_pokemon(self, pokemon):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        if response.status_code == 404:
            raise Pokemon.DoesNotExist()

        data = response.json()

        moves_can_learn = [move['move']['name'] for move in data['moves']]

        return Pokemon(moves_can_learn)
