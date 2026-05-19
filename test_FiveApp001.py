import unittest
import subprocess
import sys
from FiveApp001 import get_number


class TestFiveApp001(unittest.TestCase):
    def test_get_number(self):
        self.assertEqual(get_number(), 5)

    def test_script_outputs_number(self):
        result = subprocess.run(
            [sys.executable, "FiveApp001.py"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout.strip(), "5")


if __name__ == '__main__':
    unittest.main()
