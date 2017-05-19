from card import Card
from deck import Deck
from player import Player
from human_player import HumanPlayer
from random_player import RandomPlayer
from rulebased_player import RuleBasedPlayer
from mcts_player import MCTSPlayer
from table import Table
from scoretable import ScoreTable
from copy import deepcopy
import random
import time

class Game:

    GAME_TRICKS = 13
    WINNING_SCORE = 500
    PLAYERS_NUMBER = 4

    def __init__(self):
        self.players = Game.createPlayers(self)
        self.deck = Deck()
        self.table = Table()
        self.dealer = Game.firstDealer(self)
        self.teamA = ScoreTable((self.players[0], self.players[2]))
        self.teamB = ScoreTable((self.players[1], self.players[3]))

    def createPlayers(self):
        print("--- Welcome to Espadinha! ---\n")
        #print('Please insert your name: ')
        #p1 = HumanPlayer(input())
        p1 = MCTSPlayer("Bot 1")
        p3 = MCTSPlayer("Bot 3")
        p2 = RuleBasedPlayer("Random")
        p4 = RuleBasedPlayer("Random")
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
            #input()

    def firstDealer(self):
        return random.randint(0, 3)

    def nextDealer(self, previous_dealer):
        return (previous_dealer + 1) % 4

    def calculateFirstPlayer(self, dealer):
        return (self.dealer - 3) % 4

    def game(self):
        #Game routine
        num = 0
        while self.teamA.score < self.WINNING_SCORE and self.teamB.score < self.WINNING_SCORE:
            print("Number of games - ", num)
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
