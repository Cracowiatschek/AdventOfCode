import re

name: str = "Day 3: Mull It Over"


class MemoryScanner:
    def __init__(self):
        self.memory_content: list[tuple[int,int]] = []  #initialize input data
        self.sum_of_multiplication: int = 0  #initialize result

    def read_data(self, data: list[str]) -> None: # get data about multiplication pairs
        whole_string: str = "".join(data)
        multiplication_operations: list[str] = re.findall("mul\(\d+,\d+\)", whole_string)
        multiplication_digits: list = [(int(digit[0]), int(digit[1])) for digit in [
            (re.findall("\d+", i)) for i in multiplication_operations
        ]]

        self.memory_content = multiplication_digits

    @staticmethod
    def trim_data(data: list[str]) -> list[str]:  # trim data to part two where data between dont and do are useless
        whole_string: str = "".join(data)

        all_do_items: list[int] = [i.span()[1] for i in re.finditer("do\(\)", whole_string)]  # get all do
        all_dont_items: list[int] = [i.span()[0] for i in re.finditer("don't\(\)", whole_string)]  # get all dont

        cache: list[str] = []  #initialize cache for result

        paris_of_exclusion: list[tuple[int,int]] = []  # initialize pairs for exclusion from whole_string

        for dont in all_dont_items:  #get pairs of exclusion
            next_do: int = len(whole_string)  # set up last index
            try:
                next_do: int = min([do for do in all_do_items if do >= dont])  # get range if "dont" isn't last item
            except Exception as e:
                print(e)

            paris_of_exclusion.append((dont, next_do))

            if next_do == len(whole_string): # brake useless calculations
                break

        last_idx: int = 0  # set up start index to exclusion

        for exclusion_pair in paris_of_exclusion:  # exclude fragments from whole string
            cache.append(whole_string[last_idx: exclusion_pair[0]])  # send necessary fragment to cache
            last_idx = exclusion_pair[1]  # update start index to exclusion
        cache.append(whole_string[last_idx:]) # send last fragment to cache
        whole_string = "".join(cache)  # materialize new string

        return [whole_string]


    def get_sum_of_multiplication(self) -> None: # get multiplication result
        for i in self.memory_content:
            self.sum_of_multiplication += i[0] * i[1]

    def set_default_values(self):  # reset values in class
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
# print(output(data))