import random

def DRG():
    computer_move = random.choice(range(1, 7))

    player_move = random.choice(range(1, 7))

    print("The computer rolled a:",computer_move)
    print("You rolled a:",player_move)

    if computer_move > player_move:
        print("The computer Wins")

    elif computer_move == player_move:
        print("Its a draw you both rolled the same number.")
    else:
        print("You win!")

def RPC():
    user_Input_RPC = input("Please chose either Rock, Paper, or Scissors: ")
    computer_Choice = ["Rock", "Paper", "Scissors"]
    computer_Move = random.choice(computer_Choice)

    print("The computer Chooses:", computer_Move)

    if computer_Move == "Rock" and user_Input_RPC == "Scissors" or computer_Move == "Scissors" and user_Input_RPC == "Paper" or computer_Move == "Paper" and user_Input_RPC == "Rock":
        print("The computer wins!")

    if computer_Move == "Rock" and user_Input_RPC == "Rock" or computer_Move == "Scissors" and user_Input_RPC == "Scissors" or computer_Move == "Paper" and user_Input_RPC == "Paper":
        print("You both chose the same thing its a draw.")

    if computer_Move == "Scissors" and user_Input_RPC == "Rock" or computer_Move == "Paper" and user_Input_RPC == "Scissors" or computer_Move == "Rock" and user_Input_RPC == "Paper":
        print("You Win!")

def ng():
    print("Please guess the number 1-10")
    user_guess = int(input("What is your guess: "))
    count = 1
    computer_Guess = random.choice(range(1, 50))
    if user_guess == computer_Guess:
            print("You got it your first try!")
    
    

    while user_guess != computer_Guess:
        count += 1
        user_guess = int(input("What is your guess: "))
        
        if user_guess > computer_Guess:
            print("Lower")
        elif user_guess < computer_Guess:
            print("Higher")
        if user_guess == computer_Guess:
            print("You got it! The number was", computer_Guess)
            print("It took you this many guesses to figure it out.", count)


def Main():
    choice_selector = input("Which game would you like to play? Type 1 for Dice roll game, 2 for rock paper scissors, and 3 for number guessor.")
    

    if choice_selector == "1":
        DRG()
    elif choice_selector == "2":
        RPC()
    elif choice_selector == "3":
        ng()

Main()