from bot import DoubleBotRunner

runner = DoubleBotRunner()
runner.run()
sys.exit(0)

# moves = game.possible_moves()

# while len(moves) > 0:
# 	states = game.get_states_for_list_of_moves(moves)
# 	choice = random.choice(states)
# 	if not game.move_here(choice["move"]):
# 		sys.exit(-1)
# 	print choice
# 	moves = game.possible_moves()
# 	# sleep(0.1)

# game.end_game()
