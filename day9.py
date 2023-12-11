"""Day 9: Mirage Maintenance"""

from helper import InputLoader


def clean_input(input_data: list) -> list:
    """Cleaning the data for further use.

    :param input_data: Data from txt file
    :return: Clean dataset"""
    cleaned_input = [v.strip() for v in input_data]
    cleaned_input = [v.split() for v in cleaned_input]
    cleaned_input = [[int(v) for v in sublist] for sublist in cleaned_input]

    return cleaned_input


def get_iterations(input_data: list) -> list:
    """Iterating until zero.

    :param input_data: List of values
    :return: Lists with iterations"""
    iterated = []
    difference = []
    for x in range(len(input_data)-1):
        difference.append(int(input_data[x+1]) - int(input_data[x]))
    iterated.append(input_data)
    iterated.append(difference)
    while any([v != 0 for v in difference]):
        residual = []
        for x in range(len(difference) - 1):
            residual.append(int(difference[x + 1]) - int(difference[x]))
        iterated.append(residual)
        difference = residual

    return iterated


def find_next_value(iterated_sequence: list) -> int:
    """Forward extrapolation of the dataset.

    :param iterated_sequence: List of lists for iterations
    :return: Value we look for"""
    new_value = 0
    for x in reversed(range(1, len(iterated_sequence))):
        new_value += iterated_sequence[x-1][-1]

    return new_value


def find_previous_value(iterated_sequence: list) -> int:
    """Backwards extrapolation of the dataset.

    :param iterated_sequence: List of lists for iterations
    :return: Value we look for"""
    new_value = 0
    for x in reversed(range(1, len(iterated_sequence))):
        new_value = iterated_sequence[x-1][0] - new_value

    return new_value


if __name__ == "__main__":
    input_loader = InputLoader()
    data = input_loader.load_input_file()
    final_input = clean_input(data)
    first_star_result = 0
    second_star_result = 0
    for sequence in final_input:
        output = get_iterations(sequence)
        next_value = find_next_value(output)
        previous_value = find_previous_value(output)
        first_star_result += next_value
        second_star_result += previous_value
    print(f"First star result is: {first_star_result} and second star result is: {second_star_result}.")
