import shlex


def split_instruction(instruction):
    # Use shlex to split the instruction into tokens
    tokens = shlex.split(instruction)

    # Extract label, opcode, and operands from the tokens
    
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


class CommandType():
    INVOCATION="INVOCATION"
    NORMAL="NORMAL"
    DEFINITION="DEFINITION"
    MACRO_LITERALS="MACRO_LITERALS"

