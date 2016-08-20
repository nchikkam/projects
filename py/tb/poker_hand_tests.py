import unittest
import random

from lib.poker import (
    Card,
    Hand
)
from lib.util import (
    shuffle,     # to test the sorting of hands
    qsort,
    swap
)

"""
    Tests to validate the functionality of the Card and Hand Classes.
"""
class TestHand(unittest.TestCase):

    """ Test Data For few cases"""
    input_and_expectations = [
        ('4D 4D 4D 7H 8D', [Card('4', 'D'), Card('4', 'D'), Card('4', 'D'), Card('7', 'H'), Card('8', 'D')], ''),
        ('4D 3D 3D 7H AD', [Card('4', 'D'), Card('3', 'D'), Card('3', 'D'), Card('7', 'H'), Card('A', 'D')], ''),
        ('TS JS QS KS AS', [Card('T', 'S'), Card('J', 'S'), Card('Q', 'S'), Card('K', 'S'), Card('A', 'S')], ''),
        ('5S 6S 7S 8S 9S', [Card('5', 'S'), Card('6', 'S'), Card('7', 'S'), Card('8', 'S'), Card('9', 'S')], ''),
        ('7S TC TH TS TD', [Card('7', 'S'), Card('T', 'C'), Card('T', 'H'), Card('T', 'S'), Card('T', 'D')], ''),
        ('5H 5C QD QC QS', [Card('5', 'H'), Card('5', 'C'), Card('Q', 'D'), Card('Q', 'C'), Card('Q', 'S')], ''),
        ('2D 3D 7D QD AD', [Card('2', 'D'), Card('3', 'D'), Card('7', 'D'), Card('Q', 'D'), Card('A', 'D')], ''),
        ('4D 5D 6D 7H 8D', [Card('4', 'D'), Card('5', 'D'), Card('6', 'D'), Card('7', 'H'), Card('8', 'D')], '')
    ]

    ordered_data = [
        ('TH JH QH KH AH', "Royal Flush", 10),
        ('8D 9D TD JD QD', "Straight Flush", 9),
        ('9S 9H 9C 9D TC', "Four Of A Kind", 8),
        ('KH KC KD TC TD', "Full House", 7),
        ('2D 6D 8D JD QD', "Flush", 6),
        ('5D 6S 7C 8H 9H', "Straight", 5),
        ('8S 8D 8C 2H 5C', "Three Of A Kind", 4),
        ('9H 9D 5S 5C 3D', "Two Pair", 3),
        ('6D 6C 8S 5H TD', "One Pair", 2),
        ('QS 3D 7H TC 6D', "High Card", 1)
    ]

    """regression data """
    regression_data = [
        ('4D 4D 4D 7H 8D', "Three Of A Kind"),
        ('4D 3D 3D 7H AD', "One Pair"),
        ('TS JS QS KS AS', "Royal Flush"),  # Royal Flush - sequence with same suit
        ('5S 6S 7S 8S 9S', "Straight Flush"),
        ('7S TC TH TS TD', "Four Of A Kind"),
        ('5H 5C QD QC QS', "Full House"),
        ('2D 3D 7D QD AD', "Flush"),
        ('4D 5D 6D 7H 8D', "Straight"),
        ('2H 2D 2C KC QD', "Three Of A Kind"),
        ('2H 5H 7D 8C 9S', "High Card"),
        ('AH 2D 3C 4C 5D', "Straight"),
        ('2H 3H 2D 3C 3D', "Full House"),
        ('2H 7H 2D 3C 3D', "Two Pair"),
        ('2H 7H 7D 7C 7S', "Four Of A Kind"),
        ('TH JH QH KH AH', "Royal Flush"),
        ('4H 4S KS 5D TS', "One Pair"),
        ('QC TC 7C 6C 4C', "Flush"),
        ('TS JS QS KS AS', "Royal Flush"),
        ('TH JH QH KH AH', "Royal Flush"),
        ('3C 4C 5C 6C 7C', "Straight Flush"),
        ('8D 9D TD JD QD', "Straight Flush"),
        ('9S 9H 9C 9D TC', "Four Of A Kind"),
        ('QS QH QC QD 8S', "Four Of A Kind"),
        ('JS JH JD 4S 4C', "Full House"),
        ('KH KC KD TC TD', "Full House"),
        ('3S 5S 8S TS KS', "Flush"),
        ('2D 6D 8D JD QD', "Flush"),
        ('3S 4D 5S 6H 7C', "Straight"),
        ('5D 6S 7C 8H 9H', "Straight"),
        ('6D 6S 6C KC 4H', "Three Of A Kind"),
        ('8S 8D 8C 2H 5C', "Three Of A Kind"),
        ('4D 4H 7S 7C 9S', "Two Pair"),
        ('9H 9D 5S 5C 3D', "Two Pair"),
        ('8S 8H 3D KC 7S', "One Pair"),
        ('6D 6C 8S 5H TD', "One Pair"),
        ('9S TD 4S 6H KC', "High Card"),
        ('QS 3D 7H TC 6D', "High Card")
    ]

    """ function to test that given string is being parsed properly by Hand Ctor"""
    def test_Hand_constructor_with_string_inputs(self):
        for input_exp in self.input_and_expectations:
            inp, expected, typ = input_exp
            h = Hand(inp)
            for c, e in zip(h.cards, expected):
                self.assertTrue(c.is_same_card(e))

    """ Verify the given Cards fall under flush category"""
    def test_straight_flush(self):
        h = Hand('TH JH QH KH AH')
        self.assertTrue(h.is_straight_flush())

    """ Verify the given Cards fall under two pair category"""
    def test_two_pair(self):
        h = Hand('2H 7H 2D 3C 3D')
        self.assertTrue(h.is_two_pair())

    """ Verify the given Cards fall under one pair category"""
    def test_one_pair(self):
        h = Hand('4H 4S KS 5D TS')
        self.assertTrue(h.is_one_pair())

    """ Verify the given Cards fall under threee fo a kind category"""
    def test_three_of_a_kind(self):
        h = Hand('2H 2D 2C KC QD')
        self.assertTrue(h.is_three_of_a_kind())

    """ Verify the given Cards fall under straight category"""
    def test_straight(self):
        h = Hand('AH 2D 3C 4C 5D')
        self.assertTrue(h.is_straight())

    """ Verify the given Cards fall under flush category"""
    def test_flush(self):
        h = Hand('QC TC 7C 6C 4C')
        self.assertTrue(h.is_flush())

    """ Verify the given Cards fall under full house category"""
    def test_full_house(self):
        h = Hand('2H 3H 2D 3C 3D')
        self.assertTrue(h.is_fullhouse())

    """ Verify the given Cards fall under four of a kind category"""
    def test_four_of_a_kind(self):
        h = Hand('2H 7H 7D 7C 7S')
        self.assertTrue(h.is_four_of_a_kind())

    """ Verify the given Cards fall under hight card category"""
    def test_is_highcard(self):
        h = Hand('2H 5H 7D 8C 9S')
        self.assertTrue(h.is_highcard())

    """ Verify regressions """
    def test_get_category(self):
        for d in self.regression_data:
            s, exp = d
            h = Hand(s)
            self.assertEqual(exp, h.get_category())

    """ verify ranks are reported properly """
    def test_ranks(self):
        for h, n, r in self.ordered_data:
            h = Hand(h)
            self.assertEqual(h.rank, r)

    """
        verify string represention of Hand Object
        eg:
            <hand [TS, JS, QS, KS, AS], 'Royal Flush'>
    """
    def test_to_string_method(self):
        h = Hand('4D 5D 6D 7H 8D')
        self.assertEqual(
            "<Hand ['4D 5D 6D 7H 8D'], 'Straight', 5>",
            h.__str__()
        )

    """
        verify comparision works on Hand() class objects.
        [Note:]
        python 2.7 __cmp__ is supported,
        python 3.x __cmp__ is not supported but __[l|g][t|e|]__ are supported
    """
    def test_cmp_method(self):
        high_card = Hand('QS 3D 7H TC 6D')
        straight = Hand('4D 5D 6D 7H 8D')

        self.assertTrue(high_card < straight)
        self.assertTrue(straight > high_card)

        dummy = Hand('QS 3D 7H TC 6D')
        self.assertTrue(dummy == high_card)
        self.assertFalse(dummy == straight)
        self.assertTrue(dummy!=straight)

    """
        verify the quantitative points value of a hand
        this is useful in case of two hands having same rank
    """
    def test_winner_incase_of_one_pair_hands(self):
        player_one = Hand('5H 5C 6S 7S KD')    # 5, 5
        player_two = Hand('2C 3S 8S 8D TD')    # 8, 8 => This hand has High Points as per Poker Rules
        self.assertTrue(
            player_one.rank == player_two.rank and
            player_two.get_points() > player_one.get_points()
        )

    def test_winner_incase_of_two_pair_harnds(self):
        player_one = Hand('9D 9H 6C 8S 8C')  # (9, 9),(8, 8) => has high points
        player_two = Hand('2D 2H 6C 8S 8C')  # (2, 2),(8, 8)
        self.assertTrue(
            player_one.rank == player_two.rank and
            player_two.get_points() < player_one.get_points()
        )

    def test_winner_incase_of_three_of_a_kind(self):
        player_one = Hand('8S 8D 8C 2H 5C')    #(8, 8, 8) => has high value
        player_two = Hand('AS AD AC 2H 5C')    #(A, A, A)
        self.assertTrue(
            player_one.rank == player_two.rank and
            player_one.get_points() > player_two.get_points()
        )

    def test_winner_incase_of_full_house(self):
        player_one = Hand('KH KC KD TC TD')    #(K, K, K)  => has high points
        player_two = Hand('QH QC QD TC TD')    #(Q, Q, Q)
        self.assertTrue(
            player_one.rank == player_two.rank and
            player_one.get_points() > player_two.get_points()
        )

    def test_winner_incase_of_four_of_a_kind(self):
        player_one = Hand('9S 9H 9C 9D TC')    # (9,9,9,9) => has high points
        player_two = Hand('3S 3H 3C 3D TC')    # (3,3,3,3)
        self.assertTrue(
            player_one.rank == player_two.rank and
            player_one.get_points() > player_two.get_points()
        )

    def test_draw_condition(self):
        player_one = Hand('9S 9H 9C 9D TC')     # (9,9,9,9)  => same value
        player_two = Hand('9S 9H 9C 9D TC')     # (9,9,9,9)  => same value
        self.assertTrue(
            player_one.rank == player_two.rank and
            player_one.get_points() == player_two.get_points()
        )

    """
        verify the > operator works on Hand Class, uses qsort
        that actuall does the comparision using '>' to sort the
        Hands in Descending order of their defined ranks.
    """
    def test_sorting_harnds(self):
        expected = [
            ('TH JH QH KH AH', "Royal Flush", 10),
            ('8D 9D TD JD QD', "Straight Flush", 9),
            ('9S 9H 9C 9D TC', "Four Of A Kind", 8),
            ('KH KC KD TC TD', "Full House", 7),
            ('2D 6D 8D JD QD', "Flush", 6),
            ('5D 6S 7C 8H 9H', "Straight", 5),
            ('8S 8D 8C 2H 5C', "Three Of A Kind", 4),
            ('9H 9D 5S 5C 3D', "Two Pair", 3),
            ('6D 6C 8S 5H TD', "One Pair", 2),
            ('QS 3D 7H TC 6D', "High Card", 1)
        ]

        hands = []
        for hand in expected:
            hands.append(Hand(hand[0]))

        hands = shuffle(hands)
        qsort(hands, 0, len(hands) - 1)

        for exp, card in zip(expected, hands):
            self.assertEqual(exp[0], card.cards_repr())
            self.assertEqual(exp[1], card.get_category())
            self.assertEqual(exp[2], card.rank)

class QsortTest(unittest.TestCase):
    def generateData(self):
        data = []
        for i in range(15):
            data.append(random.randrange(100))
        return data

    def testQsort(self):
        for i in range(40):
            data = self.generateData()
            qsort(data, 0, len(data)-1)
            for i in range(1, len(data)):
                self.assertTrue(data[i-1] >= data[i])


if __name__ == "__main__":
    unittest.main()