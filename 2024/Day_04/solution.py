
name: str = "Day 4: Ceres Search"

def crossword_puzzle(puzzle: list[str]) -> int:
    xmas_count: int = 0

    directions: dict[int,dict[str,list[int]]] = {
        0: {"row": [0, 1, 2, 3], "column": [0, 0, 0, 0]},
        1: {"row": [0, 0, 0, 0], "column": [0, 1, 2, 3]},
        2: {"row": [0, 1, 2, 3], "column": [0, 1, 2, 3]},
        3: {"row": [0, 1, 2, 3], "column": [3, 2, 1, 0]}
    }

    for row_id, row_val in enumerate(puzzle):
        for col_id, col_val in enumerate(row_val):
            string_to_check: list[str] = []

            for direct in directions:
                try:
                    string_to_check.append("".join([
                        puzzle[row_id + directions[direct]["row"][0]][col_id + directions[direct]["column"][0]],
                        puzzle[row_id + directions[direct]["row"][1]][col_id + directions[direct]["column"][1]],
                        puzzle[row_id + directions[direct]["row"][2]][col_id + directions[direct]["column"][2]],
                        puzzle[row_id + directions[direct]["row"][3]][col_id + directions[direct]["column"][3]]
                    ]))
                except Exception as e:
                    pass

            for string in string_to_check:

                revers_string: str = string[::-1]

                if "XMAS" in [string,revers_string]:
                    xmas_count += 1

    return xmas_count

def find_x_mas(puzzle:list[str]) -> int:
    x_mas_count: int = 0
    find_x:list[str] = ["MMASS", "MSAMS"]
    for row_id, row_val in enumerate(puzzle):
        for col_id, col_val in enumerate(row_val):
            string_to_check: str = ""
            try:
                string_to_check = "".join([
                    puzzle[row_id][col_id],
                    puzzle[row_id][col_id+2],
                    puzzle[row_id+1][col_id+1],
                    puzzle[row_id+2][col_id],
                    puzzle[row_id+2][col_id+2]
                ])
            except Exception as e:
                pass

            for x in find_x:
                if x in [string_to_check, string_to_check[::-1]]:
                    x_mas_count += 1

    return x_mas_count


def output(data: list[str]) -> tuple:  # get solution outputs for framework

    solution_1: int = crossword_puzzle(data)
    solution_2: int = find_x_mas(data)

    return solution_1, solution_2  # change variables to correct
