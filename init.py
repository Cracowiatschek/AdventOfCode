import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup

current_date = datetime.now()

current_day = current_date.day
current_month = current_date.month
current_year = current_date.year


def find_code_after_phrase(soup, phrase):
    phrase_element = soup.find(string = lambda text: text and phrase in text)

    if not phrase_element:
        return None

    for sibling in phrase_element.find_parent().find_next_siblings():
        code_element = sibling.find('code')
        if code_element:
            return code_element.get_text(strip = True)

    return None


def get_metadata(year, day):
    request = requests.get(f"https://adventofcode.com/{year}/day/{day}")
    content = request.text
    soup = BeautifulSoup(content, "html.parser")
    challenge_title = [h2.get_text(strip = True) for h2 in soup.find_all("h2")][0][4:-4]
    code_after_phrase = find_code_after_phrase(soup, "For example")

    if code_after_phrase is None:
        codes = [restricted_code for restricted_code in [code.get_text(strip = True) for code in soup.find_all("code")]
                 if "\n" in restricted_code]
        return challenge_title, codes[0]

    return challenge_title, code_after_phrase


def create_structure(year: int, day: int):

    name = f"{year}/Day_0{day}" if day < 10 else f"{year}/Day_{day}"
    meta = get_metadata(year, day)
    try:
        os.makedirs(name)

        with open(f"{name}/sample.in", "w") as file:
            print(f"Sugested sample data: \n{meta[1]}")
            accepted = input("Do you accepted this suggestion? [y/n]: ").lower()
            if accepted == "y":
                file.write(f"{meta[1]}")
            elif accepted == "n":
                print(f"Please paste sample data to {name}/input.in")
                file.write("")
            else:
                print(f"Answer not recognized. Please paste sample data to {name}/input.in")
                file.write("")

        with open(f"{name}/input.in", "w") as file:
            print(f"Please paste input data to {name}/input.in")
            file.write("")

        with open(f"{name}/test.py", "w") as file:
            file.write(
                """
import unittest
from solution import output

def run_tests():  # runing test module for exec module
    suite = unittest.TestLoader().loadTestsFromTestCase(xyz)  # change xyz to test case
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    simple = result.wasSuccessful()
    return result, simple
                """
            )

        with open(f"{name}/solution.py", "w") as file:
            file.write(
                f"""
name: str = "{meta[0]}"



def output(data: list[str]) -> tuple:  # get solution outputs for framework

    # solution body

    return a, b  # change variables to correct
                """
            )

    except Exception as e:
        print(e)


def initialize(year, month, day):
    print("Hello!\nThis is AoC Initializer.\nInitialize mode:\n1. Auto: select challenge for current date\n"
          "2. Manual select date")
    mode = input("Select template generator mode [Press 1 or 2]: ")
    if mode == "1":
        if month == 12:
            create_structure(year, day)
        else:
            print("Month out of range. Run initializer again.")
    elif mode == "2":
        year = int(input("Write selected year: "))
        if 2015 <= year <= current_year:
            day = int(input("Write selected day: "))
            if 1 <= day <= 25:
                try:
                    create_structure(year, day)
                    print("Tempplate created! Everything it's okay! Have a fun!")
                except Exception as e:
                    print(e)
            else:
                print("Day out of range. Run initializer again.")
        else:
            print("Year out of range. Run initializer again.")
    else:
        print("Mode out of range. Run initializer again.")

if __name__ == "__main__":
    initialize(year = current_year, month = current_month, day = current_day)
