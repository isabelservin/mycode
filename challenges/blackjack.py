#!/usr/bin/env python3

#import random module
import random

#create a deck of cards
deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]

#create hands for player and dealer
p1Hand = []
dealerHand = []

#deal the deck and append the hand
def deal(player):
    card = random.choice(deck)
    player.append(card)
    deck.remove(card)
    print(card)

