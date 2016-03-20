# Template for "Guess the Number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# This is Part 1, where the computer chooses a random number from [0,100)
# User makes a series of guesses. Computer says higher or lower until the correct answer.


# 0: Import Necessary Modules
import simplegui
import random

# 1: Initialize Global Variables used in your Code
computer_num = 0
player_guess = 0



# 2: Define Initialization Function

def init():
    pass
    # welcomes user to game and starts a new game
    
# 3: Define Helper Functions
def start_new_game():
    range100()
    pass
    # starts a new game, with computer choosing a new number

# 4: Define Event Handlers for Control Panel
    
def range100():
    global computer_num
    computer_num = random.randrange(100)
    print "Guess a number between 1 and 100"

def input_guess(guess):
    global player_guess
    player_guess = int(guess)
    
    print "player guesses %d" % (player_guess)
    
    check_guess()
    # main game logic goes here	
    
def check_guess():
    global computer_num, player_guess
    
    if computer_num == player_guess:
        print "You Win!"
        start_new_game()
    elif computer_num < player_guess:
        print "Guess lower"
    else: 
        print "Guess higher"

    
# 5: Create Frame
frame = simplegui.create_frame('Testing', 150, 150)

button = frame.add_button('New Game', start_new_game)
input_guess = frame.add_input('What is your guess?', input_guess, 50)

# 6: Register Event Handlers for Control Elements



# 7: Start Frame and Initialize Game
start_new_game()

# always remember to check your completed program against the grading rubric
