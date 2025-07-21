# Class representing a playing card
class Card:
    def __init__(self, suit, rank):
        """Initialize a card with suit and rank"""
        self.suit = suit  # Card suit (Hearts, Diamonds, etc.)
        self.rank = rank  # Card rank (2, 3, ..., King, Ace)
        self.value = self.get_value()  # Blackjack value of the card

    def get_value(self):
        """Return the value of the card for Blankjack scoring"""
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10  # Face cards are worth 10
        elif self.rank == 'Ace':
            return 11  # Ace starts as 11 (can be adjusted later)
        else:
            return int(self.rank)  # Number cards are worth face value

    def __repr__(self):
        """String representation of the card"""
        return f"{self.rank} of {self.suit}"
    
# Class representing a deck of 52 playing cards
class Deck:
    def __init__(self):
        """Create a standard 52-card deck"""
        # Generate all combinations of suits and ranks
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']]

    def shuffle(self):
        """Shuffle the deck randomly"""
        import random
        random.shuffle(self.cards)
    
    def deal(self, num_cards):
        """Deal specified number of cards from the deck"""
        return [self.cards.pop() for _ in range(num_cards)]

# Class representing a player (can be human player or dealer)
class player:
    def __init__(self, name):
        """Initialize a player with a name"""
        self.name = name  # Player's name
        self.hand = []    # List of cards in hand
        self.score = 0    # Current score

    def add_card(self, card):
        """Add a card to the player's hand and update score"""
        self.hand.append(card)
        self.score += card.value

    def hit(self, deck):
        """Draw a card from the deck and add it to the player's hand"""
        if deck.cards:
            card = deck.deal(1)[0]  # Deal one card
            self.add_card(card)
            return card
        else:
            raise ValueError("The deck is empty!")
        
    def stand(self):
        """Player chooses to stand, ending their turn"""
        return self.score

    def reset_hand(self):
        """Reset player's hand for a new game"""
        self.hand = []
        self.score = 0

    def __repr__(self):
        """String representation of the player"""
        return f"{self.name} has {self.hand} with a score of {self.score}"
    
# Special dealer class that inherits from player
class Dealer(player):
    def __init__(self):
        """Initialize dealer (extends player class)"""
        super().__init__("Dealer")  # Call parent constructor
        self.hidden_card = None     # Dealer's face-down card

    def add_hidden_card(self, card):
        """Add a hidden card to the dealer's hand (face-down)"""
        self.hidden_card = card

    def reveal_hidden_card(self):
        """Reveal the hidden card (flip face-down card face-up)"""
        if self.hidden_card:
            self.hand.append(self.hidden_card)
            self.score += self.hidden_card.value
            self.hidden_card = None  # No longer hidden
        else:
            raise ValueError("No hidden card to reveal.")