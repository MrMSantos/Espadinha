from card import Card
from deck import Deck
from player import Player
from human_player import HumanPlayer
from random_player import RandomPlayer
from rulebased_player import RuleBasedPlayer
from table import Table
from scoretable import ScoreTable
import random

class Game:

    GAME_TRICKS = 13
    WINNING_SCORE = 500
    PLAYERS_NUMBER = 4

    def __init__(self):
        self.players = []

    def setup(self):
        self.players = self.createPlayers()
        self.deck = Deck()
        self.table = Table()
        self.dealer = self.firstDealer()
        self.teamA = ScoreTable((self.players[0], self.players[2]))
        self.teamB = ScoreTable((self.players[1], self.players[3]))

    def createPlayers(self):
        print("--- Welcome to Espadinha! ---\n")
        print('Please insert your name: ')
        p1 = HumanPlayer(input())
        p3 = RuleBasedPlayer("Bot 3")
        p2 = RuleBasedPlayer("Bot 2")
        p4 = RuleBasedPlayer("Bot 4")
        return (p1, p2, p3, p4)

    def dealNshuffle(self):
        self.deck.shuffle()
        h1, h2, h3, h4 = self.deck.deal()
        self.players[0].reset()
        self.players[0].hand = h1
        self.players[0].orderHand()
        self.players[1].reset()
        self.players[1].hand = h2
        self.players[1].orderHand()
        self.players[2].reset()
        self.players[2].hand = h3
        self.players[2].orderHand()
        self.players[3].reset()
        self.players[3].hand = h4
        self.players[3].orderHand()

    def bets(self, first_player):
        print("--- BIDDING ---")
        for i in range(self.PLAYERS_NUMBER):
            self.players[(first_player + i) % 4].bidding()

    def trick(self, first_player):
        for i in range(self.PLAYERS_NUMBER):
            self.players[(first_player + i) % 4].play(self.table)
            print(self.table.toString())

    def firstDealer(self):
        return random.randint(0, 3)

    def nextDealer(self, previous_dealer):
        return (previous_dealer + 1) % 4

    def calculateFirstPlayer(self, dealer):
        return (self.dealer - 3) % 4

    def game(self):

        self.setup()
        #Game routine
        while self.teamA.score < self.WINNING_SCORE and self.teamB.score < self.WINNING_SCORE:
            first_player = self.calculateFirstPlayer(self.dealer)
            self.dealNshuffle()
            self.bets(first_player)
            for i in range(self.GAME_TRICKS):
                self.trick(first_player)

                player_win = self.table.checkWinner()
                first_player = self.players.index(player_win)
                self.table.resetCards()
            self.table.reset()

            self.teamA.updateScoreTable()
            self.teamB.updateScoreTable()
            self.dealer = self.nextDealer(self.dealer)

            self.teamA.toString()
            self.teamB.toString()

game = Game()
game.game()
