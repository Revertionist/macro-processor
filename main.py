from utils import split_instruction
import pprint

content = []
split = []
lines = []
name_tab = []
index = 0
current_address = 0

def process():
    global content
    global split
    content = content.strip()
    split = content.split("\n")
    for i in split:
        lines.append(split_instruction(i))   
        
def  get_name_tab():
    global name_tab
    global current_address
    found = False
    name_tab_content = {
        "name": None,
        "start": None,
        "end": None
    }
    for i in lines:
        if i["opcode"].lower() == "macro":
            name_tab_content["name"] = i["label"]
            name_tab_content["start"] = current_address
            for j in name_tab:
                if j["name"] == i["label"]:
                    found = True
        current_address += 1
        if i["opcode"].lower() == "mend":
            if not found:
                name_tab_content["end"] = current_address
                name_tab.append(name_tab_content)
            
    

def main():
    global content
    pgm = open("code.asm")
    content = pgm.read()
    process()
    print (lines)
    get_name_tab()
    print(name_tab)

if __name__ == "__main__":
    main()