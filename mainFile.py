#these are the classes for the game black jack

import random


class deckOfCards():
		
	def make_deck(self):
		my_deck = []
		for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
			for num in range (2, 10):
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
	
	account_balance =  100
	
	def start(self):
		pass
		
	def place_bets(self):
		
		while True:
		
			bet = int(input('Place your bet: ')
			#if playBlackJack.account_balance - bet <= 0 : 
			if (1 < 3):
		 		break
		 	else: 
		 		playBlackJack.account_blance -= bet
		 		break	
			
			
	def deal_cards(self):
		pass
	
	def tap_or_pass(self):
		pass
	
	def get_random_card(self, check_deck):
		num = random.randint(0,53)
		
		while (check_deck[num]):
			num = random.randint(0,53)
	
		return num

	

def play():	


	play = playBlackJack()
	
	#while something

	#making a deck and a check deck	
	deck_of_cards = deckOfCards()
	check_deck = deck_of_cards.check_deck()
	my_deck = deck_of_cards.make_deck()

	
	play.place_bets()
	
if __name__ == "__main__":	

	play()
	
	
	
