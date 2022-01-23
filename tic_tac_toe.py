def create_board():
    board=[]
    for i in range(3):
        row=[]
        for j in range(3):
            row.append('-')
        board.append(row)
    display_board(board)
    return board

def update_board(board,x,y, player):
    board[x-1][y-1]=player
    display_board(board)


def display_board(board):
    for row in board:
        for item in row:
            print(item, end=" ")
        print()

def row_win(board,player):
    for i in range(3):
        win = True
        for j in range(3):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win

def col_win(board,player):
    for i in range(3):
        win = True
        for j in range(3):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

def check_win(board,player):
    win=False
    if (row_win(board, player) or
    col_win(board,player)):
        win=True

    return win

def play(board,player):
    print("Enter pos for "+player)
    a=int(input())
    b=int(input())
    update_board(board,a,b,player)

def board_filled(board):
    for row in board:
        for i in row:
            if i == '-':
                return False
    return True

def continue_game(cur_board):
    while(1):
        play(cur_board,'X')
        if board_filled(cur_board):
            print("Match Draw!")
            break
        if(check_win(cur_board,'X')):
            print("player 2 wins")
            break
        else:
            play(cur_board,'O')
            if board_filled(cur_board):
                print("Match Draw!")
                break
            if(check_win(cur_board,'O')):
                print("player 1 wins")
                break

def play_first_move(board, player):
    while(1):
        print("Enter pos for "+player)
        a=int(input())
        b=int(input())
        if (a-b==0 or a-b==2 or a-b==-2):
            update_board(board,a,b,player)
            break
        else:
            print("\nInvalid move. First move only on diagonal.Try again")

    return board

def start_game():
    print("Player 1 -O, Player 2-X")
    cur_board=create_board()
    cur_board=play_first_move(cur_board,'O')
    continue_game(cur_board)


start_game()