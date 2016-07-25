############################################
#
#ONLINE URL FOR THIS CODE IS 
# http://www.codeskulptor.org/#user41_vKQuMyMT64K51TS.py
#
#############################################

#Import the simplegui module
import simplegui

#Initialize the variables required
millisec = 0
sec = 0
count = 0
number_of_stops = 0
success = 0
value = '0:00.0'
stop = False

#This will increase the counter every 0.1 seconds
def number():
    global count 
    count = count + 1
    format(count)
    

#This will format the value of the counter count into the format 0:00.0
def format(val):
    global millisec, sec, value
    millisec = val % 10
    num = int(val / 10)
    min = num / 60
    sec = num % 60
    if sec < 10:
        sec_str = '0' + str(sec)
    else: sec_str = sec
    value = str(min) + ':' + str(sec_str) + '.' + str(millisec)

#This function will draw into the canvas
def draw(canvas):
    canvas.draw_text(value, (100, 150), 58, 'white', 'monospace')
    score_value = str(success) + '/' + str(number_of_stops)
    canvas.draw_text(score_value, (220, 30), 38, 'Green', 'monospace')
#Start the timer    
def start():
    global stop
    timer.start()
    stop = True

#Stop the timer and update the score valiables
def stop():
    global number_of_stops, count, success, stop
    if (count % 10 == 0 and stop):
        success = success + 1
    if (stop):
        number_of_stops = number_of_stops + 1
    timer.stop()
    stop = False
#Reset the timer and the score    
def reset():
    global count, success, number_of_stops, value
    timer.stop()
    count = 0
    value = '0:00.0'
    number_of_stops = 0
    success = 0

    
#Create a frame and timer    
frame = simplegui.create_frame('STOP WATCH', 300, 300)
timer = simplegui.create_timer(100, number)

frame.set_draw_handler(draw)

frame.add_button("START", start, 100)
frame.add_button("STOP", stop, 100)
frame.add_button("RESET", reset, 100)

frame.start()
