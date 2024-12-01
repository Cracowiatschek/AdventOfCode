from typing import List, Dict

from fontTools.ttLib.tables.ttProgram import instructions

from solutionPrinter import solution_println as sp
from itertools import product


class Processor:

    def __init__(self):
        self.registers: dict[str,int] = {
            'a': 0,
            'b': 0
        }
        self.actual_instruction: int = 0
        self.instructions: dict = {}


    def read_data(self, path):
        data = open(path,'r').read().split("\n")
        for number, line in enumerate(data):
            data_items = line.split(" ")
            register = data_items[1][0]
            operation = data_items[0]
            if len(data_items) == 3:
                value = int(data_items[2])
                self.instructions[number] = {operation: [register, value]}
            else:
                self.instructions[number] = {operation: [register]}


    def half_value(self, register: str) -> None:
        self.registers[register] = int(max(self.registers[register]/2, 0))
        self.actual_instruction += 1


    def triple_value(self, register: str) -> None:
        self.registers[register] =  max(self.registers[register]*3, 0)
        self.actual_instruction += 1


    def increment_value(self, register:str) -> None:
        self.registers[register] += 1
        self.actual_instruction += 1


    def jump_instruction(self, instruction_value: int) -> None:
        self.actual_instruction += instruction_value


    def jump_instruction_even(self, instruction_value: int, register: str) -> None:
        register_value: int = self.registers[register]

        if register_value % 2 == 0:
            self.actual_instruction = instruction_value
        else:
            self.actual_instruction += 1


    def jump_instruction_odd(self, instruction_value: int, register: str) -> None:
        register_value: int = self.registers[register]

        if register_value % 2 != 0:
            self.actual_instruction += instruction_value
        else:
            self.actual_instruction += 1


    def calculate_instructions(self) -> None:

        while self.actual_instruction in list(self.instructions.keys()):
            instruction = self.instructions[self.actual_instruction]
            process = list(instruction.keys())[0]
            register: str = None

            try:
                register: str = list(instruction.items())[0][1][0]
            except Exception:
                value: int = int(list(instruction.items())[0][1][0])

            try:
                value: int = list(instruction.items())[0][1][1]
            except Exception:
                value: int = None
            print(instruction, register, value)

            if process == "inc":
                self.increment_value(register)
            elif process == "hlf":
                self.half_value(register)
            elif process == "tpl":
                self.triple_value(register)
            elif process == "jmp":
                self.jump_instruction(value)
            elif process == "jie":
                self.jump_instruction_even(value, register)
            elif process == "jio":
                self.jump_instruction_odd(value,register)

    def printer(self):
        print(f"a: {self.registers['a']}, b: {self.registers['b']}")


a = Processor()
a.read_data("input.in")
print(a.registers["a"])
a.calculate_instructions()
a.printer()