import tkinter as tk
from tkinter import messagebox

EMPTY = 0
HUMAN_PLAYER = 1
AI_PLAYER = -1

def check_game_over(board):
    for player in [HUMAN_PLAYER, AI_PLAYER]:
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] == player:
                return player

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == player:
                return player

        if board[0][0] == board[1][1] == board[2][2] == player:
            return player

        if board[0][2] == board[1][1] == board[2][0] == player:
            return player

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                return None

    return 0

def ai_move(board):
    best_score = -float('inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = AI_PLAYER
                score = minimax(board, 0, False)
                board[row][col] = EMPTY

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move

def minimax(board, depth, is_maximizing):
    result = check_game_over(board)
    if result is not None:
        return result

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = AI_PLAYER
                    score = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN_PLAYER
                    score = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY
                    best_score = min(best_score, score)
        return best_score

def handle_human_move(row, col):
    if board[row][col] == EMPTY:
        buttons[row][col].config(text="X", state=tk.DISABLED)
        board[row][col] = HUMAN_PLAYER

        result = check_game_over(board)
        if result == HUMAN_PLAYER:
            messagebox.showinfo("Game Over", "Congratulations! You win!")
            reset_game()
        elif result == 0:
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            ai_row, ai_col = ai_move(board)
            buttons[ai_row][ai_col].config(text="O", state=tk.DISABLED)
            board[ai_row][ai_col] = AI_PLAYER

            result = check_game_over(board)
            if result == AI_PLAYER:
                messagebox.showinfo("Game Over", "AI wins! You lose.")
                reset_game()
            elif result == 0:
                messagebox.showinfo("Game Over", "It's a tie!")
                reset_game()

def reset_game():
    global board
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL)

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]
board = [[EMPTY for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=('Arial', 20), width=4, height=2,
                                   command=lambda row=i, col=j: handle_human_move(row, col))
        buttons[i][j].grid(row=i, column=j)

reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.grid(row=3, column=1)

root.mainloop()
