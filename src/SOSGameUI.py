import tkinter as tk
from board import Board
from game import Game

class SOSGameUI(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("SOS Game")
        self.game = game
        self.frame = tk.Frame(self)
        self.create_widgets()
        self.frame.pack(fill=tk.BOTH, expand=True)

    def create_widgets(self):
        self.frame.destroy()
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.game_type_var = tk.StringVar(value=self.game.game_type)

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.create_board_buttons()
        self.create_status_label()
        self.create_game_type_widgets()
        self.create_board_size_entry()
        self.update_window_size()


    def create_status_label(self):
        self.status_label = tk.Label(self.frame, text="Player 1's Turn")
        self.status_label.grid(row=self.game.board.size, column=0, columnspan=self.game.board.size)

    def create_game_type_widgets(self):
        self.game_type_label = tk.Label(self.frame, text="Game Type:")
        self.game_type_label.grid(row=self.game.board.size + 2, column=0, sticky=tk.W)
        self.game_type_var = tk.StringVar()
        self.game_type_var.set(self.game.game_type)
        simple_game_type_radiobutton = tk.Radiobutton(self.frame, text="Simple", variable=self.game_type_var,
                                                      value="simple", command=lambda: self.game.set_game_type("simple"))
        simple_game_type_radiobutton.grid(row=self.game.board.size + 2, column=1, padx=5, pady=5, sticky=tk.W)
        general_game_type_radiobutton = tk.Radiobutton(self.frame, text="General", variable=self.game_type_var,
                                                      value="general", command=lambda: self.game.set_game_type("general"))
        general_game_type_radiobutton.grid(row=self.game.board.size + 2, column=2, padx=5, pady=5, sticky=tk.W)

    def create_board_size_entry(self):
        self.board_size_label = tk.Label(self.frame, text="Board Size:")
        self.board_size_label.grid(row=self.game.board.size + 1, column=0, sticky=tk.W)
        self.board_size_entry = tk.Entry(self.frame, width=4)
        self.board_size_entry.grid(row=self.game.board.size + 1, column=1)
        self.board_size_entry.insert(0, str(self.game.board.size))

        self.board_size_button = tk.Button(self.frame, text="Play", command=self.update_board_size)
        self.board_size_button.grid(row=self.game.board.size + 1, column=2, padx=5, pady=5, sticky=tk.W)

    def create_board_buttons(self):
        for row in range(self.game.board.size):
            for col in range(self.game.board.size):
                button = tk.Button(self.frame, text=" ", width=6, height=3,
                                command=lambda r=row, c=col: self.button_click(r, c))
                button.grid(row=row, column=col)
        self.status_label = tk.Label(self.frame, text="Player 1's Turn")
        self.status_label.grid(row=self.game.board.size, column=0, columnspan=self.game.board.size)

    def button_click(self, row, col):
        current_player = self.game.get_current_player()
        if self.game.make_move(row, col):
            button = self.frame.grid_slaves(row=row, column=col)[0]
            button.config(text=current_player.letter)
            print(f"Active player's letter: {self.game.get_current_player().letter}")

    def update_window_size(self):
        padding = 50
        width = self.game.board.size * 50 + padding
        height = self.game.board.size * 50 + padding + 100
        self.frame.config(width=width, height=height)

    def update_board_size(self):
        try:
            new_size = int(self.board_size_entry.get())
            if 3 <= new_size <= 10:
                self.game.board = Board(new_size)
                self.create_widgets()

            else:
                print("Board size must be between 3 and 10.")
        except ValueError:
            print("Invalid board size. Please enter a number between 3 and 10.")
