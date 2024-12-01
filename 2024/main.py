import pathlib
import sys
from pathlib import Path
from rich.console import Console
from rich.table import Table


def init_data(path):  # function for create input/test dataset
    return open(path, 'r').read().split("\n")


def solver():

    scoreboard: dict[str: dict] = {}  # initialize scoreboard/result_board for my solutions
    base_path = Path(".")  # initialize local path

    for solution_file in base_path.rglob("solution.py"):  # iterate all challenge solutions dirs
        test_path: pathlib.WindowsPath = solution_file.parent / "test.py"  # init all important paths for tests and get solution
        sample_path: pathlib.WindowsPath = solution_file.parent / "sample.in"
        input_path: pathlib.WindowsPath = solution_file.parent / "input.in"

        if not test_path.exists() and not sample_path.exists() and not input_path.exists():  # check exists of all files
            continue

        test_data = init_data(sample_path)  # get test data from file

        try:
            sys.path.append(str(solution_file.parent))  # get path to solution file for tests

            with open(test_path, "r") as test:
                test_code: str = test.read()  # initialize tests code

                test_vars: dict[str: None] = {"data": test_data, "solution": __import__("solution")}  # initialize local variables for tests

                exec(test_code, test_vars)  # execute test file

                if 'run_tests' in test_vars: # get tests result
                    test_result, test_result_bool = test_vars['run_tests']()

                    if not test_result_bool:
                        print(f"Tests failed: {test_result.failures}")  # get information about test failures
                    else: # if everything is okay, run solution
                        try:
                            with open(solution_file, 'r') as solution:
                                solution_code: str = solution.read()  # initialize solution code
                                input_data = init_data(input_path)  # initialize challenge data

                                solution_vars: dict[str: None] = {"data": input_data}  # initialize local variables for solution file
                                exec(solution_code, solution_vars)  # execute solution file

                                result = solution_vars["output"](input_data)  # get solution of challenge
                                scoreboard[solution_vars["name"]] = {"part one": result[0], "part_two": result[1]}  # add solutions to scoreboard

                        except Exception as e:
                            print("It's edge case. Your error: \n")  # get information about my edge case input


        except Exception as e:
            print(f"Error executing test: {e}")  # get information about errors in tests

    return scoreboard  # return my scoreboard for rendering


def score_board_render(scoreboard: dict[str:dict]):
    table = Table(title = "Advent of Code 2024: Results")  # initialize header of solution board

    table.add_column("Challenge", justify = "center", style = "cyan", no_wrap = True)  # initialize headers of all columns
    table.add_column("Part one answer", justify = "center", style = "green")
    table.add_column("Part two answer", justify = "center", style = "magenta")

    for challenge, answers in scoreboard.items(): # add rows to table of results
        table.add_row(
            challenge,
            str(answers.get("part one", "N/A")),
            str(answers.get("part_two", "N/A")),
        )

    console = Console()
    console.print(table)  # render table at console


score_board_render(scoreboard = solver()) # get and print solutions
