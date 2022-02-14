from Deck import Deck
from Player import Player
from Ranker import Ranker
from Helper import Helper


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

dealer = getDealerHand()
players = getPlayerHands()


num = 1
dealerRanks = []
dealerWins = [0,0,0,0,0,0,0,0,0,0]

numLoops = 100000
for count in range(0,numLoops):
    deck.addCardsToDeck(dealer.hand)
    dealer = getDealerHand()
    wins = 0
    for count in range(0,1):
        shufflePlayerHands()
        players = getPlayerHands()
        results = getResults(dealer, players)

        dealerRank = round(ranker.checkCombo(dealer.hand)[0])
        if results[0] == 'Dealer':
            dealerWins[dealerRank] += 1

        # print('---------------------')
        print('Dealer Rank: ', dealerRank)
        print(results, '\n')
        print('Loop count: ', num,'\n')#'---------------------\n',num,'\n---------------------\n')
        num += 1
    dealerRanks.append(dealerRank)


combos = {0:'no pair', 1:'one pair', 2:'two pair', 3:'three of a kind', 4:'straight',
          5:'flush', 6:'full house', 7:'four of a kind', 8:'straight flush', 9:'royal flush'}
for num in range(0,10):
    print(combos[num],': ', dealerRanks.count(num))
    print('Wins: ', dealerWins[num])
    if dealerWins[num] > 0:
        winPercent = round((dealerWins[num] / (dealerRanks.count(num)*numLoops))*100,3)
        # comboChance = ((dealerRanks.count(num) * numLoops) / (numLoops * numLoops)) * 100
        comboChance = round((dealerRanks.count(num)/numLoops) * 100, 3)
        print('Win Percentage: ', winPercent, '%')
        print('Chance of hand: ', comboChance,'%\n-----------------------------')

# print(dealerRanks)
# print(dealerWins)



# print(results)















