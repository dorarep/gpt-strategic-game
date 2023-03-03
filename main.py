import random
import os

# Define the game parameters
num_players = 3
num_rounds = 5
max_units = 10

# Define the player classes
class Player:
    def __init__(self, name):
        self.name = name
        self.units = max_units

    def attack(self, target):
        max_attack_units = min(self.units, max_units - 1)
        max_attack_units = max(max_attack_units, 1)
        attack_units = random.randint(1, max_attack_units)
        target.defend(attack_units)

    def defend(self, units):
        self.units -= units

class CPU(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_target(self, players):
        targets = [p for p in players if p != self]
        return random.choice(targets)

# Create the players
human = Player("You")
cpu1 = CPU("1")
cpu2 = CPU("2")
players = [human, cpu1, cpu2]

# Main game loop
for i in range(num_rounds):
    print(f"Round {i+1}:")
    for p in players:
        # Human player input
        if p == human:
            target = None
            while not target:
                target_name = input("Choose a target CPU(1 or 2): ")
                target = next((t for t in players if t.name == target_name), None)
            p.attack(target)
        # CPU player logic
        else:
            target = p.choose_target(players)
            p.attack(target)

        # Check for a winner
        alive_players = [p for p in players if p.units > 0]
        if len(alive_players) == 1:
            winner = alive_players[0]
            print(f"{winner.name} wins!")
            break
    else:
        continue
    break

# Print out the final state of each player
for p in players:
    print(f"{p.name} has {p.units} units remaining.")
