from itertools import chain

def part_1():
    filepath = "day_4_input.txt"
    wordsearch_matrix = extract_matrix_from_txt(filepath)
    print(f"rows: {len(wordsearch_matrix[0])}")
    print(f"columns: {len(wordsearch_matrix)}")
    xmas_count = 0

    for row in wordsearch_matrix:
        # count rows forwards
        xmas_count += count_xmas(row)
        # count rows backwards
        xmas_count += count_xmas(row[::-1])

    wordsearch_matrix_transposed = transpose_matrix(wordsearch_matrix)

    for row in wordsearch_matrix_transposed:
        # count columns forwards
        xmas_count += count_xmas(row)
        # count columns backwards
        xmas_count += count_xmas(row[::-1])

    # count tl-br diagonals forwards
    # count tl-br diagonals backwards
    # count tr-bl diagonals forwards
    # count tr-bl diagonals backwards

    print(xmas_count)
    return xmas_count


def extract_matrix_from_txt(filepath):
    matrix = []
    with open(filepath, "r") as file:
        for line in file:
            row = [item for item in line if item != "\n"]
            matrix.append(row)
    return matrix


def count_xmas(row):
    count = 0
    string = "".join(row)
    target = "XMAS"
    count = string.count(target)
    return count


def transpose_matrix(matrix):
    new_matrix = []
    row_len = len(matrix[0])
    col_len = len(matrix)
    for i in range(row_len):
        new_row = []
        for j in range(col_len):
            new_row.append(matrix[j][i])
        new_matrix.append(new_row)
    return new_matrix


def get_diagonals_bl_tr(m):
    new_matrix = []
    max_row_len = len(m)

    for i in range(1, max_row_len+1):
        coords = get_diagonal_coordinates(i)
        new_matrix_row = []
        for j in coords:
            item = m[j[0]][j[1]]
            new_matrix_row.append(item)
        new_matrix.append(new_matrix_row)
    
    new_matrix.append([m[4][1], m[3][2],  m[2][3], m[1][4]])
    new_matrix.append([m[4][2], m[3][3],  m[2][4]])
    new_matrix.append([m[4][3], m[3][4]])
    new_matrix.append([m[4][4]])

    # print(new_matrix)
    return new_matrix
    


def get_diagonal_coordinates(length):
    coords = []
    for i in range(length):
        coords.append((length-i-1,i))
    return coords

if __name__ == "__main__":
    part_1()
