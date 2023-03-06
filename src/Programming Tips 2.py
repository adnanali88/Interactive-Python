##############
# Example of missing "global"

n1 = 0

def increment():
    global n1 # added to the function since
              # the function would not work if we dont
              # tell python that we are using GLOBAL n1.
              # It will create a local n1 and keep it as 
              # a local variable
    n1 = n1 + 1

increment()
increment()
increment()

print n1


##############
# Example of missing "global"

n2 = 0

def assign(x):
        global n2 # added to the function since
              # the function would not work if we dont
              # tell python that we are using GLOBAL n1.
              # It will create a local n2 and keep it as 
              # a local variable
        n2 = x

assign(2)
assign(15)
assign(7)

print n2


##############
# Example of missing "return"

n3 = 0

def decrement():
    global n3
    n3 = n3 - 1
    return n3   # Make sure to return your statements

x = decrement()

print "x = ", x  # This will return as None if return statement is missing
print "n = ", n3


##############
# Example of print debugging

#To debug or better understand what a code is doing
#It is better to always add print statements after EVERY
#line of a function or return value, so we know exactly
#at what stage, which function is being called and what
#it is doing. This will help in the long run when we have 
#100s of lines of codes and make sure you label each print out
#like f=n,x etc etc.

import simplegui

x = 0

def f(n):
    print "f: n,x = ", n, x
    result = n ** x
    print "f2: result = ",result
    return result
    
def button_handler():
    global x
    print "bh : x = ", x
    x += 1
    print "bh2 : x = ", x

def input_handler(text):
    print "ih : text = ", text
    print f(float(text))
    
frame = simplegui.create_frame("Example", 200, 200)
frame.add_button("Increment", button_handler)
frame.add_input("Number:", input_handler, 100)

frame.start()


##############
# Examples of simplifying conditionals

def f1(a, b):
    """Returns True exactly when a is False and b is True."""  
    if a == False and b == True:
        return True
    else:
        return False

def f2(a, b):
    """Returns True exactly when a is False and b is True."""  
    if not a and b:
        return True
    else:
        return False    

def f3(a, b):
    """Returns True exactly when a is False and b is True."""  
    return not a and b

def g1(a, b):
    """Returns False eactly when a and b are both True."""  
    if a == True and b == True:
        return False
    else:
        return True
    
def g2(a, b):
    """Returns False eactly when a and b are both True."""  
    if a and b:
        return False
    else:
        return True

def g3(a, b):
    """Returns False eactly when a and b are both True."""  
    return not (a and b)
