
import unittest
from solution import output

class TestPlutonianPebbles(unittest.TestCase):
    def test_output(self):
        self.assertEqual(output(data)[0], 55312)

def run_tests():  # runing test module for exec module
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPlutonianPebbles)  # change xyz to test case
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple
                