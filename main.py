import random

# Scissors cut Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitate Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# Rock crushes Scissors

#           0    1     2         3     4
# 	       Rock	Paper Scissors Lizard Spock
# 0 Rock      0	  -1	 1      1	   -1
# 1 Paper	  1	   0	-1	   -1	    1
# 2 Scissors -1	   1	 0	    1	   -1
# 3 Lizard	 -1	   1	-1	    0	    1
# 4 Spock	  1	  -1	 1	   -1	    0

WIN = 1
TIE = 0
LOSE = -1
rock = 0
paper = 1
scissors = 2
lizard = 3
spock = 4


def determine_winner(player1, player2):
 
    # Create a nested list for the truth table
    truth_table = [
        [TIE, LOSE, WIN, WIN, LOSE],
        [WIN, TIE, LOSE, LOSE, WIN],
        [LOSE, WIN, TIE, WIN, LOSE],
        [LOSE, WIN, LOSE, TIE, WIN],
        [WIN, LOSE, WIN, LOSE, TIE]
    ]

    outcome = truth_table[player1][player2]
    return outcome



if __name__ == '__main__':

    # key, value pairs for determining winner and labeling
    move_hash_set = {
        "Rock": 0,
        "r": 0,
        "Paper": 1,
        "p": 1,
        "Scissors": 2,
        "s": 2,
        "Lizard": 3,
        "l": 3,
        "Spock": 4
    }

    label = {
        0: "Rock",
        1: "Paper",
        2: "Scissors",
        3: "Lizard",
        4: "Spock"
    }

    # code block used to get computer and user moves
    
    computer_move = random.randint(0, 4)
    user_input = input("Rock, Paper, Scissors, Lizard, Spock\n")
    user_move = -1

    if user_input in move_hash_set:
        user_move = move_hash_set[user_input]
    else:
        print("Not a Valid Entry")


    print("Computer chooses:", label[computer_move])

    outcome = determine_winner(user_move, computer_move)
    if outcome == 1:
        print("You won!")
    if outcome == 0:
        print("Tie!")
    if outcome == -1:
        print("You Lost!")


