import sys
import unittest
from io import StringIO


def print_(s):
    print(s)

class TestConsolePrint(unittest.TestCase):
    def test_print(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        print_("test")
        # sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue().replace('\n',''), "test")

if __name__ == '__main__':
    unittest.main()