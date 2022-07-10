import random

class Hand:
    
    def __init__(self, total=0, num_cards=0, has_ace=False, ace_reduced=False, cards=[]):
        self.total = total
        self.num_cards = num_cards
        self.has_ace = has_ace
        self.ace_reduced = ace_reduced
        self.cards = cards
        


    
def draw_card(cards_drawn, num_decks, hand):
    while True:
        deck = random.randint(1, int(num_decks))
        suit = random.randint(1, 5)
        rank = random.randomint(1, 14)
        ace = False
        card = ''
        
        card_id = 100*rank + 10*suit + deck
        
        
        
        
def main():
    
    print('Welcome to blackjack!')
    print('For your deck number, please enter a number between 6 and 10. The value will default to 6 otherwise.')
    num_decks = input('How many decks would you like to play with?')
    if num_decks not in ['6', '7', '8', '9' , '10']:
        num_decks = '6'
    
    switch = True
    while switch: #start game
        player_hand = Hand()
        dealer_hand = Hand()
        cards_drawn = {}
        
        
        for turn in range(0, 4):
            if turn % 2 == 0:
                card = None
        
        
        
        

