#
#   Hello World client in Python
#   Connects DEALER socket to tcp://localhost:5555
#   Sends sends a user-specified string to the server, and receives the reply
#

# Adding ZeroMQ messaging library
import zmq
# Adding Python's logging library
import logging
import threading

# Import ClientMsgReceiver
from com.progclass.client.client_msg_receiver import ClientMsgReceiver


class Client:
    def __init__(self):
        """Initializes variables for the client."""
        # Initialize the exit_flag for the other thread
        self.exit_flag = False

        # In order to start ZeroMQ, create a context
        context = zmq.Context()
        # Create a zmq socket to talk to the server
        self.socket = context.socket(zmq.DEALER)

        # Create an event to let the main thread know when the server replies
        logging.debug("Initializing server_replied Event")
        self.server_replied = threading.Event()

    def run(self):
        """Runs the client."""
        print("Hello Client")

        # Configuring logging example
        logging.basicConfig(filename='client.log', filemode='w', format='%(asctime)s - %(levelname)s - CLIENT - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

        # Connect zmq socket to localhost
        self.socket.connect("tcp://localhost:5555")
        #  Show message on console
        print("Connecting to hello server…")
        # Show message on the log file
        logging.warning("Connecting to hello server…")

        # Start the thread to handle incoming messages
        logging.debug("Starting thread: incoming_thread")
        # Instantiate a ClientMsgReceiver
        client_msg_receiver = ClientMsgReceiver(self)
        incoming_thread = threading.Thread(target=client_msg_receiver.incoming_loop)
        incoming_thread.start()

        # Send connected message to server
        self.socket.send_string("connected")
        logging.debug("Sent message 'connected' to server")

        # Create a string variable to store user inputs and initialize to empty
        user_input = ""
        # Start an infinite loop
        while user_input != "q":
            user_input = input("Type a msg ('q' to quit program): ")
            if user_input != "q":
                # The socket can send literal strings to the server
                self.socket.send_string(user_input)
                logging.warning(f"Message to server: {user_input}")

                # Wait for the server's response, handled in the other thread
                logging.debug("Waiting for incoming_thread to receive server's reply")
                self.server_replied.wait()
                self.server_replied.clear()
                logging.debug("Server replied, clear to proceed")

        self.exit_flag = True
        logging.info("Exited normally")


# Starts the client
if __name__ == "__main__":
    client = Client()
    client.run()
