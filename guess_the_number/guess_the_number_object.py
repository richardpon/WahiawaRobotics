import simplegui
import random

"""Encapsulates the entire Guess the Number game

This example utilizes an object to help store global state
and to help modularize the logic
"""
class Guess_the_number():
    def __init__(self):
        self.computer_number = 0
        
        frame = simplegui.create_frame('Testing', 150, 150)
        button = frame.add_button('New Game', self.start_game)
        input_guess = frame.add_input('What is your guess?', self.handle_guess, 50)
        
    """Starts a new game"""    
    def start_game(self):
        self.computer_number = random.randrange(100)
        print "Guess a number between 1 and 100"
        
    """Handles a user's guess
    
    :param guess: User's guess.
    :type: string: This string should be convertible to an int
    """    
    def handle_guess(self, guess):
        guess = int(guess)
        print "player guesses %d" % (guess)
        self.output_guess(guess, self.computer_number)
        
        if (self.did_win(guess, self.computer_number)):
            self.start_game()
        
    """Outputs the result of the user's guess
    
    This outputs to the console
    
    :param guess: user's guess
    :type int: Should be between 1 and 100
    :param computer_number: The number the computer generated
    :type: computer_number: int
    """
    def output_guess(self, guess, computer_number):
        if computer_number == guess:
            print "You Win!"
        elif computer_number < guess:
            print "Guess Lower"
        else:
            print "Guess Higher"
        
    """Determines if the user won the game
    
    :param guess: user's guess
    :type guess: int
    :param computer_number: The number the computer generated
    :type computer_number: int
    :returns: Whether of not the user won the game by guessing the correct number
    :rtype: bool
    """
    def did_win(self, guess, computer_number):
        return (guess == computer_number)
        
# Create and start a new game        
game = Guess_the_number()
game.start_game()
        