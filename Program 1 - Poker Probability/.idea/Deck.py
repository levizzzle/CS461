import random

class Deck:
    deck = []

    def __init__(self):
        cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suits = ['S','H','D','C']
        for suit in suits:
            for card in cards:
                self.deck.append(card+suit)
        self.shuffleDeck()

    def showCards(self):
        for card in self.deck:
            print(card)

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def showDeckSize(self):
        print('The deck has ', len(self.deck), ' cards remaining.\n')

    def dealHand(self):
        hand = []
        numCards = range(0,5)

        for card in numCards:
            hand.append(self.deck.pop())
        return hand

    def addCardsToDeck(self, hand):
        for card in hand:
            self.deck.append(card)