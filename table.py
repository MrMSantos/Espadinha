from deck import deck

class Table:

    def __init__(self):
        self.plays = []

    def layDownCard(self, player, card):
        plays += [(player, card)]

    def checkWinner(self):

        first_play = plays[0]
        first_player = getPlayer(first_play)
        first_card = getCard(first_play)
        first_suit = first_card.getSuit()

        winning_card = first_card
        winning_player = first_player

        for play in plays[1:]:
            played_card = getCard(play)
            played_card_suit = played_card.getSuit()

            if (played_card_suit == first_suit):
                if (played_card.getSuit()) > deck.getValue(winning_card)
                    winning_card = played_card
                    winning_player = getPlayer(play)

            elif(played_card_suit = deck.SPADES):
                winning_card = player_card
                winning_player = player

        return winning_player

    def getPlayer(play):
        return play[0]

    def getCard(play):
        return play[1]
