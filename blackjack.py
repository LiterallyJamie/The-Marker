import random
import time




def slow_print(text, speed=0.05):
    """Print text letter by letter with a delay between each character.
    speed: delay in seconds between characters (default 0.05)"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()  # new line at the end

def play_blackjack():
    global money

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
        break

    player = random.randint(2, 11) + random.randint(2, 11)
    dealer = random.randint(2, 11) + random.randint(2, 11)
    slow_print("Your Total is " + str(player))

    while True:
        choice = input("Hit or stand? ").lower()
        if choice == "hit":
            player += random.randint(2, 11)
            slow_print("Your total is " + str(player))

            if player > 21:
                slow_print("Bust! You lose!")
                money -= bet
                break
        else:
            while dealer < 17:
                dealer += random.randint(2, 11)
            slow_print("Dealer has " + str(dealer))
            if dealer > 21 or player > dealer:
                slow_print("You win!")
                money += bet
            elif player < dealer:
                slow_print("You lose")
                money -= bet
            else:
                slow_print("It's a tie")
            break

    slow_print(f"Your balance is now ${money}")


play_blackjack()
