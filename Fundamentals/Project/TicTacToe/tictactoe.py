import random

#Step 1: Print out a board 
# where each index 1-9 corresponds with a number on a number pad

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


#Step 2: a function that can take in a player input and assign their marker as 'X' or 'O'. 
# Think about using while loops to continually ask until you get a correct answer.
def player_input():
    maker = ''
    
    while  not (maker == 'X' or maker == 'O'):
        maker = str(input("Do you want to be 'X' or 'O' ? ")).upper()

        if maker == 'X':
            return ('X', 'O')
        return ('O', 'X')


#Step 3:a function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position] = marker

#Step 4: a function that takes in a board and a mark (X or O) 
# and then checks to see if that mark has won.
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


#Step 5: Choosing player goes first
def choose_first():
    if random.randint(0, 1) == 1:
        return 'Player 2'
    return 'Player 1'


#Step 6: returns a boolean indicating whether a space on the board is freely available.
def space_cheack(board, position):
    return board[position] == ' '


#Step 7: checks if the board is full and returns a boolean value. True if full, Fals
def full_board_check(board):
    for i in range(1, 10):
        if space_cheack(board, i):
            return False
    return True



#Step 8: Funtion to ask  a player's next position (as a number 1-9) 
# and then uses the function from step 6 to check if it's a free position. 
# If it is, then return the position for later use.

def player_choice(board):
    position = 0
    while ( not position in range(1, 10)
    or not space_cheack(board, position)):
        position = int(input('Choose your next position: (1-9) '))
    return position


#Step 9: Funtion to ask  if they want to play again and returns a boolean True if they do want to play again.
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


#Main function
if __name__ == "__main__":
    print('Welcome to Tic Tac Toe !')

    while True:
        #reset the board
        the_board = [' '] * 10
        # ('x', 'O' ) or ('O', 'X')
        player1_marker, player2_marker = player_input()
        print(player1_marker, player2_marker)
        turn = choose_first()
        
        if turn == 'Player 1':
            print('You will go first')
        else:
            print('Player 2 will go first')
        play_game  = input('Are you ready to play? Enter Yes or No ? ')

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                #Player1's turn

                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)
            
                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print('Congratulations !!!! You have won a game !!! ')
                    game_on = False
            
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('The game is a draw!!!')
                        game_on = False
                    else:
                        turn = 'Player 2'

            else:
                #Player2'turn

                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Oh no !!! Player 2 has won !!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        print('The game is draw')
                        game_on = False
                    else:
                        turn = 'Player 1'

        if not replay():
            print('Thank for playing ^^')
            break
