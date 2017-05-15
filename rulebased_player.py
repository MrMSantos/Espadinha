from card import Card
from player import Player
import random

class RuleBasedPlayer(Player):

    def play(self, table):

        print(self.printTricks())

        highCard = self.playHighestCard(table)
        lowCard = self.playHighestCard(table)

        if len(table.plays) == 0:
            if self.trick < self.bet:
                card_to_play = highCard
            else:
                card_to_play = lowCard
        else:
            if self.trick < self.bet:
                if table.highCard().value < highCard.value:
                    card_to_play = highCard
                else:
                    card_to_play = lowCard
            else:
                card_to_play = lowCard

        table.layDownCard(self, card_to_play)
        self.playCard(card_to_play)

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