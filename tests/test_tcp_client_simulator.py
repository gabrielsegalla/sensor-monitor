import unittest
from app.tcp_client_simulator import TCPSensorSimulator

class TestTCPSensorSimulator(unittest.TestCase):
    def test_data_format(self):
        simulator = TCPSensorSimulator()
        data = simulator.generate_data()
        self.assertIsInstance(float(data), float)  # Verifica se o dado gerado é um número válido

if __name__ == "__main__":
    unittest.main()
