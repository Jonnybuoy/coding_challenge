import pytest

from matrix_algorithm import matrix_max_min_value


def test_matrix_max_min_value():
    matrix = [[5, 16, 20], [9, 11, 18], [15, 16, 17]]
    result = matrix_max_min_value(matrix)
    assert result == [17], f"Expected [] but got {result}"


    print("All tests passed!")
