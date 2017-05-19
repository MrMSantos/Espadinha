from copy import deepcopy
import numpy as np

SIMULATION_THRESHOLD = 15

class MCTS:

    self.root = None

    def __init__(self, root, max_depth):
        self.root = root
        self.depth = 0
        self.max_depth

    def search(self):
        while (self.depth < self.max_depth):

            next_node = selection(self.root)

            for i in range(SIMULATION_THRESHOLD):
                reward = playout(next_node)
                backpropagation(next_node, reward)

        return bestChild(self.root).action

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
        return node.playout()

    def backpropagation(self, node, reward):
        child_utility  = node.utility
        while node != None:
            node.visits = node.visits + 1
            node.utility = node.utility + child_utility

    def bestChild(self, node):
        bestChild = node.bestChild()
        return bestChild
