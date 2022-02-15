from Deck import Deck
from Player import Player
from Ranker import Ranker
from Helper import Helper
import random


def getDealerHand():
    dealer = Player('Dealer')

    return dealer

def getPlayerHands():
    players = [Player('Player 1'), Player('Player 2'),
               Player('Player 3'), Player('Player 4'), Player('Player 5')]
    # for player in players:
    #     playerHands.append(player)

    return players

def checkHands(dealerHand, playerHands):
    players = playerHands
    allPlayers = [dealerHand]

    for player in players:
        allPlayers.append(player)

    playerResults = []
    for player in allPlayers:
        print(player.name, player.getHand(), ranker.checkCombo(player.hand))
        playerResults.append([player.name, player.getHand(), ranker.checkCombo(player.hand)])

    return playerResults

def shufflePlayerHands():
    for player in players:
        deck.addCardsToDeck(player.hand)
    deck.shuffleDeck()

def getResults(dealerHand, playerHands):
    # playerHands = checkHands(dealerHand)

    resultHands = checkHands(dealerHand, playerHands)

    winner = None
    for player in resultHands:
        if winner == None or (player[2][0] > resultHands[winner][2][0]):
            winner = resultHands.index(player)
        # print(player)
    return [resultHands[winner][0],resultHands[winner][1],resultHands[winner][2]]


deck = Deck()
ranker = Ranker()
helper = Helper()

# two = ['10H','10S','5C','5D','2H']
# three = ['10H','10S','5C','10D','6H']
# four = ['10H','10S','10C','10D','AH']
# straight = ['AH','3S','4C','5D','2H']
# hand = straight
# random.shuffle(hand)
# print(hand)
# print(ranker.checkCombo(hand))

dealer = getDealerHand()
players = getPlayerHands()


loopCount = 0
allRanks = []
dealerRanks = []
dealerWins = [0,0,0,0,0,0,0,0,0,0]

allHands = []
dealerData = []
numLoops = 100
for count in range(0,numLoops):
    deck.addCardsToDeck(dealer.hand)
    dealer = getDealerHand()
    wins = 0
    for count in range(0,numLoops):
        loopCount += 1
        print('Loop count: ', loopCount,'\n')

        shufflePlayerHands()
        players = getPlayerHands()
        results = getResults(dealer, players)

        dealerRank = round(ranker.checkCombo(dealer.hand)[0])
        allRanks.append(dealerRank)
        dealerRanks.append(dealerRank)

        for num in range(0,5):
            allRanks.append(round(ranker.checkCombo(players[num].hand)[0]))

        if results[0] == 'Dealer':
            wins += 1
            dealerWins[dealerRank] += 1
            # print(results, '\n')

    dealerHand = dealer.hand
    handWins = wins
    handData = ranker.checkCombo(dealerHand)
    dealerData.append([dealerHand, handWins, handData[1], handData[2], handData[3], handData[0]])

combos = {0:'no pair', 1:'one pair', 2:'two pair', 3:'three of a kind', 4:'straight',
          5:'flush', 6:'full house', 7:'four of a kind', 8:'straight flush', 9:'royal flush'}

for num in range(0,0):
    print('-----------------------------')
    print(combos[num],': ', dealerRanks.count(num))
    if dealerWins[num] > 0:
        print('Wins: ', dealerWins[num])
        winPercent = round((dealerWins[num] / (dealerRanks.count(num)*numLoops))*100,3)
        comboChance = round((dealerRanks.count(num)/numLoops) * 100, 5)
        print('Win Percentage: ', winPercent, '%')
        print('Chance of hand: ', comboChance,'%')

# print(dealerRanks)
# print(dealerWins)
# print(results)

# print('\n' + str(len(allRanks)))
for num in range(10):
    percent = round((allRanks.count(num)/((numLoops*numLoops)*6)*100),3)
    print(combos[num], ': ', percent,'%')

print('\n')
for entry in dealerData:
    hand = str(entry[0])
    numWins = entry[1]
    winRatio = numWins/numLoops
    comboString = entry[2]
    highCard = entry[3]
    handScore = entry[4]
    print(entry, 'Win Chance: ', winRatio*100, '%')


# test = ['JS', '8S', 'QS', '10S', '9S']
# print(ranker.checkCombo(test))










