import requests


class APIIntegration:
    def can_learn(self, pokemon, move_name):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        data = response.json()

        for move in data['moves']:
            if move['move']['name'] == move_name:
                can_learn = True
                break
        else:
            can_learn = False

        return can_learn
