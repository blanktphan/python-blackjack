# Import required modules
import random
from entities import Card, Deck, player

# Main class for the Blackjack game
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()                # Initialize a new deck
        self.deck.shuffle()               # Shuffle the deck
        self.player = player("Player")    # Create the player object
        self.dealer = player("Dealer")    # Create the dealer object
        self.game_over = False            # Flag to indicate if the game is over

    def calculate_score(self, hand):
        score = 0
        aces = 0
        
        # Calculate the total score and count the number of Aces
        for card in hand:
            if card.rank == 'Ace':
                aces += 1
                score += 11  # Count Ace as 11 initially
            else:
                score += card.value
        
        # Adjust Ace value from 11 to 1 if score exceeds 21
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
            
        return score

    def deal_initial_cards(self):
        # Deal two cards each to player and dealer
        for _ in range(2):
            self.player.add_card(self.deck.deal(1)[0])
            self.dealer.add_card(self.deck.deal(1)[0])
        
        # Update scores after dealing
        self.player.score = self.calculate_score(self.player.hand)
        self.dealer.score = self.calculate_score(self.dealer.hand)

    def display_hands(self, hide_dealer_card=True):
        # Display player's hand and score
        print(f"\n👤 {self.player.name}'s hand:")
        for card in self.player.hand:
            print(f"    {card}")
        print(f"    Score: {self.player.score}")
        
        # Display dealer's hand, optionally hiding one card
        print(f"\n🤖 {self.dealer.name}'s hand:")
        if hide_dealer_card and len(self.dealer.hand) >= 2:
            print(f"    {self.dealer.hand[0]}")
            print("    [Hidden Card]")
        else:
            for card in self.dealer.hand:
                print(f"    {card}")
            print(f"    Score: {self.dealer.score}")
        print("\n" + "-" * 40)

    def player_turn(self):
        # Handle the player's turn: hit or stand
        while self.player.score < 21:
            self.display_hands()
            
            choice = input("\nDo you want to (h)it or (s)tand? ").lower().strip()
            
            if choice == 'h' or choice == 'hit':
                # Player chooses to hit (draw a card)
                card = self.player.hit(self.deck)
                self.player.score = self.calculate_score(self.player.hand)
                print(f"\nYou drew: {card}")
                
                if self.player.score > 21:
                    print(f"Your score: {self.player.score}")
                    print("💥 BUST! You went over 21!")
                    return False
                    
            elif choice == 's' or choice == 'stand':
                # Player chooses to stand (end turn)
                print(f"\nYou chose to stand with {self.player.score}")
                return True
            else:
                print("Invalid input! Please enter 'h' for hit or 's' for stand.")
        
        return True

    def dealer_turn(self):
        # Handle the dealer's turn according to Blackjack rules
        print("\n🤖 Dealer's turn...")
        self.display_hands(hide_dealer_card=False)
        
        # Dealer must hit until reaching at least 17
        while self.dealer.score < 17:
            print("\n   Dealer hits...")
            card = self.dealer.hit(self.deck)
            self.dealer.score = self.calculate_score(self.dealer.hand)
            print(f"   Dealer drew: {card}")
            print(f"   Dealer's score: {self.dealer.score}")

            if self.dealer.score > 21:
                print("💥 Dealer BUST!")
                return False
        
        print(f"\nDealer stands with {self.dealer.score}")
        return True

    def determine_winner(self):
        # Determine the winner and display the final results
        print("\n" + "="*50)
        print("🎉 FINAL RESULTS")
        print("="*50 + "\n")
        
        self.display_hands(hide_dealer_card=False)
        
        if self.player.score > 21:
            print("👎 You LOSE! You went bust.")
            return "dealer"
        elif self.dealer.score > 21:
            print("👍 You WIN! Dealer went bust.")
            return "player"
        elif self.player.score > self.dealer.score:
            print("👍 You WIN! Your score is higher.")
            return "player"
        elif self.dealer.score > self.player.score:
            print("👎 You LOSE! Dealer's score is higher.")
            return "dealer"
        else:
            print("🤝 It's a TIE! Same score.")
            return "tie"

    def check_blackjack(self):
        # Check for natural blackjack (21 with 2 cards)
        player_blackjack = (self.player.score == 21 and len(self.player.hand) == 2)
        dealer_blackjack = (self.dealer.score == 21 and len(self.dealer.hand) == 2)
        
        if player_blackjack or dealer_blackjack:
            print("🏆 SUUUPPERRRR BLACKJACK!!!")
            self.display_hands(hide_dealer_card=False)
            
            if player_blackjack and dealer_blackjack:
                print("🤝 Both have BLACKJACK! It's a tie.")
                return "tie"
            elif player_blackjack:
                print("👍 BLACKJACK! You WIN!")
                return "player"
            else:
                print("👎 Dealer has BLACKJACK! You lose.")
                return "dealer"
        
        return None  # No blackjack

    def play_round(self):
        # Play a single round of Blackjack
        print("\n" + "="*50)
        print("🎮 Starting new round...")
        print("="*50 + "")
        
        # Reset hands and scores for a new round
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
            return "dealer"
        
        # Dealer's turn
        if not self.dealer_turn():
            return "player"
        
        # Determine the winner
        return self.determine_winner()

# Main function to run the game loop
def play_game():
    game = BlackjackGame()
    player_wins = 0    # Number of player wins
    dealer_wins = 0    # Number of dealer wins
    ties = 0           # Number of ties
    
    # Display welcome message and rules
    print("\n🃏 Welcome to Blackjack!")
    print("📜 Rules: Get as close to 21 as possible without going over.")
    print("Face cards = 10, Aces = 1 or 11, Number cards = face value")
    
    # Main game loop for multiple rounds
    while True:
        try:
            # Play a round and update statistics
            result = game.play_round()
            
            if result == "player":
                player_wins += 1
            elif result == "dealer":
                dealer_wins += 1
            else:
                ties += 1
            
            # Show current score
            print(f"\n🏅 Score: You: {player_wins} | Dealer: {dealer_wins} | Ties: {ties}")
            
            # Ask if the player wants to play again
            play_again = input("\nDo you want to play another round? (y/n): ").lower().strip()
            if play_again not in ['y', 'yes']:
                break
            
            # Start a new game with a fresh deck
            game = BlackjackGame()
            
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    
    # Display final statistics after exiting the loop
    print("\n📋 Final Statistics:")
    print(f"Your wins: {player_wins}")
    print(f"Dealer wins: {dealer_wins}")
    print(f"Ties: {ties}")
    total_games = player_wins + dealer_wins + ties
    if total_games > 0:
        win_rate = (player_wins / total_games) * 100
        print(f"Your win rate: {win_rate:.1f}%")
    
    print("\n👋 Thanks for playing Blackjack!")

# Run the game if this script is executed directly
if __name__ == "__main__":
    play_game()
