import random
from entities import Card, Deck, player

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = player("Player")
        self.dealer = player("Dealer")
        self.game_over = False

    def calculate_score(self, hand):
        """Calculate the best possible score for a hand, handling Aces."""
        score = 0
        aces = 0
        
        for card in hand:
            if card.rank == 'Ace':
                aces += 1
                score += 11
            else:
                score += card.value
        
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
            
        return score

    def deal_initial_cards(self):
        """Deal 2 cards to player and dealer."""
        for _ in range(2):
            self.player.add_card(self.deck.deal(1)[0])
            self.dealer.add_card(self.deck.deal(1)[0])
        
        # Update scores
        self.player.score = self.calculate_score(self.player.hand)
        self.dealer.score = self.calculate_score(self.dealer.hand)

    def display_hands(self, hide_dealer_card=True):
        """Display the current hands."""
        print(f"\n🃏 {self.player.name}'s hand:")
        for card in self.player.hand:
            print(f"  {card}")
        print(f"  Score: {self.player.score}")
        
        print(f"\n🃏 {self.dealer.name}'s hand:")
        if hide_dealer_card and len(self.dealer.hand) >= 2:
            print(f"  {self.dealer.hand[0]}")
            print("  [Hidden Card]")
        else:
            for card in self.dealer.hand:
                print(f"  {card}")
            print(f"  Score: {self.dealer.score}")
        print("-" * 40)

    def player_turn(self):
        """Handle the player's turn."""
        while self.player.score < 21:
            self.display_hands()
            
            choice = input("\nDo you want to (h)it or (s)tand? ").lower().strip()
            
            if choice == 'h' or choice == 'hit':
                card = self.player.hit(self.deck)
                self.player.score = self.calculate_score(self.player.hand)
                print(f"\nYou drew: {card}")
                
                if self.player.score > 21:
                    print(f"Your score: {self.player.score}")
                    print("💥 BUST! You went over 21!")
                    return False
                    
            elif choice == 's' or choice == 'stand':
                print(f"\nYou chose to stand with {self.player.score}")
                return True
            else:
                print("Invalid input! Please enter 'h' for hit or 's' for stand.")
        
        return True

    def dealer_turn(self):
        """Handle the dealer's turn."""
        print("\n🎰 Dealer's turn:")
        self.display_hands(hide_dealer_card=False)
        
        while self.dealer.score < 17:
            print("\nDealer hits...")
            card = self.dealer.hit(self.deck)
            self.dealer.score = self.calculate_score(self.dealer.hand)
            print(f"Dealer drew: {card}")
            print(f"Dealer's score: {self.dealer.score}")
            
            if self.dealer.score > 21:
                print("💥 Dealer BUST!")
                return False
        
        print(f"\nDealer stands with {self.dealer.score}")
        return True

    def determine_winner(self):
        """Determine and announce the winner."""
        print("\n" + "="*50)
        print("🎯 FINAL RESULTS")
        print("="*50)
        
        self.display_hands(hide_dealer_card=False)
        
        if self.player.score > 21:
            print("🔴 You LOSE! You went bust.")
            return "dealer"
        elif self.dealer.score > 21:
            print("🟢 You WIN! Dealer went bust.")
            return "player"
        elif self.player.score > self.dealer.score:
            print("🟢 You WIN! Your score is higher.")
            return "player"
        elif self.dealer.score > self.player.score:
            print("🔴 You LOSE! Dealer's score is higher.")
            return "dealer"
        else:
            print("🟡 It's a TIE! Same score.")
            return "tie"

    def check_blackjack(self):
        """Check for natural blackjack (21 with first 2 cards)."""
        player_blackjack = (self.player.score == 21 and len(self.player.hand) == 2)
        dealer_blackjack = (self.dealer.score == 21 and len(self.dealer.hand) == 2)
        
        if player_blackjack or dealer_blackjack:
            print("\n" + "="*50)
            print("🎰 BLACKJACK!")
            print("="*50)
            self.display_hands(hide_dealer_card=False)
            
            if player_blackjack and dealer_blackjack:
                print("🟡 Both have BLACKJACK! It's a tie.")
                return "tie"
            elif player_blackjack:
                print("🟢 BLACKJACK! You WIN!")
                return "player"
            else:
                print("🔴 Dealer has BLACKJACK! You lose.")
                return "dealer"
        
        return None

    def play_round(self):
        """Play a single round of Blackjack."""
        print("\n🎮 Starting new round...")
        print("="*50)
        
        # Reset for new round
        self.player.hand = []
        self.dealer.hand = []
        self.player.score = 0
        self.dealer.score = 0
        
        # Deal initial cards
        self.deal_initial_cards()
        
        # Check for natural blackjack
        result = self.check_blackjack()
        if result:
            return result
        
        # Player's turn
        if not self.player_turn():
            return "dealer"  # Player busted
        
        # Dealer's turn
        if not self.dealer_turn():
            return "player"  # Dealer busted
        
        # Determine winner
        return self.determine_winner()

def play_game():
    """Main game loop."""
    game = BlackjackGame()
    player_wins = 0
    dealer_wins = 0
    ties = 0
    
    print("🎲 Welcome to Blackjack!")
    print("Rules: Get as close to 21 as possible without going over.")
    print("Face cards = 10, Aces = 1 or 11, Number cards = face value")
    
    while True:
        try:
            result = game.play_round()
            
            if result == "player":
                player_wins += 1
            elif result == "dealer":
                dealer_wins += 1
            else:
                ties += 1
            
            print(f"\n📊 Score: You: {player_wins} | Dealer: {dealer_wins} | Ties: {ties}")
            
            play_again = input("\nDo you want to play another round? (y/n): ").lower().strip()
            if play_again not in ['y', 'yes']:
                break
            
            # Create new game with fresh deck for next round
            game = BlackjackGame()
            
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    
    print("\n🎯 Final Statistics:")
    print(f"Your wins: {player_wins}")
    print(f"Dealer wins: {dealer_wins}")
    print(f"Ties: {ties}")
    total_games = player_wins + dealer_wins + ties
    if total_games > 0:
        win_rate = (player_wins / total_games) * 100
        print(f"Your win rate: {win_rate:.1f}%")
    
    print("\nThanks for playing Blackjack! 🃏")

if __name__ == "__main__":
    play_game()