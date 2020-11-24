from os import environ
from logging import basicConfig, INFO, info
from config import LOG_FILE

class Log(object):

    def __init__(self):
        basicConfig(filename=LOG_FILE, filemode='w',
            level=INFO, format="[%(asctime)s] [%(levelname)s] %(message)s")

    def log(self, message):
        info(message)
