"""
Tic Tac Toe Board:
Q Q Q
Q Q Q
Q Q Q
"""


def validate_win(bo: list) -> bool:
    for i in range(3):
        if ''.join(bo[i]) == 'xxx' or ''.join(bo[i]) == 'ooo':
            return True
    for i in range(3):
        l = ''.join([bo[i][0] + bo[i][1] + bo[i][2]])
        if l == 'xxx' or l == 'ooo':
            return True
    if ''.join([bo[0][0], bo[1][1], bo[2][2]]) == 'xxx' or ''.join([bo[0][0], bo[1][1], bo[2][2]]) == 'ooo':
        return True
    if ''.join([bo[0][2], bo[1][1], bo[2][0]]) == 'xxx' or ''.join([bo[0][2], bo[1][1], bo[2][0]]) == 'ooo':
        return True

def valid_play(y, x):
    if board[y][x] != ' ':
        return False
    return True


def player1_play():
    inp = input('Enter a location to play [n], [n] (p1): ')
    inp_list = inp.split(',')
    inp_list = list(map(int, inp_list))

    if valid_play(inp_list[0], inp_list[1]):
        board[inp_list[0]][inp_list[1]] = 'x'
    else:
        print('Invalid Play')
        player1_play()

    if validate_win(board):
        print('Congrats you (player1) won!')
        return None

    print(*board, sep='\n')
    print('================================================================')
    player2_play()


def player2_play():
    """
    Player2 play function called by when the player1 play function is over
    """
    inp = input('Enter a location to play [n], [n] (p2): ')
    inp_list = inp.split(',')
    inp_list = list(map(int, inp_list))

    if valid_play(inp_list[0], inp_list[1]):
        board[inp_list[0]][inp_list[1]] = 'o'
    else:
        print('Invalid Play')
        player1_play()

    if validate_win(board):
        print('Congrats you (player1) won!')
        return None

    print(*board, sep='\n')
    print('================================================================')
    player1_play()


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

if __name__ == '__main__':
    game = True
    player1_play()
    print(*board, sep='\n')