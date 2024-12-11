import day_5
import pytest

some_rules = [
    [47, 53],
    [97, 13],
    [97, 61],
    [97, 47],
    [75, 29],
    [61, 13],
    [75, 53],
    [29, 13],
    [97, 29],
    [53, 29],
    [61, 53],
    [97, 53],
    [61, 29],
    [47, 13],
    [75, 47],
    [97, 75],
    [47, 61],
    [75, 61],
    [47, 29],
    [75, 13],
    [53, 13],
]

some_ordered_rules = [97, 75, 47, 61, 53, 29, 13] # these should be right - I checked by eye

real_ordered_rules = [
    27,
    16,
    67,
    55,
    22,
    23,
    15,
    46,
    77,
    32,
    36,
    56,
    86,
    44,
    79,
    63,
    83,
    95,
    89,
    62,
    14,
    51,
    37,
    25,
    69,
    49,
    65,
    52,
    73,
    72,
    87,
    97,
    47,
    85,
    92,
    81,
    45,
    57,
    76,
    17,
    29,
    28,
    26,
    91,
    98,
    54,
    82,
    12,
    75,
]


@pytest.mark.parametrize(
    "rules, expected",
    [
        (
            [
                [47, 53],
            ],
            [47, 53],
        ),
        (
            [[47, 53], [53, 89]],
            [47, 53, 89],
        ),
        (
            [[47, 53], [89, 53]],
            [47, 89, 53],
        ),
        (
            [
                [47, 53],
                [97, 13],
                [97, 61],
                [61, 13],
                [53, 29],
                [29, 13],
            ],
            [47, 53, 29, 97, 61, 13],
        ),
        (
            [
                [51, 47],
                [51, 16],
                [89, 51],
                [49, 51],
                [25, 51],
            ],
            [89, 49, 25, 51, 16, 47],
        ),
        (
            [
                [85, 76],
                [27, 23],
                [85, 63],
                [63, 27],
                [27, 44],
                [44, 76],
                [76, 56],
                [56, 23],
            ],
            [85, 63, 27, 44, 76, 56, 23],
        ),
        (
            [
                [29, 13],
                [53, 13],
                [53, 29],
            ],
            [53, 29, 13]
        ),
        (some_rules, some_ordered_rules),
    ],
)
def test_order_rules(rules, expected):
    # WHEN
    actual = day_5.order_rules(rules)

    # THEN
    assert expected == actual


@pytest.mark.parametrize(
    "update, rules, expected",
    [
        ([75, 47, 61, 53, 29], some_ordered_rules, True),
        ([97, 61, 53, 29, 13], some_ordered_rules, True),
        ([75, 29, 13], some_ordered_rules, True),
        ([75, 97, 47, 61, 53], some_ordered_rules, False),
        ([61, 13, 29], some_ordered_rules, False),
        ([97, 13, 75, 29, 47], some_ordered_rules, False),
        ([51, 89, 49, 25, 69, 47, 16], real_ordered_rules, False),
        ([85, 63, 27, 44, 76, 56, 23], real_ordered_rules, False),
    ],
)
def test_update_passes_rules(update, rules, expected):
    # WHEN
    actual = day_5.update_passes_rules(update, rules)
    # THEN
    assert expected == actual
