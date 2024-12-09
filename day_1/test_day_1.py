import day_1
from unittest.mock import patch


@patch("day_1.extract_lists_from_txt")
def test_main(mock_extract):
    # GIVEN
    list_a = [
        3,
        4,
        2,
        1,
        3,
        3,
    ]

    list_b = [
        4,
        3,
        5,
        3,
        9,
        3,
    ]
    mock_extract.return_value = list_a, list_b

    # WHEN
    expected = 11
    actual = day_1.part_1()

    # THEN
    assert expected == actual


def test_extract_lists_from_txt():
    # GIVEN
    list_a = [
        3,
        4,
        2,
        1,
        3,
        3,
    ]

    list_b = [
        4,
        3,
        5,
        3,
        9,
        3,
    ]
    # WHEN
    expected = list_a, list_b
    actual = day_1.extract_lists_from_txt("day_1/day_1_test_inputs.txt")

    # THEN
    assert expected == actual


def test_extract_lists_from_txt_sample_of_real_set():
    # GIVEN
    list_a = [
        77710,
        22632,
        82229,
        35788,
        84000,
        28350,
        15185,
        59530,
    ]

    list_b = [
        11556,
        23674,
        77288,
        30924,
        63702,
        62605,
        47495,
        63702,
    ]

    # WHEN
    expected = list_a, list_b
    actual = day_1.extract_lists_from_txt("day_1/day_1_realistic_test_inputs.txt")

    # THEN
    assert expected == actual
