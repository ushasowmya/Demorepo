#log_announcements("I'm learning %s")
# print log_announcements

LOGFILE = 'logging-basic.txt'

def print_log():
    "Prints out what's written to the log file so far."
    print(open(LOGFILE).read(), end="")


# This "with" line resets the log file to be empty,
# each time you run the test:
with open(LOGFILE, 'w'): pass

# Write your code here:
