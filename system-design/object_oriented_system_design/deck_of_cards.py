from enum import Enum
import random

class Deck(object):
    def __init__(self, cards):
        self.cards = cards
        self.index = 0

    def remaining(self):
        return len(self.cards) - self.index
    
    def deal_card(self):
        if not self.remaining():
            return None

        card = self.cards[self.index]
        card.is_available = False
        self.index += 1
        return card
    
    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

class Hand(object):
    def __init__(self, cards):
        self.cards = cards

    def add(self, card):
        self.cards.append(card)

    def score(self):
        total_value = 0
        for card in self.cards:
            total_value += card.value
        return total_value

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.is_available = True

class Suit(Enum):
    HEART = 0
    DIAMOND = 1
    CLUBS = 2
    SPADE = 3