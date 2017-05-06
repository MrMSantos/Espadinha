#Card Game Espadinha

class Card:

	SPADES = '♠'
	CLUBS = '♣'
	HEARTS = '♥'
	DIAMONDS = '♦'

	values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
	suits = [SPADES, CLUBS, HEARTS, DIAMONDS]

	def __init__(self, value, suit, rep):
		self.value = value
		self.suit = suit
		self.rep = rep

	def getValue(self):
		return self.value

	def getSuit(self):
		return self.suit

	#def toString(self):
	#	return self.rep + ' ' + self.suit

	def toString(self):
		print("|-------|")
		print("| %s     |" % self.rep)
		print("|       |")
		print("|   %s   |" % self.suit)
		print("|       |")
		print("|    %s  |" % self.rep)
		print("|-------|")
		return self.rep + ' ' + self.suit