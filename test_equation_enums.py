"""
tests for CalcOperators Class
"""
from equation_enums import CalcOperators


def test_properties():
    """
    test for CalcOperators Class properties
    """
    assert CalcOperators.Equality.value == int(0)
    assert CalcOperators.Addition.value == int(1)
    assert CalcOperators.Subtraction.value == int(2)
    assert CalcOperators.Division.value == int(3)
    assert CalcOperators.Multiplication.value == int(4)
