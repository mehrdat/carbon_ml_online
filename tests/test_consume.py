import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from consume import process_message

class TestConsume(unittest.TestCase):
    def test_process_message(self):
        message = '{"relative_humidity_2m": 60, "wind_speed_10m": 5, "temperature_2m": 22.5}'
        try:
            process_message(message)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
