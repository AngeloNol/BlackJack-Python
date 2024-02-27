import random #random library

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']}  of  {self.suit}"
    
# deck class is used to set the suits, ranks and the card values
# the shuffle function with randomize the cards 
# the deal function will give the player a card 
class Deck:
    def __init__(self):
        #below are variable 
        self.cards = []
        # suit stores the card symbols
        suits = ["spades", "clubs", "hearts", "diamonds"]
        # ranks stores the card values
        ranks = [{"rank": "A", "value": 11}, 
                {"rank": "2", "value": 2}, 
                {"rank": "3", "value": 3},
                {"rank": "4", "value": 4},
                {"rank": "5", "value": 5},
                {"rank": "6", "value": 6},
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9},
                {"rank": "10", "value": 10},
                {"rank": "J", "value": 10},
                {"rank": "Q", "value": 10},
                {"rank": "K", "value": 10},
            ]

        # the for loops will put suits and ranks together 
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank)) # store in the card variable

    # the shuffle function shuffles the cards randomly
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    # the deal function will add one value into the card variable
    def deal(self,number):
        cards_dealt = []
        for x in range(number): # loop thru the number of cards dealt
            if len(self.cards)>0: # check if the card is large then zero
                card = self.cards.pop() # stores one of the cards into the card
                cards_dealt.append(card) # add a card to the list
        return cards_dealt # return the value

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)
    
    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10
    
    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21
    
    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
                  and not show_all_dealer_cards and not self.is_blackjack():
                print("hidden")
            else:
                print(card)

        if not self.dealer:
            print("Value:", self.get_value())
        print()

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number")
        
        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player = Hand()
            dealer = Hand(dealer=True)

            for i in range(2):
                player.add_card(deck.deal(1))
                dealer.add_card(deck.deal(1))
            
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player.display()
            dealer.display()

            if self.check_winner(player, dealer):
                continue

            choice = ""
            while player.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S) ").lower()
                    print()
                if choice in ["hit", "h"]:
                    player.add_card(deck.deal(1))
                    player.display()
            
            if self.check_winner(player, dealer):
                continue

            player_value = player.get_value()
            dealer_value = dealer.get_value()

            while dealer_value < 17:
                dealer.add_card(deck.deal(1))
                dealer_value = dealer.get_value()
               
            dealer.display(show_all_dealer_cards=True)

            if self.check_winner(player, dealer):
                continue

            print("Final Results")
            print("your hand:", player_value)
            print("dealer hand:", dealer_value)

            self.check_winner(player, dealer, True)

        print("\nThanks for playing!")

    # Function check the result to determine the winner
    def check_winner(self, player, dealer, game_over=False):
        if not game_over:
            if player.get_value() > 21:
                print("You busted. Dealer win!")
                return True
            elif dealer.get_value() > 21:
                print("You busted. You win!")
                return True
            elif dealer.is_blackjack() and player.is_blackjack():
                print("Both players have blackjack! Tie!")
                return True
            elif player.is_blackjack():
                print("You have blackjack. You win!")
                return True
            elif dealer.is_blackjack():
                print("You have blackjack. Dealer win!")
                return True
        else:
            if player.get_value() > dealer.get_value():
                print("You win!")
            elif player.get_value() == dealer.get_value():
                print(" Tie!")
            else:
                print("Dealer win!")
        return False

g = Game()
g.play()