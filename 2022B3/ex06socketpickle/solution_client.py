"""Client for pickled server responds."""
import pickle
import socket

SERVER_IP = '127.0.0.1'  # localhost IP.
SERVER_PORT = 9999


def send_client_message(sock: socket, message: str) -> str:
    """Sends given message through given socket & return server's respond.

    Server's respond are expected to be in pickle format.

    :param sock: socket
    :param message: message to send
    :return: respond
    """
    sock.send(message.encode())
    respond = sock.recv(1024)
    respond_obj = pickle.loads(respond)
    return respond_obj


def get_client_socket() -> socket:
    """Create and return socket for client.

    :return: socket
    """
    sock: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, SERVER_PORT))
    return sock


def run_client():
    """Test run."""
    s = get_client_socket()  # Receive no more than 1024 bytes
    print(send_client_message(s, 'numbers'))
    print(send_client_message(s, 'reverse_word elephant'))
    print(send_client_message(s, 'unicode_map abracadabra'))
    print(send_client_message(s, 'blah blah blah'))
    print(send_client_message(s, 'bye'))
    s.close()


if __name__ == '__main__':
    run_client()
