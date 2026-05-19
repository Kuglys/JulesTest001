import unittest

from server import run_number_script


class TestServer(unittest.TestCase):
    def test_run_number_script(self):
        self.assertEqual(run_number_script(), "5")


if __name__ == "__main__":
    unittest.main()
