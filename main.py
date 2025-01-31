import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    
    def test_game_initialization(self):
        game = TicTacToe()
        for i in range(3):
            for j in range(3):
                self.assertEqual(game.board[i][j], ' ')  
        self.assertEqual(game.get_current_player(), 'X')  
    
    def test_play_move(self):
        game = TicTacToe()
        game.play_move(0, 0)
        self.assertEqual(game.board[0][0], 'X')  
        
        game.play_move(0, 1)
        self.assertEqual(game.board[0][1], 'O')  
        
        game.play_move(1, 1)
        self.assertEqual(game.board[1][1], 'X')  

if __name__ == "__main__":
    unittest.main()

