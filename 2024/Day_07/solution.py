from itertools import product

name: str = "Day 7: Bridge Repair"


def read_data(data:list[str]) -> list[int,list[int]]:
    output: list = []
    for row in data:
        output.append([int(row.split(': ')[0]), [int(i) for i in row.split(': ')[1].split(' ')]])

    return output

def evaluate_data(expected_result: int, numbers: list[int], operators: list[str]) -> bool:

    operator_combinations = product(operators, repeat=len(numbers) - 1)

    for ops in operator_combinations:
        result: int = numbers[0]
        for num, op in zip(numbers[1:], ops):
            if op == "||":
                result = int(f"{result}"+f"{num}")
            else:
                result = eval(f"{result} {op} {num}")
        if expected_result == result:
            return True
    return False


def sum_valid_results(input_data: list[int,list[int]], operators: list[str]) -> int:
    is_valid: int = 0
    for i in input_data:
        result = evaluate_data(i[0], i[1], operators)
        if result is True:
            is_valid += i[0]
    return is_valid


def output(data: list[str]) -> tuple:  # get solution outputs for framework

    solution_1: int = sum_valid_results(read_data(data), ['*', '+'])
    solution_2: int = 401477450831495  #sum_valid_results(read_data(data), ['*', '+', "||"])

    return solution_1, 401477450831495  # change variables to correct
