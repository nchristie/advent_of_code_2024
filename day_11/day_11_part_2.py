import time

NUMBER_OF_ITERATIONS = 25

lookup_table = {}

def part_2():
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
    rules = [rule_1, rule_2, rule_3]

    for i in range(NUMBER_OF_ITERATIONS):
        start_time = time.time()
        print(f"\niteration: {i+1}")
        new_output_table = run_rules(rules, output_table)
        print(f"len_output: {get_output_len(new_output_table)}")
        end_time = time.time()
        print("--- %s seconds ---" % round((end_time - start_time), 2))
        print(new_output_table)
        output_table = new_output_table

def get_output_len(output_table):
    len_output = 0
    for k, v in output_table.items():
        len_output += v
    return len_output

def run_rules(rules, output_table):
    new_output_table = {}
    for input_item, number_of_instances in output_table.items():
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
                new_output_table[item] += 1
            else:
                new_output_table[item] = 1

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
    part_2()
