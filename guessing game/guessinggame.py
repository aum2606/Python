import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_ans(guess,random_number,n):
    if guess > random_number:
            print("Too high")
            return n-1
    elif guess < random_number:
        print("Too low")
        return n-1
    else:
        print(f"You guessed {random_number} correctly you won")


def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the number guessing game!")

    print("I am thinking of a number between 1 and 100. ")
    random_number = random.randint(1,100)
    n = set_difficulty()
    guess = 0
    while n!=0:
        print(f"You have {n} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        n = check_ans(guess,random_number,n)
        if n==0:
            print("You've run out of guesses, you lose.")
        elif guess!=random_number:
            print("Guess again.")

game()