# coding=utf-8

import os
import sys
from loguru import logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file_path = os.path.join(BASE_DIR, 'Log/root_{time:YYYY-MM}.log')
err_log_file_path = os.path.join(BASE_DIR, 'Log/error_{time:YYYY-MM}.log')
logger_format = "<green>{time:YYYY-MM-DD HH:mm:ss,SSS}</green> [<level>{level:<5}</level>] [{name}] [{file}:{function}():{line}] <level>{message}</level>"

"""
<Cyan></Cyan>
logger_format = "{time:YYYY-MM-DD HH:mm:ss,SSS} | {level} | [{thread}]| {file}:{function}():{line} | - {message}"
logger_format = "<level>{time:YYYY-MM-DD HH:mm:ss,SSS}</level> [{level:<5}] [{file}:{function}():{line}] <level>{message}</level>"
"""

logger.remove()
logger.add(sys.stderr, format=logger_format, colorize=True, filter="", level="DEBUG")
logger.add(log_file_path, format=logger_format, rotation="500 MB", encoding='utf-8', enqueue=True, compression="zip")
logger.add(err_log_file_path, format=logger_format, rotation="500 MB", encoding='utf-8', enqueue=True,
           compression="zip", level='ERROR')

logger: logger
