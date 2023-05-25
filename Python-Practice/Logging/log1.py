import logging

#Create and configure a logger
logging.basicConfig( filename = "E:\\python\\Lumberjack.log")
logger = logging.getLogger()

#Test the logger
logger.info("Our first message")

print(logger.level)