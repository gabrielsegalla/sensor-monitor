import socket

class TCPServer:
    def __init__(self, data_handler, host="127.0.0.1", port=65432):
        self.data_handler = data_handler
        self.host = host
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"TCP Server listening on {self.host}:{self.port}")

    def start_server(self):
        """Inicia o servidor para receber dados."""
        conn, addr = self.server_socket.accept()
        print(f"Connected by {addr}")
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                yield data.decode('utf-8')
        finally:
            conn.close()
            print("Connection closed")
