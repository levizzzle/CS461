from Deck import Deck
from Player import Player
from Ranker import Ranker
from Helper import Helper
import csv
import random
import os


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
        # print(player.name, player.getHand(), ranker.checkCombo(player.hand))
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

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

deck = Deck()
ranker = Ranker()
helper = Helper()

dealer = getDealerHand()
players = getPlayerHands()


loopCount = 0
allRanks = []
dealerRanks = []
dealerWins = [0,0,0,0,0,0,0,0,0,0]
rankWins = [0,0,0,0,0,0,0,0,0,0]

allHands = []
dealerData = []
numLoops = 1000
for count in range(0,numLoops):
    deck.addCardsToDeck(dealer.hand)
    dealer = getDealerHand()
    wins = 0
    for count in range(0,numLoops):
        loopCount += 1
        if loopCount % 500 == 0:
            clearConsole()
            progress = round((loopCount/(numLoops * numLoops) * 100),3)
            print('Progress: ', progress,'%\n')

        shufflePlayerHands()
        players = getPlayerHands()
        results = getResults(dealer, players)

        rankWins[round(results[2][0])] += 1
        dealerRank = round(ranker.checkCombo(dealer.hand)[0])
        allRanks.append(dealerRank)
        dealerRanks.append(dealerRank)

        for num in range(0,5):
            allRanks.append(round(ranker.checkCombo(players[num].hand)[0]))

        if results[0] == 'Dealer':
            wins += 1
            dealerWins[dealerRank] += 1

    dealerHand = dealer.hand
    handWins = wins
    handData = ranker.checkCombo(dealerHand)
    # print(handData)
    dealerData.append([dealerHand, handWins, handData[1], handData[2], handData[3], handData[0]])

combos = {0:'no pair', 1:'one pair', 2:'two pair', 3:'three of a kind', 4:'straight',
          5:'flush', 6:'full house', 7:'four of a kind', 8:'straight flush', 9:'royal flush'}

# for num in range(0,0):
#     print('-----------------------------')
#     print(combos[num],': ', dealerRanks.count(num))
#     if dealerWins[num] > 0:
#         print('Wins: ', dealerWins[num])
#         winPercent = round((dealerWins[num] / (dealerRanks.count(num)*numLoops))*100,3)
#         comboChance = round((dealerRanks.count(num)/numLoops) * 100, 5)
#         print('Win Percentage: ', winPercent, '%')
#         print('Chance of hand: ', comboChance,'%')

stringLines = []
for num in range(10):
    chance = round((allRanks.count(num)/((numLoops*numLoops)*6)*100),3)
    if allRanks.count(num) > 0:
        winRate = round(((rankWins[num]/allRanks.count(num)) * 100),3)
    else:
        winRate = 0

    stringLines.append('\n----------------\n')
    stringLines.append(combos[num])
    stringLines.append('\n----------------\n')
    stringLines.append('chance of hand: ' + str(chance) + '%\n')
    stringLines.append('win chance: ' + str(winRate) + '%\n')
    # print(combos[num], ': ', 'chance of hand: ', chance,'%', ' win chance: ', winRate, '%')

with open('Rank Review.txt', 'w') as f:
    f.writelines(stringLines)

file = open('Poker Probability.csv', 'w', newline='')

with file:
    writer = csv.writer(file)
    writer.writerow(['Hand', 'Combo', 'High Card', 'Combo Value', 'Hand Value', 'Win Percentage'])
    for entry in dealerData:
        hand = str(entry[0])
        numWins = entry[1]
        handWinPercent = (numWins/numLoops) * 100
        comboString = entry[2]
        highCard = str(entry[3])
        comboValue = entry[4]
        handRank = entry[5]

        columnData = [hand, comboString, highCard, comboValue, handRank, handWinPercent]
        writer.writerow(columnData)










