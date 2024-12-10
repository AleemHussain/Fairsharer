import pytest
from fair_sharer import fair_sharer

def test_fair_sharer():
    # Test 1: Single iteration
    input_values = [0, 1000, 800, 0]
    expected_output = [100, 800, 900, 0]
    assert fair_sharer(input_values, 1) == expected_output

    # Test 2: Two iterations
    input_values = [0, 1000, 800, 0]
    expected_output = [100, 890, 720, 90]
    assert fair_sharer(input_values, 2) == expected_output

if __name__ == "__main__":
    pytest.main()
