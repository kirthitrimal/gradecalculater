# test_grade_calculator.py
import pytest
from grade_calculator import average, grade, is_pass, gpa_point


def test_average_standard():
    assert average([80, 90, 100]) == 90.0
    assert average([75, 82, 91]) == 82.67


def test_grade_boundaries():
    assert grade(95) == "A+"
    assert grade(85) == "A"
    assert grade(75) == "B"
    assert grade(65) == "C"
    assert grade(55) == "D"
    assert grade(42) == "F"


def test_is_pass_valid():
    assert is_pass([60, 70, 80]) is True
    assert is_pass([50, 50, 50]) is True


def test_is_pass_fail_single_subject():
    # High overall average (74.0), but one subject is below 40 -> Fail
    assert is_pass([90, 95, 37]) is False


def test_is_pass_fail_low_average():
    # All subjects >= 40, but overall average (43.33) < 50 -> Fail
    assert is_pass([40, 45, 45]) is False


def test_gpa_point_conversion():
    assert gpa_point(92.5) == 9.25
    assert gpa_point(80.0) == 8.0


def test_invalid_inputs():
    with pytest.raises(ValueError):
        average([])
    with pytest.raises(ValueError):
        average([85, 105])
    with pytest.raises(ValueError):
        grade(-5)
