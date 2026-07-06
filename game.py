import os
import random
import time
import winsound
import pygame

# Initialize pygame mixer for music
pygame.mixer.init()

money = 20000
player_name = ""

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Print a centered header"""
    print("╔" + "═" * 50 + "╗")
    print("║" + title.center(50) + "║")
    print("╚" + "═" * 50 + "╝")

def print_box(title, content=""):
    """Print content in a box with optional title"""
    if title:
        print(f"┌─ {title} " + "─" * (46 - len(title)))
    else:
        print("┌" + "─" * 48)
    
    if content:
        for line in content.split('\n'):
            slow_print(f"│ {line:<48}")
    
    print("└" + "─" * 48)

def slow_print(text, speed=0.05, sound=True):
    """Print text letter by letter with optional beep sound
    sound: True/False to enable/disable the beep"""
    for char in text:
        print(char, end='', flush=True)
        if sound and char not in ' \n':  # Play sound for non-space characters
            winsound.Beep(800, 30)  # Frequency: 800 Hz, Duration: 30 ms
        time.sleep(speed)
    print()

def separator():
    """Print a horizontal line"""
    print("─" * 50)

def play_music(file_path, loops=-1):
    """Play music from a file
    file_path: path to audio file (.mp3, .wav, .ogg, etc.)
    loops: -1 for infinite loop, 0 for play once, or specify number of loops"""
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(loops)
       
    except Exception as e:
        print(f"Error loading music: {e}")

def stop_music():
    """Stop the currently playing music"""
    pygame.mixer.music.stop()
    

def change_music(file_path, loops=-1):
    """Stop current music and play a new file
    file_path: path to audio file
    loops: -1 for infinite loop, 0 for play once"""
    stop_music()
    time.sleep(0.5)
    play_music(file_path, loops)

def set_music_volume(volume):
    """Set music volume (0.0 to 1.0)
    0.0 = silent, 1.0 = full volume"""
    pygame.mixer.music.set_volume(max(0, min(1, volume)))
    print(f"♫ Volume: {int(volume * 100)}%")


def play_blackjack():
    """Run a simple blackjack mini-game using the shared global money variable."""
    global money
    global player_name

    win_streak = 0
    force_all_in = False

    while True:
        if force_all_in:
            bet = int(input(f"How much do you want to bet? You have ${money}: "))
            slow_print(f"{player_name}: Actually...")
            time.sleep(1)
            slow_print(f"{player_name}: You know what.. I'm going all in!")
            time.sleep(1)
            bet = money
               
        else:
            while True:
                try:
                    bet = int(input(f"How much do you want to bet? You have ${money}: "))
                except ValueError:
                    slow_print("Please enter a valid number.")
                    continue

                if bet <= 0:
                    slow_print("Bet must be greater than 0.")
                    continue
                if bet > money:
                    slow_print("You cannot bet more than you have.")
                    continue
                if bet == money:
                    slow_print(f"{player_name}: actually it's not a good idea to bet all your money.")
                    continue
                break

        slow_print("The dealer shuffles the cards.")
        time.sleep(1)

        player_total = random.randint(2, 11) + random.randint(2, 11)
        dealer_total = random.randint(2, 11) + random.randint(2, 11)

        if force_all_in:
            player_total = 22
            while dealer_total < 17:
                dealer_total += random.randint(2, 11)
            slow_print(f"Your total is {player_total}")
            slow_print(f"Dealer has {dealer_total}")
            slow_print("Bust! You lose!")
            money -= bet
            win_streak = 0
            force_all_in = False
        else:
            slow_print(f"Your total is {player_total}")
            slow_print(f"The dealer shows {dealer_total}")

            while True:
                choice = input("Hit or stand? ").lower()
                if choice == "hit":
                    player_total += random.randint(2, 11)
                    slow_print(f"Your total is {player_total}")

                    if player_total > 21:
                        slow_print("Bust! You lose!")
                        money -= bet
                        force_all_in = False
                        break
                else:
                    while dealer_total < 17:
                        dealer_total += random.randint(2, 11)
                    slow_print(f"Dealer has {dealer_total}")
                    if dealer_total > 21 or player_total > dealer_total:
                        slow_print("You win!")
                        money += bet
                        win_streak += 1
                        force_all_in = win_streak >= 2
                    elif player_total < dealer_total:
                        slow_print("You lose")
                        money -= bet
                        force_all_in = False
                    else:
                        slow_print("It's a tie")
                        force_all_in = False
                    break
        slow_print(f"Your balance is now ${money}")
        time.sleep(1)

        if money <= 0:
            slow_print("You are out of money. Game over.")
            break



# ============================================
# YOUR GAME CODE GOES HERE
# ============================================

def main():
    global money
    clear_screen()
    print_header("The Marker")
    print()

    music_file = os.path.join(os.path.dirname(__file__), "music", "start.mp3")
    play_music(music_file)
    sure = 0
    # Add your game code here!
    money = 20000
    print("Balance $" + str(money))
    slow_print("Welcome to The Marker! A text-based action game.")
    while sure == 0:
        name = input("But first What is your name? ")
        ask = input("Are you sure you want to be called " + name + "? (yes/no) ").lower()
        if ask == "yes":
            sure = 1
    global player_name
    money = int(input("How much money do you want to start with? (Default $20000) ") or 20000)
    player_name = name
    slow_print(f"Hello {name}, welcome to The Marker!")
    slow_print("You have $" + str(money) + " to start your adventure.")
    time.sleep(2)
    stop_music()
    clear_screen()
    time.sleep(4)
    music_file = os.path.join(os.path.dirname(__file__), "music", "casinojazz.mp3")
    play_music(music_file)
    time.sleep(5)
    print_header("Casino")
    slow_print("You are a known gambler in Las Vegas!")
    time.sleep(1)
    slow_print("A friend of yours told you about this casino called TONYS CASINO, and you decided to check it out.")
    time.sleep(1)
    print_box("Dealer", "Good evening sir, Welcome to TONYS CASINO! \nready for a bit of black jack?")
    time.sleep(1)
    play_blackjack()






if __name__ == "__main__":
    main()
