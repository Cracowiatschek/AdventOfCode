from itertools import product

name: str = "Day 7: Bridge Repair"


def init_data(path):  # function for create input/test dataset
    return open(path, 'r').read().split("\n")


def read_data(data:list[str]) -> list[int,list[int]]:
    output: list = []
    for row in data:
        output.append([int(row.split(': ')[0]), [int(i) for i in row.split(': ')[1].split(' ')]])

    return output

def evaluate_data(expected_result: int, numbers: list[int]) -> bool:
    operators = ['*', '+']
    operator_combinations = product(operators, repeat=len(numbers) - 1)

    for ops in operator_combinations:
        result: int = numbers[0]
        for num, op in zip(numbers[1:], ops):
            result = eval(f"{result} {op} {num}")
        if expected_result == result:
            return True
    return False


def count_valid_lists(input_data: list[int,list[int]]) -> int:
    is_valid: int = 0
    for i in input_data:
        result = evaluate_data(i[0], i[1])
        if result is True:
            is_valid += 1
    return is_valid

def output(data: list[str]) -> tuple:  # get solution outputs for framework

    solution_1: int = count_valid_lists(read_data(data))
    solution_2: int = 0

    return solution_1, solution_2  # change variables to correct
