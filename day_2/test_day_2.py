import day_2
from unittest.mock import patch
import pytest

# GIVEN
# WHEN
# THEN


@pytest.mark.parametrize(
    "all_reports, expected",
    [
        (
            [
                [7, 6, 4, 2, 1],
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
                [1, 3, 6, 7, 9],
            ],
            4,
        ),
        # (
        #     [
        #         [35, 37, 38, 41, 43, 41],
        #         [64, 66, 69, 71, 72, 72],
        #         [45, 47, 50, 51, 52, 53, 55, 59],
        #         [16, 18, 19, 20, 23, 29],
        #         [36, 39, 41, 43, 44, 41, 44],
        #         [42, 45, 46, 44, 42],
        #         [82, 85, 86, 87, 88, 86, 86],
        #         [42, 45, 46, 45, 47, 51],
        #         [57, 60, 62, 65, 63, 65, 70],
        #         [88, 90, 90, 93, 95, 97],
        #     ],
        #     5
        # )
    ],
)
@patch("day_2.extract_reports_from_txt")
def test_part_1(mock_extract, all_reports, expected):
    # GIVEN
    mock_extract.return_value = all_reports

    # WHEN
    actual = day_2.part_1()

    # THEN
    assert expected == actual


@pytest.mark.parametrize(
    "report, expected",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_safe_report(report, expected):
    # WHEN
    actual = day_2.safe_report(report)

    # THEN
    assert expected == actual


@pytest.mark.parametrize(
    "report, expected",
    [
        ([7, 6, 4, 2, 1], []),
        ([1, 2, 7, 8, 9], ["step_size_unsafe"]),
        ([9, 7, 6, 2, 1], ["step_size_unsafe"]),
        ([1, 3, 2, 4, 5],["fall_rise"]),
        ([8, 6, 4, 4, 1], ["levels_match"]),
        ([1, 3, 6, 7, 9], []),
    ],
)
def test_safe_report(report, expected):
    # WHEN
    actual = day_2.safe_report(report)

    # THEN
    assert expected == actual


@patch("day_2.extract_reports_from_txt")
def test_part_2(mock_extract):
    # GIVEN
    all_reports = [
        [7, 6, 4, 2, 1], # safe
        [1, 2, 7, 8, 9], # unsafe
        [9, 7, 6, 2, 1], # unsafe
        [1, 3, 2, 4, 5], # safe
        [8, 6, 4, 4, 1], # safe
        [1, 3, 6, 7, 9], # safe
    ] 
    mock_extract.return_value = all_reports

    # WHEN
    expected = 4
    actual = day_2.part_2()

    # THEN
    assert expected == actual


@patch("day_2.extract_reports_from_txt")
def test_part_2_example(mock_extract):
    # GIVEN
    all_reports = [
        [69, 67, 64, 63, 59], # safe
    ] 
    mock_extract.return_value = all_reports

    # WHEN
    expected = 0
    actual = day_2.part_2()

    # THEN
    assert expected == actual

@pytest.mark.parametrize(
    "levels, expected",
    [
        ([7, 6, 4], False),
        ([1, 3, 2], True),
        ([3, 1, 2], True),
        ([1, 1, 2], False),
        ([1, 2, 2], False),
    ],
)
def test_do_levels_rise_and_fall(levels, expected):
    # WHEN
    actual = day_2.do_levels_rise_and_fall(levels[0], levels[1], levels[2])

    # THEN
    assert expected == actual


@pytest.mark.parametrize(
    "report, expected",
    [
        ([1, 1, 2, 3, 4], [1, 2, 3, 4]),
        ([1, 5, 2, 3, 4], [1, 2, 3, 4]),
        ([1, 8, 2, 3, 4], [1, 2, 3, 4]),
        ([9, 1, 8, 7, 6], [9, 8, 7, 6]),
        ([9, 1, 8, 7, 6, 8], [9, 8, 7, 6, 8]),
        ([8, 6, 4, 4, 1], [8, 6, 4, 1]),
        ([69, 67, 64, 63, 59], [69, 67, 64, 63])
    ],
)
def test_clean_up(report, expected):
    # WHEN
    actual = day_2.clean_up(report)

    # THEN
    assert expected == actual

@pytest.mark.parametrize(
    "last_level, current_level, expected",
    [
        (63, 59, True)
    ]

)
def test_step_size_unsafe(last_level, current_level, expected):
    # WHEN
    actual = day_2.step_size_unsafe(last_level, current_level)

    # THEN
    assert expected == actual