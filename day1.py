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
    change_data = {"one": "1",
                   "two": "2",
                   "three": "3",
                   "four": "4",
                   "five": "5",
                   "six": "6",
                   "seven": "7",
                   "eight": "8",
                   "nine": "9",
                   "zero": "0",
                   "ten": "10",
                   "eleven": "11",
                   "twelve": "12",
                   "thirteen": "13",
                   "twenty": "20",
                   "thirty": "30",
                   "forty": "40",
                   "fifty": "50",
                   "hundred": "100"
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

