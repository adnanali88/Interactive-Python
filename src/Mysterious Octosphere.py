# The mystical octosphere is based on the teaching module
# designed by Andrea Crain from Rice University for
# "An Introduction to Interactive Programming in Python (Part 1)
# ". I Thank her for this small example of what python can do
# and a great example of calling a function within a function.


import random # random number generator module

def number_to_fortune(number):
    
    """ Helper function that sends back a string for the 
    randomrange() generator"""
    
       
    if number == 0:
        return "Yes, for sure!"
    elif number == 1:
        return "Probably yes."
    elif number == 2:
        return "Seems like yes..."
    elif number == 3:
        return "Definitely not!"
    elif number == 4:
        return "Probably not."
    elif number == 5:
        return "I really doubt it..."
    elif number == 6:
        return "Not sure, check back later!"
    elif number == 7:
        return "I really can't tell"
    else :
        return "Invalid Input"
    
    
def mystical_octosphere(question):
    
    """Main function, adds abit of depth to the question
    and returns a string as an answer"""
    
    print "Your question was... " + question
    print "You shake the mystical octosphere"
    
    answer_fortune = random.randrange (0, 8)
    
    print "The cloudy liquid swirls, and a reply comes into view.."
    
    print "The mystical octosphere says..." + number_to_fortune(answer_fortune)
    print 
    
    
    
mystical_octosphere("Type question within the commas") 

# Remove the example and ask the mystical octosphere 
# the myteries of your heart!
# Press the play button the top left to get an answer