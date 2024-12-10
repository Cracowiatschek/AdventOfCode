
name: str = "Day 8: Resonant Collinearity"

def init_data(path):  # function for create input/test dataset
    return open(path, 'r').read().split("\n")


def read_data(data):
    ranges: tuple = ()
    maps = {}
    antennas_cache = []
    cache = []
    for row_id, row in enumerate(data):
        for column_id, cell in enumerate(row):
            if cell != ".":
                antennas_cache.append((row_id, column_id))
                if cell == "#":
                    cache.append([row_id, column_id])
                if cell not in maps:
                    maps[cell] = [[row_id,column_id]]
                else:
                    maps[cell].append([row_id, column_id])
            ranges = (row_id, column_id)
    return maps, antennas_cache, ranges, cache

x = read_data(init_data("input.in"))

def build_antinodes(maps, antennas_cache, ranges):
    antinodes: set = set()
    print(maps)
    for frequencies in maps:
        for send_antenna in range(len(maps[frequencies])):
            for receive_antenna in range(send_antenna+1, len(maps[frequencies])):
                x_difference: int = maps[frequencies][receive_antenna][0] - maps[frequencies][send_antenna][0]
                y_difference: int = maps[frequencies][receive_antenna][1] - maps[frequencies][send_antenna][1]

                antinode_1 = (maps[frequencies][send_antenna][0] - x_difference, maps[frequencies][send_antenna][1]-y_difference)
                antinode_2 = (maps[frequencies][receive_antenna][0] + x_difference, maps[frequencies][receive_antenna][1]+y_difference)
                for i in [antinode_1, antinode_2]:
                    if (0 <= i[0] <= ranges[0] and 0 <= i[1] <= ranges[1]
                            and len(maps[frequencies][receive_antenna])):
                        antinodes.add(i)
    return len(antinodes)

print(build_antinodes(x[0], x[1], x[2]))


def output(data: list[str]) -> tuple:  # get solution outputs for framework
    # solution body
    solution_1: int = 0
    solution_2: int = 0

    return solution_1, solution_2  # change variables to correct
                