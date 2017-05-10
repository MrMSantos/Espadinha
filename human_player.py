from player import Player

class HumanPlayer(Player):

    def play(self, table):
        #Show players hand
        print(self.printHand())
        print(self.printTricks())

        #Show possible plays
        if len(table.plays) == 0:
            playableCards = self.eligablePlay(table.isTrumped)
        elif len(table.plays) > 0:
            playableCards = self.eligablePlay(table.isTrumped, table.plays[0][1].suit)

        #Select a playable card
        c_index = int(input())
        while (not (0 < c_index and c_index <= len(self.hand))) or self.hand[c_index - 1] not in playableCards:
            print("Please choose a playable card: ")
            c_index = int(input())
        real_index = c_index - 1
        print()
        
        #Check for Spades
        if self.hand[real_index].isSpades():
            table.isTrumped = True
        #Update table and player
        table.layDownCard(self, self.hand[real_index])
        self.playCard(self.hand[real_index])

    def bidding(self):
        print(self.printHand())
        print(self.name, "place your bet (0 to 13)")
        bet = int(input())
        while bet < 0 or bet > 13:
            print("Please make a legit bet")
            bet = int(input())
        self.bet = bet
        print()