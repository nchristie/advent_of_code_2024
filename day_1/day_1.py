def main():
    # Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called the location ID. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.

    # There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

    # For example:

    # 3   4
    # 4   3
    # 2   5
    # 1   3
    # 3   9
    # 3   3
    # Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

    # Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

    # In the example list above, the pairs and distances would be as follows:

    # The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
    # The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
    # The third-smallest number in both lists is 3, so the distance between them is 0.
    # The next numbers to pair up are 3 and 4, a distance of 1.
    # The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
    # Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
    # To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

    # Your actual left and right lists contain many location IDs. What is the total distance between your lists?
    list_a, list_b = extract_lists_from_txt("day_1_inputs.txt")
    list_a_ordered = order_list(list_a)
    list_b_ordered = order_list(list_b)
    distances = get_distances_between_two_lists(list_a_ordered, list_b_ordered)
    total_distance = sum_list(distances)
    print(total_distance)
    return total_distance


def extract_lists_from_txt(filepath):
    list_a = []
    list_b = []
    with open(filepath, "r") as file:
        for line in file:
            values = line.split()
            list_a.append(int(values[0]))
            list_b.append(int(values[1]))
    return list_a, list_b


def order_list(some_list):
    return sorted(some_list)


def get_distances_between_two_lists(list_a_ordered, list_b_ordered):
    distances_list = []
    list_len = len(list_a_ordered)
    for i in range(list_len):
        distances_list.append(abs(list_b_ordered[i] - list_a_ordered[i]))

    return distances_list


def sum_list(my_list):
    return sum(my_list)


if __name__ == "__main__":
    main()