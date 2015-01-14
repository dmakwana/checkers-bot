# test.py
from full import CheckersGame
import random
from time import sleep
import sys

game = CheckersGame()
game.start_game()

moves = game.possible_moves()

# for nodeRow in game.listOfNodes:
# 	for node in nodeRow:
# 		print node.colour

while len(moves) > 0:
	states = game.get_states_for_list_of_moves(moves)
	choice = random.choice(states)
	if not game.move_here(choice["move"]):
		sys.exit(-1)
	print choice
	moves = game.possible_moves()
	# for nodeRow in game.listOfNodes:
	# 	for node in nodeRow:
	# 		print node.colour
	# sleep(0.1)

game.end_game()
