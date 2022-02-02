from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    
    print(board[1]+'|'+board[2]+ '|'+ board[3])
    print(board[4]+'|'+board[5]+ '|'+ board[6])
    print(board[7]+'|'+board[8]+ '|'+ board[9])


def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

player_input()


def place_marker(board, marker, position):
    
     board[position] = marker
    
    
def win_check(board, mark):
    
    return((board[1]==mark and board[2]== mark and board[3]==mark )or #for row1 

            (board[4]==mark and board[5]==mark and board[6]==mark )or #for row2

            (board[7]==mark and board[8]==mark and board[9]==mark )or #for row3

            (board[1]==mark and board[4]==mark and board[7]== mark )or#for Colm1 

            (board[2]==mark and board[5]==mark and board[8]==mark )or #for Colm 2

            (board[3]==mark and board[6]==mark and board[9]==mark )or #for colm 3

            (board[1]==mark and board[5]==mark and board[9]==mark )or #daignole 1

            (board[3]==mark and board[5]==mark and board[7]==mark )) #daignole 2



import random

def choose_first():
      
    first = random.randint(1,2)
    
    if first == 1 :
        return ('Player 1')
    else:
        return ('Player 2')

def space_check(board, position):
    
    return board[position] == ' '


def full_board_check(board):
    
    count = 0
    
    for i in range(1,10):
        if space_check(board, i) :
            return False
    
    return True

def player_choice(board):
    
    position = 'wrong'
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        
        position = int(input('Choose your next position: (1-9) '))
        
    return position


def replay():
         
    choice = input('Keep playing? Y or N: ')
    
    return choice == 'Y'

#While loop to keep running the game

while True:
    
    ##set evertything up (board, who is first , marker)
    game_board = [' ']*10
    player1_marker,player2_marker = player_input() 
    turn = choose_first()
    print(turn + ' :goes first')
    
    play_game = input('Ready to play? Y or N: ')
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    ###Game play
    
    while game_on :
        
        if turn == 'Player 1':
            ###P1 turn
            
            #show the board
            display_board(game_board)
            #choose a position
            position = player_choice(game_board)
            #place the marker on the position
            place_marker(game_board,player1_marker,position)
            
            #check if they won
            if win_check(game_board,player1_marker):
                display_board(game_board)
                print('Player 1 has won')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('Tie Game')
                    break
                else:
                    turn = 'Player 2'
            
            
        else:
         ###P2 turn
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player2_marker, position)

            if win_check(game_board, player2_marker):
                display_board(game_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    
    
    if not replay():
        break