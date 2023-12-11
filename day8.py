"""Day 8: Haunted Wasteland"""
import re
from math import lcm
from helper import InputLoader


def get_instructions(info: list) -> list:
    """Convert input list into instructions.

    :param info: loaded txt
    :return: List with instructions"""
    instruct = []
    rule = info[0]
    instruction = rule.replace("L", "0")
    cleaned_rule = instruction.replace("R", "1")
    for a in cleaned_rule:
        instruct.append(a)
    return instruct[:-1]


def get_nodes(info: list) -> dict:
    """Convert input list node dictionary.

    :param info: loaded txt
    :return: Dictionary of all nodes"""
    node_list = {}
    for sequence in info:
        node = re.findall(r'[A-Z-0-9]{3}', sequence)
        if len(node) > 2:
            node_list[node[0]] = node[1:]

    return node_list


def find_starting_nodes(node_dict: dict) -> list:
    """Find the starting nodes.

    :param node_dict: Dictionary of all nodes
    :return: List with starting nodes"""
    starting_nodes = [k for k in node_dict.keys() if "A" in k]
    return starting_nodes


def go_through_nodes(instruction_list: list, node_dict: dict, ghost_name: str):
    """Go through nodes to the last one.

    :param instruction_list: List of instructions to move in nodes
    :param node_dict: Dictionary of all nodes
    :param ghost_name: The starting node
    :return: Number of steps needed to reach the destination"""
    starter = node_dict[ghost_name]
    step_count = 0
    next_step = "XXX"
    while next_step[-1] != "Z":
        for rule in instruction_list:
            next_step = starter[int(rule)]
            starter = node_dict[next_step]
            step_count += 1

    return step_count


if __name__ == "__main__":
    input_loader = InputLoader()
    data = input_loader.load_input_file()
    instructions = get_instructions(data)
    nodes = get_nodes(data)
    start = find_starting_nodes(nodes)
    part_one_result = go_through_nodes(instructions, nodes, "AAA")
    results = []
    for ghost in start:
        results.append(go_through_nodes(instructions, nodes, ghost))
    part_two_result = lcm(*results)

    print(f"First star result is: {part_one_result} and second star result is: {part_two_result}.")

