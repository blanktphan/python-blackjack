# Class representing a playing card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # The suit of the card (e.g., Hearts, Diamonds)
        self.rank = rank  # The rank of the card (e.g., 2, 3, ..., King, Ace)
        self.value = self.get_value()  # The blackjack value of the card

    def get_value(self):
        # Return the blackjack value based on the card's rank
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10  # Face cards are worth 10 points
        elif self.rank == 'Ace':
            return 11  # Ace is initially worth 11 points
        else:
            return int(self.rank)  # Number cards are worth their face value

    def __repr__(self):
        # String representation of the card
        return f"{self.rank} of {self.suit}"
    
# Class representing a standard deck of 52 playing cards
class Deck:
    def __init__(self):
        # Create all combinations of suits and ranks to form the deck
        self.cards = [Card(suit, rank) for suit in ['♥️  Hearts', '♦️  Diamonds', '♠️  Clubs', '♣️  Spades']
                      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']]

    def shuffle(self):
        # Shuffle the deck randomly
        import random
        random.shuffle(self.cards)
    
    def deal(self, num_cards):
        # Deal a specified number of cards from the deck
        return [self.cards.pop() for _ in range(num_cards)]

# Class representing a player (either human or dealer)
class player:
    def __init__(self, name):
        self.name = name  # The player's name
        self.hand = []    # List of cards currently in the player's hand
        self.score = 0    # The player's current score

    def add_card(self, card):
        # Add a card to the player's hand and update the score
        self.hand.append(card)
        self.score += card.value

    def hit(self, deck):
        # Draw one card from the deck and add it to the hand
        if deck.cards:
            card = deck.deal(1)[0]
            self.add_card(card)
            return card
        else:
            raise ValueError("The deck is empty!")
        
    def stand(self):
        # Player chooses to stand; return the current score
        return self.score

    def reset_hand(self):
        # Reset the player's hand and score for a new round
        self.hand = []
        self.score = 0

    def __repr__(self):
        # String representation of the player's hand and score
        return f"{self.name} has {self.hand} with a score of {self.score}"
    
# Class representing the dealer, inheriting from player
class Dealer(player):
    def __init__(self):
        super().__init__("Dealer")  # Initialize with the name "Dealer"
        self.hidden_card = None     # The dealer's face-down (hidden) card

    def add_hidden_card(self, card):
        # Add a hidden card to the dealer (face-down)
        self.hidden_card = card

    def reveal_hidden_card(self):
        # Reveal the hidden card and add its value to the dealer's hand and score
        if self.hidden_card:
            self.hand.append(self.hidden_card)
            self.score += self.hidden_card.value
            self.hidden_card = None  # The card is no longer hidden
        else:
            raise ValueError("No hidden card to reveal.")