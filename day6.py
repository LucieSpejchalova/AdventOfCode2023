"""Day 6: Wait For It"""
import re
from helper import InputLoader


def clean_data(input_file):
    input_dict = {}
    for x in range(len(input_file)):
        numbers = re.findall(r'\d+', input_file[x])
        input_file[x] = numbers

    for x in range(len(input_file[0])):
        input_dict[input_file[0][x]] = input_file[1][x]

    return input_dict


def calculate_possibilities(input_file: dict):
    possibilities = []
    for race in input_file.items():
        no_possibilities = 0
        race_time = race[0]
        for hold_time in range(int(race_time)):
            speed = hold_time
            new_race_time = int(race_time) - hold_time
            distance = new_race_time*speed
            if distance > int(race[1]):
                no_possibilities += 1
        possibilities.append(no_possibilities)

    return possibilities


def get_final_result(possibilities: list):
    final = 1
    for x in possibilities:
        final *= x

    return final


if __name__ == "__main__":
    input_loader = InputLoader()
    data = input_loader.load_input_file()
    data_for_work = clean_data(data)
    list_of_results = calculate_possibilities(data_for_work)
    print(get_final_result(list_of_results))



