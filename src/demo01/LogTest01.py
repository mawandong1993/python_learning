import logging

LOG_FORMAT = "%(asctime)s [%(levelname)s] [%(name)s] [%(processName)s] [%(thread)s] [%(funcName)s] [%(pathname)s:%(lineno)d] - %(message)s"
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

# create logger
logger = logging.getLogger("simpleExample")
# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")