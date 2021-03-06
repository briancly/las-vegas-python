import random

total = 0
dealer = 0
cash = 100
yes = ['Y','y','Yes','yes']
no = ['N','n','No','no']

def draw():
	hand = random.randint(1,11)
	return hand

def balance(result,bet,cash):
	if result == 'win':
		print 'You win $' + str(bet) + '. You now have $' + str(cash) + '.'
	elif result == 'lose':
		print 'You lose $' + str(bet) + '. You now have $' + str(cash) + '.'
	elif result == 'tie':
		print 'Tie game!'
		print 'Nothing happens. You have $' + str(cash) + '.'

print 'You currently have $' + str(cash) + '.'
while cash > 0:
	bet = input('How much do you want to bet? ')
	while bet > cash:
		bet = input('That is more cash than you have! How much do you want to bet? ')
	total = 0
	dealer = 0
	for _ in range(2):
		user_card = draw()
		dealer_card = draw()
		total += user_card
		dealer += dealer_card
		print 'Card: ' + str(user_card)
	print 'Total: ' + str(total)
	while total < 21:
		hit = raw_input('Hit? (Y/N): ')
		if hit in yes:
			user_card = draw()
			total += user_card
			print 'Card: ' + str(user_card)
			print 'Total: ' + str(total)
		elif hit in no:
			print 'Dealer Total: ' + str(dealer)
			while dealer < 17:
				dealer_card = draw()
				dealer += dealer_card
				print 'Dealer Card: ' + str(dealer_card)
				print 'Dealer Total: ' + str(dealer)
			if dealer > 21:
				print 'Dealer a busta. You win!'
				cash += bet
				balance('win',bet,cash)
			elif total < dealer:
				print 'Dealer wins!'
				cash -= bet
				balance('lose',bet,cash)
			elif total == dealer:
				balance('tie',bet,cash)
			else:
				print 'You win!'
				cash += bet
				balance('win',bet,cash)
			break
		else:
			print 'I do not recognize your response.'
	else:
		if total == 21:
			print 'Blackjack! You win!'
			cash += 1.5*bet
			balance('win',1.5*bet,cash)
		else:
			print 'You a busta'
			cash -= bet
			balance('lose',bet,cash)
else:
	print 'Game Over'