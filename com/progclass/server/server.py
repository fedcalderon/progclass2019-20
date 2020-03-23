#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

import logging
import pants

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - SERVER - %(message)s')
file_handler = logging.FileHandler('server.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info('waiting for next request from server')

logger.debug('This will get logged to a file')
logger.info('This will get logged to a file')
logging.warning('This will get logged to a file')
logger.error('This will get logged to a file')
logger.critical('This will get logged to a file')

logging.basicConfig(filename='client.log', filemode='w', format='%(asctime)s - %(levelname)s - SERVER - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.basicConfig(level= logging.DEBUG)


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555") #localhost xx.xx.xx.xx:port

filename = 'server.log'
with open(filename) as file_object:
    for line in file_object:
        logging.debug(line)

counter = 0
num1 = num2 = 0

while True:
    #  Wait for next request from client
    message = socket.recv_string()

    #  Do some 'work'
    time.sleep(1)
    logging.warning(f"Message from client: {message}")
    #  Send reply back to client
    socket.send_string(message)