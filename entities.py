class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value()

    def get_value(self):
        """Return the value of the card for Blackjack scoring."""
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11
        else:
            return int(self.rank)

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']]

    def shuffle(self):
        import random
        random.shuffle(self.cards)
    
    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]

class player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)
        self.score += card.value

    def hit(self, deck):
        """Draw a card from the deck and add it to the player's hand."""
        if deck.cards:
            card = deck.deal(1)[0]
            self.add_card(card)
            return card
        else:
            raise ValueError("The deck is empty!")
        
    def stand(self):
        """Player chooses to stand, ending their turn."""
        return self.score

    def reset_hand(self):
        self.hand = []
        self.score = 0

    def __repr__(self):
        return f"{self.name} has {self.hand} with a score of {self.score}"
    
class Dealer(player):
    def __init__(self):
        super().__init__("Dealer")
        self.hidden_card = None

    def add_hidden_card(self, card):
        """Add a hidden card to the dealer's hand."""
        self.hidden_card = card

    def reveal_hidden_card(self):
        """Reveal the hidden card."""
        if self.hidden_card:
            self.hand.append(self.hidden_card)
            self.score += self.hidden_card.value
            self.hidden_card = None
        else:
            raise ValueError("No hidden card to reveal.")