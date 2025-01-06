
import unittest
from unittest import TestCase

from solution import output


class TestGardensGroups(unittest.TestCase):

    def test_output(self):
        self.assertEqual(output(""), (0, 0))



def run_tests():  # runing test module for exec module
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGardensGroups)  # change xyz to test case
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple
                