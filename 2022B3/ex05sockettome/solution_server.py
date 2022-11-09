"""Simple server.

Listen at fixed port, and responds to 3 messages.
'bye' message from client closes server.

Logging to console.
"""
import socket
import logging

SERVER_IP = '127.0.0.1'  # localhost IP.
SERVER_PORT = 9999
MESSAGES = {
    'say': {'respond': lambda msg: msg, 'disconnect': False},
    'increment': {'respond': lambda i: str(int(i) + 1), 'disconnect': False},
    'bye': {'respond': lambda x: "bye", 'disconnect': True},
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
        data = client_sock.recv(1024).decode().strip()  # receive up to 1KB bytes & decode to str.
        command = data.split()[0] if data else ''
        if command not in MESSAGES:
            sent = client_sock.send(f"Unknown command '{data}'".encode())
            logging.info("Sent %d bytes in respond to unknown command (%s)." % (sent, command))
            continue

        respond = MESSAGES[command]['respond'](data[len(command):].strip())
        sent = client_sock.send(respond.encode())
        logging.info("Sent %d bytes in respond to '%s' message." % (sent, command))
        if MESSAGES[command]['disconnect']:
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
