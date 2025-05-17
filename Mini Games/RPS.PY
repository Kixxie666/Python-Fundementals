import random

# Define the hand shapes
rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    ROCK
    '''

paper = '''
        _______
    ---'   ____)_
            ______)
            _______)
            _______)
    ---.__________)
    PAPER
    '''

scissors = '''
        _______
    ---'   ____)_____
            _________)
        ______________)
        (____)
    ---.__(___)
    SCISSORS
    '''



game = input("Do you want to play a game? ")

if game.lower() == "yes":
    pc = random.randint(1, 3)
    user = int(input("What is your choice? Type '1' for rock, '2' for paper, and '3' for scissors: "))
    

    if pc == 1:
        pc_choice = rock
    elif pc == 2:
        pc_choice = paper
    elif pc == 3:
        pc_choice = scissors
    
    # Determine User's choice
    if user == 1:
        user_choice = rock
    elif user == 2:
        user_choice = paper
    elif user == 3:
        user_choice = scissors


    print("YOU PICKED:\n" + user_choice)
    print("PC:\n" + pc_choice)

    # Print choices
    if user == 1 and pc == 1:
        print("It's a draw! please try again!")

    if user == 1 and pc == 2:
        print("PC wins!")
    if user == 1 and pc == 3:
        print("You win!")

    if user == 2 and pc == 1:
        print("You win!")

    if user == 2 and pc == 2:
        print("Draw!")
    if user == 2 and pc == 3:
        print("PC Wins!")

    if user == 3 and pc == 1:
        print("PC Wins")

    if user == 3 and pc == 2:
        print("You Win!")
    if user == 3 and pc == 3:
        print("Draw!")
