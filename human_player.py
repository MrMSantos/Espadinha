from player import Player

class HumanPlayer(Player):

    #def __init__(self, name):
    #    super(HumanPlayer, self).__init__(name);

    def play(self, table):
        #Show players hand
        print(self.name, str(self.trick) + "/" + str(self.bet))
        print(self.printHand())

        #Show possible plays
        if len(table.plays) == 0:
            playableCards = self.eligablePlay(table.isTrumped)
        elif len(table.plays) > 0:
            playableCards = self.eligablePlay(table.isTrumped, table.plays[0][1].suit)

        #Select a playable card
        print(self.name, "select a card (number) to play: ")
        c_index = int(input())
        while (not (0 < c_index and c_index <= len(self.hand))) or self.hand[c_index - 1] not in playableCards:
            print("Please choose a playable card: ")
            c_index = int(input())
        real_index = c_index - 1

        #Check for Spades
        if self.hand[real_index].isSpades():
            table.isTrumped = True
        #Update table and player
        table.layDownCard(self, self.hand[real_index])
        self.playCard(self.hand[real_index])
