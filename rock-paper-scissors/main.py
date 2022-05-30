# ROCK, PAPER, SCISSORS

'''
(module) random
Random variable generators.
'''
import random

# create list of all possible options
lst = ['Rock', 'Paper', 'Scissors']

# welcome message
print('| Rock | Paper | Scissors | Are you ready to rumble?!')

# insert loop
while True:
    # accept user input and convert to uppercase for uniformity
    player_choice = input('Enter one choice from the following - "R, P or S": ')
    player_choice = player_choice.upper()
    # match input letters to words in created list of possible options
    if player_choice == 'R':
        player_choice = player_choice.replace('R', 'Rock')
    if player_choice == 'P':
        player_choice = player_choice.replace('P', 'Paper')
    if player_choice == 'S':
        player_choice = player_choice.replace('S', 'Scissors')
    # generate computer choice
    computer_choice = random.choice(lst)
    # print output of both players
    print('Player ({}) : CPU ({})'.format(player_choice, computer_choice))
    #if else statements to decide who wins
    if player_choice in lst:
        if player_choice == computer_choice:
            print("It's a tie! Try again.")
        elif player_choice == 'Rock' and computer_choice == 'Scissors':
            print ('Player Wins! Game Over!')
            break
        elif player_choice == 'Rock' and computer_choice == 'Paper':
            print ('CPU Wins! Game Over!')
            break
        elif player_choice == 'Scissors' and computer_choice == 'Paper':
            print ('Player Wins! Game Over!')
            break
        elif player_choice == 'Scissors' and computer_choice == 'Rock':
            print ('CPU Wins! Game Over!')
            break
        elif player_choice == 'Paper' and computer_choice == 'Rock':
            print ('Player Wins! Game Over!')
            break
        elif player_choice == 'Paper' and computer_choice == 'Scissors':
            print ('CPU Wins! Game Over!')
            break
        else:
            # This is, however, unlikely
            print('Invalid')
    else:
        print('Error! Please enter a valid choice.')
