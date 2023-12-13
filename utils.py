import shlex

def split_instruction(instruction):
    tokens = shlex.split(instruction)

    if len(tokens) == 3:
        label = tokens[0]
        opcode = tokens[1]
        operands = tokens[2].split(",")

    elif len(tokens) == 2:
        label = ""
        opcode = tokens[0]
        operands = tokens[1].split(",")

    elif len(tokens) == 1:
        label = ""
        opcode = tokens[0]
        operands = []
    else:
        label = None
        opcode = None
        operands = None

    # Create a dictionary to represent the structure
    result = {
        "label": label,
        "opcode": opcode,
        "operands": operands
    }

    return result
