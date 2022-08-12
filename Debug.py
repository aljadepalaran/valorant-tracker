import time

filename = 'debug.log'


def log(_message):
    file_handler = open(filename, 'w')
    file_handler.write(f"{_message} @ {time.time()}")
    file_handler.close()
