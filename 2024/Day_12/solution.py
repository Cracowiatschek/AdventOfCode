from collections import namedtuple
from functools import cache
import time

from numpy.testing.print_coercion_tables import print_new_cast_table
from rich.cells import cached_cell_len

name: str = "Day 12: Garden Groups"

def init_data(path):  # function for create input/test dataset
    return open(path, 'r').read().split("\n")

def read_data(data: list[str]):
    plots: dict[str:dict] = {}
    for row_id, row in enumerate(data):
        for column_id, cell in enumerate(row):
            if cell in plots:
                plots[cell].append((row_id, column_id))
            else:
                plots[cell] = [(row_id, column_id)]
    return plots


def group_by_adjacency(points: list):
    points_set: set = set(points)  # Zbiór punktów dla szybkiego dostępu
    visited: set = set()          # Zbiór odwiedzonych punktów
    groups: list[list] = []              # Lista grup

    # Funkcja BFS do znajdowania komponentów spójnych
    def breadth_first_search (start)-> list:
        queue:list = [start]
        group:list = []
        while queue:
            point: tuple = queue.pop(0)
            if point in visited:
                continue
            visited.add(point)
            group.append(point)
            row_id, column_id = point
            # Sprawdź sąsiednie punkty
            neighbors = [(row_id + 1, column_id), (row_id - 1, column_id), (row_id, column_id + 1), (row_id, column_id - 1)]
            for neighbor in neighbors:
                if neighbor in points_set and neighbor not in visited:
                    queue.append(neighbor)
        return group

    # Znajdowanie wszystkich grup
    for point in points:
        if point not in visited:
            groups.append(breadth_first_search(point))

    return groups


def count_edges(plot: list[tuple[int, int]]) -> tuple[int, int]:
    edges: int = 0
    visited: set = set()

    for row_id, column_id in plot:
        # Sprawdź sąsiedztwo w poziomie i pionie
        if (row_id + 1, column_id) not in plot:  # W dół
            visited.add((row_id+1, column_id))
            edges += 1
        if (row_id, column_id + 1) not in plot:  # W prawo
            visited.add((row_id, column_id+1))
            edges += 1
        if (row_id - 1, column_id) not in plot:  # W dół
            visited.add((row_id-1, column_id))
            edges += 1
        if (row_id, column_id - 1) not in plot:  # W prawo
            visited.add((row_id, column_id-1))
            edges += 1
    print(sorted(visited))
    return edges,0


def get_price(plots: dict) -> tuple[int, int]:
    total_price: int = 0
    discount = 0
    for plot in plots:
        sub_plots: list[list] = group_by_adjacency(plots[plot])
        for sub in sub_plots:
            # print(get_position(sub))
            val = count_edges(sub)
            total_price += len(sub) * val[0]
            discount += len(sub) * val[1]

    return total_price, discount


# d = read_data(init_data("sample.in"))


# print(get_price(d))
def output(data: list[str]) -> tuple:  # get solution outputs for framework
    # solution body
    solution_1: int = 0
    solution_2: int = 0

    return solution_1, solution_2  # change variables to correct
                