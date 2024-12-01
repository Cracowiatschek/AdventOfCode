import unittest
from solution import GetDistance, output

get_distance = GetDistance()

class TestGetDistance(unittest.TestCase):

    def test_data_parser(self):
        get_distance.data_parser(data)

        self.assertEqual(get_distance.left_list, [3, 4, 2, 1, 3, 3])
        self.assertEqual(get_distance.right_list, [4, 3, 5, 3, 9, 3])

    def test_get_the_smallest(self):
        test_list = [3, 4, 2, 1, 3, 3]

        smallest_index = get_distance.get_the_smallest(test_list)
        self.assertEqual(smallest_index, 3)

    def test_get_distance(self):
        get_distance.left_list = [3, 4, 2, 1, 3, 3]
        get_distance.right_list = [4, 3, 5, 3, 9, 3]

        get_distance.get_distance()

        self.assertEqual(get_distance.distance, 11)

    def test_get_increases_score(self):
        get_distance.left_list = [3, 4, 2, 1, 3, 3]
        get_distance.right_list = [4, 3, 5, 3, 9, 3]

        get_distance.get_increases_score()

        self.assertEqual(get_distance.increases_score, 31)

    def test_output(self):

        distance, increases_score = output(data)

        self.assertEqual(distance, 11)
        self.assertEqual(increases_score, 31)


# if __name__ == "__main__":
#     unittest.main()

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGetDistance)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple

# if __name__ == "__main__":
#     result, simple = run_tests()
