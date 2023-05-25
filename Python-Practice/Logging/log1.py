import logging

#Create and configure a logger
LOG_FORMAT   = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig( filename = "E:\\python\\Lumberjack.log", 
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')
logger = logging.getLogger()

#Test the logger
logger.info("Our SECOND message after implementting overwrite")

print(logger.level)

#Test Messages
logger.debug("This is a harmless debug message")
logger.info("Some useful info")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")
