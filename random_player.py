from player import Player
import random

class RandomPlayer(Player):

    def play(self, table):
        #Show players hand
        print(self.printHand())
        print(self.printTricks())
        print()
        
        #Show possible plays
        if len(table.plays) == 0:
            playableCards = self.eligablePlay(table.isTrumped)
        elif len(table.plays) > 0:
            playableCards = self.eligablePlay(table.isTrumped, table.plays[0][1].suit)

        play_index = random.randint(0, len(playableCards) - 1)
        card_to_play = playableCards[play_index]
        #Check for Spades
        if card_to_play.isSpades():
            table.isTrumped = True
        #Update table and player
        table.layDownCard(self, card_to_play)
        self.playCard(card_to_play)
