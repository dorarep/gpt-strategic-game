# Military Strategic Simulation Game

This is a simple military strategic simulation game implemented in Python. The game allows three players to participate, with two of them controlled by the LLM.

## Installation

To run the game, you'll need to have Python 3.x installed on your system. Clone this repository to your local machine, then navigate to the project directory in your terminal or command prompt.

## Usage

To start the game, simply run the main.py file using Python:

```bash
python main.py
```

The game will run for a series of rounds, with each player selecting a target to attack on their turn. The game ends when one player is eliminated (i.e., their units fall to 0).

## Game Rules

Here are the basic rules of the game:

- There are three players, two of whom are controlled by the CPU.
- Each player starts with a set number of units (10 by default).
- On their turn, a player selects a target to attack (either CPU 1 or CPU 2).
- The attacking player selects a random number of units to use in the attack (between 1 and the number of units they have left).
- The defending player selects a random number of units to use in defense (between 1 and the number of units they have left).
- If the attacking player's units are greater than the defending player's units, the defending player loses that number of units. Otherwise, no units are lost.
- The game continues until one player has been eliminated (i.e., their units have fallen to 0).

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as you see fit.
