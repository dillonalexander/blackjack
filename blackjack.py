import random

class Hand:
    
    def __init__(self, total=0, num_cards=0, has_ace=False, ace_reduced=True, hide_card=False, cards=[]):
        self.total = total
        self.num_cards = num_cards
        self.has_ace = has_ace
        self.ace_reduced = ace_reduced
        self.hide_card = hide_card
        self.cards = cards
        
    def set_hand(self, card):
        self.num_cards += 1
        if card[0] == 0:
            self.has_ace = True
        self.update_total(card)
        self.cards.append(card)
        
    def update_total(self, card):    
        big_ace = 11
        card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        if card[0] == 0 and self.ace_reduced == False:
            self.total += big_ace
        else:
            self.total += card_values[card[0]]
        
    def set_num_cards():
        pass
    
    def set_hide_card(self, status):
        self.hide_card = status
        
    #TODO: Update this
    def total_reader(self):
        return f"Total is {self.total}"
#        if self.has_ace == True:
#            return f'Your total is {player_hand.total} or {int(player_hand.total) + 10}'
#        else:
#            return f'Your total is {player_hand.total}'
        
    def dealer_game(self):
        while self.total < 17:
            self.set_hand(draw_card(cards_drawn, num_decks))
            if self.total > 21 and self.has_ace == True:
                self.total -= 10
        
        return self.total
      
            
        
def calculate_hand(hand):
    pass
        
def card_reader(card):
    ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    
    return f'{ranks[card[0]]} of {suits[card[1]]}'    
    
    
def draw_card(cards_drawn, num_decks):
    invalid_card = True
    while invalid_card:
        rank = random.choice(range(0, 13))
        suit = random.choice(range(0, 4))
        card = (rank, suit)
        
        if cards_drawn.get(card, 0) > num_decks:
            break
                
        if card not in cards_drawn:
            cards_drawn[card] = 0
            
        cards_drawn[card] += 1
        invalid_card = False
        
        return card
    
    
    
############################################################################################################################    
    

print('Welcome to blackjack!')
print('For your deck number, please enter a number between 2 and 8. The value will default to 6 otherwise.')


invalid_input = True
while invalid_input:
    try:
        num_decks = int(input('How many decks would you like to play with? '))
        if num_decks not in range(2,9):
            num_decks = 6
    except:
        num_decks = 6
    invalid_input = False
    
    
game_play = True
while game_play:
    player_hand = Hand()
    dealer_hand = Hand()
    cards_drawn = {}
    
    #initial draw
    for turn in range(0, 2):
        player_hand.set_hand(draw_card(cards_drawn, num_decks))
        print(f"Player card: {card_reader(player_hand.cards[-1])}")
        
        dealer_hand.set_hand(draw_card(cards_drawn, num_decks))
        if dealer_hand.hide_card == False:
            print(f"Dealer card: {card_reader(dealer_hand.cards[-1])}")
        dealer_hand.set_hide_card(True)
        
    
    
    
         
    #player decisions after initial draw
    standing = False
    while not standing:
#        if player_hand.has_ace == True:
#            ace_value = int(input(f'{player_hand.total_reader()}, would you like to treat your ace as a 1 or 11? '))
#            if ace_value not in [1, 11]:
#                ace_value = 1  
        answer = input(f"Player's {player_hand.total_reader()}, would you like to hit? y/n ").lower()
        if answer in ['y', 'n']:
            if answer == 'n':
                standing = True
            elif answer == 'y':
                player_hand.set_hand(draw_card(cards_drawn, num_decks))
                print(card_reader(player_hand.cards[-1]))
            
    #dealer decisions
                
                
                
    dealer_hand.dealer_game()
    print(f"Player's {player_hand.total_reader()}")
    print(f"Dealer's {dealer_hand.total_reader()}")

    game_play = False
        
     
        

