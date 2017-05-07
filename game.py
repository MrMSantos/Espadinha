
from player import Player
from deck import Deck
from table import Table
from scoretable import ScoreTable
import random

GAME_TRICKS = 13

def bets(players, first_player):
    betTable = {}
    for i in range(4):
        print("Player", i + 1, "place your bet (0 to 13)");
        players[(first_player + i) % 4].setBet(input())
    for player in players:
        betTable["player.name"] = player.getBet()
    return betTable

def dealNshuffle(deck, players):
    deck.shuffle()
    h1, h2, h3, h4 = deck.deal()
    players[0].setHand(h1)
    players[0].orderHand()
    players[1].setHand(h2)
    players[1].orderHand()
    players[2].setHand(h3)
    players[2].orderHand()
    players[3].setHand(h4)
    players[3].orderHand()


def createPlayers():
    print('Insert name player 1: ')
    p1 = Player(input())
    print('Insert name player 2: ')
    p2 = Player(input())
    print('Insert name player 3: ')
    p3 = Player(input())
    print('Insert name player 4: ')
    p4 = Player(input())
    return (p1, p2, p3, p4)

def firstDealer():
    return random.randint(0, 3)

def nextDealer(previous_dealer):
    return (previous_dealer + 1) % 4

def calculateFirstPlayer(dealer):
    return (dealer - 3) % 4


def playHuman(player, table):
    #Show all hand
    print("Your Cards", player.name, ": ")
    player.printHand()
    playableCards = player.eligablePlay(player, )


    print("Select a card (number) to play: ")
    c_index = int(input())
    while not (0 < c_index and c_index <= len(player.getHand())):
        c_index = int(input())
    real_index = c_index - 1
    
    table.layDownCard(player, player.getHand()[real_index])
    player.playCard(player.getHand()[real_index])

def playAi():
    1

def game():

    players = createPlayers()
    deck = Deck()
    table = Table()
    dealer = firstDealer()
    first_player = calculateFirstPlayer(dealer)
    teamA = ScoreTable(players[0].name + ' & ' + players[2].name)
    teamB = ScoreTable(players[1].name + ' & ' + players[3].name)

    #Game routine
    while True:
        dealNshuffle(deck, players)
        betTable = bets(players, first_player)
        for i in range(GAME_TRICKS):
            for player in players:
                playHuman(player, table)

            teamA.updateScoreTable(players[0], players[2])
            teamB.updateScoreTable(players[1], players[3])
            print(table.checkWinner().getName(),"gets the trick")
            print(table.toString())
            table.reset()
        dealer = nextDealer(dealer)

game()