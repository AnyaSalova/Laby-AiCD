import tkinter as tk
import random

WIDTH = 300
HEIGHT = 400  # Увеличиваем высоту для отображения текста
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.canvas = tk.Canvas(self.frame, width=WIDTH, height=WIDTH, bg="lightblue", highlightthickness=0)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)

        self.status_label = tk.Label(self.frame, text="Ход игрока: X", font=('Helvetica', 14), bg="lightblue",
                                     fg="darkblue")
        self.status_label.pack(pady=10)

        self.reset_button = tk.Button(self.frame, text="Сбросить игру", font=('Helvetica', 12), command=self.reset_game)
        self.reset_button.pack(pady=10)

        self.board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.player = 'X'
        self.game_over = False

        self.draw_grid()
        self.update_status()

    def draw_grid(self):
        for i in range(1, BOARD_ROWS):
            self.canvas.create_line(0, i * SQUARE_SIZE, WIDTH, i * SQUARE_SIZE, width=2, fill="white")
        for j in range(1, BOARD_COLS):
            self.canvas.create_line(j * SQUARE_SIZE, 0, j * SQUARE_SIZE, BOARD_ROWS * SQUARE_SIZE, width=2,
                                    fill="white")

    def draw_board(self):
        self.canvas.delete("symbol")
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                x0 = col * SQUARE_SIZE
                y0 = row * SQUARE_SIZE
                x1 = (col + 1) * SQUARE_SIZE
                y1 = (row + 1) * SQUARE_SIZE
                if self.board[row][col] == 'X':
                    self.canvas.create_line(x0 + 10, y0 + 10, x1 - 10, y1 - 10, width=4, tags="symbol", fill="red")
                    self.canvas.create_line(x1 - 10, y0 + 10, x0 + 10, y1 - 10, width=4, tags="symbol", fill="red")
                elif self.board[row][col] == 'O':
                    self.canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, width=4, tags="symbol", outline="green")

    def check_winner(self, player):
        for row in self.board:
            if all(symbol == player for symbol in row):
                return True
        for col in range(BOARD_COLS):
            if all(self.board[row][col] == player for row in range(BOARD_ROWS)):
                return True
        if all(self.board[i][i] == player for i in range(BOARD_ROWS)) or \
                all(self.board[i][BOARD_COLS - 1 - i] == player for i in range(BOARD_ROWS)):
            return True
        return False

    def bot_move(self, bot_player, human_player):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == '':
                    self.board[row][col] = bot_player
                    if self.check_winner(bot_player):
                        return row, col
                    self.board[row][col] = ''
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == '':
                    self.board[row][col] = human_player
                    if self.check_winner(human_player):
                        self.board[row][col] = bot_player
                        return row, col
                    self.board[row][col] = ''
        empty_cells = [(row, col) for row in range(BOARD_ROWS) for col in range(BOARD_COLS) if
                       self.board[row][col] == '']
        return random.choice(empty_cells)

    def on_click(self, event):
        if self.game_over:
            return

        col = event.x // SQUARE_SIZE
        row = event.y // SQUARE_SIZE

        if self.board[row][col] == '':
            self.board[row][col] = self.player
            if self.check_winner(self.player):
                self.game_over = True
                self.update_status(f"Игрок {self.player} выиграл!")
            elif all(symbol != '' for row in self.board for symbol in row):
                self.game_over = True
                self.update_status("Ничья!")
            else:
                self.player = 'O' if self.player == 'X' else 'X'
                if self.player == 'O':
                    row, col = self.bot_move('O', 'X')
                    self.board[row][col] = self.player
                    if self.check_winner(self.player):
                        self.game_over = True
                        self.update_status("Игрок O выиграл!")
                    elif all(symbol != '' for row in self.board for symbol in row):
                        self.game_over = True
                        self.update_status("Ничья!")
                    else:
                        self.player = 'X'
        self.draw_board()
        if not self.game_over:
            self.update_status(f"Ход игрока: {self.player}")

    def update_status(self, text=None):
        if text is None:
            text = f"Ход игрока: {self.player}"
        self.status_label.config(text=text)

    def reset_game(self):
        self.board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.player = 'X'
        self.game_over = False
        self.draw_board()
        self.update_status()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
