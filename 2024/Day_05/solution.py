from collections import namedtuple


name: str = "Day 5: Print Queue"

Rule = namedtuple("Rule",["right","left"])
Section = namedtuple("Section", ["values", "is_valid"])


def read_rules(data: list[str]) -> list[Rule]:
    rules: list[Rule] = []
    for row in data:
        if row == '' :
            break
        else:
            pages: list[str] = row.split('|')
            rules.append(Rule(int(pages[0]),int(pages[1])))

    return rules


def read_sections(data: list[str]) -> list[Section]:
    sections: list[Section] = []
    start_reading: bool = False
    for row in data:
        if start_reading is True:
            sections.append(Section(values=[int(i) for i in row.split(',')], is_valid = True))

        if row == '':
            start_reading = True

    return sections

def validation(rules: list[Rule], section: list[int]) -> bool:
    is_valid: bool = True
    for rule in rules:
        if rule.right in section and rule.left in section:
            index_right: int = section.index(rule.right)
            index_left: int = section.index(rule.left)

            if index_right > index_left:
                is_valid = False

    return is_valid

def sum_valid_pages(rules: list[Rule], sections: list[Section]) -> int:
    pages_sum: int = 0

    for section in sections:
        checked_section: Section = section._replace(is_valid = validation(rules, section.values))

        if checked_section.is_valid is True:
            middle_page: int = len(checked_section.values) // 2
            pages_sum += checked_section.values[middle_page]

    return pages_sum

def output(data: list[str]) -> tuple:  # get solution outputs for framework
    rules: list[Rule] = read_rules(data)
    sections: list[Section] = read_sections(data)
    solution_1: int = sum_valid_pages(rules, sections)
    solution_2: int = 0
    return solution_1, solution_2 # change variables to correct
                