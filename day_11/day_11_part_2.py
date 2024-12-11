import time

lookup_table = {}
output_table = {
    112: 1, 
    1110: 1, 
    163902: 1, 
    0: 1, 
    7656027: 1, 
    83039: 1, 
    9: 1, 
    74: 1
}

def part_1():
    input = [112, 1110, 163902, 0, 7656027, 83039, 9, 74]
    rules = [rule_1, rule_2, rule_3]
    output = input
    len_output = len(output)
    input_table = output_table

    number_of_iterations = 1
    for i in range(number_of_iterations):
        start_time = time.time()
        print(f"\niteration: {i+1}")
        output_table = run_rules(input_table, rules)
        len_output = len(output)
        print(f"len_output: {len_output}")
        end_time = time.time()
        print("--- %s seconds ---" % round((end_time - start_time), 2))
        print(output_table)
        input_table = output_table

def run_rules(input_table, rules):
    new_output_table = {}
    for input_item, number_of_instances in input_table.iteritems():
        if lookup_table.get(input_item):
            morph = lookup_table[input_item]
        else:
            for rule in rules:
                morph = rule(input_item)
                if morph:
                    lookup_table[input_item] = morph
                    break
        for item in morph:
            if new_output_table.get(item):
                new_output_table[item] *= number_of_instances
            else:
                new_output_table[item] = number_of_instances

    return new_output_table

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
