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
		self.create_weight_file()
		self.outputFile =  None
		self.weights = self.get_weights()
		self.bot1 = CheckersBot(self.weights, game, Colour.BLACK)
		self.bot2 = CheckersBot(self.weights, game, Colour.RED)

	def run(self):
		while self.game.gameRunning:
			self.bot1.play_turn()
			if self.game.gameRunning:
				self.bot2.play_turn()

		print "Bot 1 Variables: ", bot1.w1, bot1.w2, bot1.w3, bot1.w4, bot1.w5, bot1.w6
		print "Bot 2 Variables: ", bot2.w1, bot2.w2, bot2.w3, bot2.w4, bot2.w5, bot2.w6

		self.update_weight_file()
		game.end_game()

	def create_weight_file(self):
		directory  = os.path.join(os.getcwd(), 'weights')
		if not os.path.exists(directory):
			os.makedirs(directory)

		file_path = os.path.join(directory, 'checkers_weights')
		write = os.path.exists(file_path)
		if write:
			self.outputFile = open(file_path, 'r')
		else:
			self.outputFile = open(file_path, 'w+')
			defaultWeight = 1
			self.outputFile.write(defaultWeight+'\n')
			self.outputFile.write(defaultWeight+'\n')
			self.outputFile.write(defaultWeight+'\n')
			self.outputFile.write(defaultWeight+'\n')
			self.outputFile.write(defaultWeight+'\n')
			self.outputFile.write(defaultWeight+'\n')

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
	def __init__(weights, game, colour, n = 1):
		self.weights = weights
		self.staticWeights = list(weights)
		self.variables = [0,0,0,0,0,0]
		self.game = game
		self.colour = colour
		self.previousState = None
		self.wonGame = True
		self.gameRunning = True
		self.n = n

	def play_turn(self):
		moves = game.possible_moves()
		
		if len(moves) == 0:
			self.gameRunning = False
			self.wonGame = False
			return
		else:
			states = game.get_states_for_list_of_moves(moves)
			score = self.calc_score_for_state(states[1])
			stateChosen=state[1]
			for state in states:
				if self.calc_score_for_state(state)>score:
					score = self.calc_score_for_state
					stateChosen = state

			if self.previousState:
				self.update_weights(score)
			self.previousState= stateChosen

	def state_to_variables(self, state):
		self.variables[0] = state['numBlack']
		self.variables[1] = state['numRed']
		self.variables[2] = state['numBlackKings']
		self.variables[3] = state['numRedKings']
		self.variables[4] = state['numBlackThreatened']
		self.variables[5] = state['numRedThreatened']

	def calc_score_for_state(self, state):
		totalScore = 0
		for weight in self.staticWeights:
			totalScore += weight*variables[self.staticWeights.index(weight)]
		return totalScore

	def update_weights (self, score):
		for weight in self.weights:
			weight += self.n*(score-self.calc_score_for_state(self.previousState))*variables[self.weights.index(weight)]




