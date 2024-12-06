from tic_tac_toe.core.game_logic import GameLogic

def main():
    print("Welcome to Tic Tac Toe!")
    game = GameLogic()
    game.add_player("Player 1", "X")
    game.add_player("Player 2", "O")
    game.play_game()

if __name__ == "__main__":
    main()
