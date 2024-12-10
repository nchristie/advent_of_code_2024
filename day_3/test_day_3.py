import day_3
from unittest.mock import patch
import pytest

# GIVEN
# WHEN
# THEN

def test_extract_relevant_text():
    # GIVEN
    input_text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    
    # WHEN
    expected = [
        "mul(2,4)",
        "mul(5,5)",
        "mul(11,8)",
        "mul(8,5)"
    ]
    actual = day_3.extract_relevant_text(input_text)
    
    # THEN
    assert expected == actual