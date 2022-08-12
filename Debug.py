import time

filename = 'debug.log'


def log(_message):
    file_handler = open(filename, 'a')
    file_handler.write(f"{_message} @ {time.ctime()} \n")
    file_handler.close()
