import random


#create a 52 deck of cards
suits = ['Clubs','Dimonds','Hearts','Spades']
ranks= ['Ace','King','Queen','Jack','10', '9','8','7','6','5','4','3','2']
value= {'Ace':10,'King':10,'Queen':10,'Jack':10,'10':10, '9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

class BankAccount:
    def __init__ (self,dealer_balance=0,player_balance=0):
        self.dealer_balance=dealer_balance
        self.player_balance= player_balance

    pass

# this class allows player to make a bet 
# bet amount in self.money 
# Dealer and player start with $0 in the bank

class Bet:
    def __init__(self,player_one = 0,dealer= 0 ):
        self.money = int(input('Place your bet  $'))
        self.player_one = player_one
        self.dealer = dealer
    def amount(self):
        print(self.money)

# the Class Deck holds the cards 
class Deck:
    def __init__(self,suits,ranks,deck_of_52=[]):
        self.suits = suits
        self.ranks = ranks
        self.deck_of_52= deck_of_52

#this function creates a deck of 52 cards and shuffles it into a random order 
    def full_deck(self):
        for suit in suits:
            for rank in ranks:
                self.deck_of_52.append(suit+' '+rank)
            random.shuffle(self.deck_of_52)
        return(self.deck_of_52)
# this function prints the deck of cards 
    def deck_print(self):
        return(self.deck_of_52)

# assigns cards to deck 
class Dealer_player_cards:
    def __init__(self,deck_of_cards,player_one= [],dealer=[]):
        self.deck_of_cards=deck_of_cards
        self.player_one = player_one
        self.dealer = dealer
    def cards_for_players(self):
        for i in range(0,2): # the function repeats twice so each player has 2 cards to start out with 
            #adds card from deck in index 0 to player one and removes it from the deck 
            self.player_one.append(deck_of_cards[0])
            self.deck_of_cards.pop(0)

            #adds card from deck in index 0 to dealer and removes it from the deck 
            self.dealer.append(deck_of_cards[0])
            self.deck_of_cards.pop(0)
# the following functions return player_one, player_two, and dealer deck 
    def player1_cards(self):
        return self.player_one
    def dealer_cards(self):
        return self.dealer
    def new_deck(self):
        return self.deck_of_cards

class Player_One:
# this class inputs cards of player 1, the full deck of cards and default value points
    def __init__(self,cards_of_player1,full_deck_cards,points_of_cards= 0):
        self.cards_of_player1=cards_of_player1
        self.points_of_cards= points_of_cards
        self.full_deck_cards= full_deck_cards

    # calculates the current points 
    def current_points(self):
        ace_values = {'11':11,'1':1}
        # finds the value for each card 
        for card in self.cards_of_player1:
            card_value= card.split()
            # splits the card to look up value in the dictonary 
            # first checks if it's an ace and gives the player an option if it is  
            if card_value[1] == 'Ace':
                points_for_ace  = input('do you want your Ace to be worth 1 point or 11 points?  ')
                self.points_of_cards+= ace_values[points_for_ace]
            else:
                # adds value to points_of cards 
                self.points_of_cards += value[card_value[1]]
            # checks if points_of is greater than 21 after adding points 

            # FIX ME 
            # if self.points_of_cards > 21:
            #     return 'Bust'
            #     break
        return self.points_of_cards
    def user_choice(self):
        ace_values = {'11':11,'1':1}
        #asks player to Hit or Stay
        while self.points_of_cards<=21:
            choice = input('Hit or Stay: ')
            # adds new card to deck if choice is hit 
            while choice == 'Hit':
                new_card= self.full_deck_cards[0]
                self.cards_of_player1.append(new_card)
                self.full_deck_cards.pop(0)
                # hit _card is used for the dictonary matching value 
                hit_card= new_card.split()

                if hit_card[1] == 'Ace':
                    # asks player if they want ace be 1 or 11 
                    points_for_ace  = input('do you want your Ace to be worth 1 point or 11 points?  ')
                    # adds value to points_of cards 
                    self.points_of_cards+= ace_values[points_for_ace]
                    print(self.cards_of_player1)
                    print(self.points_of_cards)
                    choice= input('Hit or Stay: ')
                    continue

                else:
                    # adds value to player one points_of_cards 
                    self.points_of_cards += value[hit_card[1]]
                    print(self.cards_of_player1)
                    print(self.points_of_cards)
                    choice= input('Hit or Stay: ')

            if (choice =='Stay') and (self.points_of_cards<=21):
                return self.points_of_cards
                break
            #FIX ME 
            elif (choice =='Stay'):
                return 'Bust'
                break

        # returns bust if points_of_cards greater than 21
        else:
            return 'Bust'
                

    def final_deck(self):
        if self.points_of_cards>21:
            return 'Bust'
        else:
            return self.full_deck_cards

class Dealer:
    def __init__(self,dealer_card_values,dealers_deck, deck_of_cards,dealer_points=0):
        self.dealer_card_values = dealer_card_values
        self.dealers_deck = dealers_deck
        self.dealer_points=dealer_points
        self.deck_of_cards = deck_of_cards
    def dealers_turn(self):
        self.dealer_points= 0
        for card in  self.dealer_card_values:
            card_value = card.split()
            if card_value[1]== 'Ace':
                if self.dealer_points + 11 <= 21:
                    self.dealer_points += 11
                else:
                    self.dealer_points +=1
            else:
                self.dealer_points += value[card_value[1]]
                
            if (self.dealer_points + (value[self.deck_of_cards[0].split()[1]]) <= 21):
                self.dealer_card_values.append(self.deck_of_cards[0])
                self.deck_of_cards.pop(0)
                continue
            else:
                break
                
        if self.dealer_points> 21:
            return 'Bust'
        else:
            return self.dealer_points

moneys =Bet()
gamble= moneys.amount()

card_deck=Deck(suits,ranks)
deck_of_cards=card_deck.full_deck()

card_assignment=Dealer_player_cards(deck_of_cards)
card_assignment.cards_for_players()

cards_of_player1= card_assignment.player1_cards()
cards_of_dealer= card_assignment.dealer_cards()
deck_for_player_one = card_assignment.new_deck()

print(f'your cards {cards_of_player1[0:]}')
print(f'dealer card {cards_of_dealer[0]}')

player_1_start=Player_One(cards_of_player1,deck_for_player_one)
player_one_points= player_1_start.current_points()
print(player_one_points)
player_turn =player_1_start.user_choice()
dealers_deck= player_1_start.final_deck()

dealers_deck_turn= Dealer(cards_of_dealer,dealers_deck,deck_for_player_one)
dealer_score = dealers_deck_turn.dealers_turn()

print(dealer_score)

if dealers_deck == 'Bust':
    BankAccount(dealer_balance=gamble,player_balance=0)
    print(f'dealer has won ${moneys.money}')
elif (dealer_score =='Bust') or (dealer_score >21):
        BankAccount(dealer_balance=0,player_balance=gamble)
        print(f'the player has won ${moneys.money}')
elif dealer_score> player_one_points:
        BankAccount(dealer_balance=gamble,player_balance=0)
        print(f'dealer has won ${moneys.money}')
elif player_one_points> dealer_score:
        BankAccount(dealer_balance=0,player_balance=gamble)
        print(f'the player has won ${moneys.money}')
        