
import unittest
from solution import output

class TestHoofIt(unittest.TestCase):
    def test_output(self):
        self.assertEqual(output(data), (36, 81))

def run_tests():  # runing test module for exec module
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHoofIt)  # change xyz to test case
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple
                