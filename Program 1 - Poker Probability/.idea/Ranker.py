

class Ranker:

    comboCard = ''
    comboCard2 = ''
    highCard = ''

    def rankHand(self, hand):
        self.checkCombo(hand)

    def setComboCard(self,comboCard):
        pass

    def checkWinner(self, players):
        pass

    def checkCombo(self, hand):
        values = self.castValue(hand)

        noPair = [False, 'No Pair', hand[-1:]]
        onePair = self.checkOnePair(hand)
        twoPair = self.checkTwoPair(hand)
        threeOfAKind = self.checkThreeOfAKind(hand)
        straight = self.checkStraight(hand)
        flush = self.checkFlush(hand)
        fullHouse = self.checkFullHouse(hand)
        fourOfAKind = self.checkFourOfAKind(hand)
        straightFlush = [(straight[0] == flush[0] == True), 'Straight Flush: ' + str(hand),
                         self.cardToString(values[4]), self.castValue(hand)[4]]
        royalFlush = [False, 'No Royal Flush']

        if flush[0] and (values == [10,11,12,13,14]):
            royalFlush = [True, 'Royal Flush: ' + str(hand), self.cardToString(values[4]), 14]

        ranks = [royalFlush, straightFlush, fourOfAKind, fullHouse, flush, straight, threeOfAKind, twoPair, onePair, noPair]

        rankStrings = {0:'Royal Flush', 1:'Straight Flush', 2:'Four of a Kind', 3:'Full House', 4:'Flush', 5:'Straight',
                       6:'Three of a Kind', 7:'Two Pair', 8:'One Pair', 9:'No Pair'}

        count = 0
        highCard = ''
        comboString = ''
        comboValue = 0

        for rank in ranks:
            if rank[0]== True:
                # print(rankStrings[ranks.index(rank)])
                comboString = rank[1]
                comboValue = rank[3]
                highCard = rank[2]
                # print('High Card: ',highCard)
                combo = rankStrings[ranks.index(rank)]
                count += 1
                break

        if count == 0:
            noPair = [True, 'No Pair', highCard]
            combo = rankStrings[9]
            comboString = 'No combo'
            highCard = self.cardToString(self.castValue(hand)[4])
            # highCard = hand[-1:][0][:-1]

        # print('CHECKING: ', self.getRank(combo, hand, comboString, highCard, comboValue))
        return self.getRank(combo, hand, comboString, highCard, comboValue)

    def getRank(self, combo, hand, comboString, highCard, comboValue):
        combos = {'no pair':0, 'one pair':1, 'two pair':2, 'three of a kind':3, 'straight':4,
                  'flush':5, 'full house':6, 'four of a kind':7, 'straight flush':8, 'royal flush':9}
        values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
        rank = combos[combo.lower()]

        valueHand = self.castValue(hand)
        totalValue = rank + (comboValue/100) + (self.cardToValue(highCard)/1000)

        return [round(totalValue,4), comboString, highCard, comboValue]


    def checkFlush(self, hand):
            suits = []
            [suits.append(card[-1:]) for card in hand if card[-1:] not in suits]

            dataHand = self.splitHand(hand)
            handValues = dataHand[1]
            values = self.removeDuplicates(handValues)

            comboValue = 0
            if len(suits) == 1:
                self.comboCard = suits[0]
                handValues.sort()
                comboValue = handValues[4]
                highCard = self.cardToString(self.getHighCard(values))
                return  [True, 'Flush: ' + self.comboCard,
                         highCard, comboValue]
            return [False, 'No Flush']

    def checkStraight(self, hand):
        valueHand = self.castValue(hand)
        values = []
        [values.append(card) for card in valueHand if card not in values]

        firstCard = valueHand[0]
        straightHand = [firstCard, firstCard + 1, firstCard + 2, firstCard + 3, firstCard + 4]
        aceStraight = [2, 3, 4, 5, 14]

        comboValue = 0
        if valueHand == straightHand or valueHand == aceStraight:
            self.comboCard = hand[0]
            comboValue = valueHand[4]
            highCard = hand[-1:][0]
            # print(comboValue)
            return [True, 'Straight: ' + str(hand),
                    self.cardToString(self.getHighCard(values)), comboValue]
        return [False, 'No Straight']

    def checkFullHouse(self, hand):
        valueHand = self.castValue(hand)

        values = []
        [values.append(card) for card in valueHand if card not in values]

        comboValue = 0
        if len(values) == 2:
            self.comboCard = [self.cardToString(values[0]), self.cardToString(values[1])]
            fullHouse = abs(valueHand.count(values[0]) - valueHand.count(values[1])) == 1
            highCard = self.cardToString(self.getHighCard(values))
            comboValue = (values[0] + values[1])
            return [fullHouse, 'FullHouse: ' + self.comboCard[0] + ' and ' + self.comboCard[1],
                    highCard, comboValue]
        else:
            return [False, 'No Full House']

    def checkFourOfAKind(self, hand):
        valueHand = self.castValue(hand)

        values = []
        [values.append(card) for card in valueHand if card not in values]

        comboValue = 0
        if len(values) <= 2:
            for card in values:
                if valueHand.count(card) == 4:
                    comboValue = card
                    self.comboCard = self.cardToString(card)
                    values.remove(card)
                    return [True, 'Four of a kind: ' + self.comboCard,
                            self.cardToString(self.getHighCard(values)), comboValue]
        return [False, 'No Four of a kind']

    def checkThreeOfAKind(self, hand):
        valueHand = self.castValue(hand)
        values = []
        [values.append(card) for card in valueHand if card not in values]

        comboValue = 0
        if len(values) == 3:
            for card in values:
                if valueHand.count(card) == 3:
                    comboValue = card
                    self.comboCard = self.cardToString(card)
                    values.remove(card)
                    return [True, 'Three of a kind: ' + self.comboCard,
                            self.cardToString(self.getHighCard(values)), comboValue]
        return [False, 'No Three of a kind']

    def checkTwoPair(self, hand):
        dataHand = self.splitHand(hand)
        cardNames = dataHand[0]
        handValues = dataHand[1]
        handSuits = dataHand[2]
        values = self.removeDuplicates(handValues)

        comboValue = 0
        self.comboCard = []
        if len(values) <= 3:
            for card in values:
                if handValues.count(card) == 2:
                    self.comboCard.append(self.cardToString(card))

            if len(self.comboCard) == 2:
                for card in self.comboCard:
                    comboValue += self.cardToValue(card)
                    values.remove(self.cardToValue(card))
                return [True, 'Two Pair of: ' + self.comboCard[0] + ' and ' + self.comboCard[1],
                        self.cardToString(values[-1:][0]), comboValue]
        return [False, 'No Two Pair']

    def checkOnePair(self, hand):
        dataHand = self.splitHand(hand)
        cardNames = dataHand[0]
        handValues = dataHand[1]
        handSuits = dataHand[2]
        values = self.removeDuplicates(handValues)

        comboValue = 0
        if len(values) == 4:
            for card in values:
                if handValues.count(card) == 2:
                    self.comboCard = self.cardToString(card)
                    values.remove(card)
                    comboValue = (card)
                    return [True, 'Pair of: ' + self.comboCard, self.cardToString(values[-1:][0]), comboValue]
        return [False, 'No Pair']

    def castValue(self, hand):
        values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}

        valueHand = []
        for card in hand:
            valueHand.append(values[card[:(len(card)-1)]])
        valueHand.sort()

        return valueHand

    def castDataHand(self, hand):
        values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
        dataHand = {}

        for card in hand:
            cardValue = values[card[:(len(card)-1)]]
            cardSuit = card[-1:]
            dataHand[card] = [cardValue, cardSuit]

        return dataHand

    def splitHand(self, hand):
        values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
        cardName, handValues, handSuits = [], [], []

        for card in hand:
            cardName.append(card)
            handValues.append(values[card[:(len(card)-1)]])
            handSuits.append(card[-1:])

        return [cardName, handValues, handSuits]

    def castString(self, hand):
        values = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:"J", 12:'Q', 13:'K', 14:'A'}

        stringHand = []
        for card in hand:
            stringHand.append(values[card])

        return stringHand

    def cardToString(self, card):
        values = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:"J", 12:'Q', 13:'K', 14:'A'}

        return values[card]

    def cardToValue(self, card):
        values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
        # print(card)
        return values[card]

    def sortHand(self, hand):
        # suits = []
        # [suits.append(card[-1:]) for card in hand]
        #
        # valueHand = self.castValue(hand)
        # stringHand = self.castString(valueHand)
        #
        # sortedHand = []
        # for card in range(len(stringHand)):
        #     sortedHand.append(stringHand[card] + suits[card])

        return hand #sortedHand

    def removeDuplicates(self, hand):
        values = []
        [values.append(card) for card in hand if card not in values]
        values.sort()

        return values

    def getHighCard(self, values):
        return values[-1:][0]
