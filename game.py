
from player import Player
from deck import Deck
from table import Table
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
    deck.shuffle()
    h1, h2, h3, h4 = deck.deal()
    players[0].setHand(h1)
    players[1].setHand(h2)
    players[2].setHand(h3)
    players[3].setHand(h4)


def createPlayers():
    print('Insert name: ')
    p1 = Player(input())
    print('Insert name: ')
    p2 = Player(input())
    print('Insert name: ')
    p3 = Player(input())
    print('Insert name: ')
    p4 = Player(input())

    return (p1, p2, p3, p4)

def firstDealer():
    return random.randint(0, 3)

def nextDealer(previous_dealer):
    return (previous_dealer + 1) % 4

def calculateFirstPlayer(dealer):
    return (dealer - 3) % 4


def playHuman(player, table):
    print("Your Cards : ")
    i = 1
    #getting them possibilities
    for card in player.getHand():
        print(i, " - ", card.toString(), " ")
        i+=1
    print("\n")
    print("Select a card (number) to play\n")
    c_index = int(input())
    while (not (0 < c_index and c_index <= len(player.getHand()))):
        c_index = int(input())
    real_index = c_index - 1
    table.layDownCard(player, player.getHand()[real_index])
    player.playCard(player.getHand()[real_index])








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
                playHuman(player, table)
            print(table.checkWinner().getName()," was the winner!")
            print(table.toString())
            table.reset()


        dealer = nextDealer(dealer)
game()
