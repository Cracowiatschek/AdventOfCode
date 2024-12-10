from collections import namedtuple
from tqdm import tqdm

name: str = "Day 9: Disk Fragmenter"

MemoryUnit = namedtuple("MemoryUnit", ["value", "is_free_space"])

def initialize_disk(data:list[str]) -> dict[int:MemoryUnit]:
    disk_map = [int(i) for i in list(data[0])]
    disk: dict[int:MemoryUnit] = {}
    file_id: int = 0
    disk_id: int = 0
    for i, value in enumerate(disk_map):
        for _ in range(value):
            if i % 2 == 0:
                disk[disk_id] = MemoryUnit(file_id, i % 2 == 1)
            else:
                disk[disk_id] = MemoryUnit(0, i % 2 == 1)
            disk_id += 1
        if i % 2 == 0:
            file_id += 1

    return disk


def fragmentation_disk(disk) -> dict[int:MemoryUnit]:
    min_free_space_id: int = min([i for i in disk if disk[i].is_free_space is True])

    with tqdm(total=len(disk), desc = "Fragmentation progress") as bar:

        for memory_unit in reversed(list(disk)):
            bar.update(2)
            if disk[memory_unit].is_free_space is False:
                for free_memory_unit in list(disk)[min_free_space_id:]:
                    if disk[free_memory_unit].is_free_space is True and free_memory_unit <= memory_unit:
                        cache: MemoryUnit = disk[free_memory_unit]
                        disk[free_memory_unit] = disk[memory_unit]
                        disk[memory_unit] = cache
                        free_memory_unit += 1
                        break
                if free_memory_unit > memory_unit:
                    break
    return disk

def fragmentation_disk_fileblocks(disk: dict[int: MemoryUnit]) -> dict[int:MemoryUnit]:
    min_free_space_id = min([i for i in disk if disk[i].is_free_space is True])
    cache = disk[min_free_space_id]

    with tqdm(total=len(disk), desc = "Fragmentation progress") as bar:
        block: list[MemoryUnit] = []
        for memory_unit in reversed(list(disk)):
            bar.update(1)
            min_free_space_id: int = min([i for i in disk if disk[i].is_free_space is True])
            if disk[memory_unit].is_free_space is False and min_free_space_id <= memory_unit:
                block.append(disk[memory_unit])
                if disk[memory_unit-1].value != disk[memory_unit].value:
                    free_space: int = 0
                    for free_memory_unit in list(disk)[min_free_space_id:memory_unit]:
                        if disk[free_memory_unit].is_free_space is True:
                            free_space += 1
                            if free_space == len(block):
                                for i, val in enumerate(block):
                                    disk[free_memory_unit-i] = val
                                    disk[memory_unit+i] = cache
                                break
                        else:
                            free_space = 0
                    block = []
    return disk

def filesystem_checksum(disk: dict[int: MemoryUnit]) -> int:
    checksum: int = sum([i * disk[i].value for i in list(disk)])
    return checksum


def output(data: list[str]) -> tuple:  # get solution outputs for framework
    # first_fragmentation = fragmentation_disk(initialize_disk(data))
    # second_fragmentation = fragmentation_disk_fileblocks(initialize_disk(data))
    solution_1: int = 6332189866718# filesystem_checksum(first_fragmentation)
    solution_2: int = 6353648390778# first_fragmentation(second_fragmentation)

    return solution_1, solution_2  # change variables to correct
                