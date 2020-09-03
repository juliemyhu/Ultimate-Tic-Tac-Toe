# welcome message
# Start Game:
# ask player for board (n)
# create board
# print tic tac toe board 
# Ask Player #1 to give us a spot 
# Check if the game has been won (horizontal, vertical, diagonal)
# Print the board with the spot taken
# Ask Player #2 or computer move to give us coordinates for their spot
# Check if the game has been won (horizontal, vertical, diagonal)
# Print the board with the spot taken
# Do these steps again and again until:
# If someone wins, end the game and print ‘Winner!’
# If the board is full, print “Tie!” """"

import random 

# A function that takes in as input an integer n and returns a board of size n x n
# Meaning n rows with n elements inside each row. 
# example: n = 3
# Creates [[0, 1, 2],
#          [3, 4, 5],
#          [6, 7, 8]]
def create_board_ultimate(n):
    board = []
    for row in range(0, n):
        list = []
        for col in range(0, n):
            # difference = n * row
            # position = difference + col 
            # +1 is to account for 0 index
            list.append(n * row + col + 1)
        board.append(list)
    return board
#ex. if n = 3 it would loop through list 0,1,2,3
# 3 * 0 + 0 + 1 = 1
# 3 * 0 + 1 + 1 = 2
# 3 * 0 + 2 + 1 = 3
# 3 * 1 + 0 + 1 = 4
# 3 * 1 + 1 + 1 = 5
# 3 * 1 + 2 + 1 = 6
# 3 * 2 + 0 + 1 = 7
# 3 * 2 + 1 + 1 = 8
# 3 * 2 + 2 + 1 = 9


# A function that takes in any size board and prints it nicely
def print_board(board):
    n = len(board)
    # We want to print each element of the list right?
    print(*board[0], sep = " | ")
    for i in range(1, n):
        print("-" * (n - 1 + (3 * n - 1)))
        print(*board[i], sep = " | ")
    """
    for row in board:
        print(row)
    """

# A function checks that the position is not x or o already.
def check_move(move, board):
    # Imagine move/position is 5 this means board[1][1] board[row][col]
    # 5 - 1 this gives us 4
    # 4
    n = len(board)
    row = (move - 1) // n
    col = (move - 1) % n
    if board[row][col] == move:
        return True #true means its a valid move 
    else:
        return False
    
# A function that takes in a string player and a board and updates player chosen location with player piece
def make_move(player, board):
    next_player = ""
    if (player == "X"):
        next_player = "O"
    else: 
        next_player = "X"
    n = len(board)
    while True:
        move = int(input("Where do you want to put your {}? ".format(player)))
        if move < 0 or move > n*n or check_move(move, board) == False:
            print("Invalid move. Try again.")
        else:
            row = (move - 1) // n
            col = (move - 1) % n
            board[row][col] = player
            return board, move, next_player


def check_win(board, last_move):
    n = len(board)
    row = (last_move - 1) // n
    col = (last_move - 1) % n
    # if move is 5, col is 1 
    player = board[row][col] 
    # check left two spaces. (horizontal)
    if (col - 1 >= 0 and board[row][col - 1] == player) and (col - 2 >= 0 and board[row][col - 2] == player):
        return True
    # check 1 left and 1 right(horizontal)
    elif (col - 1 >= 0 and board[row][col - 1] == player) and (col + 1 < n  and board[row][col + 1] == player):
        return True
    # check 2 right(horizontal)
    elif (col + 1 < n and board[row][col +1 ] == player) and (col + 2 < n and board[row][col + 2 ] == player):
        return True
    # check up 2 (vertical)
    elif (row - 1 >= 0 and board[row-1][col] == player) and (row - 2 >= 0 and board[row-2][col] == player):
        return True
    # check down 2 (vertical)
    elif (row + 1 < n and board[row + 1][col] == player) and (row + 2 < n and board[row + 2][col] == player): 
        return True
    # check up 1 down 1 (vertical)
    elif (row - 1 >= 0 and board[row-1][col] == player) and (row + 1 < n and board[row + 1][col] == player):
        return True
    # check diagonal going up left and down right
    elif (row - 1 >= 0 and col - 1 >= 0 and board[row-1][col-1] == player) and (row + 1 < n and col + 1 < n and board[row+1][col+1] == player):
        return True
    # check diagonal going up right and down left
    elif (row - 1 >= 0 and col + 1 < n and board[row-1][col+1] == player) and (row + 1 < n and col - 1 >= 0 and board[row+1][col-1] == player):
        return True
    # check diagonal up left 1 and up left 2 
    elif (row - 1 >= 0 and col - 1 >= 0 and board[row-1][col-1] == player) and (row - 2 >= 0 and col - 2 >= 0 and board[row-2][col-2] == player):
        return True
    # check diagonal down right 1 and down right 2 
    elif (row + 1 < n and col + 1 < n and board[row+1][col+1] == player) and (row + 2 < n and col + 2 < n and board[row+2][col+2] == player):
        return True 
    # check diagonal up right 1 and up right 2 
    elif (row - 1 >= 0 and col + 1 < n and board[row-1][col+1] == player) and (row - 2 >= 0 and col + 2 < n and board[row-2][col+2] == player):
        return True
    # check diagonal down left 1 and down left 2
    elif (row + 1 < n and col - 1 >= 0 and board[row+1][col-1] == player) and (row + 2 < n and col - 2 >= 0 and board[row+2][col-2] == player):
        return True
    else:
        return False

