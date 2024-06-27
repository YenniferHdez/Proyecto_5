        #GUESS THE NUMBER

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Fuction to check user's guess against actual answer.
def check_answer (guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#Make fuction to set difficulty.
def set_difficulty():
    level = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psssst, the correct answer is {answer}.")

    turns = set_difficulty()

    #Repeat the guessing fuctionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the number.")
        
        #Let the user guess a number.
        guess = int(input("Make the guess:"))

        #Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0: 
            print("You've run out of guesses, you lose.")
            print(f"Psssst, the correct answer is {answer}.")
            return
        elif guess != answer:
            print("Guess again.")



game()