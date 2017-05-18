#Card Game Espadinha

class Card:

	SPADES = '♠'
	DIAMONDS = '♦'
	CLUBS = '♣'
	HEARTS = '♥'

	values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
	suits = [SPADES, DIAMONDS, CLUBS, HEARTS]

	def __init__(self, value, suit, rep):
		self.value = value
		self.suit = suit
		self.rep = rep

	def isSpades(self):
		return self.suit == self.SPADES

	def toString(self):
		return self.rep + '' + self.suit

	'''def toString(self):
		print("|-----|")
		print("|%s    |" % self.rep)
		print("|  %s  |" % self.suit)
		print("|    %s|" % self.rep)
		print("|-----|")
		return self.rep + ' ' + self.suit'''

	def equal(self, card):
		return self.value == card.value and self.suit == card.suit
