import logging

import logging

logging.basicConfig(force=True,
level=logging.DEBUG, 
format='%(asctime)s - %(name)s %(levelname)s - %(message)s',
handlers=[
    logging.FileHandler("app1.log"),
    logging.StreamHandler()
])


logger = logging.getLogger("ArithmeticApp")

def add(x, y):
    result = x + y
    logger.debug(f"Addition of {x} and {y} is {result}")
    return result

def subtract(x, y):
    result = x - y
    logger.debug(f"Subtraction of {x} and {y} is {result}")
    return result

def multiply(x, y):
    result = x * y
    logger.debug(f"Multiplication of {x} and {y} is {result}")
    return result

def divide(x, y):
    try:
        result = x / y
        logger.debug(f"Division of {x} and {y} is {result}")
        return result
    except ZeroDivisionError:
        logger.error("Cannot divide by zero")
        return None

add(2, 3)
subtract(5, 3)
multiply(4, 6)
divide(10, 2)
divide(10, 0)
