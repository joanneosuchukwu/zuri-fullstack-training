# ROCK PAPER SCISSORS
**This is a simple Python code for the famous game, Rock, Paper, Scissors.**

More information on Rock, Paper, Scissors and how to play it can be found <a href = "https://www.youtube.com/watch?v=ND4fd6yScBM">here<a> and <a href = "https://en.wikipedia.org/wiki/Rock_paper_scissors">here<a>.

* The code is for a two-player game that accepts user input and compares it to a randomly generated computer choice within a given list of corresponding options

* The program accepts **input** of one of "R", "P", or "S" and returns and error message and chance to try again, in a **while loop**, if entry is invalid
```player_choice = input('Enter one choice from the following - "R, P or S": ')```

* Case of string input does not matter as all user string entries are changed to **uppercase** for uniformity
```player_choice = player_choice.upper()```
 

* The letter input, "R", "P", or "S", is then replaced with the game keywords, "Rock", "Paper", or "Scissors" 
```if player_choice == 'R':```
        ```player_choice = player_choice.replace('R', 'Rock')```
    ```if player_choice == 'P':```
        ```player_choice = player_choice.replace('P', 'Paper')```
    ```if player_choice == 'S':```
        ```player_choice = player_choice.replace('S', 'Scissors')```
* This is compared with the created **list of possible options within the program**.
```lst = ['Rock', 'Paper', 'Scissors']```


* Having imported the Python inbuilt **random module**, code is written for the computer (CPU) generated player entry. (See <a href = "https://docs.python.org/3/library/random.html">link<a> for random.choice documentation)
```import random```
``` computer_choice = random.choice(lst)```

* After which, the **user entry and CPU entry are printed** as so:
```print('Player ({}) : CPU ({})'.format(player_choice, computer_choice))```

* A **nested if, else loop is used to determine the winner**. If there, is a winner, the winner is printed. If there is a tie, the game is returned to the input phase in the **while loop** to try again.
```if player_choice in lst:```
        ```if player_choice == computer_choice:```
            ```print("It's a tie! Try again.")```
        ```elif player_choice == 'Rock' and computer_choice == 'Scissors':```
            ```print ('Player Wins! Game Over!')```
            ```break```
        ```elif player_choice == 'Rock' and computer_choice == 'Paper':```
            ```print ('CPU Wins! Game Over!')```
            ```break```
        ```elif player_choice == 'Scissors' and computer_choice == 'Paper':```
            ```print ('Player Wins! Game Over!')```
            ```break```
       ```` elif player_choice == 'Scissors' and computer_choice == 'Rock':````
            ````print ('CPU Wins! Game Over!')````
            ```break```
        ```elif player_choice == 'Paper' and computer_choice == 'Rock':```
            ```print ('Player Wins! Game Over!')```
            ```break```
        ```elif player_choice == 'Paper' and computer_choice == 'Scissors':```
            ```print ('CPU Wins! Game Over!')```
            ```break```
        ```else:```
            ```# This is, however, unlikely```
            ```print('Invalid')```
    ```else:```
        ```print('Error! Please enter a valid choice.')```

### Joanne Osuchukwu
**Zuri Fullstack Training**
***Student ID: I4G000936QEB***