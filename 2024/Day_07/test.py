
import unittest
from solution import output


class TestBridgeRepair(unittest.TestCase):
    def test_output(self):
        self.assertEqual(output(data), (3749, 11387))


def run_tests():  # runing test module for exec module
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBridgeRepair)  # change xyz to test case
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple
                