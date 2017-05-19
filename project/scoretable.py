from player import Player

MAX_BAGS = 10

class ScoreTable:

    def __init__(self, team):
        self.team = team
        self.totalBid = 0
        self.totalTricks = 0
        self.bags = 0
        self.score = 0

    def updateScoreTable(self):
        p1, p2 = self.team[0], self.team[1]
        self.checkNill()
        self.totalBid = p1.bet + p2.bet
        self.totalTricks = p1.trick + p2.trick
        if self.totalTricks < self.totalBid:
            self.score -= self.totalBid * 10
        elif self.totalTricks == self.totalBid:
            self.score += self.totalBid * 10
        elif self.totalTricks > self.totalBid:
            newBags = self.totalTricks - self.totalBid
            if self.bags + newBags >= MAX_BAGS:
                self.score -= 100
                self.bags = 0
            else:
                self.score += self.totalBid * 10 + newBags
                self.bags += newBags

    def checkNill(self):
        for p in self.team:
            if p.bet == 0:
                if p.trick == 0:
                    self.score += 100
                elif p.trick > 0:
                    self.score -= 100

    def toString(self):
        print("--------------------")
        print(self.team[0].name + " & " + self.team[1].name)
        print("Total Bid:", self.totalBid)
        print("Total Tricks:", self.totalTricks)
        print("Bags:", self.bags)
        print("Score:", self.score)
        print("--------------------")

    def reset(self):
        self.totalBid = 0
        self.totalTricks = 0
        self.bags = 0
        self.score = 0