def make_move_computer(player, board):
    next_player = ""
    if (player == "X"):
        next_player = "O"
    else: 
        next_player = "X"
    n = len(board)
    while True:
        random_move = random.randint(1,n*n)
        if random_move < 0 or random_move > n*n or check_move(random_move, board) == False:
            print("Invalid move. Try again.")
        else:
            row = (random_move - 1) // n
            col = (random_move - 1) % n
            board[row][col] = player
            print("Computer chose to move:{} ".format(random_move))
            print_board(board)
            return board, random_move, next_player

def num_players():
    while True:
        players = int(input("How many players are there? "))
        if players == 1:
            return 1
        elif players == 2:
            return 2
        else:
            print("Not a valid number of players")
"""            
board = create_board_ultimate(3)
print_board(board)

print()
board_2 = create_board_ultimate(9)
print_board(board_2)

print()
#board = create_board_dynamic(4)
#print_board(board)
"""
def ask_play_again():
  while True:
    play_again = input("Want to play again?: (Y/N) ")
    play_again = play_again.upper()
    if play_again == "Y":
        print()
        play()
    elif play_again == "N":
      print("okay goodbye")
      break
    else: 
      print("Invalid input")

"""
play function:
    1. ask player how big board they want
    2. create that board save it to variable
    3. ask if they want 1 or 2 player
    4. while loop until game ends
        4.a: first player makes move
        4.b check if that move ends the game. 
        4.c next player/computer makes move
        4.d check if that move ends the game.
    5. game ends. Tie or someone wins. We can ask if they want to play again. 
"""
def play():
    print("Welcome to Ultimate TicTacToe!")
    n = 0
    while n < 3:
        n = int(input("How ultimate do you want to be? \n(Choose how big of a board you want to play with. At least 3): "))
    board = create_board_ultimate(n)
    number_players = num_players()
    player = "X"
    moves_made = 0
    while True:
        if (number_players == 2):
            # Player 1 moves
            print_board(board)
            board, last_move, player = make_move(player, board)
            if(check_win(board, last_move)):
                last_player = ""
                if(player == "X"):
                    last_player = "O"
                else:
                    last_player = "X"
                print_board(board)
                print()
                print("Player {} wins!".format(last_player))
                break
            moves_made += 1
            if (moves_made >= n*n):
                print("Tie! No one wins.")
                break
            # Player 2 moves
            print_board(board)
            print()
            board, last_move, player = make_move(player, board)
            if(check_win(board, last_move)):
                last_player = ""
                if(player == "X"):
                    last_player = "O"
                else:
                    last_player = "X"
                print_board(board)
                print("Player {} wins!".format(last_player))
                break
            moves_made += 1
            if (moves_made >= n*n):
                print("Tie! No one wins.")
                break
        else:
            # Player 1 moves
            print_board(board)
            board, last_move, player = make_move(player, board)
            if(check_win(board, last_move)):
                last_player = ""
                if(player == "X"):
                    last_player = "O"
                else:
                    last_player = "X"
                print_board(board)
                print("Player {} wins!".format(last_player))
                break
            moves_made += 1
            if (moves_made >= n*n):
                print("Tie! No one wins.")
                break
            # computer moves
            print_board(board)
            board, last_move, player = make_move_computer(player, board)
            if(check_win(board, last_move)):
                last_player = ""
                if(player == "X"):
                    last_player = "O"
                else:
                    last_player = "X"
                print("Player {} wins!".format(last_player))
                break
            moves_made += 1
            if (moves_made >= n*n):
                print("Tie! No one wins.")
                break
    ask_play_again()

play()