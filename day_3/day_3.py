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

def part_2():
    filename = "day_3_input.txt"
    input_text = get_input_text(filename)
    relevant_text = extract_relevant_text_part_2(input_text)

    output = 0
    perform = True
    for line in relevant_text:
        if line == "do()":
            perform = True
        elif line == "don't()":
            perform = False
        else:
            if perform:
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

def extract_relevant_text_part_2(input_text):
    pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
    relevant_text = re.findall(pattern, input_text)
    return relevant_text

def mul(int_a, int_b):
    return int_a * int_b

if __name__ == "__main__":
    # part_1()
    part_2()

