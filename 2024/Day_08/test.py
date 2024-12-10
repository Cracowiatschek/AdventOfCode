
import unittest
from solution import output

class TestXD(unittest.TestCase):
    def test_test(self):
        self.assertEqual(0,0)

def run_tests():  # runing test module for exec module
    suite = unittest.TestLoader().loadTestsFromTestCase(TestXD)  # change xyz to test case
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple
                