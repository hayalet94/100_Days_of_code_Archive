import random

user_score = 0
computer_score = 0

def rock():

    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

def paper():

# Paper
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

def scissors():

# Scissors
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("Welcome to the Rock, Paper, Scissors - Game! Type number for your choice: ")

while True:

    user_choice = int(input("\n0 - Rock | 1 - Paper | 2 - Scissors : "))
    computer_choice = random.randint(0,2)
    
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number. Try again!")
    elif user_choice == 0 and computer_choice == 2:
        print("\n\nYour Choice:")
        print("_"*40)
        rock()
        print("Computer Choice:")
        print("_"*40)
        scissors()
        print("You win!")
        user_score += 1
        print("_"*40)
        print(f"\nYour Score: {user_score}")
        print(f"Computer Score: {computer_score}")
        print("_"*40)

    elif computer_choice == 0 and user_choice == 2:
        print("\n\nYour Choice:")
        print("_"*40)
        scissors()
        print("Computer Choice:")
        print("_"*40)
        rock()
        print("You lose!")
        computer_score += 1
        print("_"*40)
        print(f"\nYour Score: {user_score}")
        print(f"Computer Score: {computer_score}")
        print("_"*40)
    elif computer_choice > user_choice:
        print("\n\nYour Choice:")
        print("_"*40)
        if user_choice == 0:
            rock()
        elif user_choice == 1:
            paper()
        elif user_choice == 2:
            scissors()
        print("Computer Choice:")
        print("_"*40)
        if computer_choice == 0:
            rock()
        elif computer_choice == 1:
            paper()
        elif computer_choice == 2:
            scissors()
        print("You lose!")

        computer_score += 1
        print("_"*40)
        print(f"\nYour Score: {user_score}")
        print(f"Computer Score: {computer_score}")
        print("_"*40)
    elif user_choice > computer_choice:
        print("\n\nYour Choice:")
        print("_"*40)
        if user_choice == 0:
            rock()
        elif user_choice == 1:
            paper()
        elif user_choice == 2:
            scissors()
        print("Computer Choice:")
        print("_"*40)
        if computer_choice == 0:
            rock()
        elif computer_choice == 1:
            paper()
        elif computer_choice == 2:
            scissors()
        print("You win!")
        user_score += 1
        print("_"*40)
        print(f"\nYour Score: {user_score}")
        print(f"Computer Score: {computer_score}")
        print("_"*40)
    elif computer_choice == user_choice:
        print("\n\nYour Choice:")
        print("_"*40)
        if user_choice == 0:
            rock()
        elif user_choice == 1:
            paper()
        elif user_choice == 2:
            scissors()
        print("Computer Choice:")
        print("_"*40)
        if computer_choice == 0:
            rock()
        elif computer_choice == 1:
            paper()
        elif computer_choice == 2:
            scissors()
        print("It's a draw!")
        print("_"*40)
        print(f"\nYour Score: {user_score}")
        print(f"Computer Score: {computer_score}")

