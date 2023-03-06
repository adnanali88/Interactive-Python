# calculator with all buttons


import simplegui

# intialize globals
store = 0
operand = 0


# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()
    
def reset():
    """ Reset operand and store to 0"""
    global store, operand
    store = 0
    operand = 0
    output()

def enter(t): # where t is a string, so it wont compute numbers.
    """ enter a new operand"""
    global operand
    operand = float(t) #you can change it to int(t) to remove 0.0
    output()
    
# create frame
f = simplegui.create_frame("Calculator",300,300)

# register event handlers and create control elements
f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)
f.add_button("Add", add, 100)
f.add_button("Sub", sub, 100)
f.add_button("Mult", mult, 100)
f.add_button("Div", div, 100)
f.add_button("Reset", reset, 100)
f.add_input("Enter", enter, 100)


# get frame rolling
f.start()