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
# 		print str(node.row) + " - " + str(node.col)
# 		print node.colour
		# if node.upRight:
		# 	print "upright exists"
		# if node.downLeft:
		# 	print "downLeft exists"
		# if node.upLeft:
		# 	print "upLeft exists"
		# if node.downRight:
		# 	print "downright exists"

# 		# print "-----"
print moves
print "GOT POSSIBLE MOVES"
while len(moves) > 0:
	states = game.get_states_for_list_of_moves(moves)
	print "GOT STATES"
	if not game.move_here(states[0]['move']):
		print "MOVE FAILED, EXITING"
		sys.exit(-1)
	# game.move_here(random.choice(states)).['move']
	moves = game.possible_moves()
	print moves
	# sleep(0.1)

game.end_game()