import random

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.x = 0
        self.y = 0
        self.health = 100
        self.coin = 0

    def move(self, direction, map_size):
        direction = direction.lower()

        if direction == "w":  # up
            if self.x > 0:
                self.x -= 1
            else:
                print("You cannot move that way!")
        elif direction == "s":  # down
            if self.x < map_size - 1:
                self.x += 1
            else:
                print("You cannot move that way!")
        elif direction == "a":  # left
            if self.y > 0:
                self.y -= 1
            else:
                print("You cannot move that way!")
        elif direction == "d":  # right
            if self.y < map_size - 1:
                self.y += 1
            else:
                print("You cannot move that way!")
        else:
            print("Invalid move!")


class GameMap:
    def __init__(self, size):
        self.size = size

    def draw(self, player):
        for i in range(self.size):
            for j in range(self.size):
                if i == player.x and j == player.y:
                    print("C", end=" ")
                elif i == self.size - 1 and j == self.size - 1:
                    print("M", end=" ")
                else:
                    print(".", end=" ")
            print()
        print(f"Health: {player.health}")
        print(f"Coin: {player.coin}")


class Game:
    def __init__(self, size=9):
        self.game_name = "Panama Man"
        self.name = "Tester"
        self.map_size = size                               # ⭐ FIXED
        self.events = ["find a coin", "meet a monster", "do nothing"]

        self.player = Player(self.name)
        self.map = GameMap(self.map_size)                  # ⭐ NOW VALID

    def check_event(self):
        event = random.choice(self.events)

        if event == "find a coin":
            self.player.coin += 1
        elif event == "meet a monster":
            self.player.health -= 10
        # "do nothing" → no changes

    def play(self):
        print("Game started!")
        while True:
            self.map.draw(self.player)

            if self.player.x == self.map_size - 1 and self.player.y == self.map_size - 1:
                print("You reached the exit!")
                break

            move = input("Move (w/a/s/d): ")
            self.player.move(move, self.map_size)
            self.check_event()
            