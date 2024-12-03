import unittest
from app.tcp_server import TCPServer
from threading import Thread
import socket

class TestTCPServer(unittest.TestCase):
    def setUp(self):
        self.server = TCPServer()
        self.server_thread = Thread(target=self.server.start_server, daemon=True)
        self.server_thread.start()

    def test_server_receives_data(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(('127.0.0.1', 65432))
            client.sendall(b"42.5\n")
            received = client.recv(1024).decode()
            self.assertEqual(received.strip(), "42.5")


if __name__ == "__main__":
    unittest.main()
