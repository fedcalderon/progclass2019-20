The resources directory is meant to have configuration files used by both the server and the client.

Here is the homework assignment:

Asher: The client shall send the server a heartbeat message (a time stamp) every second. The time stamp must larger than the received timestamp from server. Must do time comparison.
Andrew: The server shall send the client a heartbeat message (a time stamp) every second. The time stamp must larger than the received timestamp from client. Must do time comparison.
Xade: Configure the logging to support warning, info, debug, critical for the server and client to utilize.
Micah: Research how to implement MySQL database in Python and code a prototype to store user information such as username and email.
Jazmin: Configure server to detect the first heartbeat from the client and output message to the server log saying the server is initialized.
Kino: Setup logging configuration file to specify file names, logging types, etc., to be used by both server and client.
Milton: Research ZeroMQ implementation in Python to design a software bus to handle the incoming and outgoing messages.
