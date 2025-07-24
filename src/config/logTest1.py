import sys

from GlobalLog import logger

def test1():
    logger.debug("That's it, beautiful and simple logging!")
    logger.info("中文日志可以不")
    logger.error("严重错误")

    logger.debug('这是一条debug测试信息')
    logger.info('这是一条info测试信息')
    logger.warning('这是一条warning测试信息')
    logger.error('这是一条error测试信息')


if __name__ == '__main__':
    test1()
    sys.exit()
