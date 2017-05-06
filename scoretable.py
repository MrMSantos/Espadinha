from player import Player

class ScoreTable:

    def __init__(self, team):
        self.team = team
        self.totalBid = 0
        self.totalTricks = 0
        self.bags = 0
        self.score = 0

    def updateScoreTable(self, p1, p2):
        checkNill(p1)
        checkNill(p2)
        self.totalBid = p1.bid + p2.bid
        self.totalTricks = p1.trick + p2.trick
        if self.totalTricks < self.totalBid:
            self.score -= self.totalBid * 10
        elif self.totalTricks == self.totalBid:
            self.score += self.totalBid * 10
        elif self.totalTricks > self.totalBid:
            newBags = self.totalTricks - self.totalBid
            if self.bags + newBags > 10:
                self.score -= 100
                self.bags = 0
            else:
                self.score += self.totalBid * 10 + newBags
                self.bags += newBags

    def checkNill(self, p):
        if p.bid == 0:
            if p.trick == 0:
                self.score += 100
            elif p.trick > 0:
                self.score -= 100