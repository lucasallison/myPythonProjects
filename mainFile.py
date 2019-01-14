#these are the classes for the game black jack

import random


class deckOfCards():
		
	def make_deck(self):
		my_deck = []
		for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
			for num in range (2, 11):
				my_deck.append(str(num) + ' of ' + suit)
			for special in ['Jack', 'Queen', 'King', 'Ace']:
				my_deck.append(special + ' of ' + suit)
		return my_deck
	
	
	def check_deck(self):
		check_deck = []
		for num in range (0, 53):
			check_deck.append(False)
		return check_deck

class playBlackJack(): 
	
	#making a deck and a check deck	
	deck_of_cards = deckOfCards()
	check_deck = deck_of_cards.check_deck()
	my_deck = deck_of_cards.make_deck()
	account_balance =  100
	
	
	dealer_cards = []
	player_cards = []
	
	def start(self):
		pass
		
	def place_bets(self):
	
		while True:
			bet = int(input('Place your bet: '))
			if (playBlackJack.account_balance - bet > 0):
				playBlackJack.account_balance -= bet
				break
		
	
	def tap_or_pass(self):
		pass
	
	def get_random_card(self):
		num = random.randint(0,53)
		
		while (playBlackJack.check_deck[num]):
			num = random.randint(0,53)
	
		
		playBlackJack.check_deck[num] = True
		return playBlackJack.my_deck[num]
		
	def deal_cards(self):
		playBlackJack.dealer_cards.append(self.get_random_card())
		playBlackJack.player_cards.append(self.get_random_card())
		playBlackJack.dealer_cards.append(self.get_random_card())
		playBlackJack.player_cards.append(self.get_random_card())
		
		print ('your cards: ')
		print (playBlackJack.player_cards[0], ' and ', playBlackJack.player_cards[1])
	

def play():	


	play = playBlackJack()
	
	#while something
	
	play.place_bets()
	play.deal_cards()
	
	
	
if __name__ == "__main__":	

	play()
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	
	
