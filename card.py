#Card Game Espadinha

class card:

	def __init__(self, value, suit, rep):
		self.value = value
		self.suit = suit
		self.rep = rep

	def getValue(self):
		return self.value

	def getSuit(self):
		return self.suit

	def toString(self):
		return self.rep + ' ' + self.suit