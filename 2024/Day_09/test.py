
import unittest
from solution import output


class TestDiskFragmenter(unittest.TestCase):
    def test_output(self):
        self.assertEqual(output(data), (6332189866718, 6353648390778))

def run_tests():  # runing test module for exec module
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDiskFragmenter)  # change xyz to test case
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple
                