import pathlib
import sys
from pathlib import Path
from rich.console import Console
from rich.table import Table


def init_data(path):
    return open(path, 'r').read().split("\n")


def solver():

    scoreboard: dict[str: dict] = {}
    base_path = Path(".")

    for solution_file in base_path.rglob("solution.py"):
        test_path: pathlib.WindowsPath = solution_file.parent / "test.py"
        sample_path: pathlib.WindowsPath = solution_file.parent / "sample.in"
        input_path: pathlib.WindowsPath = solution_file.parent / "input.in"

        if not test_path.exists() and not sample_path.exists() and not input_path.exists():
            continue

        sample_data = init_data(sample_path)

        try:
            sys.path.append(str(solution_file.parent))

            with open(test_path, "r") as test:
                test_code: str = test.read()

                test_vars: dict[str: None] = {"data": sample_data, "solution": __import__("solution")}

                exec(test_code, test_vars)

                if 'run_tests' in test_vars: # Run tests
                    test_result, test_result_bool = test_vars['run_tests']()

                    if not test_result_bool:
                        print(f"Tests failed: {test_result.failures}")
                    else:
                        try:
                            with open(solution_file, 'r') as solution:
                                solution_code: str = solution.read()
                                input_data = init_data(input_path)

                                solution_vars: dict[str: None] = {"data": input_data}
                                exec(solution_code, solution_vars)

                                result = solution_vars["output"](input_data)
                                scoreboard[solution_vars["name"]] = {"part one": result[0], "part_two": result[1]}

                        except Exception as e:
                            print("It's edge case. Your error: \n")


        except Exception as e:
            print(f"Error executing test: {e}")

    return scoreboard


def score_board_render(scoreboard: dict[str:dict]):
    table = Table(title = "Challenge Results")

    table.add_column("Challenge", justify = "center", style = "cyan", no_wrap = True)
    table.add_column("Part one answer", justify = "center", style = "green")
    table.add_column("Part two answer", justify = "center", style = "magenta")

    for challenge, answers in scoreboard.items():
        table.add_row(
            challenge,
            str(answers.get("part one", "N/A")),
            str(answers.get("part_two", "N/A")),
        )

    console = Console()
    console.print(table)


score_board_render(scoreboard = solver())
