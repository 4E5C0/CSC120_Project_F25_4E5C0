import random

game_name = "Panama Man"
print(f"Welcome to {game_name}!")
print("======================")


name = "Tester"

print(f"Great, {name}! Let's begin the adventure!")

player = {
    "name": name,
    "health": 100,
    "coin": 0,
    "x": 0,
    "y": 0
}

map_size = 9
events = ["find a coin", "meet a monster","nothing happens"]

def check_event():
    global events, player
    event = random.choice(events)
    if event == "find a coin":
        player["coin"] += 1
    elif event == "meet a monster":
        player["health"] -= 10
    else:
        pass

def draw_ui(x, y):
    print("=========================")
    for i in range(map_size):
        for j in range(map_size):
            if i == x and j == y:
                print("C", end=" ")
            elif i == map_size - 1 and j == map_size - 1:
                print("M", end=" ")
            else: 
                print(".", end=" ")
        print()
    print("=========================")
    print(f"Health: {player['health']}")
    print("-------------------------")
    print(f"Coins: {player['coin']}")
    print("=========================")
    print("Your move (w/a/s/d/q):")

def move(direction):
    global player
    if direction == "w" and player["x"] > 0:
        player["x"] -= 1
    elif direction == "s" and player["x"] < map_size - 1:
        player["x"] += 1
    elif direction == "a" and player["y"] > 0:
        player["y"] -= 1
    elif direction == "d" and player["y"] < map_size - 1:
        player["y"] += 1
    elif direction == "a" and player["x"] > 0:
        player["x"] -= 1
    elif direction == "d" and player["x"] < map_size - 1:
        player["x"] += 1
    else:
        print("You cannot move that way!")


def main():
    draw_ui(0,0)
    direction = input("Your move (w/a/s/d/q): ")
    while direction != "q":
        move(direction)
        if player["x"] == map_size - 1 and player["y"] == map_size - 1:
            print("Congratulations! You have reached the gate for the next level.")
            break
        check_event()
        draw_ui(player["x"], player["y"])
        direction = input("Your move (w/a/s/d/q): ")

if __name__ == "__main__":
    main()