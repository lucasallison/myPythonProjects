#these are the classes for the game black jack

import random
money = 0

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
	
	deck_of_cards = deckOfCards()
	check_deck = deck_of_cards.check_deck()
	my_deck = deck_of_cards.make_deck()
	dealer_cards = []
	player_cards = []
	bet = 0
	
	def place_bets(self):
		global money
		while True:
			try:
				playBlackJack.bet = int(input('Place your bet: '))
			except: 
				print('try again')
			else:
				if (money - playBlackJack.bet >= 0):
					money -= playBlackJack.bet
					break
				else: 
					print('You do not have enough money') 
	
	def check_score(self, the_cards):
		score = 0
		for card in the_cards:
			try: 
				score += int(card[0])
			except:
				score += 10
		return score
		
	def check_busted(self, the_cards):
		return self.check_score(the_cards) > 21
	
	def tap_or_pass(self):
		
		choice = 1
		while(not self.check_busted(playBlackJack.player_cards) and choice != 0):
			try: 
				choice = int(input('press [0] to pass and [1] to get a card'))
			except: 
				print('Try again')
			else:
				if choice != 0: 
					playBlackJack.player_cards.append(self.get_random_card())
					print('Your cards: ', playBlackJack.player_cards)
			
		
		if (self.check_busted(playBlackJack.player_cards)): 
			print ('You are busted, the dealer won this round')
			return True
		else: 
			return False
					
	def get_random_card(self):
		num = random.randint(0,52)
		
		while (playBlackJack.check_deck[num]):
			num = random.randint(0,52)
	
		playBlackJack.check_deck[num] = True
		return playBlackJack.my_deck[num]
		
	def deal_cards(self):
		playBlackJack.dealer_cards.append(self.get_random_card())
		playBlackJack.player_cards.append(self.get_random_card())
		playBlackJack.dealer_cards.append(self.get_random_card())
		playBlackJack.player_cards.append(self.get_random_card())
		
	def dealer_play(self):
		score = self.check_score(playBlackJack.dealer_cards)
		
		while True:
			if score <= 16: 
				playBlackJack.dealer_cards.append(self.get_random_card())
				score = self.check_score(playBlackJack.dealer_cards) 
			else: 
				break 
		return score
		
	def card_handout(self):
		global money
		if (not self.tap_or_pass()):
			score_dealer = self.dealer_play()
			score_player = self.check_score(playBlackJack.player_cards)
			if (score_player > score_dealer) or (score_dealer > 21): 
				print(f'You won this round with {score_player} points. The dealer had {score_dealer} points. His cards: {playBlackJack.dealer_cards}.')
				money += playBlackJack.bet * 2
			else: 
				print(f'The dealer won this round with {score_dealer} points. His cards: {playBlackJack.dealer_cards}. You had {score_player} points')
				
	def money_start(self):
		while True:
			try:
				money = int(input('Starting amount: '))
			except:
				print('Try again')
			else: 
				break
			
		

#will end up in a different file..
def play():	
	global money
	choice = 1
	
	play = playBlackJack()
	play.money_start()
	
	while choice != 0:
	
		play.place_bets()
		play.deal_cards()
		print('Your cards: \n', play.player_cards)
		play.card_handout()
		print(f'Your account balance {money}')
		
		if(money <= 0): 
			choice = 0
		else: 
			while True:
				try:
					choice = int(input('[0] exit [1] play another round'))
				except:
					print('Try again')
				else: 
					break
				
			
if __name__ == "__main__":	

	play()
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	
	
