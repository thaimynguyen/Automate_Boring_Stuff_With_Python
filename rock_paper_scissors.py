"""
link: https://automatetheboringstuff.com/2e/chapter2/#calibre_link-129
textbook page 51

This program creates a simple rock, paper, scissors game. The output will look like this:

ROCK, PAPER, SCISSORS
0 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
p
PAPER versus...
PAPER
It is a tie!
0 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
s
SCISSORS versus...
PAPER
You win!
1 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
q

"""
import sys, random

# These variables keep track of the number of wins, losses and ties.
win_count = 0
loss_count = 0
tie_count = 0

# first key represents user's choice, second key represents computer's choice
# final value represents result (1 = user wins, 0 = tie, -1 = user loses)
score_matrix = {    
    'r': {'r': 0, 's': 1, 'p': -1},
    'p': {'p': 0, 'r': 1, 's': -1},
    's': {'s': 0, 'p': 1, 'r': -1}
    }


print("ROCK, PAPER, SCISSORS")

while True: # the main game loop
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    print(f'{win_count} Wins, {loss_count} Losses, {tie_count} Ties')
    user_choice = input()
    if user_choice == 'q':
        sys.exit() # Quit the program

    #Display user's choice:
    if user_choice == 'r':
        print('ROCK versus....')
    elif user_choice == 'p':
        print('PAPER versus....')
    elif user_choice == 's':
        print('SCISSORS versus....')

    # Display computer's choice:
    computer_number = random.randint(1,3)
    if computer_number == 1:
        computer_choice = 'r'
        print('ROCK')
    elif computer_number == 2:
        computer_choice = 'p'
        print('PAPER')
    else:
        computer_choice = 's'
        print('SCISSORS')

    # Display result
    if score_matrix[user_choice][computer_choice] == 0:
        print('It is a tie!')
        tie_count += 1
    elif score_matrix[user_choice][computer_choice] == 1:
        print('You win!')
        win_count +=1
    elif score_matrix[user_choice][computer_choice] == -1:
        print('You lose!')
        loss_count += 1

    # Quit the program if input is invalid
    else:
        sys.exit()

