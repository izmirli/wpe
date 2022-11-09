import pytest
import socket

from threading import Thread

from solution_server import run_server
from solution_client import get_client_socket, send_client_message


@pytest.fixture
def running_server():
    t = Thread(target=run_server)
    t.start()
    yield


@pytest.fixture()
def client_socket():
    s = get_client_socket()
    yield s
    s.close()


def test_say(running_server, client_socket):
    assert send_client_message(client_socket, 'say goodnight').strip() == 'goodnight'


def test_bad_command(running_server, client_socket):
    assert send_client_message(client_socket, 'blah blah blah').strip() == "Unknown command 'blah blah blah'"


def test_saying_goodbye(running_server, client_socket):
    assert send_client_message(client_socket, 'say hello').strip() == "hello"
    assert send_client_message(client_socket, 'bye').strip() == 'bye'


def test_increment(running_server, client_socket):
    assert send_client_message(client_socket, 'increment 5').strip() == '6'
