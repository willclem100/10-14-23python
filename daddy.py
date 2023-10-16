import random

print("Welcome to the coolness checker!")
name = input("What is your name? ")

cool_names = ["Nathan", "Daddy", "Mommy", "Gammaw", "Gangan", "Adam", "Logan"]
if name.capitalize() in cool_names:
    print(f"You are cool, {name}!")
elif name.capitalize() == "Jackson":
    print(f"You are not cool, {name}!")
else:
    print(f"You are mediocrily cool, {name}!")
    
print("Welcome to the Rock, Paper, Scissors game!")

player = input("Enter a choice (rock, paper, scissors): ")
options = ["rock", "paper", "scissors"]
computer = random.choice(options)

def check_win():
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    
    elif player == "rock" and computer == "paper":
        return "Paper covers rock! You lose."
    
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors! You win!"
    
    elif player == "paper" and computer == "rock":
        return "Paper covers rock! You win!"
    
    elif player == "paper" and computer == "scissors":
        return "Scissors cuts paper! You lose."
    
    elif player == "scissors" and computer == "rock":
        return "Rock smashes scissors! You lose."
    
    elif player == "scissors" and computer == "paper":
        return "Scissors cuts paper! You win!"
    
    else:
        return "Invalid input! You have not entered rock, paper or scissors, try again."

print(check_win())