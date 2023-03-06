# Testing template for format function in "Stopwatch - The game"

###################################################
# Student should add code for the format function here

time = 0

def format(time):
    global a, b, c, d
   
    a = str(time // 600)
    b = str ((time//100)%6)
    c = str (time//10)
    d = str (time)

    return a + ":" + b[0] + c[-1] + "." + d[-1]   


###################################################
# Test code for the format function
# Note that function should always return a string with 
# six characters


print format(0) + "- 1"
print format(7) + "- 2"
print format(17) + "- 3"
print format(60) + "- 4"
print format(63) + "- 5"
print format(214) + "- 6"
print format(599) + "- 7"
print format(600) + "- 8"
print format(602) + "- 9"
print format(667) + "- 10"
print format(1325) + "- 11"
print format(4567) + "- 12"
print format(5999) + "- 13"

###################################################
# Output from test

#0:00.0 - 1
#0:00.7 - 2
#0:01.7 - 3
#0:06.0 - 4
#0:06.3 - 5
#0:21.4 - 6
#0:59.9 - 7
#1:00.0 - 8
#1:00.2 - 9
#1:06.7 - 10
#2:12.5 - 11
#7:36.7 - 12
#9:59.9 - 13

