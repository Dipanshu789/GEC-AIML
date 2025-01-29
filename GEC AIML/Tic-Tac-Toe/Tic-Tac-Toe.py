import math


PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = '_'


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY or board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[1][1]
    return None


def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 1
    elif winner == PLAYER_O:
        return -1
    elif EMPTY not in [cell for row in board for cell in row]:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score


def find_best_move(board):
    best_move = None
    best_score = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                score = minimax(board, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


board = [
    ['X', 'O', '_'],
    ['_', 'O', '_'],
    ['_', '_', 'X']
]


print("Current Board:")
for row in board:
    print(row)


best_move = find_best_move(board)
print(f"Best move for Player X: {best_move}")
