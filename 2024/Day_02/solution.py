
name: str = "Day 2: Red-Nosed Reports"

class RedNosedReports:
    def __init__(self):
        self.reports: dict[int:list[int]] = {}
        self.safe_reports: list[int] = []
        self.safe_reports_non_restrict: list[int] = []


    def data_reader(self, input_data: list[str]) -> None:
        for report, content in enumerate(input_data):
            self.reports[report] = [int(i) for i in content.split(' ')]


    @staticmethod
    def check_safety_report(report: list[int]) -> bool:

        unsafety_indicator: bool = True # initialize simple unsafety indicator

        is_increasing = [report[i] <= report[i+1] for i in range(len(report)-1)]  #check descending or ascending
        is_decreasing = [report[i] >= report[i+1] for i in range(len(report)-1)]

        if all(is_increasing) or all(is_decreasing):  # get simple indicator
            for i in range(len(report)-1):
                diff = report[i+1] - report[i]
                if 1 > abs(diff) or abs(diff) > 3:
                    unsafety_indicator = False
        else:
            unsafety_indicator = False

        return unsafety_indicator


    def check_all_reports(self) -> None:
        for i in self.reports:  # check safty all reports
            safety_result: bool = self.check_safety_report(report = self.reports[i])
            if safety_result is True: # update safety lists
                self.safe_reports.append(i)


def output(data: list[str]) -> tuple:  # get solution outputs for framework

    reports_machine = RedNosedReports()
    reports_machine.data_reader(data)
    reports_machine.check_all_reports()
    solution_1: int = len(reports_machine.safe_reports)
    solution_2: int = len(reports_machine.safe_reports_non_restrict)

    return solution_1, solution_2
                