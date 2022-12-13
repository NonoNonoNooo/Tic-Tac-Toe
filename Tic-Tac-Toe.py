print('*'*10, 'Tic-Tac-Toe', '*'*10)

board = list(range(1, 10))

def draw_board(board):
    print('-'*13)
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answear = input('Where do we put' + player_token + '?')
        try:
            player_answear = int(player_answear)
        except:
            print('Incorrect input are you sure you wrote the number')
            continue
        if player_answear >= 1 and player_answear <= 9:
            if (str(board[player_answear-1]) not in 'XO'):
                board[player_answear-1] = player_token
                valid = True
            else: print('This cell is already occupied')
        else:
            print('Enter a number from 1 to 9')

def chec_win(board):
    win_cord = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for each in win_cord:
        if board[each[0]] == board[each[1]] == each[each[2]]:
            return board[each[0]]
        return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1

        if counter > 4:
            tmp = chec_win(board)
            if tmp:
                print(tmp, 'Your win')
                win = True
                break
            if counter == 9:
                print('Draw')
                break
    draw_board(board)
main(board)