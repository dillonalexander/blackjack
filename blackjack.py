import random

class Hand:
    
    def __init__(self, total=0, num_cards=0, has_ace=False, ace_reduced=False, cards=[]):
        self.total = total
        self.num_cards = num_cards
        self.has_ace = has_ace
        self.ace_reduced = ace_reduced
        self.cards = cards
        
    def set_hand(self, card):
        self.num_cards += 1
        #TODO: create update_total method
        self.total += card[0]
        if card[0] == 1:
            self.has_ace = True
        self.cards.append(card)
    
    def set_num_cards():
        pass
    
    
def card_reader(card):
    ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    
    return f'{ranks[card[0]]} of {suits[card[1]]}'    
    
    
#TODO: determine best way to handle cards_drawn dictionary    
def draw_card(cards_drawn, num_decks):
    invalid_card = True
    while invalid_card:
        rank = random.choice(range(1,14))
        suit = random.choice(range(1, 5))
        card = (rank, suit)
        
        if cards_drawn.get(card, 0) > num_decks:
            continue
                
        if card not in cards_drawn:
            cards_drawn[card] = 0
            
        cards_drawn[card] += 1
        invalid_card = False
        
        return card

print('Welcome to blackjack!')
print('For your deck number, please enter a number between 2 and 8. The value will default to 6 otherwise.')

invalid_input = True
num_decks = 2
while invalid_input:
    try:
        num_decks = int(input('How many decks would you like to play with? '))
        if num_decks not in range(2,9):
            num_decks = 2
    
        break        
    except:
        print(f"Please enter a valid integer between 2 and 8")
    
game_play = True
while game_play:
    player_hand = Hand()
    dealer_hand = Hand()
    cards_drawn = {}
    
    #initial draw
    for turn in range(0, 2):
        player_hand.set_hand(draw_card(cards_drawn, num_decks))
        
        dealer_hand.set_hand(draw_card(cards_drawn, num_decks))
 
    valid_answer = False
    while not valid_answer:
        answer = input('Would you like to hit? y/n ')
    
        if answer.lower() in ['y', 'n']:
            valid_answer = True
            
    

    game_play = False
        
     
        

