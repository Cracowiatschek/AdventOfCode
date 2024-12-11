from tqdm import tqdm

name: str = "Day 11: Plutonian Pebbles"

def init_data(path):  # function for create input/test dataset
    return open(path, 'r').read().split("\n")

def read_data(data: list[str]) -> list[int]:
    return list(map(int,data[0].split(' ')))
#
# def check_stone(stone: int) -> int or list[int]:
#     stone_str: str = str(stone)
#     if stone == 0:
#         return 1
#     elif len(stone_str) > 1 and  len(stone_str) % 2 == 0:
#         return int(stone_str[:len(stone_str)//2]), int(stone_str[len(stone_str)//2:])
#     else:
#         return stone * 2024

def blink(stones: list[int], blink_count: int) -> int:
    with tqdm(total = blink_count) as bar:
        for _ in range(blink_count):
            bar.update(1)
            stones_after_blink: list[int] = []
            for stone in stones:
                stone_str: str = str(stone)
                stone_len: int = len(stone_str)
                if stone == 0:
                    stones_after_blink.append(1)
                elif len(stone_str) > 1 and len(stone_str) % 2 == 0:
                    stones_after_blink.append(int(stone_str[:stone_len // 2]))
                    stones_after_blink.append(int(stone_str[stone_len // 2:]))
                else:
                    stones_after_blink.append(stone * 2024)
            stones = stones_after_blink.copy()
    return len(stones)

print(blink(read_data(init_data("input.in")), 25))
# print(blink(read_data(init_data("input.in")), 75))

def output(data: list[str]) -> tuple:  # get solution outputs for framework
    # solution body
    solution_1: int = 0
    solution_2: int = 0

    return solution_1, solution_2  # change variables to correct
                