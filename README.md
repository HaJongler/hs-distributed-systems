# hs-distributed-systems
Simple python xmlrpc chat client & server prototype

This is a simple prototype for chat system based on xmlrpc.
The server stores all the messages and the user list only in memory.

Server start:  
 `$ python server.py`

Client:  
 `$ python client.py [username]`

By default the server will start on port 8000 and the client will
try to connect to http://localhost:8000/

The client accepts the following commands:  
/quit - end session and exit  
/list - list current online users  
/kick [user] - list available commands  