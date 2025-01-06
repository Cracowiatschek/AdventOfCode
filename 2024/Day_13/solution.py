
from collections import namedtuple
from dataclasses import dataclass

name: str = "Day 13: Claw Contraption"

dt: list[str] = open("input.in", 'r').read().split("\n")


Button = namedtuple("Button", ["X", "Y", "Cost"])
Prize = namedtuple("Prize", ["X", "Y"])


@dataclass
class Machine:
    buttons: list[Button]
    prize: Prize


def read_data(data: list[str]) -> list[Machine]:

    machines = []
    buttons: list[Button] = []

    for row in data:
        meta: list[str] = row.split(" ")

        if "A:" in meta or "B:" in meta:
            x: int = int(meta[-2].split('+')[1][:-1])
            y: int = int(meta[-1].split('+')[1])
            cost: int = 1

            if "A:" in meta:
                cost = 3
                buttons.append(Button(X = x, Y = y, Cost = cost))
            else:
                buttons.append(Button(X = x, Y = y, Cost = cost))

        if "Prize:" in meta:
            x: int = int(meta[-2].split('=')[1][:-1])
            y: int = int(meta[-1].split('=')[1])
            machines.append(Machine(buttons = buttons, prize = Prize(X = x, Y = y)))
            buttons = []

    return machines

machines = read_data(dt)

def cost_calculator(machines_set, correct_factor: int):
    result: int = 0
    for game in machines_set:
        cost: list[int] = []
        a: Button = game.buttons[0]
        b: Button = game.buttons[1]
        prize: Prize = Prize(X = game.prize.X + correct_factor, Y = game.prize.Y + correct_factor)
        push_a: int = -1

        while push_a < 100:
            push_a += 1
            x: int = 0
            y: int = 0
            x += a.X * push_a
            y += a.Y * push_a

            b_x: int = (prize.X - x) // b.X
            b_y: int = (prize.Y - y) // b.Y

            mod_x: int = (prize.X-x) % b.X
            mod_y: int = (prize.Y-y) % b.Y

            if b_x == b_y and mod_y + mod_x == 0:
                cost.append(push_a * a.Cost + b_x * b.Cost)

        if len(cost) > 0:
            result += min(cost)
    return result

print(cost_calculator(machines, 0))

print(cost_calculator(machines, 10000000000000))




def output(data: list[str]) -> tuple:  # get solution outputs for framework
    # solution body
    solution_1: int = 0
    solution_2: int = 0

    return solution_1, solution_2  # change variables to correct
                