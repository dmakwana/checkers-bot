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
import sys

class DoubleBotRunner():
	def __init__(self):
		self.game = CheckersGame()
		self.file =  None
		self.file_path = None
		self.create_weight_file()
		self.weights = []
		self.get_weights()
		self.bot1 = CheckersBot(self.weights, self.game, Colour.BLACK)
		self.bot2 = CheckersBot(self.weights, self.game, Colour.RED)


	def run(self):
		self.game.start_game()
		while self.game.gameRunning:
			self.bot1.play_turn()
			if self.game.gameRunning:
				self.bot2.play_turn()

		print "Bot 1 Variables: ", self.bot1.weights[0], self.bot1.weights[1], self.bot1.weights[2], self.bot1.weights[3], self.bot1.weights[4], self.bot1.weights[5]
		print "Bot 2 Variables: ", self.bot2.weights[0], self.bot2.weights[1], self.bot2.weights[2], self.bot2.weights[3], self.bot2.weights[4], self.bot2.weights[5]

		self.update_weight_file()
		self.game.end_game()

	def create_weight_file(self):
		directory  = os.path.join(os.getcwd(), 'weights')
		if not os.path.exists(directory):
			os.makedirs(directory)

		self.file_path = os.path.join(directory, 'checkers_weights')
		write = os.path.exists(self.file_path)
		if write:
			self.file = open(self.file_path, 'r')
		else:
			self.file = open(self.file_path, 'w+')
			defaultWeight = 10
			for i in range(6):
				self.file.write(str(defaultWeight)+'\n')
		self.file.close()

	def get_weights(self):
		self.file = open(self.file_path, 'r')
		for line in self.file.readlines():
			self.weights.append(int(line.strip()))
		self.file.close()

	def update_weight_file(self):
		self.file = open(self.file_path, 'w+')
		for weight in self.weights:
			self.file.write(str(weight)+'\n')
		self.file.close()

class CheckersBot():
	def __init__(self, weights, game, colour, n = 1):
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
		moves = self.game.possible_moves()
		
		if len(moves) == 0:
			self.gameRunning = False
			self.wonGame = False
			return
		else:
			states = self.game.get_states_for_list_of_moves(moves)
			self.state_to_variables(states[0])
			score = self.calc_score_for_state(states[0])
			stateChosen=states[0]
			for state in states:
				self.state_to_variables(state)
				if self.calc_score_for_state(state)>score:
					score = self.calc_score_for_state(state)
					stateChosen = state

			if self.previousState:
				self.state_to_variables(self.previousState)
				print "Score is " + str(score)
				self.update_weights(score)
			self.previousState= stateChosen
			self.game.move_here(stateChosen["move"])

	def state_to_variables(self, state):

		self.variables[0+self.colour] = state['numBlack']
		self.variables[1-self.colour] = state['numRed']
		self.variables[2+self.colour] = state['numBlackKings']
		self.variables[3-self.colour] = state['numRedKings']
		self.variables[4+self.colour] = state['numBlackThreatened']
		self.variables[5-self.colour] = state['numRedThreatened']

	def calc_score_for_state(self, state):
		totalScore = 0
		for weight in self.staticWeights:
			totalScore += weight*self.variables[self.staticWeights.index(weight)]
		return totalScore

	def update_weights (self, score):
		for weight in self.weights:
			weight += self.n*(score-self.calc_score_for_state(self.previousState))*self.variables[self.weights.index(weight)]
			print "The new weight " + str(score-self.calc_score_for_state(self.previousState))




