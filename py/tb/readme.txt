Description: Implementation of Hand Class for Poker Game:
------------------------------------------------------------------------------
VALUES = ['2','3','4','5','6','7','8','9','T', 'J', 'Q', 'K', 'A']
Where T = 10, J = 'Jack', Q = 'Queen', K = 'King' and A is 'Ace'
SUITS = ['C', 'D', 'H', 'S']
Where C = 'Clubs', D = 'Diamonds', H = 'Hearts' and S = 'Spades'.

Directory Structure of the Code:
	|
	|
	+----- lib
	|		|
	|		+------ util.py 	(shuffle, swap and qsort used for demo in test)
	|		|
	|		+------ constants.py	(all constants/global variables used)
	|
	|
	+------ readme.txt (this file)
	|
	|
	+------ poker_hand_tests.py (python unit tests for Card, Hand class)

Card:
	A custom class to represent the Card Number, Card Suit values as object.

Hand: 
	A class that creates an object from a given Hand string which could be 
	of the form:
	"<NS> <NS> <NS> <NS> <NS>"
	where N denotes a Card Numeral and S denotes first letter of suit.




Command line to Get a Category of a Hand String:
----------------------------------------------------------------------
C:\hand>python demo.py --hand "4D 4D 4D 7H 8D"
INFO:root:Details: <Hand ['4D 4D 4D 7H 8D'], 'Three Of A Kind', 4>



Command line Demo to run the tests:
----------------------------------------------------------------------
C:\hand>python poker_hand_tests.py
......................
----------------------------------------------------------------------
Ran 22 tests in 0.046s

OK