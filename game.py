
from player import player
import deck as d
import random

GAME_TRICKS = 13

def bets(players, first_player):
    betTable = {}
    for i in range(4):
        print("Player ", i +1, " place your bet");
        players[(first_player + i) % 4].setBet(input())
    for player in players:
        betTable["player.name"] = player.getBet()
    return betTable




def dealNshuffle(deck, players):
    d.shuffle(deck)
    h1, h2, h3, h4 = d.deal(deck)
    players[0].setHand(h1)
    players[1].setHand(h2)
    players[2].setHand(h3)
    players[3].setHand(h4)


def createPlayers():
    print('Insert name: ')
    p1 = player(input())
    print('Insert name: ')
    p2 = player(input())
    print('Insert name: ')
    p3 = player(input())
    print('Insert name: ')
    p4 = player(input())

    return (p1, p2, p3, p4)

def firstDealer():
    return random.randint(0, 3)

def nextDealer(previous_dealer):
    return (previous_dealer + 1) % 4

def calculateFirstPlayer(dealer):
    return (dealer - 3) % 4


def playHuman(player):
    for card in player.getHand():
        print()


def playAi():
    1



def game():

    players = createPlayers()
    scoreTable = {players[0].name + ' & ' + players[2].name : [0,0], players[1].name + ' & ' + players[3].name : [0,0]}
    deck = Deck()
    table = Table()
    dealer = firstDealer()
    first_player = calculateFirstPlayer(dealer)

    #Game routine
    while True:
        dealNshuffle(deck, players)
        betTable = bets(players, first_player)
        for i in range(GAME_TRICKS):
            for player in players:
                play()
        table.checkWinner()


        dealer = nextDealer(dealer)
game()
