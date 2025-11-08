game_name = "Panama Man"
print(f"Welcome to {game_name}!")
print("======================")


print("Before we begin, what is your character's name?")
name = input("Enter your name: ")

print(f"Great, {name}! Let's begin the adventure!")

player = {
    "name": name,
    "health": 100,
    "coin": 0
}

import random
events = ["find a coin", "meet a monster","nothing happens"]

event = random.choice(events)
print(f"While exploring the Panama jungle, you encounter an event: {event}")

if event == "find a coin":
    player["coin"] += 1
    print(f"{name} found a coin, {name} now has {player['coin']} coins.")
elif event == "meet a monster":
    player["health"] -= 10
    print(f"{name} got hurt by a monster, {name}'s health is now {player['health']}.")
else:
    pass

