import re

name: str = "Day 3: Mull It Over"


class MemoryScanner:
    def __init__(self):
        self.memory_content: list[tuple[int,int]] = []
        self.sum_of_multiplication: int = 0

    def read_data(self, data: list[str]) -> None:
        whole_string: str = "".join(data)
        multiplication_operations: list[str] = re.findall("mul\(\d+,\d+\)", whole_string)
        multiplication_digits: list = [(int(digit[0]), int(digit[1])) for digit in [
            (re.findall("\d+", i)) for i in multiplication_operations
        ]]

        self.memory_content = multiplication_digits

    @staticmethod
    def trim_data(data: list[str]) -> list[str]:
        whole_string: list[str] = []
        for string in data:
            all_do_items: list[int] = [i.span()[1] for i in re.finditer("do\(\)", string)]
            all_dont_items: list[int] = [i.span()[0] for i in re.finditer("don\'t\(\)", string)]

            paris_of_exclusion: list[tuple[int,int]] = []


            for dont in all_dont_items:
                next_do: int = len(string)
                try:
                    next_do: int = min([do for do in all_do_items if do >= dont])
                except Exception as e:
                    print(e)
                paris_of_exclusion.append((dont, next_do))


            if max(all_dont_items) > max(all_do_items):
                paris_of_exclusion.append((max(all_dont_items), len(string)))

            for exclusion_pair in paris_of_exclusion:
                exclusion: str = string[exclusion_pair[0]: exclusion_pair[1]]
                string = string.replace(exclusion, "")
            whole_string.append(string)

        return whole_string

    def get_sum_of_multiplication(self) -> None:
        for i in self.memory_content:
            self.sum_of_multiplication += i[0] * i[1]

    def set_default_values(self):
        self.memory_content = []
        self.sum_of_multiplication = 0



def output(data: list[str]) -> tuple:  # get solution outputs for framework

    memory_scanner = MemoryScanner()

    memory_scanner.read_data(data)
    memory_scanner.get_sum_of_multiplication()

    solution_1: int = memory_scanner.sum_of_multiplication

    memory_scanner.set_default_values()
    trim_data: list[str] = memory_scanner.trim_data(data)
    memory_scanner.read_data(trim_data)
    memory_scanner.get_sum_of_multiplication()

    solution_2: int = memory_scanner.sum_of_multiplication

    return solution_1, solution_2  # change variables to correct
