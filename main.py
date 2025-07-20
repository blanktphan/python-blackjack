# Import main game function from game_logic.py
from game_logic import play_game

def display_title():
    """Display beautiful blue ASCII art title for the game"""
    
    # Display top and bottom border lines
    print("=" * 72)
    print("""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝""")
    # Display bottom border line
    print("=" * 72)

def main():
    """Main function that runs the Blackjack game"""
    # Display game title screen
    display_title()
    
    # Welcome messages
    print("\nWelcome to the Casino!")
    print("Get ready to play Blackjack!")
    
    # Wait for player to press Enter to start
    input("\nPress \"Enter\" to start the game...")
    
    # Start the Blackjack game
    play_game()

# Check if this file is run directly (not imported)
if __name__ == "__main__":
    main()  # Run the main function


