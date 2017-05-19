from deck import Deck
from card import Card

def getPlayer(play):
    return play[0]

def getCard(play):
    return play[1]

class Table:

    def __init__(self):
        self.plays = []
        self.isTrumped = False
        self.cardsUsed = []

    def layDownCard(self, player, card):
        self.plays += [(player, card)]

    def checkWinner(self):

        first_play = self.plays[0]
        first_player = getPlayer(first_play)
        first_card = getCard(first_play)
        first_suit = first_card.suit

        winning_card = first_card
        winning_player = first_player

        for play in self.plays[1:]:
            played_card = getCard(play)
            played_card_suit = played_card.suit

            if (played_card_suit == winning_card.suit):
                if (played_card.value > winning_card.value):
                    winning_card = played_card
                    winning_player = getPlayer(play)

            elif(played_card_suit == Card.SPADES):
                winning_card = played_card
                winning_player = getPlayer(play)

        for play in self.plays:
            self.cardsUsed.append(getCard(play))
            
        winning_player.trick += 1
        return winning_player

    def highCard(self):

        first_play = self.plays[0]
        first_card = getCard(first_play)
        first_suit = first_card.suit

        winning_card = first_card

        for play in self.plays[1:]:
            played_card = getCard(play)
            played_card_suit = played_card.suit

            if (played_card_suit == winning_card.suit):
                if (played_card.value > winning_card.value):
                    winning_card = played_card

            elif(played_card_suit == Card.SPADES):
                winning_card = played_card

        return winning_card

    def resetCards(self):
        self.plays = []

    def reset(self):
        self.plays = []
        self.isTrumped = False
        self.cardsUsed = []

    def toString(self):
        tablestr = "--- Table --- \n"
        for play in self.plays:
            tablestr = tablestr + getPlayer(play).name + " "
            tablestr = tablestr + "Card: "
            tablestr = tablestr + getCard(play).toString() + " // "
        return tablestr + "\n"
