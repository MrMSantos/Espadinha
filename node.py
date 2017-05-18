from math import log, sqrt
from __future__ import division


class Node:
    self.game = None
    self.action = None
    self.parent = None
    self.playableCards = None
    self.children = []
    self.currentPlayer = None
    self.utility = 0
    self.visits = 0
    self.wins = 0
    self.parentVisits = 0
    self.isNotTerminal = True

    def __init__(self, game, action, parent,  player):
        self.currentPlayer = player
        self.game = game
        self.action = action
        self.parent = parent
        self.playableCards = self.currentPlayer.playableCards()



    def expand(self):
        chosen_card = random.choice(playableCards)
        playableCards.remove(chosen_card)
        self.current_player.playCard(chosen_card)#on the copy
        next_state = game.nextState(chosen_card, self.current_player)#on copy
        next_node = Node(next_state, game, action, self, self.current_player)
        self.children += [next_node]
        return next_node



    def bestChild(self):
        bestChild = self.children[0]
        if len(node.children > 1):
            for child in node.children[1:]:
                if(child.UCTValue() > bestChild.UCTValue):
                    bestChild = child
        return bestChild

    def playout(self):
        while self.game.notFinished:
            #get beliefs
            #based on belief randomly distribute cards to other players
            #make them chose one of the possible cards at random
        #calculate utility for the finished state (win or lose and card played are parameters)
f
    def UCTValue(self):
        C = 1.4
        return (self.utility / self.visits) + (C * sqrt(log(self.parentVisits) / self.visits)
