#
#   Hello World server in Python
#   Binds DEALER socket to tcp://*:5555
#   Waits for a message from the client, and sends the same message back
#

import time
import zmq
import logging
import threading

# Import ServerHeartbeat
from com.progclass.server.server_heartbeat import ServerHeartbeat


class Server:
    def __init__(self):
        """Initializes variables used by the server."""
        # Initialize logging example
        logging.basicConfig(filename='server.log', filemode='w', format='%(asctime)s - %(levelname)s - SERVER - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logging.warning('This will get logged to a file')

        # Create a ZeroMQ context in order to talk to the client
        context = zmq.Context()
        # Create a zmq socket
        self.socket = context.socket(zmq.DEALER)

    def run(self):
        """Runs the server."""
        # Bind zmq socket to listen from any IP address on port 5555
        self.socket.bind("tcp://*:5555")

        # Wait for first message from client
        # It is not from the user, just a way for the server to know when to start the heartbeats
        print("Waiting for client...")
        message = self.socket.recv_string()
        logging.info(f"Received first message from client: {message}")
        print(f"First message from client: {message}")

        logging.debug("Starting heartbeat_thread")
        # Instantiate a ServerHeartbeat class
        server_heartbeat = ServerHeartbeat(self)
        heartbeat_thread = threading.Thread(target=server_heartbeat.heartbeat_loop)
        heartbeat_thread.start()

        # Start infinite loop
        while True:
            #  Wait for next request from client
            message = self.socket.recv_string()

            #  Do some 'work' like wait for 1 second
            time.sleep(1)
            # Show message on log
            logging.warning(f"Message from client: {message}")

            #  Send reply back to client
            # Formatted as "/{msg_type}/{msg_contents}"
            reply = f"/reply/{message}"
            print(f"Sending reply to client: {reply}")
            logging.info(f"Sending reply to client: {reply}")
            self.socket.send_string(reply)


# Run the server
if __name__ == '__main__':
    server = Server()
    server.run()
