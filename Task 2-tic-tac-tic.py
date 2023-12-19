import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'tie': 0}

    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    empty_cells = get_empty_cells(board)

    if is_maximizing:
        max_eval = float('-inf')
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'O'
            eval = minimax(board, depth + 1, False)
            board[cell[0]][cell[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'X'
            eval = minimax(board, depth + 1, True)
            board[cell[0]][cell[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    best_move = None
    for cell in get_empty_cells(board):
        board[cell[0]][cell[1]] = 'O'
        move_val = minimax(board, 0, False)
        board[cell[0]][cell[1]] = ' '
        if move_val > best_val:
            best_move = cell
            best_val = move_val
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True 

    while True:
        print_board(board)

        if player_turn:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                player_turn = not player_turn
            else:
                print("Cell already occupied. Try again.")
        else:
            print("AI's turn:")
            move = best_move(board)
            board[move[0]][move[1]] = 'O'
            player_turn = not player_turn

        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        elif check_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
