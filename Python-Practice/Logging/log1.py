import logging
import math
#Create and configure a logger
LOG_FORMAT   = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig( filename = "E:\\python\\Lumberjack.log", 
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')
logger = logging.getLogger()

#Test the logger
# logger.info("Our SECOND message after implementting overwrite")

# print(logger.level)

# #Test Messages
# logger.debug("This is a harmless debug message")
# logger.info("Some useful info")
# logger.warning("I'm sorry, but I can't do that, Dave.")
# logger.error("Did you just try to divide by zero?")
# logger.critical("The entire internet is down!!")

def quadratic_formula(a, b, c):
    """Returns the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2} )".format(a, b, c))

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots
    logger.debug("# Return the roots")
    return (root1, root2)

roots = quadratic_formula(1, 0, 1)
print(roots)
