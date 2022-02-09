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

class Ranker:

    def rankHand(self, hand):
        self.checkCombo(hand)

    def checkCombo(self, hand):
        noPair = False
        onePair = self.checkOnePair(hand)
        twoPair = self.checkTwoPair(hand)
        threeOfAKind = self.checkThreeOfAKind(hand)
        straight = self.checkStraight(hand)
        flush = self.checkFlush(hand)
        fullHouse = self.checkFullHouse(hand)
        fourOfAKind = self.checkFourOfAKind(hand)
        straightFlush = (straight == flush)
        royalFlush = False

        if flush and (self.castValue(self.sortHand(hand)) == [10,11,12,13,14]):
            royalFlush = True

        print('No pair: ', noPair,'\nOne Pair: ', onePair, '\nTwo pair: ', twoPair, '\nThree of a kind: ', threeOfAKind,
              '\nStraight: ', straight, '\nFlush: ', flush, '\nFull house: ', fullHouse,
              '\nFour of a kind: ', fourOfAKind, '\nStraight Flush: ', straightFlush, '\nRoyal flush: ', royalFlush)


    def checkFlush(self, hand):
        suits = []
        [suits.append(card[-1:]) for card in hand if card[-1:] not in suits]

        return len(suits) == 1

    def checkStraight(self, hand):
        valueHand = self.castValue(hand)

        firstCard = valueHand[0]
        straightHand = [firstCard, firstCard + 1, firstCard + 2, firstCard + 3, firstCard + 4]

        return valueHand == straightHand

    def checkFullHouse(self, hand):
        valueHand = self.castValue(hand)

        values = []
        [values.append(card) for card in valueHand if card not in values]

        if len(values) == 2:
            return abs(valueHand.count(values[0]) - valueHand.count(values[1])) == 1
        else:
            return False

    def checkFourOfAKind(self, hand):
        valueHand = self.castValue(hand)

        values = []
        [values.append(card) for card in valueHand if card not in values]

        if len(values) <= 2:
            for card in values:
                if valueHand.count(card) == 4:
                    return True
        return False

    def checkThreeOfAKind(self, hand):
        valueHand = self.castValue(hand)

        values = []
        [values.append(card) for card in valueHand if card not in values]

        if len(values) <= 3:
            for card in values:
                if valueHand.count(card) == 3:
                    return True
        return False

    def checkTwoPair(self, hand):
        valueHand = self.castValue(hand)

        values = []
        [values.append(card) for card in valueHand if card not in values]

        if len(values) <= 3:
            for card in values:
                if valueHand.count(card) == 2:
                    return True
        return False

    def checkOnePair(self, hand):
        valueHand = self.castValue(hand)

        values = self.removeDuplicates(valueHand)#[]

        if len(values) <= 4:
            for card in values:
                if valueHand.count(card) == 2:
                    return True
        return False

    def castValue(self, hand):
        values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}

        valueHand = []
        for card in hand:
            valueHand.append(values[card[:(len(card)-1)]])
        valueHand.sort()

        return valueHand

    def castString(self, hand):
        values = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:"J", 12:'Q', 13:'K', 14:'A'}

        stringHand = []
        for card in hand:
            stringHand.append(values[card])

        return stringHand

    def sortHand(self, hand):
        suits = []
        [suits.append(card[-1:]) for card in hand]

        valueHand = self.castValue(hand)
        stringHand = self.castString(valueHand)

        sortedHand = []
        for card in range(len(stringHand)):
            sortedHand.append(stringHand[card] + suits[card])

        return sortedHand

    def removeDuplicates(self, hand):
        values = []
        [values.append(card) for card in hand if card not in values]

        return values






deck = Deck()

dealer = Player(deck.dealHand(), 'Dealer')
player1 = Player(deck.dealHand(), 'Player 1')
player2 = Player(deck.dealHand(), 'Player 2')
player3 = Player(deck.dealHand(), 'Player 3')
player4 = Player(deck.dealHand(), 'Player 4')
player5 = Player(deck.dealHand(), 'Player 5')

ranker = Ranker()
# print('Flush: ', ranker.checkFlush(['2C', 'KC', '5C', '9C', '10C']))
# print('Straight: ', ranker.checkStraight(['6C', '6C', '6C', '9C', '9C']))
# print('Full House: ', ranker.checkFullHouse(['6C', '6D', '6H', '9D', '9C']))
# print('Three of a kind: ', ranker.checkThreeOfAKind(['6C', '8D', 'AH', '8S', '8C']))
# print('Two pair: ', ranker.checkTwoPair(['6C', 'AD', '7H', '7S', '7C']))
# print('One pair: ', ranker.checkOnePair(['6C', 'AD', '7H', '5S', '5C']))
# print('Sorted: ', ranker.sortHand(['2C', 'KC', '5C', '9C', '10C']))

# print(dealer.showHand())
hand = ['JH','JH','9H','KH','KH']
print('Hand: ',hand)
ranker.checkCombo(hand)

# print(player1.showHand())
# print(player2.showHand())
# print(player3.showHand())
# print(player4.showHand())
# print(player5.showHand())