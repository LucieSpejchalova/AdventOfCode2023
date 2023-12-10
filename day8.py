"""Day 8: Haunted Wasteland"""
import re
from helper import InputLoader


def get_instructions(data: list):
    instructions = []
    rule = data[0]
    instruction = rule.replace("L", "0")
    cleaned_rule = instruction.replace("R", "1")
    for a in cleaned_rule:
        instructions.append(a)
    return instructions[:-1]


def get_nodes(data: list):
    node_list = {}
    for sequence in data:
        node = re.findall(r'[A-Z]{3}', sequence)
        if len(node) > 2:
            node_list[node[0]] = node[1:]

    return node_list


def go_through_nodes(instruction_list: list, node_dict: dict):
    start = node_dict["AAA"]
    step_count = 0
    next_step = ""
    while next_step != "ZZZ":
        for rule in instruction_list:
            next_step = start[int(rule)]
            start = node_dict[next_step]
            step_count += 1

    return step_count


if __name__ == "__main__":
    input_loader = InputLoader()
    data = input_loader.load_input_file()
    instructions = get_instructions(data)
    nodes = get_nodes(data)
    result = go_through_nodes(instructions, nodes)
    print(result)
