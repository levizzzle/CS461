from Deck import Deck
from Player import Player
from Ranker import Ranker
from Helper import Helper

deck = Deck()
ranker = Ranker()
helper = Helper()

# dealer = Player(deck.dealHand(), 'Dealer')
# player1 = Player(deck.dealHand(), 'Player 1')
# player2 = Player(deck.dealHand(), 'Player 2')
# player3 = Player(deck.dealHand(), 'Player 3')
# player4 = Player(deck.dealHand(), 'Player 4')
# player5 = Player(deck.dealHand(), 'Player 5')

dealer = Player([], 'Dealer')
player1 = Player([], 'Player 1')
player2 = Player([], 'Player 2')
player3 = Player([], 'Player 3')
player4 = Player([], 'Player 4')
player5 = Player([], 'Player 5')

players = [dealer, player1, player2, player3, player4, player5]

def playerHands():
    for player in players:
        # player.setHand(ranker.sortHand(player.getHand()))
        player.sortHand()
        print(player.name, ': ', player.getHand())
        ranker.checkCombo(player.hand)
        print('---------------------------')

playerHands()
print(deck.showDeckSize())
# print(dealer.showHand())
# hand = ['10H','JH','QH','KH','AH']
# print('Hand: ',hand,'\n')

# print(ranker.checkOnePair(hand))
# print(ranker.checkTwoPair(hand))
# print(ranker.checkThreeOfAKind(hand))
# print(ranker.checkFourOfAKind(hand))
# print(ranker.checkFullHouse(hand))
# print(ranker.checkStraight(hand))
# print(ranker.checkFlush(hand))














