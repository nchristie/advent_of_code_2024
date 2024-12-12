import day_11
import day_11_part_2
import pytest
RULES = [day_11_part_2.rule_1, day_11_part_2.rule_2, day_11_part_2.rule_3]

@pytest.mark.parametrize(
    "input_item, expected",
    [(10, [1, 0]), (1000, [10, 0]), (1234, [12, 34]), (1, None), (123, None)],
)
def test_rule_2(input_item, expected):
    # WHEN
    actual = day_11.rule_2(input_item)

    # THEN
    assert expected == actual

def test_run_rules():
    # GIVEN
    rules = RULES
    output_table = {
        0: 1,
        1: 1,
        10: 1,
        100: 1,
        1000: 1
    }

    # WHEN
    expected = {
        0: 2,
        1: 2,
        10: 1,
        2024: 1,
        202400: 1,
    }
    actual = day_11_part_2.run_rules(rules, output_table)
    
    # THEN
    assert expected == actual

def test_get_output_len():
    # GIVEN
    # WHEN
    # THEN
    pass
