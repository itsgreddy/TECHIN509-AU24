class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.grid:
            print(" | ".join(row))
            print("-" * 9)

    def update(self, row, col, symbol):
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def is_winner(self, symbol):
        # Check rows
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True
        # Check columns
        for col in range(3):
            if all(self.grid[row][col] == symbol for row in range(3)):
                return True
        # Check diagonals
        if all(self.grid[i][i] == symbol for i in range(3)) or all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell != " " for row in self.grid for cell in row)
