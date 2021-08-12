from player import Player


class Game:
    def __init__(self, id):
        self.id = id
        self.player1 = Player(0, 0, 50, 50, (255, 0, 0))
        self.player2 = Player(100, 100, 50, 50, (0, 0, 255))
        self.ready = False
