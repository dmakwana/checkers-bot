# test.py
from full import CheckersGame
import random
from time import sleep

game = CheckersGame()
game.start_game()
# for nodeRow in game.listOfNodes:
# 	for node in nodeRow:
# 		print str(node.row) + " - " + str(node.col)
# 		if node.upRight:
# 			print "upright exists"
# 		if node.downLeft:
# 			print "downLeft exists"
# 		if node.upLeft:
# 			print "upLeft exists"
# 		if node.downRight:
# 			print "downright exists"

# 		print "-----"
game.test_function()
moves = game.possible_moves()
print "GOT POSSIBLE MOVES"
while len(moves) > 0:
	states = game.get_states_for_list_of_moves(moves)
	print "GOT STATES"
	game.move_here(states[0]['move'])
	# game.move_here(random.choice(states)).['move']
	moves = game.possible_moves()
	sleep(1)
