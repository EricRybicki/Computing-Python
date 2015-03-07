# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

num_range = 100
limit = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0,num_range)
    print ""
    print "New game. Range is from 0 to ", num_range
    print "Number of remaining guesses is ", limit
    # remove this when you add your code    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range, limit
    num_range = 100
    limit = 7
    new_game()
    # remove this when you add your code    
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range, limit
    num_range = 1000
    limit = 10
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global pl_guess, limit
    pl_guess = float(guess)
    if limit == 0:
        print "Out of Guesses."
        if num_range == 100:
            range100()
        else:
            range1000()
    else:        
        limit -= 1
        print ""
        print "Guess was ", guess
        print "Number of remaining guesses is ", limit
        if pl_guess < secret_number:
            print "Higher"
        elif pl_guess > secret_number:
            print "Lower"
        else:
            print "Correct!"
            if num_range == 100:
                range100()
            else:
                range1000()
    

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
