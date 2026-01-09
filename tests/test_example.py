"""Tests for the example module."""

from pyospackage_tirthjoshi.example import add_num, subtract_num


def test_add_num():
    """Test the add_num function."""
    assert add_num(2, 3) == 5
    assert add_num(-1, 1) == 0
    assert add_num(0, 0) == 0


def test_subtract_num():
    """Test the subtract_num function."""
    assert subtract_num(5, 3) == 2
    assert subtract_num(10, 15) == -5
    assert subtract_num(0, 0) == 0
