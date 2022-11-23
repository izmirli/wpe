"""Dynamic function server (Pickled).

Listen at fixed port (9999);
Support functions from "server_func*.py" local files, and 'bye" command.
Respond in "pickle" format.
Logging to console.
"""
import glob
import logging
import pickle
import socket
from types import FunctionType

SERVER_IP = '127.0.0.1'  # localhost IP.
SERVER_PORT = 9999

logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', level=logging.INFO)


def get_actions_from_local_files() -> dict:
    """Return actions functions-dict for server.

    Find local files with names of this pattern: "server_func_*.py"
    Load their functions to the "actions" mapping.
    Add 2 special functions: "bye" and "" (empty string for unknown).

    :return: mapping for functions the server supports.
    """
    actions = {}
    for func_file in glob.iglob('server_func_*.py'):
        code_globals = {}
        with open(func_file) as ffh:
            code = ffh.read()
        exec(code, code_globals)
        for code_global in code_globals:
            if not code_global.startswith('__') and isinstance(code_globals[code_global], FunctionType):
                actions[code_global] = code_globals[code_global]

    actions['bye'] = lambda x: "bye"
    actions[''] = lambda x: f"Unknown command '{x}'"
    return actions


def run_server():
    """Runs a single connection server, respond in pickle format.

    Support pre-defined message types, otherwise sends "Unknown" respond.

    :return: None
    """
    actions = get_actions_from_local_files()
    logging.info(actions)

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

        if command not in actions:
            logging.warning(f"Unknown command '{data}'")
            command = ''

        respond = actions[command](data[len(command):].strip())
        sent = client_sock.send(pickle.dumps(respond))
        logging.info("Sent %d bytes in respond to '%s' message." % (sent, command if command else 'Unknown'))
        if command == 'bye':
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
