from table import *
from card import *

class Belief:
    self.bid = 0
    self.suits = {Card.SPADES : True, Card.DIAMONDS : True, Card.HEARTS : True, Card.CLUBS : True }
    self.playedCards = []
    self.leftToPlay = 13

    def __init__(self, game, player):
        self.bid = player.bid

    def update(self, gameState, player):
        table = gameState.table
        self.leftToPlay = len(player.hand)
        for play in table.plays:
            if getPlayer(play) == player:
                playedCards += [getCard(play)]
                if getCard(play).suit != getCard(table.plays[0]).suit:
                    self.suits[getCard(table.plays[0]).suit] = False
                    break

    def  highCards(self, playedCards, bid):
        high_count = 0
        for card in self.playedCards:
            if (card.value == 13 or card.value == 14 or card.suit == Card.SPADES):
                high_count++
        if(bid - high_count < 0 ):
            return 0
        else:
            return bid - high_count
