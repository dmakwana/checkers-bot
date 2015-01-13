# test.py
from full import CheckersGame
import random

game = CheckersGame()
game.start_game()
moves = game.possible_moves()
while len(moves) > 0:
	states = game.get_states_for_list_of_moves(moves)
	game.move_here(random.choice(states['move']))
	
