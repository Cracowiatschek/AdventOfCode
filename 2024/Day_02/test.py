
import unittest
from solution import output, RedNosedReports

red_nosed_reports = RedNosedReports()

class TestRedNosedReports(unittest.TestCase):
    def test_data_parser(self):
        red_nosed_reports.read_data(data)
        self.assertEqual(red_nosed_reports.reports, {0:[7,6,4,2,1], 1:[1,2,7,8,9],2:[9,7,6,2,1],3:[1,3,2,4,5],
                                                     4:[8,6,4,4,1],5:[1,3,6,7,9]})

    def test_check_safety_report_positive_asc(self):
        test_positive_list: list[int] = [1,2,3,4,5]
        result: bool = red_nosed_reports.check_safety_report(test_positive_list)
        self.assertEqual(result, True)

    def test_check_safety_report_positive_desc(self):
        test_positive_list: list[int] = [5, 4, 3, 2, 1]
        result: bool = red_nosed_reports.check_safety_report(test_positive_list)
        self.assertEqual(result, True)

    def test_check_safety_report_negative_desc(self):
        test_negative_list: list[int] = [1, 2, 3, 2, 5]
        result: bool = red_nosed_reports.check_safety_report(test_negative_list)
        self.assertEqual(result, False)

    def test_check_safety_report_negative_const(self):
        test_negative_list: list[int] = [1, 2, 3, 3, 5]
        result: bool = red_nosed_reports.check_safety_report(test_negative_list)
        self.assertEqual(result, False)

    def test_check_safety_report_negative_asc(self):
        test_negative_list: list[int] = [1, 2, 3, 9, 5]
        result: bool = red_nosed_reports.check_safety_report(test_negative_list)
        self.assertEqual(result, False)

    def test_part_one_all_safety_reports(self):
        red_nosed_reports.check_all_reports()
        self.assertEqual(len(red_nosed_reports.safe_reports), 2)

    def test_part_two_all_safety_reports(self):
        self.assertEqual(len(red_nosed_reports.safe_reports_non_restrict), 4)


def run_tests():  # runing test module for exec module
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRedNosedReports)  # change xyz to test case
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple
                