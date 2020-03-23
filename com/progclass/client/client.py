#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

# Adding ZeroMQ messaging library
import zmq
# Adding Python's logging library
import logging

print("Hello Client, this is Mr Fed")

# Configuring logging example
logging.basicConfig(filename='client.log', filemode='w', format='%(asctime)s - %(levelname)s - CLIENT - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# In order to start ZeroMQ, create a context
context = zmq.Context()
# Create a zmq socket to talk to the server
socket = context.socket(zmq.REQ)
# Connect zmq socket to localhost
socket.connect("tcp://localhost:5555")
#  Show message on console
print("Connecting to hello server…")
# Show message on the log file
logging.warning("Connecting to hello server…")
# Create a string variable to store user inputs and initialize to empty
user_input = ""
# Start an infinite loop
while user_input != "q":
    user_input = input("Type a msg ('q' to quit program): ")
    if user_input != "q":
        # The socket can send literal strings to the server
        socket.send_string(user_input)
        logging.warning(f"Message to server: {user_input}")
        #  Get the reply.
        message = socket.recv()
        logging.warning(f"Reply from server: {message}")
