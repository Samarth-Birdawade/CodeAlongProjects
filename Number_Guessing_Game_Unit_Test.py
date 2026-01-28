import unittest
from unittest.mock import patch
import io
from Number_guessing_game import number_guessing_game

class NumberGuessingGameUnitTest(unittest.TestCase):

    def run_game(self, inputs, random_value = 5):
        with patch('builtins.input', side_effect = inputs), patch('random.randint', return_value = random_value), patch('sys.stdout', new_callable = io.StringIO) as mock_stdout:
            number_guessing_game()
            return mock_stdout.getvalue()

    def test_validate_correct_guess(self):
        output = self.run_game(['5'])
        self.assertIn("Yay! Your guess is correct", output)

    def test_validate_invalid_input_handling(self):
        output = self.run_game(['A', '5'])
        self.assertIn("Please enter a valid number.", output)
        self.assertIn("Yay! Your guess is correct", output)

    def test_validate_failure_message(self):
        output = self.run_game(['1', '2', '3'])
        self.assertIn("0 attempts left.", output)
        self.assertIn("Oops all your guesses are wrong. Please retry your luck!", output)

if __name__ == "__main__":
    unittest.main()