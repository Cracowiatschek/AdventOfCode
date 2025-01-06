
from collections import namedtuple
from dataclasses import dataclass

import sympy.core.numbers
from sympy import symbols, Eq, solve

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


def cost_solver(machines_set, correct_factor: int):
    result: int = 0
    for game in machines_set:
        a: Button = game.buttons[0]
        b: Button = game.buttons[1]
        prize: Prize = Prize(X = game.prize.X + correct_factor, Y = game.prize.Y + correct_factor)
        x, y = symbols("x y")

        eq1 = Eq(a.X * x + b.X * y, prize.X)
        eq2 = Eq(a.Y * x + b.Y * y, prize.Y)
        solution = solve((eq1, eq2), (x, y))
        press_a = solution.get(list(solution.keys())[0])
        press_b = solution.get(list(solution.keys())[1])

        if type(press_a) is sympy.core.numbers.Integer and type(press_b) is sympy.core.numbers.Integer:
            result += press_a * a.Cost + press_b * b.Cost
    return result

print(cost_solver(machines, 0))
print(cost_solver(machines, 10000000000000))




def output(data: list[str]) -> tuple:  # get solution outputs for framework
    # solution body
    solution_1: int = 0
    solution_2: int = 0

    return solution_1, solution_2  # change variables to correct
                