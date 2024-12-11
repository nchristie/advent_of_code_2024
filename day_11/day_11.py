import time

lookup_table = {}

def part_1():
    input = [112, 1110, 163902, 0, 7656027, 83039, 9, 74]
    rules = [rule_1, rule_2, rule_3]
    output = input
    len_output = len(output)

    for i in range(75):
        start_time = time.time()
        print(f"\niteration: {i+1}")
        output = run_rules(output, rules)
        len_output = len(output)
        print(f"len_output: {len_output}")
        end_time = time.time()
        print("--- %s seconds ---" % round((end_time - start_time), 2))

def run_rules(input, rules):
    output = []
    for input_item in input:
        if lookup_table.get(input_item):
            morph = lookup_table[input_item]
        else:
            for rule in rules:
                morph = rule(input_item)
                if morph:
                    lookup_table[input_item] = morph
                    break
        for item in morph:
            output.append(item)
    return output

def rule_1(input_item):
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if input_item == 0:
        return [1]


def rule_2(input_item):
    # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    str_input_item = str(input_item)
    len_input_item = len(str_input_item)
    if len_input_item % 2 == 0:
        midpoint = int(len_input_item / 2)
        return [int(str_input_item[0:midpoint]), int(str_input_item[midpoint:])]


def rule_3(input_item):
    # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    return [input_item * 2024]


if __name__ == "__main__":
    part_1()
