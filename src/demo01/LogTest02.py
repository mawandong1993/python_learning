import logging
import sys

LOG_FORMAT = "%(asctime)s [%(levelname)s] [%(name)s] [%(processName)s] [%(thread)s] [%(funcName)s] [%(pathname)s:%(lineno)d] - %(message)s"

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
rf_handler = logging.StreamHandler(sys.stderr)  # 默认是sys.stderr
rf_handler.setLevel(logging.DEBUG)
rf_handler.setFormatter(logging.Formatter(LOG_FORMAT))

f_handler = logging.FileHandler('my02.log')
f_handler.setLevel(logging.DEBUG)
f_handler.setFormatter(logging.Formatter(LOG_FORMAT))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')