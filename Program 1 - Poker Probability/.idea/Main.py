from Deck import Deck
from Player import Player
from Ranker import Ranker

deck = Deck()
ranker = Ranker()

dealer = Player(deck.dealHand(), 'Dealer')
player1 = Player(deck.dealHand(), 'Player 1')
player2 = Player(deck.dealHand(), 'Player 2')
player3 = Player(deck.dealHand(), 'Player 3')
player4 = Player(deck.dealHand(), 'Player 4')
player5 = Player(deck.dealHand(), 'Player 5')

players = [dealer, player1, player2, player3, player4, player5]
for player in players:

    player.sortHand()
    print(player.name, ': ', player.showHand())
    ranker.checkCombo(player.hand)
    print('---------------------------')


# print(dealer.showHand())
# hand = ['JH','JH','9H','KH','KH']
# print('Hand: ',hand)
# ranker.checkCombo(hand)









