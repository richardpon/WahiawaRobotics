# Template for "Stopwatch: The Game"
import simplegui

# Define Global Variables

# Tracks the global time in tenths of a second
time_count = 0

# Flag to determine if the clock is running
is_running = False

# Define Helper Function 
''' format(t) converts "t" into formatted string A:BC.D

This is the most complex function in this solution. The approach is to calculate
the largest units first (minutes), and then work down to smaller units one by one
'''
def format(t):

	# Get the number of minutes
	minutes = t / 600

	# Total number of tenths of seconds left. The amount of time here is less than one minute
	remainder = t - (minutes * 600)

	# Calculate number of tens of seconds. If ten_seconds = 4, it represents 40 seconds 
	ten_seconds = remainder / 100

	# Number of tenths of seconds. The amount of time here is less than 10 seconds
	remainder = remainder % 100

	# Number of seconds. 
	seconds = remainder / 10

	# Number of tenths of seconds.
	tenths = remainder % 10

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
	global time_count
	time_count = 0

# Define Event Handler for timer with 0.1 sec interval

# Just increment the time by 1
def increment_time():
	global time_count
	time_count += 1

# Callback for the timer set to trigger every 100ms
def timer_handler():
	global is_running
	if (is_running):
		increment_time()

# Main canvas draw handler. Publish the time to the canvas
def draw_handler(canvas):
	canvas.draw_text(format(time_count), (100, 100), 100, 'Blue')

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
