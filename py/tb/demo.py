import argparse
import logging

from lib.poker import (
    Hand
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Calculate Category of A Poker Hand')

    parser.add_argument('--hand', help='flag to pass poker hand string to the Hand Class')

    args = parser.parse_args()

if  args.hand :
    hand = Hand(args.hand)
    logging.info("Details: " + hand.__str__())
else:
    logging.info("Please pass all the positional Arguments and try again.")