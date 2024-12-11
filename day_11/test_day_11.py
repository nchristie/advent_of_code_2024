import day_11
import pytest

# Initial arrangement:
# 125 17

# After 1 blink:
# 253000 1 7

# After 2 blinks:
# 253 0 2024 14168

# After 3 blinks:
# 512072 1 20 24 28676032

# After 4 blinks:
# 512 72 2024 2 0 2 4 2867 6032

# After 5 blinks:
# 1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

# After 6 blinks:
# 2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2


@pytest.mark.parametrize(
    "input_item, expected",
    [(10, [1, 0]), (1000, [10, 0]), (1234, [12, 34]), (1, None), (123, None)],
)
def test_rule_2(input_item, expected):
    # WHEN
    actual = day_11.rule_2(input_item)

    # THEN
    assert expected == actual
