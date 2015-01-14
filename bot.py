'''Checkers Bot

BOT 1 - BLACK - STARTS FIRST
BOT 2 - RED - STARTS SECOND

x1 - numBlack
x2 - numRed
x3 - numBlackKings
x4 - numRedKings
x5 - numBlackThreatened
x6 - numRedThreatened

'''

from full import CheckersGame
from full import Colour

class DoubleBotRunner():
	def __init__():
		self.game = CheckersGame()
		self.bot1 = CheckersBot(1,1,1,1,1,1, game, Colour.BLACK)
		self.bot2 = CheckersBot(1,1,1,1,1,1, game, Colour.RED)

	def run(self):
		while self.game.gameRunning:
			self.bot1.play_turn()
			if self.game.gameRunning:
				self.bot2.play_turn()

		print "Bot 1 Variables: ", bot1.x1, bot1.x2, bot1.x3, bot1.x4, bot1.x5, bot1.x6
		print "Bot 2 Variables: ", bot2.x1, bot2.x2, bot2.x3, bot2.x4, bot2.x5, bot2.x6

		game.end_game()


class CheckersBot():
	def __init__(x1, x2, x3, x4, x5, x6, game, colour):
		self.x1 = x1
		self.x2 = x2
		self.x3 = x3
		self.x4 = x4
		self.x5 = x5
		self.x6 = x6
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
		


	def calc_weight_for_state(self, state):
		return (state['numBlack']*self.x1 + state['numRed']*self.x2 + state['numBlackKings']*self.x3 + \
				state['numRedKings']*self.x4 + state['numBlackThreatened']*self.x5 + state['numRedThreatened']*self.x6)



