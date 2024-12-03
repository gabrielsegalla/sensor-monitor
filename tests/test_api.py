import unittest
from flask import Flask
from app.api import app, data_handler

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        data_handler.add_to_queue("25.6") 

    def test_get_latest(self):
        response = self.app.get("/latest")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"latest": 25.6})

    def test_get_history(self):
        response = self.app.get("/history")
        self.assertEqual(response.status_code, 200)
        self.assertIn("25.6", response.json["history"])
