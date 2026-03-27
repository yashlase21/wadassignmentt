import random

print("Welcome to Rock-Paper-Scissors Game!")

choices = ["rock", "paper", "scissors"]

# User choice
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Computer choice
computer_choice = random.choice(choices)

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

# Decide winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("🎉 You win!")
elif user_choice in choices:
    print("💻 Computer wins!")
else:
    print("❌ Invalid choice, please type rock, paper, or scissors.")
