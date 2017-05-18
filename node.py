from math import log, sqrt
from __future__ import division

class Node:
    self.table = None
    self.action = None
    self.parent = None
    self.playableCards = None
    self.children = []
    self.scoreTables = None
    self.currentPlayer = None
    self.utility = 0
    self.visits = 0
    self.wins = 0
    self.parentVisits = 0
    self.isNotTerminal = True

    def __init__(self, table, action, parent, scoreTables, player):
        #initializes with gameState
        self.currentPlayer = player
        self.table = table
        self.action = action
        self.parent = parent
        self.scoreTables = scoreTables
        self.playableCards = self.currentPlayer.playableCards()



    def expand(self):
        #AdvancesGameState

        #choose most likely good action
        chosen_action =
        #produce next node with next state
        next_table =
        next_player =
        next_parent =
        next_scoreTables = self.scoreTables
        next_node = Node()
        #action of new node = action that created it


    def bestChild(self):
        bestChild = self.children[0]
        if len(node.children > 1):
            for child in node.children[1:]:
                if(child.UCTValue() > bestChild.UCTValue):
                    bestChild = child
        return bestChild

    def playout(self):
        #simmulate
        #in the end if you "meet the objective" increment wins
        pass

    def UCTValue(self):
        C = 1.4
        return (self.utility / self.visits) + (C * sqrt(log(self.parentVisits) / self.visits)
