#
# This module will contain all the code that manages heartbeats sent from the server
#

# Import necessary modules
import time
import datetime
import logging


class ServerHeartbeat:
    def __init__(self, server_class):
        """Initializes the ServerHeartbeat class and sets the server class for later use."""
        self.server = server_class

        logging.basicConfig(filename='server_heartbeat.log', filemode='w',
                            format='%(asctime)s - %(levelname)s - SERVER - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    def heartbeat_loop(self):
        """Sends heartbeats to the client on a regular interval."""
        print("Starting heartbeats...")
        logging.info("Starting heartbeats")
        while True:
            self.send_heartbeat()
            time.sleep(1)

    def send_heartbeat(self):
        """Sends a heartbeat to the client with the current time."""
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # Formatted as "/{msg_type}/{msg_contents}"
        heartbeat_message = f"/heartbeat/{timestamp}"
        logging.debug(f"Sending heartbeat: {heartbeat_message}")

        # TIP: Uncomment the following line to see heartbeats in the console.
        # print(f"Sending heartbeat: {heartbeat_message}")

        self.server.socket.send_string(heartbeat_message)
