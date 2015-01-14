'''Checkers Bot

BOT 1 - BLACK - STARTS FIRST
BOT 2 - RED - STARTS SECOND

w1 - numBlack
w2 - numRed
w3 - numBlackKings
w4 - numRedKings
w5 - numBlackThreatened
w6 - numRedThreatened

'''
import os
from full import CheckersGame
from full import Colour

class DoubleBotRunner():
	def __init__():
		self.game = CheckersGame()
		self.create_weight_file(1,1,1,1,1)
		self.outputFile =  None
		self.weights = self.get_weights()
		self.bot1 = CheckersBot(self.weights[1], self.weights[2], self.weights[3], self.weights[4], self.weights[5], self.weights[6], game, Colour.BLACK)
		self.bot2 = CheckersBot(self.weights[1], self.weights[2], self.weights[3], self.weights[4], self.weights[5], self.weights[6], game, Colour.RED)

	def run(self):
		while self.game.gameRunning:
			self.bot1.play_turn()
			if self.game.gameRunning:
				self.bot2.play_turn()

		print "Bot 1 Variables: ", bot1.w1, bot1.w2, bot1.w3, bot1.w4, bot1.w5, bot1.w6
		print "Bot 2 Variables: ", bot2.w1, bot2.w2, bot2.w3, bot2.w4, bot2.w5, bot2.w6

		self.update_weight_file()
		game.end_game()

	def create_weight_file(self, w1, w2, w3, w4, w5):
		directory  = os.path.join(os.getcwd(), 'weights')
		if not os.path.exists(directory):
			os.makedirs(directory)

		file_path = os.path.join(directory, 'checkers_weights')
		write = os.path.exists(file_path)
		if write:
			self.outputFile = open(file_path, 'r')
		else:
			self.outputFile = open(file_path, 'w+')
			self.outputFile.write(w1+'\n')
			self.outputFile.write(w2+'\n')
			self.outputFile.write(w3+'\n')
			self.outputFile.write(w4+'\n')
			self.outputFile.write(w5+'\n')

	def get_weights(self):
		weights = outputFile.readlines()
		self.outputFile.close()
		return weights

	def update_weight_file(self):
		self.outputFile = open(file_path, 'w+')
		for weight in self.weights:
			self.outputFile.write(weight+'\n')
		self.outputFile.close()

class CheckersBot():
	def __init__(w1, w2, w3, w4, w5, w6, game, colour):
		self.w1 = w1
		self.w2 = w2
		self.w3 = w3
		self.w4 = w4
		self.w5 = w5
		self.w6 = w6
		self.game = game
		self.colour = colour
		self.previousState = None
		self.wonGame = True
		self.gameRunning = True


	def play_turn(self):
		moves = game.possible_moves()
		
		if len(moves) == 0:
			self.gameRunning = False
			self.wonGame = False
			return
		else:
			states = game.get_states_for_list_of_moves(moves)
			score = self.calc_weight_for_state(states[1])
			stateChosen=state[1]
			for state in states:
				if self.calc_weight_for_state(state)>score:
					score = self.calc_weight_for_state
					stateChosen = state

			if self.previousState:
				self.update_weights(previousState,score)
			self.previousState= stateChosen



	def calc_weight_for_state(self, state):
		return (state['numBlack']*self.w1 + state['numRed']*self.w2 + state['numBlackKings']*self.w3 + \
				state['numRedKings']*self.w4 + state['numBlackThreatened']*self.w5 + state['numRedThreatened']*self.w6)

	def update_weights (self,state, score):
		DoubleBotRunner.weights[1]=DoubleBotRunner.weights[1] + DoubleBotRunner.n*(score-self.calc_weight_for_state(state))#*x1
		DoubleBotRunner.weights[2]=DoubleBotRunner.weights[2] + DoubleBotRunner.n*(score-self.calc_weight_for_state(state))#*x2
		DoubleBotRunner.weights[3]=DoubleBotRunner.weights[3] + DoubleBotRunner.n*(score-self.calc_weight_for_state(state))#*x3
		DoubleBotRunner.weights[4]=DoubleBotRunner.weights[4] + DoubleBotRunner.n*(score-self.calc_weight_for_state(state))#*x4
		DoubleBotRunner.weights[5]=DoubleBotRunner.weights[5] + DoubleBotRunner.n*(score-self.calc_weight_for_state(state))#*x5


