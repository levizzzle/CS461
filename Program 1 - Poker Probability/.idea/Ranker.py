

class Ranker:

    comboCard = ''

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

        count = 0
        for rank in ranks:
            if rank == True:
                print(rankStrings[ranks.index(rank)])
                combo = rankStrings[ranks.index(rank)]
                count += 1
                break

        if count == 0:
            noPair = True
            print(rankStrings[9])
            combo = rankStrings[9]

        self.getRank(combo, hand)

    def getRank(self, combo, hand):
        combos = {'no pair':0, 'one pair':1, 'two pair':2, 'three of a kind':3, 'straight':4,
                  'flush':5, 'full house':6, 'four of a kind':7, 'straight flush':8, 'royal flush':9}
        values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}

        rank = combos[combo.lower()]

        valueHand = self.castValue(hand)
        print('Rank  value: ',rank)
        print('ComboValue: ', self.comboCard)


    def checkFlush(self, hand):
            suits = []
            [suits.append(card[-1:]) for card in hand if card[-1:] not in suits]

            if len(suits) == 1:
                self.comboCard = hand[0]
                return  True

    def checkStraight(self, hand):
        valueHand = self.castValue(hand)

        firstCard = valueHand[0]
        straightHand = [firstCard, firstCard + 1, firstCard + 2, firstCard + 3, firstCard + 4]

        if valueHand == straightHand:
            self.comboCard = hand[0]
            return True

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
                    self.comboCard = card
                    return True
        return False

    def checkThreeOfAKind(self, hand):
        valueHand = self.castValue(hand)

        values = []
        [values.append(card) for card in valueHand if card not in values]

        if len(values) <= 3:
            for card in values:
                if valueHand.count(card) == 3:
                    self.comboCard = card
                return True
        return False

    def checkTwoPair(self, hand):
        valueHand = self.castValue(hand)

        values = []
        [values.append(card) for card in valueHand if card not in values]

        if len(values) <= 3:
            for card in values:
                if valueHand.count(card) == 2:
                    self.comboCard = card
                    return True
        return False

    def checkOnePair(self, hand):
        valueHand = self.castValue(hand)

        values = self.removeDuplicates(valueHand)#[]

        if len(values) <= 4:
            for card in values:
                if valueHand.count(card) == 2:
                    self.comboCard = card
                    print(self.comboCard)
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
