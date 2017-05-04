import deck

class Table:

    def __init__(self):
        self.cards = {}
        self.player_order = []

    def layDownCard(self, player, card):
        cards[player.getName()] = card
        player_order + [player.getName()]

    def checkWinner(self):
        first_player = order[0].getName(())
        first_card = cards[first_player]
        first_suit = deck.getSuit(first_card)

        winning_card = first_card
        for player in player_order[1:]:
            played_card = cards[player.getName()]
            #FIXME TODO TODO
