import json


class Player:

    def __init__(self, filename):
        self.name = filename
        self.open_json()

    def open_json(self):
        init_path = 'game\\players\\'

        path = init_path + self.name + '\\attributes.json'

        with open(path) as f:
            data = json.load(f)

        self.name = data['name']
        self.health = data['health']
        self.speed = data['speed']
        self.defense = data['defense']
        self.moves = []
        ar = ['11','12','21','22']
        for i in ar:
            move = data['move'+i][0]
            self.moves.append(move)


