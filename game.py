from card import Card
from deck import Deck
from player import Player
from human_player import HumanPlayer
from random_player import RandomPlayer
from rulebased_player import RuleBasedPlayer
from table import Table
from scoretable import ScoreTable
import random

GAME_TRICKS = 13
WINNING_SCORE = 500
PLAYERS_NUMBER = 4

def createPlayers():
    print("--- Welcome to Espadinha! ---\n")
    print('Please insert your name: ')
    p1 = HumanPlayer(input())
    p3 = RuleBasedPlayer("Bot 3")
    p2 = RuleBasedPlayer("Bot 2")
    p4 = RuleBasedPlayer("Bot 4")
    return (p1, p2, p3, p4)

def dealNshuffle(deck, players):
    deck.shuffle()
    h1, h2, h3, h4 = deck.deal()
    players[0].reset()
    players[0].hand = h1
    players[0].orderHand()
    players[1].reset()
    players[1].hand = h2
    players[1].orderHand()
    players[2].reset()
    players[2].hand = h3
    players[2].orderHand()
    players[3].reset()
    players[3].hand = h4
    players[3].orderHand()

def bets(players, first_player):
    print("--- BIDDING ---")
    for i in range(PLAYERS_NUMBER):
        players[(first_player + i) % 4].bidding()

def trick(players, first_player, table):
    for i in range(PLAYERS_NUMBER):
        players[(first_player + i) % 4].play(table)
        print(table.toString())

def firstDealer():
    return random.randint(0, 3)

def nextDealer(previous_dealer):
    return (previous_dealer + 1) % 4

def calculateFirstPlayer(dealer):
    return (dealer - 3) % 4

def game():
    players = createPlayers()
    deck = Deck()
    table = Table()
    dealer = firstDealer()
    teamA = ScoreTable((players[0], players[2]))
    teamB = ScoreTable((players[1], players[3]))

    #Game routine
    while teamA.score < WINNING_SCORE and teamB.score < WINNING_SCORE:
        first_player = calculateFirstPlayer(dealer)
        dealNshuffle(deck, players)
        bets(players, first_player)
        for i in range(GAME_TRICKS):
            trick(players, first_player, table)

            player_win = table.checkWinner()
            first_player = players.index(player_win)
            table.resetCards()
        table.reset()

        teamA.updateScoreTable()
        teamB.updateScoreTable()
        dealer = nextDealer(dealer)

        teamA.toString()
        teamB.toString()

game()