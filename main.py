from utils import split_instruction

split = []
lines = []
name_tab = []
def_tab = []
expanded_file = []
arg_tab = []
line_counter = 0
arg_address = 0

def process(content):
    content = content.strip()
    split = content.split("\n")
    for i in split:
        lines.append(split_instruction(i))

def one_pass_macro():
    global expanding
    expanding = False
    for i in lines:
        while i["opcode"].lower() != "end":
            get_line()
            process_line(i)
        line_counter += 1

def get_line():
    return

def process_line(line):
    found = False
    for i in name_tab:
        print(i["opcode"])
        if i["opcode"] == line["opcode"]:
            found = True
            break
    if found:
        expand(line, i)
    elif line["opcode"] == "macro":
        define(line)
    else:
        expanded_file.append(line)
    
def expand(current_line, name):
    expanding = True
    prototype = None
    
    for i in def_tab:
        if name["start"] == i["label"]:
            prototype = i
    for i in prototype["operands"]:
        arg_tab_contents = {
            "argument": i,
            "label": arg_address
        }
        arg_address += 1
    expanded_file.append(current_line)
    
    

def define(current_line):
    name_tab_content = {
        "name": current_line["label"],
        "start": line_counter,
        "end": None
    }
    current_address = line_counter
    current_line["index"] = current_address
    def_tab.append(current_line)
    level = 1
    
    while level > 0:
        get_line()
        def_tab.append(current_line)
        current_address += 1
        if current_line["opcode"].lower() == "macro":
            level += 1
        elif current_line["opcode"].lower() == "mend":
            level -= 1
    name_tab_content["end"] = current_address
    name_tab.append(name_tab_content)
    

def main():
    pgm = open("code.asm")
    content = pgm.read()
    process (content)
    
    print (lines)
    one_pass_macro()

if __name__ == "__main__":
    main()