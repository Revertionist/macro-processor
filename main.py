from utils import split_instruction
import pprint, copy

content = ""
lines = []
name_tab = []
arg_tab = []
def_tab = []
current_address = 0

def process():
    global content, lines
    content = content.strip()
    split = content.split("\n")
    lines.extend(split_instruction(i) for i in split)

def get_name_tab():
    global name_tab, current_address

    for i, line in enumerate(lines):
        if line["opcode"].lower() == "macro":
            name_tab_content = {
                "name": line["label"],
                "start": current_address,
                "end": None
            }
            get_arg_tab(line)
            found = any(j["name"] == line["label"] for j in name_tab)
            if not found:
                name_tab.append(name_tab_content)
        elif line["opcode"].lower() == "mend":
            if not found:
                name_tab_content["end"] = current_address
        current_address += 1

def get_arg_tab(operand_line):
    global arg_tab
    for val, name in enumerate(operand_line["operands"]):
        arg_tab_content = {
            "name": name,
            "value": f"?{val + 1}"
        }
        arg_tab.append(arg_tab_content)


def get_def_tab():
    global def_tab
    expanded = False
    for i, line in enumerate(lines):
        if line["opcode"].lower() == "macro":
            expanded = True
            def_tab_contents = {
                "label": line["label"],
                "opcode": line["opcode"],
                "operands": line["operands"]
            }
            
            def_tab.append(def_tab_contents)
        elif line["opcode"].lower() == "mend":
            expanded = False
            def_tab_contents = {
                "label": line["label"],
                "opcode": line["opcode"],
                "operands": line["operands"]
            }
            def_tab.append(def_tab_contents)
        elif expanded:
            operand_switch = list(line["operands"])
            counter = 0
            for i in operand_switch:
                for j in arg_tab:
                    if j["name"] == i:
                        operand_switch[counter] = j["value"]
                        counter += 1
                
            
            def_tab_contents = {
                "label": line["label"],
                "opcode": line["opcode"],
                "operands": operand_switch
            }
            def_tab.append(def_tab_contents)

def main():
    global content, lines
    pgm = open("code.asm")
    content = pgm.read()
    process()
    get_name_tab()
    pprint.pprint(name_tab)
    pprint.pprint(arg_tab)
    get_def_tab()
    pprint.pprint(def_tab)

if __name__ == "__main__":
    main()
