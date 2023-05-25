import logging

#Create and configure a logger
LOG_FORMAT   = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig( filename = "E:\\python\\Lumberjack.log", 
                    level = logging.DEBUG,
                    format = LOG_FORMAT)
logger = logging.getLogger()

#Test the logger
logger.info("Our first message")

print(logger.level)

#Test Messages
