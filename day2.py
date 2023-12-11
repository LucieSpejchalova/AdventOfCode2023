"""Day 2: Cube Conundrum"""
import re
from helper import InputLoader


def clean_data(raw_input: list) -> dict:
    """Cleaning the data for further use.

    :param raw_input: Data from txt file
    :return: Clean dataset"""
    game_dict = {}
    for x in range(1, 1 + len(raw_input)):
        game_dict[x] = raw_input[x-1]

    return game_dict


def find_max_of_cubes(clean_input: dict) -> dict:
    """Get only maximum for each color.

    :param clean_input: Input data
    :return: Dictionary in format {GameID: [max(red), max(green), max(blue)]}"""
    dict_cube_max = {}
    for i, game in clean_input.items():
        find_red = re.findall(r'(?P<amount>\d+) red', game)
        find_red = max([int(i) for i in find_red])
        find_blue = re.findall(r'(?P<amount>\d+) blue', game)
        find_blue = max([int(i) for i in find_blue])
        find_green = re.findall(r'(?P<amount>\d+) green', game)
        find_green = max([int(i) for i in find_green])
        dict_cube_max[i] = [find_red, find_green, find_blue]

    return dict_cube_max


def find_possible_games(set_amount: list, lookup: dict) -> int:
    """Find games that are possible with the amount of cubes we have.

    :param set_amount: Amount of cubes we have to play with
    :param lookup: Input data
    :return: Sum of IDs of possible games"""
    possible_games = 0
    for game_id, game in lookup.items():
        checking_true = []
        for x in range(len(game)):
            if game[x] <= set_amount[x]:
                checking_true.append(True)
            else:
                checking_true.append(False)
        if all(checking_true):
            possible_games += game_id

    return possible_games


def calculate_lowest_amount(lookup: dict) -> int:
    """Calculate the power for lowest amount of cubes needed for a game.

    :param lookup: Input data set
    :return: Sum of power"""
    sum_of_power = 0
    for game in lookup.values():
        power = 1
        for x in range(len(game)):
            power *= game[x]
        sum_of_power += power

    return sum_of_power


if __name__ == "__main__":
    input_loader = InputLoader()
    data = input_loader.load_input_file()
    final_input = clean_data(data)
    cubes_present = find_max_of_cubes(final_input)

    bag = [12, 13, 14]

    part_one_result = find_possible_games(bag, cubes_present)
    part_two_result = calculate_lowest_amount(cubes_present)

    print(f"First star result is: {part_one_result} and second star result is: {part_two_result}.")

