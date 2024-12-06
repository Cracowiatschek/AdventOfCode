import datetime

name: str = "Day 6: Guard Gallivant"

def init_data(path):  # function for create input/test dataset
    return open(path, 'r').read().split("\n")

matrix: dict = {}

def create_matrix(data: list[str]) -> None:
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            matrix[(x, y)] = cell

create_matrix(init_data("input.in"))


def get_position(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a+b for a,b in zip(x,y))

directions: list[tuple[int,int]] = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def count_available_positions(matrix, directions:list[tuple[int,int]]):
    cache = set()
    actual_position: tuple[int, ...] = [i for i, j in matrix.items() if j == "^"][0]
    cache.add(actual_position)
    movement = 0

    while True:
        new_position: tuple = get_position(actual_position, directions[movement])
        cache.add(actual_position)
        if  new_position in matrix and matrix[new_position] != '#':
            actual_position = new_position
        else:
            new_position = get_position(actual_position, directions[(movement+1) % 4])
            if new_position in matrix and matrix[new_position] != '#':
                movement: int = (movement + 1) % 4
                actual_position = get_position(actual_position, directions[movement])
            else:
                break
    print(len(cache))

print(datetime.datetime.now())
count_available_positions(matrix, directions)
print(datetime.datetime.now())

def output(data: list[str]) -> tuple:  # get solution outputs for framework
    # solution body
    solution_1: int = 0
    solution_2: int = 0

    return solution_1, solution_2  # change variables to correct
                