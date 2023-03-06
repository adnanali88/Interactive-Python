# template for "Stopwatch: The Game"

import simplegui

# define global variables

stop = False
time = 0
tries = 0
wins = 0
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_timer():
    global time, stop
    
    stop = True
    time +=1
    timer.start()
     
def stop_timer():
    global time, tries, wins, stop
    
    if (stop == True):
        tries += 1
        
    else:
        tries = tries
        
        
    if (stop == True) and (time % 10 == 0):
        wins += 1
            
    else:
        wins = wins
        
    
    stop = False
    timer.stop()
        
def reset_timer():
    global time, tries, wins, stop
    
    stop = False
    time = 0
    tries = 0
    wins = 0
    timer.stop()


    
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global time, a, b, c, d
   
    a = str(time // 600)
    b = str((time // 100) % 6)
    c = str(time // 10)
    d = str(time)

    return a, b, c, d
         
# define event handler for timer with 0.1 sec interval

# define draw handler

def draw_handler(canvas):
    global time, a, b, c, d
    format()
    
    canvas.draw_text( a + ":" + b[0] + c[-1] + "." + d[-1], (100, 220), 80, "Red")
    canvas.draw_text ("success/attempts = " + str(wins)+ "/" + str(tries), (120, 50), 30, "Green")

    
# create frame
frame = simplegui.create_frame("Stopwatch", 400,400)
timer = simplegui.create_timer(100, start_timer)

# register event handlers
frame.set_draw_handler(draw_handler)
button1 = frame.add_button("Start", start_timer, 200)
button2 = frame.add_button("Stop", stop_timer, 200)
button3 = frame.add_button("Reset", reset_timer, 200)

# start frame
frame.start()


# Please remember to review the grading rubric
