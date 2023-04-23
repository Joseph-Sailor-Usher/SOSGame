class Board:
    def __init__(self, size):
        self.size = size
        self.board = [['' for _ in range(size)] for _ in range(size)]

    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ''
    
    def place_move(self, row, col, move):
        if self.is_valid_move(row, col) and move in ('S', 'O'):
            self.board[row][col] = move
            return True
        return False


    def __str__(self):
        board_str = []
        for row in self.board:
            row_str = ' '.join([cell if cell != '' else '.' for cell in row]).strip()
            board_str.append(row_str)
        return '\n'.join(board_str)
    
    def set_value(self, row, col, value):
        self.board[row][col] = value

    def get_value(self, row, col):
        return self.board[row][col]

    def is_full(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == '':
                    return False
        return True

    def get_empty_cells(self):
        empty_cells = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == '':
                    empty_cells.append((row, col))
        return empty_cells