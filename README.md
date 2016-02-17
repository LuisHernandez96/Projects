#Introduction to Networks Final Project:

Using code provided by the teacher as base, I implemented a client and a server for a chat using the UDP protocol.
For the client I had to implement threads so the terminal can receive and send messages simultaneously, without this, the client is waiting for an imput from the user and it doesn't display the messages received until the imput is given.
In the server I implemented a linked list to save the data from the incoming connections.

Using Linux, when you comlpie the Client code, you need to add "-lpthread".

When running the Client use this format: clientUDP dirIPServer

Client commands:
To enter the username: -u "username"
To finish conection: -q
to send private meessage: -p"username" "message"
