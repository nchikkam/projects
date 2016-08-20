""" This file holds the constants and definitions of Global Variables used """

SUITS = {
    "H":    "Hearts",
    "S":    "Spades",
    "D":    "Diamonds",
    "C":    "Clubs"
}

_A = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")

A_ = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K")

VALUES = {
    'Royal Flush' :     10, # these values define the ranking order of the Hand[5 cards]
    'Straight Flush':   9,
    'Four Of A Kind':   8,
    'Full House':       7,
    'Flush':            6,
    'Straight':         5,
    'Three Of A Kind':  4,
    'Two Pair':         3,
    'One Pair':         2,
    'High Card':        1
}

LETTERS_MAP = {  # since we are using T,Q,K,J,A, we need this mapping
    'T': '10',
    'J': '11',
    'Q': '12',
    'K': '13',
    'A': '1'  # default one
}

