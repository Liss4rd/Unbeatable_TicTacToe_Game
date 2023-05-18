from player import HumanPlayer, GeniusComputerPlayer


class TicTacToe:
    """Class to represent the TicTacToe game."""

    def __init__(self):
        """Initialize the standard TicTacToe board."""
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        """Print the current state of the game board."""
        for row in (self.board[i*3:(i+1)*3] for i in range(3)):
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        """Print the numbering scheme of the game board."""
        # 0 | 1 | 2 (number corresponds with box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        """Get a list of available moves on the game board.

        Returns:
            list[int]: List of available move positions.
        """
        return [i for i, spot in enumerate(self.board) if spot not in ['X', 'O']]

    def empty_squares(self):
        """Check is there are any empty squares remaining on the game board.

        Returns:
            bool: True is there are any empty squares, False otherwise.
        """
        return ' ' in self.board

    def num_empty_squares(self):
        """Count the number of empty squares on the game board.

        Return:
            int: Number of empty squares.
        """
        return self.board.count(' ')

    def make_move(self, square, letter):
        """Make a move on the game board.

        Args:
            square(int): The position on the board to make the move (0-8).
            letter(str): The player's letter ('X' or 'O').

        Returns:
            bool: True if the move was successfully made, False otherwise.
         """

        if self.board[square] not in ['X', 'O']:
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # Winner Func checks if there is 3 in a row
    def winner(self, square, letter):
        """Check if the specified move resulted in a winning condition.

        Args:
            square (int): The position on the board where the move was made.
            letter (str): The player's letter ('X' or 'O').

        Returns:
            bool: True if the move resulted in a win, False otherwise.
        """
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Checks Winner in Column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Checks Winner in Diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


def play(game, x_player, o_player, print_game=True):
    """Play a game of TicTacToe.

    Args:
        game (TicTacToe): The TicTacToe game instance.
        x_player (Player): The player who plays as 'X'.
        o_player (Player): The player who plays as 'O'.
        print_game (bool, optional): Whether to print the game board after each move.
                                     Defaults to True.

        Returns:
            str or None: The winner of the game or None for a tie.
        """
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Define func to make a move
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter

            # Alternate to the other player after a move
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It's a tie!")


def main():
    """The entry point of the TicTacToe game."""
    while True:
        x_player = HumanPlayer('X')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player, print_game=True)

        while True:
            quit_game = input("Play again? [Y/N]: ").upper()
            if quit_game in ['Y', 'N']:
                break
            print("Invalid input. Please enter [Y/N]:")

        if quit_game == 'N':
            print("Thanks for playing! Quitting game...")
            break


if __name__ == '__main__':
    main()
