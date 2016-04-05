# Template for "Stopwatch: The Game"
import simplegui

# Define Global Variables

# Tracks the global time in tenths of a second
tenths = 0
seconds = 0
ten_seconds = 0
minutes = 0

# Flag to determine if the clock is running
is_running = False

# Define Helper Function 
''' formatted_time(t) converts the time into formatted string A:BC.D

This is the most complex function in this solution. The approach is to calculate
the largest units first (minutes), and then work down to smaller units one by one
'''
def formatted_time():
	global tenths, seconds, ten_seconds, minutes

	return str(minutes) + ":" + str(ten_seconds) + str(seconds) + "." + str(tenths)

# Define Event Handlers for buttons; "Start", "Stop", "Reset"

# Start counting
def handle_start():
	global is_running
	is_running = True

# Stop counting
def handle_stop():
	global is_running
	is_running = False

# Reser the time
def handle_reset():
	global tenths, seconds, ten_seconds, minutes
	tenths = 0
	seconds = 0
	ten_seconds = 0
	minutes = 0

# Define Event Handler for timer with 0.1 sec interval

# Just increment the time by 1
def increment_time():
	global tenths, seconds, ten_seconds, minutes

	# Tenths of seconds is always incremented by 1
	tenths += 1

	# If there are 10 tenths of a second, then we really have one more whole second
	# This happens when the time goes from 0:00.9 to 0:01:0
	if tenths >= 10:
		seconds += 1
		tenths = 0

	# We have a new ten seconds. This happens when the time goes from
	# 0:09.9 to 0:10.0, or 0:19.9 to 0:20.0, 0:29.9 to 0:30.0, etc..
	if seconds >= 10:
		ten_seconds += 1
		seconds = 0

	# We need to increment the minutes! This happens when the time goes from
	# 0:59.9 t0 1:00.0 or 3:59.9 to 4:00.0, etc..
	if ten_seconds >= 6:
		minutes += 1
		ten_seconds = 0


# Callback for the timer set to trigger every 100ms
def timer_handler():
	global is_running
	if (is_running):
		increment_time()

# Main canvas draw handler. Publish the time to the canvas
def draw_handler(canvas):
	canvas.draw_text(formatted_time(), (100, 100), 100, 'Blue')

# Create Frame
frame = simplegui.create_frame("stopwatch", 500, 150)
frame.set_draw_handler(draw_handler)

# Register Event Handlers
start_button = frame.add_button("start", handle_start)
stop_button = frame.add_button("stop", handle_stop)
reset_button = frame.add_button("reset", handle_reset)

# Start Timer and Frame
frame.start()
timer = simplegui.create_timer(100, timer_handler)
timer.start()
