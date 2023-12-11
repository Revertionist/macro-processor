from utils import split_instruction
import pprint
import copy

content = ""
lines = []
name_tab = []
val_table = []
arg_tab = []
def_tab = []
exp_code = []
index = 1
start_index = 0
end_index = 0
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
            get_val_tab(line)
            found = any(j["name"] == line["label"] for j in name_tab)
            if not found:
                name_tab.append(name_tab_content)
        elif line["opcode"].lower() == "mend":
            if not found:
                name_tab_content["end"] = current_address
        current_address += 1


def get_val_tab(operand_line):
    global val_table
    for val, name in enumerate(operand_line["operands"]):
        val_tab_content = {
            "name": name,
            "value": f"?{val + 1}"
        }
        val_table.append(val_tab_content)


def get_def_tab():
    global def_tab
    expanded = False
    global index
    for i, line in enumerate(lines):
        if line["opcode"].lower() == "macro":
            expanded = True
            def_tab_contents = {
                "index": index,
                "label": line["label"],
                "opcode": line["opcode"],
                "operands": line["operands"]
            }
            index += 1
            def_tab.append(def_tab_contents)
        elif line["opcode"].lower() == "mend":
            expanded = False
            def_tab_contents = {
                "index": index,
                "label": line["label"],
                "opcode": line["opcode"],
                "operands": line["operands"]
            }
            index += 1
            def_tab.append(def_tab_contents)
        elif expanded:
            operand_switch = list(line["operands"])
            counter = 0
            for i in operand_switch:
                for j in val_table:
                    if j["name"] == i:
                        operand_switch[counter] = j["value"]
                        counter += 1

            def_tab_contents = {
                "index": index,
                "label": line["label"],
                "opcode": line["opcode"],
                "operands": operand_switch
            }
            index += 1
            def_tab.append(def_tab_contents)


def expanded_code():
    global lines
    global exp_code
    global def_tab
    global name_tab
    global start_index
    global end_index
    operands = []

    for i, line in enumerate(lines):
        fun_call = False
        expanded = False
        if line["opcode"].lower() == "start":
            exp_code_content = {
                "name": line["label"],
                "opcode": line["opcode"],
                "operands": line["operands"]
            }
            exp_code.append(exp_code_content)
        else:
            for i in name_tab:
                if line["opcode"] == i["name"]:
                    fun_call = True
                    expanded = True
                    break
                elif line["opcode"].lower() == "mend":
                    expanded = False

        if fun_call == True:
            operands = line["operands"]
            exp_code_content = {
                "name": '',
                "opcode": "."+line["opcode"],
                "operands": line["operands"]
            }
            exp_code.append(exp_code_content)

        if expanded == True:
            for i in operands:
                for j in line["operands"]:
                    if j == i:
                        exp_code_content = {
                            "name": "",
                            "opcode": line["opcode"],
                            "operands": i
                        }
                        exp_code.append(exp_code_content)

def get_arg_tab(operands):
    global arg_tab
    val = 1
    for i in operands["operands"]:
        arg_tab_contents = {
            "name": i,
            "value": "?"+str(val)
        }
        val += 1
        arg_tab.append(arg_tab_contents)


def main():
    global content, lines
    pgm = open("code.asm")
    content = pgm.read()
    process()
    get_name_tab()
    print("lines")
    pprint.pprint(lines)
    print("name table")
    pprint.pprint(name_tab)
    print("val table")
    cont = False
    for i, line in enumerate(lines):
        for j, name in enumerate(name_tab):
            if line["opcode"] == name["name"]: 
                get_arg_tab(line)
                
    pprint.pprint(val_table)
    print ("arg table")
    pprint.pprint (arg_tab)
    get_def_tab()
    print("def table")
    pprint.pprint(def_tab)
    expanded_code()
    print("expanded code")
    pprint.pprint(exp_code)


if __name__ == "__main__":
    main()
