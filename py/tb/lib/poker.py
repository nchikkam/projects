from .constants import (
    A_,         # prefixes 'A' to represent A as 1
    _A,         # postfixes 'A' to represent A as 14
    VALUES,     # Rank Values for all 10 Hands
    SUITS,      # Letter to Suit Names Map
    LETTERS_MAP
)

""" Basic Card class to represent Card(Number, Suit)"""
class Card:
    def __init__(self, numeral, suit):
        self.numeral = numeral
        self.suit = suit

    def __str__(self):
        return "{0}{1}".format(self.numeral, self.suit)

    def is_same_card(self, another):
        if self.numeral == another.numeral and self.suit == another.suit:
            return True
        return False

    def get_suit_name(self):
        return SUITS[self.suit]


""" Hand Class to encapsulate various management activities on a Hand object"""
class Hand:
    """ ctor method that parses a given string into hand object for easy maintenance"""
    def __init__(self, cards_string):
        self.cards = self.parse_cards_from_string(cards_string)
        self.numbers = {}       # map to hold unique numeral in the hand
        self.suits = {}         # map to hold unique suit names in hand
        for card in self.cards:
            self.numbers[card.numeral] = self.numbers.get(card.numeral, 0) + 1
            self.suits[card.suit] = self.numbers.get(card.suit, 0) + 1

        self.categories = (     # container that is used to iterate to verify category of self card
            self.is_royal_flush,
            self.is_straight_flush,
            self.is_four_of_a_kind,
            self.is_fullhouse,
            self.is_flush,
            self.is_straight,
            self.is_three_of_a_kind,
            self.is_two_pair,
            self.is_one_pair,
            self.is_highcard
        )

        self.category = self.get_category()      # category of the card
        self.rank = VALUES[self.category]        # its corresponding number rank
        # update letters map for points calculation
        LETTERS_MAP['A'] = '1' if '2' in self.numbers else '14'

    """ parses the string into a list """
    def parse_cards_from_string(self, cards_string):
        cards_str_list = cards_string.split(' ')
        cards = []
        for card_str in cards_str_list:
            card_no = card_str[0]
            card_st = card_str[1]
            cards.append(Card(card_no, card_st))
        return cards

    """ compses string representation for cards """
    def cards_repr(self):
        cards = ""
        for c in self.cards:
            cards += "{0} ".format(c)
        return cards.strip()

    def __str__(self):
        return "<{0} ['{1}'], '{2}', {3}>".format(
            self.__class__.__name__,
            self.cards_repr(),
            self.category,
            self.rank
        )

    def __repr__(self):
        return "<{0} ['{1}'], '{2}', {3}>".format(
            self.__class__.__name__,
            self.cards_repr(),
            self.category,
            self.rank
        )


    """ compares a given hand object to current one and returns -1/0/1 based on standard 'C' strcmp version """
    def __cmp__(self, other):  # support for python 2.x, in python 3 there is no __cmp__
        if type(other) == Hand:
            if self.rank < other.rank: return -1
            if self.rank > other.rank: return  1
            return 0
        else:
            raise TypeError("Hand cannot be compared to %s" % str(type(other)))

    def __lt__(self, other): # less than operator
        if type(other) == Hand:
            if self.rank < other.rank: return True
            return False
        else:
            raise TypeError("Hand cannot be compared to %s" % str(type(other)))

    def __le__(self, other): # less than or equal to operator
        if type(other) == Hand:
            if self.rank <= other.rank: return True
            return False
        else:
            raise TypeError("Hand cannot be compared to %s" % str(type(other)))

    def __gt__(self, other):   # greater than operator
        if type(other) == Hand:
            if self.rank > other.rank: return True
            return False
        else:
            raise TypeError("Hand cannot be compared to %s" % str(type(other)))

    def __eq__(self, other): # equal to operator
        if type(other) == Hand:
            if self.rank == other.rank: return True
            return False
        else:
            raise TypeError("Hand cannot be compared to %s" % str(type(other)))

    def __ne__(self, other): # not equal to operator
        if type(other) == Hand:
            if self.rank != other.rank: return True
            return False
        else:
            raise TypeError("Hand cannot be compared to %s" % str(type(other)))

    def is_one_pair(self):
        """
            checker to see if current hand is a one pair catergory
        :return: return 'One Pair' if there is only one pair or nums
        """
        pairs = [num for num in self.numbers if self.numbers[num] == 2]
        if len(pairs) == 1:
            return 'One Pair'
        return False

    def is_two_pair(self):
        """
            checker to see if current hand is a two pair catergory
        :return: return "Two Pair" if there are 2 suits with same num
        """
        pairs = [num for num in self.numbers if self.numbers[num] == 2]
        if len(pairs) == 2:
            return 'Two Pair'
        return False

    def is_three_of_a_kind(self):
        """
            checker to see if current hand is a three of a kind catergory
        :return: return "Three of A Kind" if there there are 3 suits with same num
        """
        if len(self.numbers) <= 2:
            return False
        for num in self.numbers:
            if self.numbers[num] == 3:
                return 'Three Of A Kind'
        return False

    def is_four_of_a_kind(self):
        """
            checker to see if current hand is a four of a kind catergory
        :return: return "Three of A Kind" if there there are 3 suits with same num
        """
        if len(self.numbers) != 2:
            return False
        for num in self.numbers:
            if self.numbers[num] == 4:
                return 'Four Of A Kind'
        return False

    def is_flush(self):
        """
        :return: return flush if current hand comes under flush category
        """
        if len(self.suits) == 1:
            return 'Flush'
        return False

    def is_royal_flush(self):
        """ checks if current hand is royal flush category"""
        if len(self.suits) == 1 and set(self.numbers.keys()) == set(['T', 'J', 'Q', 'K', 'A']):
            return "Royal Flush"
        return False

    def is_fullhouse(self):
        """ checks if hand is full house category"""
        if len(self.numbers) != 2:
            return False
        for num in self.numbers:
            if self.numbers[num] == 3:
                return 'Full House'
        return False

    def is_straight_flush(self):
        """ checks for straight flush category """
        n = A_ if '2' in self.numbers else _A
        s = ' '.join(n)
        d = sorted(self.cards, key=lambda card: (n.index(card.numeral), card.suit))
        first, rest = d[0], d[1:]
        if (all(card.suit == first.suit for card in rest) and
                    ' '.join(card.numeral for card in d) in s):
            return 'Straight Flush'
        return False

    def is_straight(self):
        """ checks if current hand is straight category """
        n = A_ if '2' in self.numbers else _A
        s = ' '.join(n)
        d = sorted(self.cards, key=lambda card: (n.index(card.numeral), card.suit))
        if ' '.join(card.numeral for card in d) in s:
            return 'Straight'
        return False

    def is_highcard(self):
        """ checks if current hand is any of the defined categories, if none
            mathc, sets the category to highhand
        """
        for fun in self.categories:
            if fun.__name__ == 'is_highcard':
                continue
            if fun():
                return False
        return 'High Card'

    def get_category(self):
        """returns the category of the current hand"""
        for fun in self.categories:
            category = fun()
            if category:
                return category
        return self.is_highcard()

    def get_points(self):
        """
            The Necessity of this method is to compare players by points
            when their hands result in same category.
            formala used in Standard Poker Games:
            H * 13**5 + F1 * 13**4 + F2 * 13**3 + F3 * 13**2 + F4 * 13 + F5
            where
            H           is the rank of the hand (Category-Rank)
            F[1..5]     are Card Numeral
        :return: A number that is calculated using above formula.
        """
        def create_numbers(l):
            """Helper method to create numbers from card face values for points
            :param l: list
            :param A: value of A to be used, either 1 or 14
            :return:  array with descending order of the values
            """
            ret = []
            for v in l:
                ret.append(LETTERS_MAP.get(v, v))
            return ret

        if self.category == "One Pair":
            """F1 and F2 are the ranks of the pair of cards having the
            same rank. F3, F4, and F5 are the ranks of the side cards
            from highest to lowest rank.
            """
            c =[]
            pairs = [num for num in self.numbers if self.numbers[num] == 2]
            c.append(pairs[0]) # F1
            c.append(pairs[0]) # F2
            l = create_numbers(set(self.numbers.keys()) - set(c[0]))
            l = list(map(int, l))
            rest = sorted(l, reverse=True)
            c = c + rest

        elif self.category == "Two Pair":
            """F1 and F2 are the ranks of the first and higher ranking pair.
            F3 and F4 are the ranks of the second and lower ranking pair.
            F5 is the rank of the remaining side card.
            """
            pairs = [num for num in self.numbers if self.numbers[num] == 2]
            rest =  [num for num in self.numbers if self.numbers[num] == 1]
            a, b = pairs
            mx = max(a, b)
            mn = min(a, b)
            c = [mx, mx, mn, mn,rest[0]]
            c = create_numbers(c)
            c = list(map(int, c))

        elif self.category == "Three Of A Kind":
            """F1, F2, and F3 are the ranks of the three cards of the same rank
            and F4 and F5 are the ranks of the remaining cards where F4 has
            higher rank than F5.
            """
            triple = [num for num in self.numbers if self.numbers[num] == 3]
            rest =   [num for num in self.numbers if self.numbers[num] == 1]
            t = triple[0]
            c = [t, t, t, max(rest), min(rest)]
            c = create_numbers(c)
            c = list(map(int, c))

        elif self.category == "Full House":
            """F1, F2, and F3 are the ranks of the three cards having the same rank
            and F4 and F5 are the ranks of the two remaining cards having the
            same rank.
            """
            triple = [num for num in self.numbers if self.numbers[num] == 3]
            pair   = [num for num in self.numbers if self.numbers[num] == 2]
            t = triple[0]
            c = [t, t, t, pair[0], pair[0]]
            c = create_numbers(c)
            c = list(map(int, c))

        elif self.category == "Four Of A Kind":
            """c1, c2, c3, and c4 are the ranks of the four of a kind cards and
            c5 is the side card.
            """
            quin    =  [num for num in self.numbers if self.numbers[num] == 4]
            single  =  [num for num in self.numbers if self.numbers[num] == 1]
            t = quin[0]
            c = [t, t, t, t, single[0]]
            c = create_numbers(c)
            c = list(map(int, c))

        points = self.rank * 13 ** 5
        for p, x in zip(map(int, c), [4, 3, 2, 1, 0]):
            points += p * 13 ** x
        return points

