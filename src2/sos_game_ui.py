import tkinter as tk
from cell import Cell
from game import Game

'''
class SOSGameUI:
    1. Creates the UI for the game
    2. Adds listeners to the buttons
        2.1 __init__: initializes the UI
        2.2 create_widgets: creates the widgets for the UI
'''

class SOSGameUI(tk.Tk):
    #SOSGameUI(game, change_gametype, change_player_type, start_game, make_move, end_game)
    def __init__(self, game):
        super().__init__()
        self.game = game
        #setup and construct the GUI
        self.title("SOS Game")
        self.frame = tk.Frame(self)
        self.create_pregame_widgets()
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.S_radiobutton = None
        self.O_radiobutton = None
        self.buttons = {}
    
    def __str__(self) -> str:
        return "SOSGameUI"

    def create_pregame_widgets(self):
        self.frame.destroy()
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.game_type_var = tk.StringVar(value=self.game.__str__())

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.create_game_type_widgets()
        self.create_board_size_entry()
        self.create_play_button()
        self.update_window_size()
        self.create_red_player_type_widgets()
        self.create_blue_player_type_widgets()
    
    def create_in_game_widgets(self):
        self.frame.destroy()
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.game_type_var = tk.StringVar(value=self.game.__str__())

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.create_board_buttons()
        self.create_status_label()
        self.update_window_size()
        self.create_change_player_move_type_widgets()

    def create_post_game_widgets(self):
        self.frame.destroy()
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.game_type_var = tk.StringVar(value=self.game.__str__())

        for widget in self.frame.winfo_children():
            widget.destroy()
        
        self.create_continue_button()
        self.create_winner_label()

    def create_status_label(self):
        self.status_label = tk.Label(self.frame, text="Red Player's turn")
        self.status_label.grid(row=self.game.board.board_size + 2, column=0, columnspan=self.game.board.board_size, sticky="nsew")

    def create_winner_label(self):
        message = "Tied game."
        if self.game.winner != None:
            if(self.game.winner == self.game.players[0]):
                message = "Red player wins!"
            elif(self.game.winner == self.game.players[1]):
                message = "Blue player wins!"
        else:
            message = "Tied game."
        self.winner_label = tk.Label(self.frame, text=message)
        self.winner_label.grid(row=self.game.board.board_size + 2, column=0, columnspan=self.game.board.board_size, sticky="nsew")

    def create_game_type_widgets(self):
        self.game_type_label = tk.Label(self.frame, text="Game Type:")
        self.game_type_label.grid(row=self.game.board.board_size + 2, column=0, sticky=tk.W)
        self.game_type_var = tk.StringVar()
        self.game_type_var.set(self.game.gametype.__str__())
        simple_game_type_radiobutton = tk.Radiobutton(self.frame, text="Simple", variable=self.game_type_var,
                                                      value="Simple", command=lambda: self.game.change_gametype(self.game, "Simple"))
        simple_game_type_radiobutton.grid(row=self.game.board.board_size + 2, column=1, padx=5, pady=5, sticky=tk.W)
        general_game_type_radiobutton = tk.Radiobutton(self.frame, text="General", variable=self.game_type_var,
                                                      value="General", command=lambda: self.game.change_gametype(self.game, "General"))
        if(self.game.gametype.__str__() == "General"):
            general_game_type_radiobutton.select()
        elif(self.game.gametype.__str__() == "Simple"):
            simple_game_type_radiobutton.select()
        else:
            print(self.game.gametype.__str__())
        general_game_type_radiobutton.grid(row=self.game.board.board_size + 2, column=2, padx=5, pady=5, sticky=tk.W)

    def create_red_player_type_widgets(self):
        self.red_player_type_label = tk.Label(self.frame, text="Red Player Type: ")
        self.red_player_type_label.grid(row=self.game.board.board_size + 3, column=0, sticky=tk.W)
        self.red_player_type_var = tk.StringVar()
        self.red_player_type_var.set(self.game.players[0].__str__())
        
        human_player_type_radiobutton = tk.Radiobutton(self.frame, text="Human", variable=self.red_player_type_var,
                                                      value="Human", command=lambda: self.game.change_player_type(0, "Human"))
        human_player_type_radiobutton.grid(row=self.game.board.board_size + 3, column=1, padx=5, pady=5, sticky=tk.W)
        ai_player_type_radiobutton = tk.Radiobutton(self.frame, text="AI", variable=self.red_player_type_var,
                                                      value="AI", command=lambda: self.game.change_player_type(0, "AI"))
        ai_player_type_radiobutton.grid(row=self.game.board.board_size + 3, column=2, padx=5, pady=5, sticky=tk.W)
        
        if(self.game.players[0].__str__() == "Human"):
            human_player_type_radiobutton.select()
        elif(self.game.players[0].__str__() == "AI"):
            ai_player_type_radiobutton.select()
        else:
            print(self.game.players[0].__str__())
        self.game.players[0].sos_game_ui = self
        self.game.players[1].sos_game_ui = self


    def create_blue_player_type_widgets(self):
        self.blue_player_type_label = tk.Label(self.frame, text="Blue Player Type: ")
        self.blue_player_type_label.grid(row=self.game.board.board_size + 3, column=3, sticky=tk.W)
        self.blue_player_type_var = tk.StringVar()
        self.blue_player_type_var.set(self.game.players[1].__str__())
        
        blue_human_player_type_radiobutton = tk.Radiobutton(self.frame, text="Human", variable=self.blue_player_type_var,
                                                      value="Human", command=lambda: self.game.change_player_type(1, "Human"))
        blue_human_player_type_radiobutton.grid(row=self.game.board.board_size + 3, column=4, padx=5, pady=5, sticky=tk.W)
        blue_ai_player_type_radiobutton = tk.Radiobutton(self.frame, text="AI", variable=self.blue_player_type_var,
                                                      value="AI", command=lambda: self.game.change_player_type(1, "AI"))
        blue_ai_player_type_radiobutton.grid(row=self.game.board.board_size + 3, column=5, padx=5, pady=5, sticky=tk.W)
        
        if(self.game.players[1].__str__() == "Human"):
            blue_human_player_type_radiobutton.select()
        elif(self.game.players[0].__str__() == "AI"):
            blue_ai_player_type_radiobutton.select()
        else:
            print(self.game.players[0].__str__())

        self.game.players[0].sos_game_ui = self
        self.game.players[1].sos_game_ui = self

    def create_change_player_move_type_widgets(self):
        self.move_type_label = tk.Label(self.frame, text="Move type: ")
        self.move_type_label.grid(row=self.game.board.board_size + 3, column=0, sticky=tk.W)
        self.move_type_var = tk.StringVar()
        self.move_type_var.set(self.game.players[0].get_cell_type())
        
        #change_player_move_type(self, player, move_type):
        self.S_radiobutton = tk.Radiobutton(self.frame, text="S", variable=self.move_type_var,
                                                      value=Cell.S, command=lambda: self.game.change_player_move_type(self.game.current_player, Cell.S))
        self.S_radiobutton.grid(row=self.game.board.board_size + 3, column=1, padx=5, pady=5, sticky=tk.W)
        self.O_radiobutton = tk.Radiobutton(self.frame, text="O", variable=self.move_type_var,
                                                      value=Cell.O, command=lambda: self.game.change_player_move_type(self.game.current_player, Cell.O))
        self.O_radiobutton.grid(row=self.game.board.board_size + 3, column=2, padx=5, pady=5, sticky=tk.W)

        if(self.game.players[self.game.current_player_index].get_cell_type() == Cell.S):
            self.S_radiobutton.select()
        elif(self.game.players[self.game.current_player_index].get_cell_type() == Cell.O):
            self.O_radiobutton.select()
        else:
            print(self.game.players[0].__str__())

    def create_board_size_entry(self):
        self.board_size_label = tk.Label(self.frame, text="Board Size:")
        self.board_size_label.grid(row=self.game.board.board_size + 1, column=0, sticky=tk.W)
        self.board_size_entry = tk.Entry(self.frame, width=4)
        #update the text on the entry box to the current board size
        self.board_size_entry.default_text = str(self.game.board.board_size)
        self.board_size_entry.grid(row=self.game.board.board_size + 1, column=1)
        self.board_size_entry.insert(0, str(self.game.board.board_size))

        self.board_size_entry.bind("<KeyRelease>", self.on_board_size_change)

    def on_board_size_change(self, event):
        # Retrieve the new value of the entry widget
        new_board_size = event.widget.get()
        print("New board size:", new_board_size)
        self.resize_board()

    def create_play_button(self):
        self.board_size_button = tk.Button(self.frame, text="Play", command=self.start_new_game)
        self.board_size_button.grid(row=self.game.board.board_size + 1, column=2, padx=5, pady=5, sticky=tk.W)

    def create_continue_button(self):
        self.board_size_button = tk.Button(self.frame, text="Continue", command=self.create_pregame_widgets)
        self.board_size_button.grid(row=self.game.board.board_size + 1, column=2, padx=5, pady=5, sticky=tk.W)

    def create_board_buttons(self):
        new_name = ""
        for row in range(self.game.board.board_size):
            for col in range(self.game.board.board_size):
                new_name = str(row) + str(col)
                new_name = str(row) + str(col)
                button = tk.Button(self.frame, text=self.game.board.board[row][col].__str__(), 
                                   width=6, height=3, command=lambda r=row, c=col: self.button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[new_name] = button
                print(button.config('text')[-1])

    def button_click(self, row, col):
        if(self.game.accepting_input == False): return
        tempHolder = self.game.players[self.game.current_player_index].letter.__str__()
        #call make move on the game object
        if self.game.board.make_move(row, col, self.game.players[self.game.current_player_index].get_cell_type()):
            button = self.frame.grid_slaves(row=row, column=col)[0]
            button.config(text=tempHolder)
            if(self.game.current_player_index == 0):
                self.status_label.config(text="Red player's turn")
            elif(self.game.current_player_index == 1):
                self.status_label.config(text="Blue player's turn")
        else:
            print("Invalid move.")
        #update the move type indicator relative to players
        if(self.game.players[self.game.current_player_index].get_cell_type() == Cell.S):
            self.S_radiobutton.select()
        elif(self.game.players[self.game.current_player_index].get_cell_type() == Cell.O):
            self.O_radiobutton.select()
        else:
            print(self.game.players[0].__str__())

        if self.game.game_over == True:
            self.create_post_game_widgets()
        self.game.accepting_input = False

    def update_window_size(self):
        padding = 50
        width = self.game.board.board_size * 50 + padding
        height = self.game.board.board_size * 50 + padding + 100
        self.frame.config(width=width, height=height)

    def resize_board(self):
        if(self.game.game_over == False):
            return
        try:
            new_size = int(self.board_size_entry.get())
            if 3 <= new_size <= 10:
                self.game.board.update_board_size(new_size)
                self.create_pregame_widgets()
            else:
                print("Board size must be between 3 and 10.")
        except ValueError:
            print("Invalid board size. Please enter a number between 3 and 10.")

    def start_new_game(self):
        temp_game = Game(self.game.board.board_size, self.game.gametype, self.game.players[0], self.game.players[1])
        self.game = temp_game
        self.game.players[0].sos_game_ui = self
        self.game.players[1].sos_game_ui = self
        self.game.start_game()
        self.resize_board()
        self.create_in_game_widgets()
        self.game.players[0].make_next_move(self.game)
    
    def rename_board_buttons(self, row, col, cell_type):
        if(self.buttons.__len__() == 0 or self.game.game_over == True):
            return
        if(self.buttons.__len__() == 0):
            self.create_board_buttons()
        button = self.buttons[str(row) + str(col)]
        if(cell_type == Cell.S):
            button.config(text="S")
        elif(cell_type == Cell.O):
            button.config(text="O")
