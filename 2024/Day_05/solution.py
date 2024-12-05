from collections import namedtuple, defaultdict,deque
from itertools import permutations

from requests.utils import is_valid_cidr

name: str = "Day 5: Print Queue"

Rule = namedtuple("Rule",["right","left"])
Section = namedtuple("Section", ["values", "is_valid"])


def read_rules(data: list[str]) -> list[Rule]: # get rules in Rule objects
    rules: list[Rule] = []
    for row in data:
        if row == '' :
            break
        else:
            pages: list[str] = row.split('|')
            rules.append(Rule(int(pages[0]),int(pages[1])))

    return rules


def read_sections(data: list[str]) -> list[Section]: # get sections in Section objects
    sections: list[Section] = []
    start_reading: bool = False
    for row in data:
        if start_reading is True:
            sections.append(Section(values=[int(i) for i in row.split(',')], is_valid = True))

        if row == '':
            start_reading = True

    return sections


def validation(rules: list[Rule], section: list[int]) -> bool:  # validation of compliance rules
    is_valid: bool = True
    for rule in rules:
        if rule.right in section and rule.left in section:
            index_right: int = section.index(rule.right)
            index_left: int = section.index(rule.left)

            if index_right > index_left:
                is_valid = False

    return is_valid

def correction(rules: list[Rule], section: list[int]) -> list[int]:  # matching the rules
    is_valid: bool = False
    while is_valid is False:
        temp_valid: bool = True
        for rule in rules:
            if rule.right in section and rule.left in section:
                index_right: int = section.index(rule.right)
                index_left: int = section.index(rule.left)

                if index_right > index_left:
                    temp_valid = False
                    section[index_right] = rule.left
                    section[index_left] = rule.right
        if temp_valid is True:
            is_valid = True
    return section


def sum_valid_pages(rules: list[Rule], sections: list[Section]) -> tuple[int,int]:  # get results
    valid_pages_sum: int = 0
    invalid_pages_sum: int = 0

    for section in sections:
        checked_section: Section = section._replace(is_valid = validation(rules, section.values))

        if checked_section.is_valid is True:
            middle_page: int = len(checked_section.values) // 2
            valid_pages_sum += checked_section.values[middle_page]
        else:
            sorted_section: list[int] = correction(rules, section.values)
            middle_page: int = len(checked_section.values) // 2
            invalid_pages_sum += sorted_section[middle_page]


    return valid_pages_sum, invalid_pages_sum


def output(data: list[str]) -> tuple:  # get solution outputs for framework
    rules: list[Rule] = read_rules(data)
    sections: list[Section] = read_sections(data)
    solution: tuple[int,int] = sum_valid_pages(rules, sections)
    solution_1: int = solution[0]
    solution_2: int = solution[1]
    return solution_1, solution_2 # change variables to correct

