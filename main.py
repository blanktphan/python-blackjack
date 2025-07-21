# Import main game function from game_logic.py
from game_logic import play_game

def display_title():
    """Display beautiful ASCII art title for the game with custom colors"""
    
    # ANSI escape codes for colors
    RED = "\033[91m"
    BLACK = "\033[30m" # Although black is usually default, explicitly setting it for clarity
    RESET = "\033[0m" # Reset to default color

    # Display top and bottom border lines
    print("=" * 72)
    print(f"""
{RED}██████╗ ██╗      █████╗ ██   ██╗██╗  ██╗{RESET}     {BLACK}██╗ █████╗  ██████╗██╗  ██╗{RESET}
{RED}██╔══██╗██║     ██╔══██╗███  ██║██║ ██╔╝{RESET}     {BLACK}██║██╔══██╗██╔════╝██║ ██╔╝{RESET}
{RED}██████╔╝██║     ███████║███████║█████╔╝ {RESET}     {BLACK}██║███████║██║     █████╔╝ {RESET}
{RED}██╔══██╗██║     ██╔══██║██╔═███║██╔═██╗ {RESET}{BLACK}██   ██║██╔══██║██║     ██╔═██╗ {RESET}
{RED}██████╔╝███████╗██║  ██║██║  ██║██║  ██╗{RESET}{BLACK}╚█████╔╝██║  ██║╚██████╗██║  ██╗{RESET}
{RED}╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝{RESET}{BLACK} ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝{RESET}""")
    # Display bottom border line
    print("=" * 72)

def main():
    """Main function that runs the Blankjack game"""
    # Display game title screen
    display_title()
    
    # Welcome messages
    print("\nWelcome to the Casino!")
    print("Get ready to play Blankjack!")
    
    # Wait for player to press Enter to start
    input("\nPress \"Enter\" to start the game...")
    
    # Start the Blackjack game
    play_game()

# Check if this file is run directly (not imported)
if __name__ == "__main__":
    main()  # Run the main function