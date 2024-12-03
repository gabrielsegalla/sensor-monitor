import unittest
from app.data_handler import DataHandler

class TestDataHandler(unittest.TestCase):
    def setUp(self):
        self.data_handler = DataHandler(file_name="test_sensor_data.csv")

    def test_add_to_queue(self):
        self.data_handler.add_to_queue("25.6")
        # Verifique os dados na fila
        self.assertEqual(list(self.data_handler.data_queue.queue), [25.6])

    def test_save_data(self):
        self.data_handler.save_data("28.4")
        with open("test_sensor_data.csv", "r") as file:
            lines = file.readlines()
        # Verifique se o dado foi salvo no arquivo
        self.assertIn("28.4\n", lines)

    def test_get_data(self):
        self.data_handler.add_to_queue("30.1")
        self.data_handler.add_to_queue("28.4")
        # Verifique o dado mais recente
        self.assertEqual(self.data_handler.get_data(), 30.1)
        self.assertEqual(list(self.data_handler.data_queue.queue), [28.4])
