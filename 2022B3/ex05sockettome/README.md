# WPE 2022 B3 Exercise 5: Socket to me

The idea is that the server will listen on port 9999, and wait for connections to it.

The client can send one of three messages:
* "say".  The "say" message is followed by a string, which the server should then repeat back.
* "increment".  The "increment" message is followed by an integer.  The server responds with 1 more than that integer.
* "bye".  The "bye" message indicates that we want to hang up.  The server responds with "bye", and then disconnects.

Any other message will result in "Unknown command" being returned, followed by whatever the user entered.

Code structured as follows:

* `solution_server.py`:
  * **run_server** runs the server, waiting for client connections and implementing the functionality we had before.
It takes no arguments, and runs an infinite "while" loop that exits when the server gets "bye" from the client.
  * **get_client_connection** is a convenience function that grabs the connection from the client when it is made.

* `solution_client.py`:
  * **send_client_message** takes two arguments, a socket and a message (a string). It sends the message to the server,
receives up to 1024 bytes of a response, and returns the response (a string) to the caller.
  * **get_client_socket** creates a client socket, connects to the server, and returns the socket object.


We should then be able to write the following kind of code:

```python
def run_client():
    s = get_client_socket()  # Receive no more than 1024 bytes
    for i in range(5):
        print(send_client_message(s, f'say {i}'))

    print(send_client_message(s, 'say goodnight'))
    print(send_client_message(s, 'say goodnight, Gracie'))

    print(send_client_message(s, 'garbage'))

    print(send_client_message(s, 'increment 5'))
    print(send_client_message(s, 'increment 12345'))

    print(send_client_message(s, 'bye'))

    s.close()
```
