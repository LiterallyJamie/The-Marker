import random
player = random.randint(2,11) + random.randint(2,11)
dealer = random.randint(2,11) + random.randint(2,11)
print("Your Total is",player)
while True:
    choice = input("Hit or stand?").lower()
    if choice == "hit":
        player += random.randint(2,11)
        print("Your total is",player)
        
        if player > 21:
            print("Bust! You lose!")
            break
    else:
        while dealer < 17:
            dealer += random.randint(2,11)
        print("Dealer has",dealer)
        if dealer > 21 or player > dealer:
            print("You win!")
        elif player < dealer:
            print("You lose")
        else:
            print("Its a tie")
        break
