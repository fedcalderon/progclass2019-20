#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import logging

# Initialize logging example
logging.basicConfig(filename='server.log', filemode='w', format='%(asctime)s - %(levelname)s - SERVER - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('This will get logged to a file')

# Create a ZeroMQ context in order to talk to the client
context = zmq.Context()
# Create a zmq socket
socket = context.socket(zmq.REP)
# Bind zmq socket to listen from any IP address on port 5555
socket.bind("tcp://*:5555")
# Start infinite loop
while True:
    #  Wait for next request from client
    message = socket.recv_string()
    #  Do some 'work' like wait for 1 second
    time.sleep(1)
    # Show message on log
    logging.warning(f"Message from client: {message}")
    #  Send reply back to client
    socket.send_string(message)