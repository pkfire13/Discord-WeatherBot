import unittest
import requests
from config import APIKEY
from weatherbot import weather

class test_weather(unittest.TestCase):

    def test_weather(self):
        testing = weather('Kingwood')
        print(testing)

if __name__ == "__main__":
    unittest.main()