from copy import deepcopy
from game import Game
from player import Player
from table import Table
from card import Card

class mcts_Game:

    def __init__(self, game):
        self.players = deepcopy(game.players)
        self.table = deepcopy(game.table)
        self.dealer = deepcopy(game.dealer)
        self.teamA = deepcopy(game.teamA)
        self.teamB = deepcopy(game.teamB)


    def setTable(self, table):
        self.table = table

    def setDealer(self, dealer):
        self.dealer = dealer

    def setTeamA(self, teamA):
        self.teamA = teamA

    def setTeamB(self, teamB):
        self.teamB = teamB

    def nextState(self, card, player):
        #one card played by one single player
        for individual in self.players:
            if individual.name == player.name:
                self.table.layDownCard(player, card)
                individual.playCard(card)
