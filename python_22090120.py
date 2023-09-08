import random

# Creates a game board using 2Dlist
ttt_board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

# Variables to store user and computer scores
score_user = 0
score_comp = 0


# Main user-defined function that contains all other main user-defined functions
def main():
    global ttt_board, score_user, score_comp

    # Creates a text file and writes the header for the logs data
    file = open('log.txt', 'w')
    file.write('Move Count' + '         ' + 'Comp(C)/Human(H)' + '      ' + 'Row' + '                ' + 'Column' + '              ' + 'Piece(O/X)')
    file.write('\n')
    file.close()

    # Creates players (human-X & computer-O)
    players = ["X", "O"]
    # List that holds data of moves
    data = []   
    # Determines who moves (human-X & computer-O )
    move = 0
    move_count = 0
    draw = True

    # If game is not tied, this while loop will be execute
    while check_draw(ttt_board) != draw:
        # Displays game board
        display_board(ttt_board)
        # Human makes the first move
        if move == 0:
            print("\nYour turn!")
            # Retrieves the values of row and columns and displays in onto the board
            row, col = user_move(ttt_board)
            ttt_board[row][col] = players[move]
            # To keep track of the number of moves
            move_count += 1
            # Calls log_info function and receives the data as arguments
            log_info(data, move_count, players, move, row, col)
        else:
            # Computer' makes the second move
            print("\nComputer plays!")
            # Retrieves the values of row and columns and displays in onto the board
            row, col = comp_move(ttt_board)
            ttt_board[row][col] = players[move]
            # To keep track of the number of moves
            move_count += 1
            # Calls log_info() function and receives the data as arguments 
            log_info(data, move_count, players, move, row, col)
            

        # Checks if any player has won
        if check_win(ttt_board):
            display_board(ttt_board)
            # Human wins, human gains 1 point
            if move == 0:
                print('\nHuman wins!')
                print('Human gained 1 point!!!')
                score_user += 1
                break
            # Computer wins, computer wins 1 point
            else:
                print('\nComputer wins!')
                print('Computer gained 1 point!!!')
                score_comp += 1
                break

        # Switches to next player
        move = 1 - move

    # If game is tied, it will simply print the final board
    else:
        display_board(ttt_board)
        print('\nGame over')
        print("It's a tie!")

# Displays title and instructions
def main_menu():
    # Displays title
    print("------------------------")
    print("---   TIC TAC TOE   ---")
    print('Human (X) vs Computer (O)')
    print("------------------------")

    # Displays instructions
    print('\nInstructions :')
    print('1. Human makes the first move')
    print('2. Human types in the row number')
    print('2. Human types in the column number')
    print('3. Computer makes the next move')
    print('4. Game ends when 3 of the same piece are placed in a row, column or diagonal\n')


# Displays game board
def display_board(ttt_board):
    # The index of each item will be used as the row and column values
    print("\n     1     2    3 \n")
    print('1   ' + ttt_board[0][0] + '  |  ' + ttt_board[0][1] + '  |  ' + ttt_board[0][2])
    print('    ---+-----+---')
    print('2   ' + ttt_board[1][0] + '  |  ' + ttt_board[1][1] + '  |  ' + ttt_board[1][2])
    print('    ---+-----+---')
    print('3   ' + ttt_board[2][0] + '  |  ' + ttt_board[2][1] + '  |  ' + ttt_board[2][2])


# Retrives user input/move and checks it
def user_move(ttt_board):
    # All possible values for rows and columns
    posibble_inputs = [1, 2, 3]
    while True:
        # Asks human for row value and stores it in row variable
        row = input("\nEnter row number: ")
        # Checks input for error
        while not row.isdigit() or int(row) not in posibble_inputs:
            row = input("Enter row number between 1-3: ")
        row = int(row)
        # Asks human for column value and stores it in col variable
        col = input("Enter column number: ")
        # Checks input for error
        while not col.isdigit() or int(col) not in posibble_inputs:
            col = input("Enter column number between 1-3: ")
        col = int(col)
        # When human selects filled box, request another input value
        if ttt_board[row-1][col-1] != " ":
            print("Pick an empty box!")
        else:
            return (row-1, col-1)
            

