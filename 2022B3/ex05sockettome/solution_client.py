"""Simple message client."""
import socket

SERVER_IP = '127.0.0.1'  # localhost IP.
SERVER_PORT = 9999


def send_client_message(sock: socket, message: str) -> str:
    """Sends given message through given socket & return server's respond.

    :param sock: socket
    :param message: message to send
    :return: respond
    """
    sock.send(message.encode())
    return sock.recv(1024).decode()


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
    print(send_client_message(s, 'say goodnight'))
    print(send_client_message(s, 'say goodnight, Gracie'))
    for i in range(5):
        print(send_client_message(s, f'say {i}'))
    print(send_client_message(s, 'garbage'))
    print(send_client_message(s, 'increment 5'))
    print(send_client_message(s, 'increment 12345'))
    print(send_client_message(s, 'bye'))
    s.close()


if __name__ == '__main__':
    run_client()
