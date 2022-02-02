#Dictionaries for the cards and teh suits
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#class for the cards
class Card:

    def __init__(self,suit,rank):

        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


#class for creating and shuffling the deck
class Deck:

    def __init__(self):

        self.deck = []  # start with an empty list

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list

    #deck shuffle method
    def shuffle_deck(self):
        
        random.shuffle(self.deck)
        
    #dealing method
    def deal_one(self):
        
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    #when he wins the bet
    def win_bet(self):

        betting = int(input('Place your bet'))
    
        self.total += self.bet*2

    
    #when he loses the bet
    def lose_bet(self):

        self.total -= self.bet


# a function to place the players bet and check if he has enough to bet
def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('Place your bet please: '))
        except:
            print('Sorry your bet must be an integer')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

#a function to hit(give another card ) to the player
def hit(deck, hand):
    
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()
    

#hit or stand function

def hit_or_stand(deck,hand):

    global playing

    while playing:
        choice = input('Would you like to hit or stand? H/S: ')

        if choice == 'H':
            hit(deck,hand)
        elif choice == 'S':
            print('Dealers turn')
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break

#functions to display cards
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    

#functions to handle game scenarios
def player_busts(player,dealer,chips):
    print('Player busts')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player wins')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Dealer busts')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('Dealer wins')
    chips.lose_bet()
    
def push(player,dealer):
     print("Dealer and Player tie! It's a push.")


while True:
    # Print an opening statement
    print('Hello player welcome to a game of blackjack')

    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle_deck()
    
 
    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())
            

    # Set up the Player's chips
    chips = Chips(2000)
    
    # Prompt the Player for their bet
    take_bet(chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <=21 :
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

    
         # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'Y' or 'N' ")
    
    if new_game=='Y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break