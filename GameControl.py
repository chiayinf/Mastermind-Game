'''
   CS5001
   Spring 2021
   Chiayin Fan
   Class to control the game flow
'''
import random


class Game:
    '''
    Information for game, (guess, position, color_choice)
    '''

    def __init__(self, guess, position, color_choice=[]):
        '''
        Create an onject with some user input information (guess, position, color_choice)
        '''
        self.guess = guess
        self.position = position
        self.color_choice = color_choice

    def __str__(self):
        '''
        Returns a list to show the player's choices
        '''
        return self.color_choice

    def __eq__(self, other):
        '''
        Compares current game instance to another one.
        Returns True if they are equal, False otherwise
        '''
        # If the sequence of color is the same, the guess is the same
        if self.color_choice == other.color_choice:
            return True
        return False


def secret_code():
    '''
    function: secret_code, create a randon secret code
    parameter: None
    return: a secret code list
    '''
    # Colors that could be chosen in the game
    colors = ["red", "blue", "green", "yellow", "purple", "black"]
    secret_code = []
    # Choose 4 different colors
    while len(secret_code) < 4:
        # Randomly pick up a color
        color_code = random.choice(colors)
        # If the color is not chosen, add it to the list
        if color_code not in secret_code:
            secret_code.append(color_code)
    return secret_code
