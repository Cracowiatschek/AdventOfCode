import datetime

name: str = "Day 6: Guard Gallivant"

def init_data(path):  # function for create input/test dataset
    return open(path, 'r').read().split("\n")

class GuardGallivant:
    def __init__(self):
        self.directions: list[tuple[int,int]] = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.matrix: dict[tuple[int, int],str] = {}
        self.movement: int = 0

    def create_matrix(self, data: list[str]) -> None:
        for y, row in enumerate(data):
            for x, cell in enumerate(row):
                self.matrix[(x, y)] = cell

    @staticmethod
    def get_position(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(a+b for a,b in zip(x,y))


    def count_available_positions(self):
        cache: set = set()
        actual_position: tuple[int, ...] = [i for i, j in self.matrix.items() if j == "^"][0]

        while True:
            new_position: tuple = self.get_position(actual_position, self.directions[self.movement])
            cache.add(actual_position)
            if new_position in self.matrix:
                if self.matrix[new_position] != '#':
                    actual_position = new_position
                else:
                    self.movement = (self.movement+1) % 4
            else:
                break

        return len(cache)


def output(data: list[str]) -> tuple:  # get solution outputs for framework

    guard = GuardGallivant()
    guard.create_matrix(data)
    print(guard.count_available_positions())

    solution_1: int = 0
    solution_2: int = 0

    return solution_1, solution_2  # change variables to correct

output(init_data("input.in"))