import re

def part_1():
    filename = "day_3_input.txt"
    input_text = get_input_text(filename)
    relevant_text = extract_relevant_text(input_text)
    output = 0
    for line in relevant_text:
        output += eval(line)
    print(output)
    return output

def get_input_text(filename):
    with open(filename, "r") as file:
        return file.read()


def extract_relevant_text(input_text):
    pattern = r'mul\(\d+,\d+\)'
    relevant_text = re.findall(pattern, input_text)
    return relevant_text

def mul(int_a, int_b):
    return int_a * int_b

if __name__ == "__main__":
    part_1()

