import random


print("welcome to rock paper scissors !!!")
my_choice = input("Enter your choice : ")
choices = ["rock", "paper", "scissors"]
sys_choice = random.choice(choices)
print(f"\nYou chose {my_choice}, computer chose {sys_choice}.\n")

if my_choice == sys_choice:
    print(f"Both players selected {my_choice}. It's a tie!")
elif my_choice == "rock":
    if sys_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif my_choice == "paper":
    if sys_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif my_choice == "scissors":
    if sys_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")


