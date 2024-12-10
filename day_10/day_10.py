def part_1():
    """
    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732
    
    This larger example has 9 trailheads. Considering the trailheads in reading order, they have scores of 5, 6, 5, 3, 1, 3, 5, 3, and 5. Adding these scores together, the sum of the scores of all trailheads is 36.
    """
    print("working")
    filepath = "day_10_inputs.txt"
    print(extract_matrix_from_txt(filepath))
    pass

def extract_matrix_from_txt(filepath):
    matrix = []
    with open(filepath, "r") as file:
        for line in file:
            row = [int(item) for item in line if item != "\n"]
            matrix.append(row)
    return matrix

if __name__ == "__main__":
    part_1()
