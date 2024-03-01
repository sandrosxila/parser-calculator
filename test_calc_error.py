"""
checking CalcError Class
"""
from calc_error import CalcError


def test_properties():
    """
    test for CalcError Class Properties
    """
    assert CalcError.__str__(CalcError.DivisionError) ==\
           "(Error: divide by 0)"
    assert CalcError.__str__(CalcError.SymbolError) ==\
           "( Error: Equation Contains Unpermitted Symbol )"
    assert CalcError.__str__(CalcError.FormatError) ==\
           "( Error: Please Enter the Equation in Correct Format )"
