from card import Card
from deck import Deck
from player import Player
from table import Table
from scoretable import ScoreTable
import random

GAME_TRICKS = 13
WINNING_SCORE = 500
PLAYERS_NUMBER = 4

def bets(players, first_player):
    for i in range(PLAYERS_NUMBER):
        print(players[(first_player + i) % 4].printHand())
        print("Player", players[(first_player + i) % 4].name, "place your bet (0 to 13)");
        players[(first_player + i) % 4].setBet(input())

def trick(players, first_player, table):
    for i in range(PLAYERS_NUMBER):
        playHuman(players[(first_player + i) % 4], table)

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
    #Show players hand
    print("Your Cards", player.name, ": ")
    player.printHand()

    #Show possible plays
    if len(table.plays) == 0:
        playableCards = player.eligablePlay(table.isTrumped)
    elif len(table.plays) > 0:
        playableCards = player.eligablePlay(table.isTrumped, table.plays[0][1].suit)

    #Select a playable card
    print("Select a card (number) to play: ")
    c_index = int(input())
    while (not (0 < c_index and c_index <= len(player.getHand()))) or player.hand[c_index - 1] not in playableCards:
        print("Please choose a playable card: ")
        c_index = int(input())
    real_index = c_index - 1

    #Check for Spades
    if player.hand[real_index].isSpades():
        table.isTrumped = True
    #Update table and player
    table.layDownCard(player, player.getHand()[real_index])
    player.playCard(player.getHand()[real_index])

def playAi():
    1

def game():

    players = createPlayers()
    deck = Deck()
    table = Table()
    dealer = firstDealer()
    teamA = ScoreTable((players[0], players[2]))
    teamB = ScoreTable((players[1], players[3]))

    #Game routine
    while teamA.score < WINNING_SCORE or teamB.score < WINNING_SCORE:
        first_player = calculateFirstPlayer(dealer)
        dealNshuffle(deck, players)
        bets(players, first_player)
        for i in range(GAME_TRICKS):
            trick(players, first_player, table)
            print(table.toString())

            player_win = table.checkWinner()
            first_player = players.index(player_win)
            table.resetCards()
        table.reset()

        teamA.updateScoreTable()
        teamB.updateScoreTable()
        dealer = nextDealer(dealer)

        teamA.toString()
        print()
        teamB.toString()

game()