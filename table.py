from deck import Deck
from card import Card

def getPlayer(play):
    return play[0]

def getCard(play):
    return play[1]
    
class Table:

    def __init__(self):
        self.plays = []

    def layDownCard(self, player, card):
        self.plays += [(player, card)]

    def checkWinner(self):

        first_play = self.plays[0]
        first_player = getPlayer(first_play)
        first_card = getCard(first_play)
        first_suit = first_card.getSuit()

        winning_card = first_card
        winning_player = first_player

        for play in self.plays[1:]:
            played_card = getCard(play)
            played_card_suit = played_card.getSuit()

            if (played_card_suit == winning_card.getSuit()):
                if (played_card.getValue() > winning_card.getValue()):
                    winning_card = played_card
                    winning_player = getPlayer(play)

            elif(played_card_suit == Card.SPADES):
                winning_card = played_card
                winning_player = getPlayer(play)

        return winning_player

    def reset(self):
        self.plays = []

    def toString(self):
        tablestr = ""
        for play in self.plays:
            tablestr = tablestr + "Player:"
            tablestr = tablestr + getPlayer(play).getName() + " "
            tablestr = tablestr + "Card:"
            tablestr = tablestr + getCard(play).toString() + "//"
        return tablestr
