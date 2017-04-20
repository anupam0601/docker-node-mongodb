import logmatic
import logging
import socket
import logging.handlers
import datetime

# Create logger with TestCase1 application
logger = logging.getLogger("TestCase1")

""" 
	Create file handler :
		1. Formats the log to json
		2. Creates a new file with time stamp for every run
"""
dateTag = datetime.datetime.now().strftime("%Y:%b:%d-%H:%M:%S")
fh = logging.FileHandler(('TestCase1_%s.json') %dateTag)
fh.setFormatter(logmatic.JsonFormatter(extra={"hostname":socket.gethostname()}))

# create console handler with same log level
ch = logging.StreamHandler()
ch.setFormatter(logmatic.JsonFormatter(extra={"hostname":socket.gethostname()}))

# Add handlers and set log level
logger.addHandler(fh)
logger.addHandler(ch)
logger.setLevel(logging.INFO)

def func_test():
	logger.info("func_test")

func_test()
