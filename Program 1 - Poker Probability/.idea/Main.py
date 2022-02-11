from Deck import Deck
from Player import Player
from Ranker import Ranker
from Helper import Helper

deck = Deck()
ranker = Ranker()
helper = Helper()

dealer = Player(deck.dealHand(), 'Dealer')
player1 = Player(deck.dealHand(), 'Player 1')
player2 = Player(deck.dealHand(), 'Player 2')
player3 = Player(deck.dealHand(), 'Player 3')
player4 = Player(deck.dealHand(), 'Player 4')
player5 = Player(deck.dealHand(), 'Player 5')

players = [dealer, player1, player2, player3, player4, player5]
# for player in players:
#
#     # player.setHand(ranker.sortHand(player.getHand()))
#     player.sortHand()
#     print(player.name, ': ', player.getHand())
#     ranker.checkCombo(player.hand)
#     print('---------------------------')


# print(dealer.showHand())
hand = ['10H','KS','AC','KD','AH']
print('Hand: ',hand)
# ranker.castDataHand(hand)

print(ranker.checkTwoPair(hand))









