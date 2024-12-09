import day_2
from unittest.mock import patch
import pytest

# GIVEN
# WHEN
# THEN

@patch("day_2.extract_reports_from_txt")
def test_part_1(mock_extract):
    # GIVEN
    all_reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    mock_extract.return_value = all_reports
    
    # WHEN
    expected = 2
    actual = day_2.part_1()
    
    # THEN
    assert expected == actual

@pytest.mark.parametrize("report, expected", [
    ([7, 6, 4, 2, 1], True),
    ([1, 2, 7, 8, 9], False),
    ([9, 7, 6, 2, 1], False),
    ([1, 3, 2, 4, 5], False),
    ([8, 6, 4, 4, 1], False),
    ([1, 3, 6, 7, 9], True),
])
def test_safe_report(report, expected):   
    # WHEN
    actual = day_2.safe_report(report)
    
    # THEN
    assert expected == actual

@pytest.mark.xfail
def test_part_2():
    # GIVEN
    # WHEN
    expected = True
    actual = False
    # THEN
    assert expected == actual