"""Day 1: Trebuchet?!"""
import re
from helper import InputLoader


def find_first_digit(input_line: str):
    numbers = re.findall(r'\d', input_line)
    first_digit = numbers[0]
    return first_digit


def find_last_digit(input_line: str):
    numbers = re.findall(r'\d', input_line)
    last_digit = numbers[-1]
    return last_digit


def clean_up(input_line: str):
    change_data = {"one": "o1e",
                   "two": "t2o",
                   "three": "t3e",
                   "four": "f4r",
                   "five": "f5e",
                   "six": "s6x",
                   "seven": "s7n",
                   "eight": "e8t",
                   "nine": "n9e",
                   "zero": "z0e",
                   }
    for word, digit in change_data.items():
        if word in input_line:
            input_line = input_line.replace(word, digit)

    return input_line


if __name__ == "__main__":
    input_loader = InputLoader()
    data = input_loader.load_input_file()
    result = 0
    count = 0

    for line in data:
        new_line = clean_up(line)
        addition = int(find_first_digit(new_line) + find_last_digit(new_line))
        result += addition

    print(result)
