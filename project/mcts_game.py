from copy import deepcopy
from game import Game
from player import Player
from table import Table
from card import Card

class mcts_Game:

    def __init__(self, game):
        self.players = deepcopy(game.players) #FIXME
        self.table = deepcopy(game.table)     #FIXME
        self.dealer = deepcopy(game.dealer)
        self.teamA = deepcopy(game.teamA)
        self.teamB = deepcopy(game.teamB)
        self.currentPlayer = (self.dealer - 3) % 4
        self.winner = None
        self.isFinished = False

    def setTable(self, table):
        self.table = table

    def setDealer(self, dealer):
        self.dealer = dealer

    def setTeamA(self, teamA):
        self.teamA = teamA

    def setTeamB(self, teamB):
        self.teamB = teamB

    def getCurrentPlayer(self):
        return self.currentPlayer

    def checkWinner(self, player):
        return player.equal(self.winner)

    def nextState(self, card, player):
        #one card played by one single player
        for individual in self.players:
            if individual.name == player.name:
                self.table.layDownCard(player, card)
                individual.playCard(card)
        self.currentPlayer = (self.dealer - 3) % 4

        if len(self.table.plays) == 3:
            self.winner = self.table.checkWinner()
            self.currentPlayer = self.currentPlayer
            self.isFinished = True
