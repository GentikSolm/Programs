import sys
import time
toolbar_width = 40

# setup toolbar
sys.stdout.write("[{}]".format(" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("#")
    sys.stdout.flush()

sys.stdout.write("\n")
