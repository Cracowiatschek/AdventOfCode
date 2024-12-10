
import unittest
from solution import output

def run_tests():  # runing test module for exec module
    suite = unittest.TestLoader().loadTestsFromTestCase(xyz)  # change xyz to test case
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple
                