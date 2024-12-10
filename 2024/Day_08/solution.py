
name: str = "Day 8: Resonant Collinearity"

def init_data(path):  # function for create input/test dataset
    return open(path, 'r').read().split("\n")


def read_data(data):
    ranges: tuple = ()
    maps = {}

    for row_id, row in enumerate(data):
        for column_id, cell in enumerate(row):
            if cell != ".":

                if cell not in maps:
                    maps[cell] = [[row_id,column_id]]
                else:
                    maps[cell].append([row_id, column_id])
            ranges = (row_id, column_id)
    return maps, ranges


def build_antinodes(maps, ranges):
    antinodes: set = set()

    for frequencies in maps:
        for send_antenna in range(len(maps[frequencies])):
            for receive_antenna in range(send_antenna+1, len(maps[frequencies])):
                x_difference: int = maps[frequencies][receive_antenna][0] - maps[frequencies][send_antenna][0]
                y_difference: int = maps[frequencies][receive_antenna][1] - maps[frequencies][send_antenna][1]

                antinode_1 = (maps[frequencies][send_antenna][0] - x_difference, maps[frequencies][send_antenna][1]-y_difference)
                antinode_2 = (maps[frequencies][receive_antenna][0] + x_difference, maps[frequencies][receive_antenna][1]+y_difference)
                for i in [antinode_1, antinode_2]:
                    if 0 <= i[0] <= ranges[0] and 0 <= i[1] <= ranges[1]:
                        antinodes.add(i)
    return len(antinodes)


def build_many_antinodes(maps, ranges):
    antinodes: set = set()

    for frequencies in maps:
        for send_antenna in range(len(maps[frequencies])):
            for receive_antenna in range(send_antenna+1, len(maps[frequencies])):
                x_difference: int = maps[frequencies][receive_antenna][0] - maps[frequencies][send_antenna][0]
                y_difference: int = maps[frequencies][receive_antenna][1] - maps[frequencies][send_antenna][1]
                antinodes_cache = []
                antinode = (
                maps[frequencies][send_antenna][0]-x_difference, maps[frequencies][send_antenna][1]-y_difference)
                if 0 <= antinode[0] <= ranges[0] and 0 <= antinode[1] <= ranges[1]:
                    antinodes_cache.append(antinode)
                    while True:
                        x = antinode[0] - x_difference
                        y = antinode[1] - y_difference
                        if 0 <= x <= ranges[0] and 0 <= y <= ranges[1]:
                            antinode = (antinode[0] - x_difference, antinode[1]-y_difference)
                            antinodes_cache.append(antinode)
                        else:
                            break
                antinode = (maps[frequencies][receive_antenna][0] + x_difference, maps[frequencies][receive_antenna][1]+y_difference)
                if 0 <= antinode[0] <= ranges[0] and 0 <= antinode[1] <= ranges[1]:
                    antinodes_cache.append(antinode)
                    while True:
                        x = antinode[0] + x_difference
                        y = antinode[1] + y_difference
                        if 0 <= x <= ranges[0] and 0 <= y <= ranges[1]:
                            antinode = (antinode[0] + x_difference, antinode[1]+y_difference)
                            antinodes_cache.append(antinode)
                        else:
                            break
                for i in antinodes_cache:
                    antinodes.add(i)
        for i in maps:
            if len(maps[i]) > 1:
                for j in maps[i]:
                    antinodes.add(tuple(j))
    return len(antinodes)


def output(data: list[str]) -> tuple:  # get solution outputs for framework
    # solution body
    maps = read_data(data)
    solution_1: int = build_antinodes(maps[0], maps[1])
    solution_2: int = build_many_antinodes(maps[0], maps[1])
    return solution_1, solution_2  # change variables to correct
