'''
   CS5001
   Spring 2021
   Chiayin Fan
   file to test count_bulls_and_cows and file functions
'''
from count_bulls_and_cows import count_bulls_and_cows, write_msg, read_msg
import unittest
from GameControl import Game
from Marble import Marble

class TestGameControl(unittest.TestCase):
    def test_init(self):
        # check whether the guess, position and the color_choice are as expected
        game = Game([], [-250, 310], ['red', "black", "green", "yellow"])
        self.assertEqual(game.guess, [])
        self.assertEqual(game.position, [-250, 310])
        self.assertEqual(game.color_choice, ['red', "black", "green", "yellow"])

    def test_append(self):
        # Check whether a string could be added to color_choice
        game = Game([], [-250, 310], [])
        game.color_choice.append('blue')
        new_game = game.color_choice
        self.assertEqual(new_game, ['blue'])
        # Check whether an object could be added to guess
        game = Game([], [-250, 310], [])
        marble = Marble([0,0], 'blue')
        game.guess.append(marble)
        self.assertEqual(game.guess, [marble])
    def test_pop(self):
        # Check whether a string could be popped from color_choice
        game = Game([], [-250, 310], ['blue', 'red'])
        game.color_choice.pop()
        new_game = game.color_choice
        self.assertEqual(new_game, ['blue'])
        # Check whether an object could be popped from guess
        game = Game([Marble([0,0], 'blue')], [-250, 310], ['blue'])
        game.guess.pop()
        self.assertEqual(game.guess, [])
    def test_str(self):
        # Test the display of string
        game = Game([Marble([0,0], 'blue')], [-250, 310], ['blue'])
        self.assertEqual(game.__str__(), ['blue'])
    def test_equal(self):
        # Test the equality of guesses
        game_1 = Game([Marble([0,0], 'blue')], [-250, 310], ['blue'])
        game_2 = Game([Marble([0,0], 'blue')], [-99, 260], ['blue'])
        self.assertEqual(game_1, game_2)

        # Test the equality of two different guesses
        game_3 = Game([Marble([0,0], 'blue'), Marble([2,2], 'green')], [-99, 260], ['green'])
        self.assertNotEqual(game_1, game_3)



def main():
    # Test for count_bulls_and_cows()
    # Test case 1, correct positions and colors
    secret_code = ['red', "blue", "green", "yellow"]
    guess_1 = ['red', "blue", "green", "yellow"]
    respond_1 = count_bulls_and_cows(secret_code, guess_1)
    print(respond_1, (0, 4))
    # Test case 2, 2 correct positions and  4 correct colors
    secret_code = ['red', "blue", "green", "yellow"]
    guess_2 = ['red', "blue", "yellow", "green"]
    respond_2 = count_bulls_and_cows(secret_code, guess_2)
    print(respond_2, (2, 2))
    # Test case 3, 2 correct positions and  3 correct colors
    secret_code = ['red', "blue", "green", "yellow"]
    guess_3 = ['red', "blue", "purple", "yellow"]
    respond_3 = count_bulls_and_cows(secret_code, guess_3)
    print(respond_3, (1, 3))

    # Test for write_msg(score, name)
    # Test case 1, write dwon 1 case
    write_msg(3, 'Chia')
    leaderboard = read_msg()
    print(leaderboard, [[3, 'Chia']])
    # Test case 2, write down another case and check the sort function
    write_msg(1, 'Yin')
    leaderboard = read_msg()
    standard_output = [[1, 'Yin'], [3, 'Chia']]
    print(leaderboard, standard_output)
    # Test for GameControl class
    unittest.main(verbosity=3)

main()

