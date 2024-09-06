import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from consume import process_message

class TestConsume(unittest.TestCase):
    def test_process_message(self):
        message = "{'forecast': 94.0,'actual': 93.0,'index': 0.0,'Biomass': 120.0,'Coal': 937.0,'Dutch_imports': 474.0,'French_imports': 53.0,'Gas_combined': 394.0,'Gas_open': 651.0,'Hydro': 0.0,'Irish_imports': 458.0,'Nuclear': 0.0,'Oil': 935.0,'Other': 300.0,'Pumped_storage': 0.0,'Solar': 0.0,'Wind': 0.0}"
        try:
            process_message(message)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
