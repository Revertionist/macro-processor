from utils import split_instruction

split = []
lines = []

def process(content):
    content = content.strip()
    split = content.split("\n")
    for i in split:
        lines.append(split_instruction(i))

def main():
    pgm = open("code.asm")
    content = pgm.read()
    process (content)
    print (lines)

if __name__ == "__main__":
    main()