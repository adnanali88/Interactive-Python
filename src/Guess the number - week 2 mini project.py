
import math
import simplegui
import random

num_range = 100 # global for number of guesses

def new_game():
    range100()
                

def range100():
    """Handler for button 1-100 range"""
    
    global secret_number
    global num_range
    num_range = 6
    secret_number = random.randrange(0,100)
    
    
    print ""
    print "New Game. Range is from 0 to 100"
    print "Number of remaining guesses is", (num_range + 1)    
    

def range1000():
    """Handler for button 1-1000 range"""
    
    global secret_number
    secret_number = random.randrange(0,1000)
    global num_range
    num_range = 9
    
    print ""
    print "New Game. Range is from 0 to 1000"
    print "Number of remaining guesses is", (num_range + 1)
   
    
def input_guess(guess):
    """Handler for guess input"""
    
    global num_range
        
    number = int(guess)
    
    print ""
    print "Guess was", number
    
    if number == secret_number:
        print "Correct!"
        new_game()
    
    elif num_range < 1:
        print "You are out of guesses"
        new_game()
      
    elif secret_number > number:
        num_range -= 1
        print "Higher"
        print "Number of remaining guesses is", (num_range + 1)
        
    elif secret_number < number:
        num_range -= 1
        print "Lower"
        print "Number of remaining guesses is", (num_range + 1)
        
    else:
        print "Invalid"
    
    
frame =	simplegui.create_frame ("Guess the Number - Mini project game", 200, 200)

button1 = frame.add_button ("Range is [0, 100)", range100, 200)
button2 = frame.add_button ("Range is [0, 1000)", range1000, 200)
inp = frame.add_input ("Enter a Guess", input_guess, 200)

new_game()

frame.start()
