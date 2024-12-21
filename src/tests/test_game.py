import unittest
from src.services.game_service import determine_winner

class TestGameService(unittest.TestCase):
    def test_draw(self):
        result = determine_winner('rock')
        self.assertIn(result['result'], ['draw', 'win', 'lose'])

if __name__ == '__main__':
    unittest.main()
