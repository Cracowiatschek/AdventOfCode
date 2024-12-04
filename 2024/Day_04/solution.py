
name: str = "Day 4: Ceres Search"


def init_data(path):  # function for create input/test dataset
    return open(path, 'r').read().split("\n")



puzzle = init_data("input.in")

def crossword_puzzle(puzzle: list[str]) -> int:
    xmas_count: int = 0
    for row_id, row_val in enumerate(puzzle):
        for col_id, col_val in enumerate(row_val):
            string_to_check: list[str] = []

            try:
                string_to_check.append("".join([row_val[col_id], row_val[col_id+1], row_val[col_id+2], row_val[col_id+3]]))
            except Exception as e:
                e = e

            try:
                string_to_check.append("".join([row_val[col_id], puzzle[row_id+1][col_id+1], puzzle[row_id+2][col_id+2], puzzle[row_id+3][col_id+3]]))
            except Exception as e:
                e = e

            try:
                string_to_check.append("".join([row_val[col_id], puzzle[row_id+1][col_id+1], puzzle[row_id+2][col_id+2], puzzle[row_id+3][col_id+3]]))
            except Exception as e:
                e = e

            try:
                string_to_check.append("".join([puzzle[row_id+3][col_id], puzzle[row_id+2][col_id], puzzle[row_id+1][col_id], row_val[col_id]]))
            except Exception as e:
                e = e

            for string in string_to_check:

                revers_string = string[::-1]

                if "XMAS" in [string,revers_string]:
                    xmas_count += 1
                    print([row_id,col_id],[string,revers_string], xmas_count)

    return xmas_count


print(crossword_puzzle(puzzle))
# def output(data: list[str]) -> tuple:  # get solution outputs for framework
#
#     # solution body
#
#     return a, b  # change variables to correct
#