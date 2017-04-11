
from player import player
import deck as d

def bets(players):
    for player in players:
        print('Place your bet (0 to 13):')
        player.setBet(input())


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

def game():

    players = createPlayers()
    scoreTable = {players[0].name + ' & ' + players[2].name : [0,0], players[1].name + ' & ' + players[3].name : [0,0]}
    deck = d.create()

    #Game routine
    while 1:

        dealNshuffle(deck, players)
        bets(players)

game()
