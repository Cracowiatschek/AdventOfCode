
name: str = "Day 10: Hoof It"

def create_map(data: list[str]) -> list[list[int]]:
    ready_map: list[list[int]] = []
    for row in data:
        ready_map.append([int(i) for i in row])
    return ready_map


def generate_paths(actual_path: list[tuple[int,int]], length: int):
    if len(actual_path) == length:
        yield tuple(actual_path)
        return

    last_direction = actual_path[-1] if actual_path else None
    available_directions = {
        (0, -1): [(0, -1), (1, 0), (-1, 0)],
        (0, 1): [(0, 1), (1, 0), (-1, 0)],
        (-1, 0): [(-1, 0), (0, -1), (0, 1)],
        (1, 0): [(1, 0), (0, -1), (0, 1)],
        None: [(0, -1), (0, 1), (-1, 0), (1, 0)],
    }

    for direction in available_directions[last_direction]:
        yield from generate_paths(actual_path+[direction], length)


def find_start_positions(ready_map: list[list[int]]) -> list[tuple[int,int]]:
    start_positions: list[tuple[int,int]] = []
    for row, value in enumerate(ready_map):
        for column, height in enumerate(value):
            if height == 0:
                start_positions.append((row,column))
    return start_positions


def create_path(trim_map: list[list[int]], start_position: list[int], path: list[tuple[int,int]]) :
    cache: list[int] = [0]
    path_result: list[tuple[int,int]] = [(start_position[0], start_position[1])]
    x, y = start_position[0], start_position[1]
    try:
        for direction in path:
            x += direction[0]
            y += direction[1]
            if trim_map[x][y] == cache[-1]+1 and x >= 0 and y >= 0:
                cache.append(trim_map[x][y])
                path_result.append((x,y))
            else:
                break
    except:
        pass
    if len(cache) == 10:
        return {"result":True, "start": path_result[0], "end":path_result[-1], "data": path_result}
    else:
        return {"result": False}


def count_paths(ready_map: list[list[int]], start_positions: list[tuple[int, int]]) -> tuple[int,int]:
    rows: int = len(ready_map)
    columns: int = len(ready_map[0])
    paths_calculation: object = generate_paths([], 10)
    paths: list = list(set(path for i, path in enumerate(paths_calculation) if len(path) == 10))
    result: int = 0
    count_unique_paths = 0

    for position in start_positions:
        min_row: int = max(0, position[0]-19)
        max_row: int = min(rows, position[0]+19)
        min_column: int = max(0, position[1]-19)
        max_column: int = min(columns, position[1]+19)
        maps: list[list[int]]= [row[min_column:max_column] for row in ready_map[min_row:max_row]]
        new_position: list[int] = [position[0]-min_row, position[1]-min_column]
        endpoints: set = set()
        unique_paths: set = set()
        for path in paths:
            path_result = create_path(maps, new_position, path)
            if path_result["result"] is True:
                endpoints.add((path_result["start"], path_result["end"]))
                unique_paths.add(tuple(path_result["data"]))

        result += len(endpoints)
        count_unique_paths += len(unique_paths)

    return result, count_unique_paths


def output(data: list[str]) -> tuple:  # get solution outputs for framework
    ready_map = create_map(data)
    calculations = count_paths(ready_map, find_start_positions(ready_map))
    solution_1: int = calculations[0]
    solution_2: int = calculations[1]

    return solution_1, solution_2  # change variables to correct
                