# Retrives computer input/move
def comp_move(ttt_board):
    # List to store all possible moves a computer may choose
    possible_moves = []
    # Iterates through each row
    for row in range(len(ttt_board)):
        # Iterate through each column for the current row
        for col in range(len(ttt_board[0])):
            # Checks if any of the row and column values are empty
            if ttt_board[row][col] == " ":
                possible_moves.append((row, col))
    # Return the randomised row and column values
    return possible_moves[random.randrange(len(possible_moves))]


# Checks each row of game board
def check_row(ttt_board, row):
    # Checks if each row has similar pieces
    if ttt_board[row][0] == ttt_board[row][1] and ttt_board[row][1] == ttt_board[row][2] and ttt_board[row][0] != " ":
        return True
    else:
        return False

# Checks each column of game board
def check_column(ttt_board, col):
    # Checks if each row has similar pieces
    if ttt_board[0][col] == ttt_board[1][col] and ttt_board[1][col] == ttt_board[2][col] and ttt_board[0][col] != " ":
        return True
    else:
        return False

# Checks each diagonal of game board
def check_diagonals(ttt_board):
    # Checks if each row has similar pieces
    if ttt_board[0][0] == ttt_board[1][1] and ttt_board[1][1] == ttt_board[2][2] and ttt_board[0][0] != " ":
        return True
    elif ttt_board[2][0] == ttt_board[1][1] and ttt_board[1][1] == ttt_board[0][2] and ttt_board[2][0] != " ":
        return True
    else:
        return False

# Checks if any players won
def check_win(ttt_board):
    # Iterates 3 times to be able to go through every column and row
    for i in range(3):
        if check_row(ttt_board, i):
            return True
        if check_column(ttt_board, i):
            return True
    if check_diagonals(ttt_board):
        return True
    else:
        return False

# Checks if the game board is full
def check_draw(ttt_board):
    # Iterates through every item in the board, check if empty space exists
    for item in ttt_board:
        if " " in item:
            return False
    return True



# Records/logs all moves of the game
def log_info(data, move_count, players, move, row, col):
    # Opens the file for appending data
    file = open('log.txt', 'a')

    # List that holds data of moves
    data = []
    
    # Appends data of moves into a list called data
    data.append(str(move_count))
    if move == 0:
        data.append('H')
    else:
        data.append('C')
    data.append(str(row+1))
    data.append(str(col+1))
    data.append(str(players[move]))

    # Iterates through the list of data and writing it into the log text file
    for i in range(len(data)):
        entry_1 = data[i] + '                    '
        file.write(entry_1)
    
    file.write('\n')

    file.close()


# Prints the scores for computer and user
def score_board():
    print("\n\n--------------------------------")
    print("            SCOREBOARD       ")
    print("--------------------------------")
    print('      Human : ' + str(score_user) + ' points')
    print('      Computer : ' + str(score_comp) + ' points')
    print("--------------------------------\n")


# Asks human if want to play again
def play_again():
    global ttt_board, score_comp, score_user

    while True:
        # Asks human if want to play again
        play_again = input("\nPlay again? Type 'y' for Yes or 'n' for No: ")

        # Checks if input is y or n
        if  play_again == "y":
             # Asks human if want to reset score
            reset_score =  input("\nReset score? (y/n): ") 
            # Checks the input if it is valid
            if reset_score == 'y':
                score_user = 0
                score_comp = 0
                ttt_board = [ [" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
                return True
            elif reset_score == "n":
                ttt_board = [ [" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
                return True
            # Checks input for error
            else:
                continue 
            
        elif play_again == 'n':
           break
        # Checks input for error
        else:
            continue

        
    


# Runs all the main user-defined functions
while True:
    # Prints the main menu alongside the instructions
    main_menu()
    # Store human input, asking if they would like to start the game
    start_game = input('Start game? "y" for yes or "n" for no : ')

    # If human types in y, the while loop executes every main functions
    while start_game == 'y':
        main()
        score_board()
        if play_again():
            pass
        else:
            break
    # If human types in n, the program breaks out of the main while loop, ending the program
    if start_game == 'n':
        break
    # Checks the input of human
    elif start_game != 'n' and 'y':
        continue

    break
    

        
    
        

        

    
    
    
    
     