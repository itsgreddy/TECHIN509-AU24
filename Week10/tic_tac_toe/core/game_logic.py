from tic_tac_toe.core.board import Board
from tic_tac_toe.core.player import Player

class GameLogic:
    def __init__(self):
        self.board = Board()
        self.players = []

    def add_player(self, name, symbol):
        self.players.append(Player(name, symbol))

    def play_turn(self, player):
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if row in range(3) and col in range(3):
                    if self.board.update(row, col, player.symbol):
                        break
                    else:
                        print("Cell is already occupied. Try again.")
                else:
                    print("Invalid input. Row and column must be between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")

    def play_game(self):
        current_player_index = 0
        while True:
            self.board.display()
            player = self.players[current_player_index]
            self.play_turn(player)

            if self.board.is_winner(player.symbol):
                self.board.display()
                print(f"Congratulations! {player.name} wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break

            current_player_index = 1 - current_player_index
