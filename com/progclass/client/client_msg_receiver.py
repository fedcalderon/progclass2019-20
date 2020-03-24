#
# This module contains the ClientMsgReceiver to handle messages received by the client
#

# Import necessary module(s)
from datetime import datetime
import logging


class ClientMsgReceiver:
    def __init__(self, client_class):
        """Initializes the ClientMsgReceiver, and sets the client_class field for later use."""
        self.client = client_class

        # Configuring logging example
        logging.basicConfig(filename='client_msg_receiver.log', filemode='w',
                            format='%(asctime)s - %(levelname)s - CLIENT - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    def incoming_loop(self):
        """Waits for messages from the server and decides what to do with each one."""
        while True:
            if self.client.exit_flag:
                break
            incoming_message = self.client.socket.recv_string()
            logging.debug(f"Received message: {incoming_message}")

            # Message formatted as "/{msg_type}/{msg_contents}"
            split = incoming_message.split('/')
            message_type = split[1]
            message_text = split[2]
            if message_type == 'heartbeat':
                logging.debug(f"Received heartbeat: {message_text}")

                # TIP: Uncomment the following line to see heartbeats in the console.
                # print(f"Received heartbeat: {message_text}")

                self.check_heartbeat_time(message_text)
            elif message_type == 'reply':
                logging.info(f"Server reply: {message_text}")
                print(f"Received reply: {message_text}")
                # Notify the main thread
                self.client.server_replied.set()
            else:
                logging.warning(f"Unknown message: {incoming_message}")

    def check_heartbeat_time(self, timestamp):
        """Extracts the timestamp from the heartbeat and compares it to the current time."""
        dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
        diff = datetime.now() - dt
        if diff.total_seconds() == 0.0:
            logging.debug("Ping: < 1 ms")
        else:
            ms = int(diff.total_seconds() * 1000)
            diff_string = f"{ms} ms"
            logging.debug(f"Ping: {diff_string}")
