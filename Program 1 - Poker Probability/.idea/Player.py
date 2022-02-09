from Tools import Tools

class Player:
    hand = []
    name = ''

    def __init__(self, hand, name):
        self.hand = hand
        self.name = name

    def showCards(self):
        print('Cards in hand:\n', self.hand, '\n')

    def handRank(self, combo, value):
        combos = {'no pair':0, 'one pair':1, 'two pair':2, 'three of a kind':3, 'straight':4,
                  'flush':5, 'full house':6, 'four of a kind':7, 'straight flush':8, 'royal flush':9}
        values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}

        rank = combos[combo] + (values[value]/100)

    def showHand(self):
        return self.hand

    # def sortHand(self):
    #     suits = []
    #     [suits.append(card[-1:]) for card in self.hand]
    #
    #     temp = self.hand
    #     valueHand = Tools.castValue(temp)
    #     stringHand = Tools.castString(valueHand)
    #
    #     sortedHand = []
    #     for card in range(len(stringHand)):
    #         sortedHand.append(stringHand[card] + suits[card])
    #
    #     return sortedHand