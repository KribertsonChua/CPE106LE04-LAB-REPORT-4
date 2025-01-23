import os, random
import oxo_data
 
class Game:
    @classmethod
    def newGame(cls):
        """Create a new game with an empty 3x3 board."""
        return [[" " for _ in range(3)] for _ in range(3)]
 
    @classmethod
    def saveGame(cls, game):
        """Save the current game state."""
        oxo_data.saveGame(game)
    @classmethod
    def restoreGame(cls):
        """Restore the game state from a saved file."""
        try:
            game = oxo_data.restoreGame()
            if len(game) == 3 and all(len(row) == 3 for row in game):
                return game
            else: 
                return cls.newGame()
        except IOError:
            return cls.newGame()
    @staticmethod
    def _generateMove(game):
        """Generate a random move for the computer."""
        options = [(i, j) for i in range(3) for j in range(3) if game[i][j] == " "]
        if options:
            return random.choice(options)
        else: 
            return -1, -1
    @staticmethod
    def _isWinningMove(game):
        """Check if the current move is a winning move."""
        wins = [
            [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)],  # rows
            [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)],  # columns
            [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]  # diagonals
        ]
 
        for line in wins:
            chars = [game[i][j] for i, j in line]
            if chars == ['X', 'X', 'X'] or chars == ['O', 'O', 'O']:
                return True
        return False
 
    @staticmethod
    def _isDraw(game):
        """Check if the game is a draw."""
        return all(cell != " " for row in game for cell in row)
 
    def userMove(self, game, cell):
        """Make a move for the user."""
        i, j = cell
        if game[i][j] != ' ':
            raise ValueError('Invalid cell')
        else:
            game[i][j] = 'X'
        if self._isWinningMove(game):
            return 'X'
        elif self._isDraw(game):
            return 'D'
        else:
            return ""
 
    def computerMove(self, game):
        """Make a move for the computer."""
        i, j = self._generateMove(game)
        if (i, j) == (-1, -1):
            return 'D'
        game[i][j] = 'O'
        if self._isWinningMove(game):
            return 'O'
        elif self._isDraw(game):
            return 'D'
        else:
            return ""
 
    def test(self):
        """Test the game by playing a full game."""
        result = ""
        game = self.newGame()
        while not result:
            for row in game:
                print(row)
            try:
                result = self.userMove(game, self._generateMove(game))
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computerMove(game)
            if result == 'D':
                print("It's a draw")
                break
            elif result:
                print("Winner is:", result)
                for row in game:
                    print(row)
                break
            print("-" * 10)  # Add this line to separate the game moves
 
if __name__ == "__main__":
    game = Game()
    game.test()
