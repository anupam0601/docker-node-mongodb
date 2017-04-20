import logmatic
import logging
import socket
import logging.handlers
import datetime

# Create logger with TestCase1 application
# logger = logging.getLogger("TestCase1")

#"""
#   Create file handler :
#       1. Formats the log to json
#       2. Creates a new file with time stamp for every run
# """
# dateTag = datetime.datetime.now().strftime("%Y:%b:%d-%H:%M:%S")
# fh = logging.FileHandler(('TestCase1_%s.json') % dateTag)
# fh.setFormatter(logmatic.JsonFormatter(
#     extra={"hostname": socket.gethostname()}))

# # create console handler with same log level
# ch = logging.StreamHandler()
# ch.setFormatter(logmatic.JsonFormatter(
#     extra={"hostname": socket.gethostname()}))

# # Add handlers and set log level
# logger.addHandler(fh)
# logger.addHandler(ch)
# logger.setLevel(logging.INFO)

# # def func_test():
# #     logger.info("func_test")

# # func_test()

#INFO = logging.INFO


class Logger(object):

    def __init__(self, logger=None, date_tag=None, filehandler=None,
                 consolehandler=None, test_id=None):

        if logger is None:
            logger = logging.getLogger(test_id)
            # Add handlers and set log level

        if test_id is None:
            test_id = "TC1"

        if date_tag is None:
            dateTag = datetime.datetime.now()\
                .strftime("%Y:%b:%d-%H:%M:%S")

        if filehandler is None:
            filehandler = logging.FileHandler(
                ('%s_%s.json') % (test_id, dateTag))
            filehandler.setFormatter(logmatic.JsonFormatter(
                extra={"hostname": socket.gethostname()}))

        if consolehandler is None:
            consolehandler = logging.StreamHandler()
            consolehandler.setFormatter(logmatic.JsonFormatter(
                extra={"hostname": socket.gethostname()}))

        logger.addHandler(filehandler)
        logger.addHandler(consolehandler)
        logger.setLevel(logging.DEBUG)

        

        self.logger = logger
        self.info = logger.info
        self.debug = logger.debug 
        self.dateTag = dateTag
        self.filehandler = filehandler
        self.consolehandler = consolehandler
        self.test_id = test_id

    def info(self, message):
        return self.logger.info(message)

    def debug(self, message):
        return self.logger.debug(message)

if __name__ == '__main__':

    log = Logger()
    log.info("anupam")
   #  log.info("debnath")
