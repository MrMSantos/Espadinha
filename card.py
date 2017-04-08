#Card Game Espadinha

values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def getValue(card):
	value = card[0]
	return values[value]

def getSuit(card):
	return card[1]