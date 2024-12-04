
import unittest
from solution import output


class TestCrossword(unittest.TestCase):
    def test_part_one(self):
        solution_1: int = output(data)[0]
        self.assertEqual(solution_1, 18)

    def test_part_two(self):
        solution_2: int = output(data)[1]
        self.assertEqual(solution_2, 9)


def run_tests():  # runing test module for exec module
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCrossword)  # change xyz to test case
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple
                