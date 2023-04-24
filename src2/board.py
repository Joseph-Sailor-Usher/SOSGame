from cell import Cell

'''
The board class: 
    1. stores game state as cell enums in one of three states: EMPTY, CROSS, or CIRCLE
    2. provides methods for interacting with the board.
        2.1 __init__: initializes the board
        2.2 __str__: prints the board
        2.3 is_valid_move: checks if a move is valid
        2.4 make_move: places a move on the board
        2.5 get_value: gets the value of a cell
        2.6 is_full: checks if the board is full
        2.7 count_new_soss: counts the number of new sos's made by a move
'''

class Board:
    #constructor
    def __init__(self, size):
        self.board_size = size
        self.board = [[Cell.EMPTY for _ in range(size)] for _ in range(size)]

    #print board
    def __str__(self):
        board_str = []
        for row in self.board:
            row_str = ' '.join([cell.value if cell != Cell.EMPTY else '.' for cell in row]).strip()
            board_str.append(row_str)
        return '\n'.join(board_str)
    
    #check if move is valid
    def is_valid_move(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == Cell.EMPTY
    
    #place move on board
    def make_move(self, row, col, move):
        #print(self.board)
        if self.is_valid_move(row, col) and move in (Cell.S, Cell.O):
            self.board[row][col] = move
            return True
        return False

    #get value of cell
    def get_value(self, row, col):
        return self.board[row][col]

    #check if board is full
    def is_full(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == Cell.EMPTY:
                    return False
        return True
    
    #counts the new sos's made by a move at row, col
    def count_soss(self, row, col, move_type):
        sos_count = 0
        if(move_type == Cell.S):
            if(row < self.board_size - 2):
                if(self.board[row + 1][col] == Cell.O and self.board[row + 2][col] == Cell.S):
                    sos_count += 1
                    print("SOS")
            if(row < self.board_size - 2 and col > 1):
                if(self.board[row + 1][col - 1] == Cell.O and self.board[row + 2][col - 2] == Cell.S):
                    sos_count += 1
                    print("SOS")
            if(col > 1):
                if(self.board[row][col - 1] == Cell.O and self.board[row][col - 2] == Cell.S):
                    sos_count += 1
                    print("SOS")
            if(row > 1 and col > 1):
                if(self.board[row - 1][col - 1] == Cell.O and self.board[row - 2][col - 2] == Cell.S):
                    sos_count += 1
                    print("SOS")
            if(row > 1):
                if(self.board[row - 1][col] == Cell.O and self.board[row - 2][col] == Cell.S):
                    sos_count += 1
                    print("SOS")
            if(row > 1 and col < self.board_size - 2):
                if(self.board[row - 1][col + 1] == Cell.O and self.board[row - 2][col + 2] == Cell.S):
                    sos_count += 1
                    print("SOS")
            if(col < self.board_size - 2):
                if(self.board[row][col + 1] == Cell.O and self.board[row][col + 2] == Cell.S):
                    sos_count += 1
                    print("SOS")
            if(row < self.board_size - 2 and col < self.board_size - 2):
                if(self.board[row + 1][col + 1] == Cell.O and self.board[row + 2][col + 2] == Cell.S):
                    sos_count += 1
                    print("SOS")
        elif(move_type == Cell.O):
            if(row > 0 and col > 0 and row < self.board_size - 1 and col < self.board_size - 1):
                if(self.board[row - 1][col - 1] == Cell.S and self.board[row + 1][col + 1] == Cell.S):
                    sos_count += 1
                    print("SOS")
                if(self.board[row - 1][col + 1] == Cell.S and self.board[row + 1][col - 1] == Cell.S):
                    sos_count += 1
                    print("SOS")
                if(self.board[row - 1][col] == Cell.S and self.board[row + 1][col] == Cell.S):
                    sos_count += 1
                    print("SOS")
                if(self.board[row][col - 1] == Cell.S and self.board[row][col + 1] == Cell.S):
                    sos_count += 1
                    print("SOS")
        return sos_count
    
    #clears the board
    def clear_board(self):
        self.board = [[Cell.EMPTY for _ in range(self.board_size)] for _ in range(self.board_size)]

    #resizes the board
    def resize_board(self, size):
        self.board_size = size
        self.board = [[Cell.EMPTY for _ in range(size)] for _ in range(size)]
