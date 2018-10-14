import logging

FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
logger = logging.getLogger('wallet')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('wallet.log')
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)
