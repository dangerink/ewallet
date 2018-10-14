import logging
import uuid

from functools import wraps


FORMAT = '%(asctime)-15s %(levelname)-5s %(message)s'
logger = logging.getLogger('wallet')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('wallet.log')
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)


def log_action(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        _id = uuid.uuid4().hex
        logger.info('Starting {0} {1} args={2}, kwargs={3}'.format(_id, f.__name__, args, kwargs))
        try:
            result = f(*args, **kwargs)
        finally:
            logger.info('Finishing {0}'.format(_id))
        return result

    return wrapper
