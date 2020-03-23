#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

# Adding ZeroMQ messaging library
import zmq
# Adding Python's logging library
import logging
#import zmq
#import logging


# create logger
module_logger = logging.getLogger('spam_application.helper')

class Pants:
    def __init__(self):
        self.logger = logging.getLogger('spam_application.helper.Helper')
        self.logger.info('creating an instance of Helper')

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')

def some_function():
    module_logger.info('received a call to "some_function"')





"""logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - CLIENT - %(message)s')
file_handler = logging.FileHandler('client.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info('waiting for next request from client')

logger.debug('This will get logged to a file')
logger.info('This will get logged to a file')
logging.warning('This will get logged to a file')
logger.error('This will get logged to a file')
logger.critical('This will get logged to a file')"""

logging.basicConfig(filename='client.log', filemode='w', format='%(asctime)s - %(levelname)s - CLIENT - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.basicConfig(level= logging.DEBUG)


filename = 'client.log'
with open(filename) as file_object:
    for line in file_object:
        logging.debug(line)

context = zmq.Context()
#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
user_input = ""
while user_input != "q":
    user_input = input("Type a num: ")
    if user_input != "q":
        socket.send_string(user_input)
        logging.warning(f"Message to server: {user_input}")
        #  Get the reply.
        message = socket.recv()
        logging.debug(message)
