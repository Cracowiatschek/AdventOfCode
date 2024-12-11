from tqdm import tqdm
from collections import Counter

name: str = "Day 11: Plutonian Pebbles"

def init_data(path):  # function for create input/test dataset
    return open(path, 'r').read().split("\n")

def read_data(data: list[str]) -> list[int]:
    return list(map(int,data[0].split(' ')))
#
def check_stone(stone: int) -> int or list[int]:
    if stone == 0:
        return [1]
    stone_str: str = str(stone)
    stone_len: int = len(stone_str)


    if stone_len % 2 == 0:
        stone_center: int = stone_len // 2
        return [int(stone_str[:stone_center]), int(stone_str[stone_center:])]

    return [stone * 2024]

def blink(stones: list[int], blink_count: int) -> int:
    cache: dict[int:int] = {}
    with tqdm(total = blink_count*len(stones)) as bar:
        for stone in stones:
            stone_cache: dict = {stone: 1}
            for _ in range(blink_count):
                bar.update(1)
                stones_after_blink: dict[int:int] = {}
                for cached_stone in stone_cache:
                    for i in check_stone(cached_stone):
                        if i in stones_after_blink:
                            stones_after_blink[i] += stone_cache[cached_stone]
                        else:
                            stones_after_blink[i] = stone_cache[cached_stone]
                stone_cache = stones_after_blink

            for cached_stone in stone_cache:
                if cached_stone in cache:
                    cache[cached_stone] += stone_cache[cached_stone]
                else:
                    cache[cached_stone] = stone_cache[cached_stone]
    result = [cache[i] for i in cache]
    return sum(result)


def output(data: list[str]) -> tuple:  # get solution outputs for framework
    # solution body
    solution_1: int = blink(read_data(data), 25)
    solution_2: int = blink(read_data(data), 75)

    return solution_1, solution_2  # change variables to correct
                