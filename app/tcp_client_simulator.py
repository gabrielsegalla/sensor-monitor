import socket
import time
import random

class TCPSensorSimulator:
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port

    def send_data(self):
        """Envia dados simulados ao servidor."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
            try:
                while True:
                    # Simula um valor de sensor
                    sensor_value = random.uniform(20.0, 30.0)
                    message = f"{sensor_value:.2f}"
                    print(f"Sending: {message}")
                    s.sendall(message.encode('utf-8'))
                    time.sleep(1)  # Intervalo de 1 segundo
            except KeyboardInterrupt:
                print("Simulation stopped by user")
            finally:
                s.close()
