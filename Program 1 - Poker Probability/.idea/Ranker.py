

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
        straightFlush = (straight == flush == True)
        royalFlush = False

        if flush and (self.castValue(self.sortHand(hand)) == [10,11,12,13,14]):
            royalFlush = True

        # print('No pair: ', noPair,'\nOne Pair: ', onePair, '\nTwo pair: ', twoPair, '\nThree of a kind: ', threeOfAKind,
        #       '\nStraight: ', straight, '\nFlush: ', flush, '\nFull house: ', fullHouse,
        #       '\nFour of a kind: ', fourOfAKind, '\nStraight Flush: ', straightFlush, '\nRoyal flush: ', royalFlush)

        ranks = [royalFlush, straightFlush, fourOfAKind, fullHouse, flush, straight, threeOfAKind, twoPair, onePair, noPair]
        rankStrings = {0:'Royal Flush', 1:'Straight Flush', 2:'Four of a Kind', 3:'Full House', 4:'Flush', 5:'Straight',
                       6:'Three of a Kind', 7:'Two Pair', 8:'One Pair', 9:'No Pair'}

        for rank in ranks:
            if rank == True:
                print(rankStrings[ranks.index(rank)])
                break


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
