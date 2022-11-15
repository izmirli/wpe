"""Simple server.

Listen at fixed port, and responds to 3 messages.
'bye' message from client closes server.

Logging to console.
"""
import logging
import pickle
import socket

SERVER_IP = '127.0.0.1'  # localhost IP.
SERVER_PORT = 9999
MESSAGES = {
    'numbers': {'respond': lambda r: list(range(int(r) if r.isdigit() else 10)), 'disconnect': False},
    'reverse_word': {'respond': lambda w: w[::-1], 'disconnect': False},
    'unicode_map': {'respond': lambda w: {c: ord(c) for c in w}, 'disconnect': False},
    'bye': {'respond': lambda x: "bye", 'disconnect': True},
    '': {'respond': lambda x: f"Unknown command '{x}'", 'disconnect': False},
}

logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', level=logging.INFO)


def run_server():
    """Runs a single connection server.

    Support 3 message types: "say", "increment" & "bye".
    Other messages will result in "Unknown command" being returned.

    :return: None
    """
    sock: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP/IP
    sock.bind((SERVER_IP, SERVER_PORT))  # bind server's address.
    sock.listen()
    logging.info("Server is UP (listening at %s:%d)" % (SERVER_IP, SERVER_PORT))

    client_sock = get_client_connection(sock)
    while True:
        try:
            data = client_sock.recv(1024).decode().strip()  # receive up to 1KB bytes & decode to str.
        except ConnectionAbortedError as cae:
            logging.error(cae)
            break
        command = data.split()[0] if data else ''
        if not command:  # looks like user has disconnected.
            logging.warning("User has disconnected before 'bye' message.")
            client_sock.close()
            break

        if command not in MESSAGES:
            logging.warning(f"Unknown command '{data}'")
            command = ''

        respond = MESSAGES[command]['respond'](data[len(command):].strip())
        sent = client_sock.send(pickle.dumps(respond))
        logging.info("Sent %d bytes in respond to '%s' message." % (sent, command if command else 'Unknown'))
        if command in MESSAGES and MESSAGES[command]['disconnect']:
            client_sock.close()
            break

    sock.close()
    logging.info("Server closed")


def get_client_connection(sock: socket) -> socket:
    """Accept connection from client and return the socket to it.

    :param sock: server socket
    :return: client socket
    """
    (client_sock, client_address) = sock.accept()
    logging.info("Client connected from: %s:%d" % client_address)
    return client_sock


if __name__ == '__main__':
    run_server()
