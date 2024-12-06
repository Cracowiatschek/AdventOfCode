
import unittest
from solution import read_rules, read_sections, validation, sum_valid_pages, correction, Rule, Section

class TestPrintQueue(unittest.TestCase):

    def test_data(self):
        self.test_rules: list[Rule] = [
            Rule(47, 53),
            Rule(97, 13),
            Rule(97, 61),
            Rule(97, 47),
            Rule(75, 29),
            Rule(61, 13),
            Rule(75, 53),
            Rule(29, 13),
            Rule(97, 29),
            Rule(53, 29),
            Rule(61, 53),
            Rule(97, 53),
            Rule(61, 29),
            Rule(47, 13),
            Rule(75, 47),
            Rule(97, 75),
            Rule(47, 61),
            Rule(75, 61),
            Rule(47, 29),
            Rule(75, 13),
            Rule(53, 13)
        ]
        self.test_sections: list[Section] = [
            Section([75, 47, 61, 53, 29], True),
            Section([97, 61, 53, 29, 13], True),
            Section([75, 29, 13], True),
            Section([75, 97, 47, 61, 53], True),
            Section([61, 13, 29], True),
            Section([97, 13, 75, 29, 47], True)
        ]

    def test_read_rules(self):
        self.test_data()
        self.assertEqual(read_rules(data), self.test_rules)

    def test_section_rules(self):
        self.test_data()
        self.assertEqual(read_sections(data), self.test_sections)

    def test_validation_positive(self):
        self.test_data()
        test_data: Section = Section([75,47,61,53,29], True)
        self.assertEqual(validation(self.test_rules, test_data.values), True)

    def test_validation_negative(self):
        test_data: Section = Section([61,13,29], True)
        self.test_data()
        self.assertEqual(validation(self.test_rules, test_data.values), False)

    def test_correction(self):
        test_data: list[int] = [61,13,29]
        self.test_data()
        self.assertEqual(correction(self.test_rules, test_data), [61,29,13])

    def test_sum_valid_pages(self):
        self.test_data()
        self.assertEqual(sum_valid_pages(self.test_rules, self.test_sections), (143,123))


def run_tests():  # runing test module for exec module
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPrintQueue)  # change xyz to test case
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple
                