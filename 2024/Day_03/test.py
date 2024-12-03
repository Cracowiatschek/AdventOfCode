
import unittest
from solution import  MemoryScanner, output

memory_scanner = MemoryScanner()


class TestMemoryScanner(unittest.TestCase):
    def test_read_data(self):
        memory_scanner.read_data(data)
        self.assertEqual(memory_scanner.memory_content, [(2, 4), (5, 5), (11, 8), (8, 5)]) #

    def test_sum_of_multiplication(self):
        memory_scanner.get_sum_of_multiplication()
        memory_scanner.trim_data(data)
        self.assertEqual(memory_scanner.sum_of_multiplication, 161)

    def test_trim_data(self):
        trim_data: list[str] = memory_scanner.trim_data(data)
        memory_scanner.read_data(trim_data)
        self.assertEqual(memory_scanner.memory_content, [(2, 4), (8, 5)])

    def test_output(self):
        self.assertEqual(output(data), (161, 48))


def run_tests():  # runing test module for exec module
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMemoryScanner)  # change xyz to test case
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple
                