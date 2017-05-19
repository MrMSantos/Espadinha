from card import Card
from deck import Deck
from player import Player
import random
import operator

class MCTSPlayer(Player):

    def __init__(self, name):
        self.suits = {Card.SPADES: True, Card.DIAMONDS: True, Card.CLUBS: True, Card.HEARTS: True}
        self.belief = {}
        super(MCTSPlayer, self).__init__(name)

    def initBelief(self):
        for card in self.hand:
            self.belief[card] = 0

    def updateBelief(self, table, eligibleCards):
        if len(table.plays) > 0:
            firstSuit = table.plays[0][1].suit
        else:
            firstSuit = None

        for card in self.hand:
            cardValue = card.value
            if card not in eligibleCards:
                self.belief[card] = 0
            else:
                if self.suits[card.suit]:
                    if card.isHighest(table.cardsUsed):
                        if firstSuit == card.suit or firstSuit == None:
                            self.belief[card] = card.value * 2
                        else:
                            self.belief[card] = 1 / card.value
                    else:
                        self.belief[card] = 1 / card.value
                else:
                    self.belief[card] = (1 / card.value) * 2

        for card in eligibleCards:
            if card.suit == Card.SPADES:
                self.belief[card] *= 15 - card.value


    def updateSuits(self, table):
        spades, diamonds, clubs, hearts = self.numSuits(table.cardsUsed)
        spades += self.numSpades()
        diamonds += self.numDiamonds()
        clubs += self.numClubs()
        hearts += self.numDiamonds()
        if spades == 13:
            self.suits[Card.SPADES] = False
        if diamonds == 13:
            self.suits[Card.DIAMONDS] = False
        if clubs == 13:
            self.suits[Card.CLUBS] = False
        if hearts == 13:
            self.suits[Card.HEARTS] = False

    def play(self, table):
        print(self.printTricks())
        playableCards = self.playableCards(table)
        self.initBelief()
        self.updateSuits(table)
        self.updateBelief(table, playableCards)
        self.printBelief()

        card_to_play = max(self.belief.items(), key=operator.itemgetter(1))[0]

        del self.belief[card_to_play]
        table.layDownCard(self, card_to_play)
        self.playCard(card_to_play)

    def minBelief(self):
        minValue = 10000
        for card in self.belief:
            if self.belief[card] < minValue and self.belief[card] != 0:
                minCard = card
                minValue = self.belief[card]
        return minCard


    def bidding(self):
        bet = 0
        dup = 0
        trump = []
        spades = self.numSpades()
        diamonds = self.numDiamonds()
        clubs = self.numClubs()
        hearts = self.numHearts()
        for card in self.hand:
            if card.value == Card.values['A']:
                bet += 1
                if card.suit == Card.SPADES:
                    dup += 1
            elif card.value == Card.values['K']:
                if card.suit == Card.SPADES:
                    bet += 1
                    dup += 1
                elif card.suit == Card.DIAMONDS:
                    if diamonds < 5:
                        bet += 1
                elif card.suit == Card.CLUBS:
                    if clubs < 5:
                        bet += 1
                elif card.suit == Card.HEARTS:
                    if hearts < 5:
                        bet += 1
        trump.append(spades - diamonds)
        trump.append(spades - clubs)
        trump.append(spades - hearts)
        trump = max(trump)
        if trump > 0:
            bet += trump
        self.bet = bet - dup
        print(self.name, "bidding:", self.bet, "tricks\n")

    def numSuits(self, cardsList):
        spades, diamonds, clubs, hearts = 0, 0, 0, 0
        for card in cardsList:
            if card.suit == Card.SPADES:
                spades += 1
            elif card.suit == Card.DIAMONDS:
                diamonds += 1
            elif card.suit == Card.CLUBS:
                clubs += 1
            elif card.suit == Card.HEARTS:
                hearts += 1
        return spades, diamonds, clubs, hearts

    def printBelief(self):
        belief = ""
        for card in self.belief:
            belief += card.toString() + ' -> ' + str(self.belief[card]) + ' '
        print(belief + "\n")
