import random
import math


class Player:
    """
    Represents a player in the TicTacToe game.
    """
    def __init__(self, letter):
        """
        Initialize a player with the specified letter (X or O).

        Args:
            letter (str): The player's letter (X or O).
        """
        self.letter = letter

    def get_move(self, game) -> int:
        """
        Get the player's next move.

        Args:
            game (TicTacToe): The TicTacToe game instance.

        Returns:
            int: The chosen move (square number).
        """


class RandomComputerPlayer(Player):
    """
    Represents a player that makes random moves in the TicTacToe game.
    """

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game) -> int:
        """
        Get the player's next move by choosing a random available square.

        Args:
            game (TicTacToe): The TicTacToe game instance.

        Returns:
            int: The randomly chosen move (square number).
        """
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    """
    Represents a human player in the TicTacToe game.
    """
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game) -> int:
        """
        Get the player's next move by accepting user input.

        Args:
            game (TicTacToe): The TicTacToe game instance.

        Returns:
            int: The chosen move (square number).

        Raises:
            ValueError: If an invalid move is entered.
        """
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input next move (0-8): ')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square! Try again!')

        return val


class GeniusComputerPlayer(Player):
    """
    Represents a genius computer player in the TicTacToe game.
    """

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game) -> int:
        """
        Get the player's next move using the minimax algorithm.

        Args:
             game (TicTacToe): The TicTacToe game instance.

        Returns:
            int: The chosen move (square number).
        """
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        """
        Perform the minimax algorithm to determine the best move.

        Args:
             state (TicTacToe): The TicTacToe game state.
             player(str): The current player's letter.

        Returns:
            dict: The best move position and score.
        """
        # State variable: is like a screenshot of the current game
        max_player = self.letter  # human player
        other_player = 'O' if player == 'X' else 'X'  # labels the other player/genius

        # check to see if previous move made someone a winner
        # this is the base case
        if state.current_winner == other_player:
            # we should return position AND score because we need to keep track of score
            # for minimax to work
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player
                    else -1 * (state.num_empty_squares() + 1)
                    }

        elif not state.empty_squares():  # no empty squares
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize

        for possible_move in state.available_moves():
            # Steps for possible moves algorithm:
            # 1. Try a new spot
            state.make_move(possible_move, player)

            # 2. Recurse using minimax to simulate a game after that move is made
            sim_score = self.minimax(state, other_player)

            # 3. Undo the tested move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this is the start of the possibilities

            # 4. Update the dictionary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score  # replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score  # replace best

        return best
