import pytest
import day_4


@pytest.mark.parametrize(
    "row, expected",
    [
        (["M", "M", "M", "M"], 0),
        (["X", "M", "A", "S"], 1),
        (["X", "M", "A", "S", "X", "M", "A", "S"], 2),
    ],
)
def test_count_xmas(row, expected):
    # WHEN
    actual = day_4.count_xmas(row)

    # THEN
    assert expected == actual


def test_transpose_matrix():
    # GIVEN
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # WHEN
    expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    actual = day_4.transpose_matrix(matrix)
    # THEN
    assert expected == actual


# def test_get_diagonals_tl_br():
#     # GIVEN
#     matrix = [
#         [1, 2, 3], 
#         [4, 5, 6], 
#         [7, 8, 9]
#     ]
#     # WHEN
#     expected = [
#         [1], 
#         [4, 2], 
#         [7, 5, 3], 
#         [8, 6], 
#         [9]
#     ]
#     actual = day_4.get_diagonals_bl_tr(matrix)
#     # THEN
#     assert expected == actual

def test_get_diagonals_tl_br_again():
    # GIVEN
    matrix = [ 
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
        [26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35]
    ]
    # WHEN
    expected = [
        [11],
        [16, 12],
        [21, 17, 13],
        [26, 22, 18, 14],
        [31, 27, 23, 19, 15],
        [32, 28, 24, 20],
        [33, 29, 25],
        [34, 30],
        [35]
    ]
    actual = day_4.get_diagonals_bl_tr(matrix)
    # THEN
    assert expected == actual

def test_get_diagonal_coordinates():
    # GIVEN
    length =  3
    
    # WHEN
    expected = [(2,0), (1,1), (0,2)]
    actual = day_4.get_diagonal_coordinates(length)

    # THEN
    assert expected == actual

def test_get_diagonal_coordinates_bigger():
    # GIVEN
    length =  6
    
    # WHEN
    expected = [(5,0), (4,1), (3,2), (2,3), (1, 4), (0, 5)]
    actual = day_4.get_diagonal_coordinates(length)

    # THEN
    assert expected == actual

def test_get_diagonal_coordinates_even():
    # GIVEN
    length =  7
    
    # WHEN
    expected = [(6,0), (5,1), (4,2), (3,3), (2, 4), (1, 5), (0, 6)]
    actual = day_4.get_diagonal_coordinates(length)

    # THEN
    assert expected == actual

def test_get_diagonal_coordinates_small():
    # GIVEN
    length =  1
    
    # WHEN
    expected = [(0,0)]
    actual = day_4.get_diagonal_coordinates(length)

    # THEN
    assert expected == actual
