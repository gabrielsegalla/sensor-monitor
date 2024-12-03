import unittest
from app.plotter import Plotter
from app.data_handler import DataHandler

class TestPlotter(unittest.TestCase):
    def setUp(self):
        self.data_handler = DataHandler()
        self.plotter = Plotter(self.data_handler)

    def test_plot_initialization(self):
        self.assertEqual(self.plotter.data_handler, self.data_handler)

if __name__ == "__main__":
    unittest.main()
