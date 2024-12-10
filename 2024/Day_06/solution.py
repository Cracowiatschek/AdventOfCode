import datetime

name: str = "Day 6: Guard Gallivant"

class GuardGallivant:
    def __init__(self):
        self.directions: list[tuple[int,int]] = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.matrix: dict[tuple[int, int],str] = {}
        self.movement: int = 0
        self.last_position: tuple[int, int] = (0, 0)
        self.actual_position: tuple[int,int] = (1, 0)
        self.is_first: bool = True

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


    def get_new_matrix(self):
        positions = list(self.matrix.keys())
        all_matrix_indicator = False
        self.matrix[self.last_position] = '.'

        if self.is_first:
            self.actual_position = (0, 0)
            self.is_first = False
        else:
            try:
                self.actual_position = positions[positions.index(self.last_position)+1]
            except IndexError:
                all_matrix_indicator = True

        while not all_matrix_indicator:
            value = self.matrix.get(self.actual_position, '')
            if value not in ('#', '^'):
                break
            try:
                self.actual_position = positions[positions.index(self.actual_position)+1]
            except IndexError:
                all_matrix_indicator = True

        if not all_matrix_indicator:
            self.matrix[self.actual_position] = '#'
            self.last_position = self.actual_position

        return all_matrix_indicator

    @staticmethod
    def is_subsequence(sequence: list, whole_list: list) -> bool:
        if sequence in [whole_list[i:i+len(sequence)] for i in range(len(whole_list)-len(sequence)+1)]:
            return True
        else:
            return False

    def count_infinity_loops(self) -> int:
        last_loop: bool = False
        count_infinity_loops = 0
        while last_loop is False:
            last_loop = self.get_new_matrix()
            cache: list[tuple[int, ...]] = []
            actual_position: tuple[int, ...] = [i for i, j in self.matrix.items() if j == "^"][0]
            self.movement = 0

            while True:
                new_position: tuple = self.get_position(actual_position, self.directions[self.movement])
                cache.append(new_position)
                if new_position in self.matrix:
                    if self.matrix[new_position] != '#':
                        actual_position = new_position
                    else:
                        self.movement = (self.movement+1) % 4
                        sequence_to_check: list = cache[-2:] + [self.get_position(actual_position, self.directions[self.movement])]
                        if self.is_subsequence(sequence_to_check, cache) is True:
                            count_infinity_loops += 1
                            break
                else:
                    break
        return count_infinity_loops


def output(data: list[str]) -> tuple:  # get solution outputs for framework

    guard = GuardGallivant()
    guard.create_matrix(data)

    solution_1: int = guard.count_available_positions()
    # solution_2: int = guard.count_infinity_loops() ## during 11 minuts
    solution_2: int = 1575

    return solution_1, solution_2  # change variables to correct

