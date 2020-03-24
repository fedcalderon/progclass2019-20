import zmq
import logging
import datetime
import time

logging.basicConfig(filename='client.log', filemode='w', format='%(asctime)s - %(levelname)s - CLIENT - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

context = zmq.Context()
#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
user_input = ""


def send_heartbeat_message():
    x = datetime.datetime.now()
    month = x.month
    day = x.day
    hour = x.hour
    minute = x.minute
    second = x.second

    if day < 10:
        day = "0" + str(day)
    if hour < 10:
        hour = "0" + str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    if second < 10:
        second = "0" + str(second)

    # Keep in mind that client_heartbeat is a string, not an integer.
    client_heartbeat = f"{month}{day}{hour}{minute}{second}"

    # Send client_heartbeat to server and log it.
    socket.send_string(client_heartbeat)
    logging.warning(f"Message to server: {client_heartbeat}")

    #######################################################################
    # TIME COMPARISON
    #######################################################################

    # Keep in mind that server_heartbeat is a string, not an integer.
    server_heartbeat = socket.recv_string()
    print(server_heartbeat)

    # Once the server heartbeat is received, do the time comparison.
    if int(client_heartbeat) > int(server_heartbeat):
        print("client_heartbeat is larger")
    elif int(server_heartbeat) > int(client_heartbeat):
        print("server_heartbeat is larger")


while True:
    send_heartbeat_message()