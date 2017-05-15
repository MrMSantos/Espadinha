from copy import deepcopy
import numpy as np
class MCTS:

    self.root= None

def __init__(self, root):
    self.root = root

def search(self):
    while in range(computational_range):
        next_node = selection(root)
        reward = playout(next_node)
        backpropagation(next_node, reward)
    return bestChild(root).action

def selection(self, node):
    selected_node = node
    while node.isNotTerminal:
        if node.isNotFullyExpanded:
            return expansion(node)
        else:
            selected_node =  node.bestChild()
    return selected_node

def expantion(self, node):
    return node.expand()

def playout(self, node):
    while node.game.notFinished:
        #random_action = random.choice(node.playableCards)
        #nextState = deepcopy(node.game)
        #nextState = nextState.play


def backpropagation(self, node, reward):
    child_utility  = node.utility
    while node != None:
        node.visits = node.visits + 1
        node.utility = node.utility + child_utility


def bestChild(self, node):
    bestChild = node.bestChild()
    return bestChild
