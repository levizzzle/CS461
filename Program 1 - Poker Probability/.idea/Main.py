from Deck import Deck
from Player import Player
from Ranker import Ranker
from Helper import Helper

deck = Deck()
ranker = Ranker()
helper = Helper()
playerHands = []
count1 = 0
count2 = 0

def getDealerHand():
    dealer = Player('Dealer')

    return dealer

def getPlayerHands():
    players = [Player('Player 1'), Player('Player 2'),
               Player('Player 3'), Player('Player 4'), Player('Player 5')]
    for player in players:
        playerHands.append(player)

    return players

def checkHands(dealerHand):
    players = getPlayerHands()
    allPlayers = [dealerHand]

    for player in players:
        allPlayers.append(player)

    playerResults = []
    for player in allPlayers:
        print(player.getHand())
        playerResults.append([player.name, player.getHand(), ranker.checkCombo(player.hand)])

    return playerResults

def shufflePlayerHands():
    for player in playerHands:
        deck.addCardsToDeck(player.hand)
    deck.shuffleDeck()

def getResults(dealerHand, playerHands):
    playerHands = checkHands(dealerHand)
    winner = None
    for player in playerHands:
        if winner == None or (player[2][0] > playerHands[winner][2][0]):
            winner = playerHands.index(player)
        # print(player)
    return [playerHands[winner][0],playerHands[winner][1],playerHands[winner][2]]

for count in range(1,500):
    # deck.newDeck()
    dealerHand = getDealerHand()
    for count in range(1,500):
        # dealerRank = d
        winners = []
        results = getResults(dealerHand, playerHands)
        shufflePlayerHands()
        # winners.append
        print('---------------------')
        print('Dealer Rank: ', round(ranker.checkCombo(dealerHand.hand)[0]))
        print(results, '\n')



# print(results)















