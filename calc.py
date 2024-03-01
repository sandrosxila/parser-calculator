"""
Created By Sandro Skhirtladze
"""
import sys
from calc_error import CalcError
from equation_parser import EquationParser


def permitted_operators():
    """
    returns list of the permitted operators
    :return: [str]
    """
    return ['+', '-', '*', '/']


def permitted_symbols():
    """
    returns list of the permitted symbols
    :return: bool
    """
    return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def is_operator(_chr):
    """
    checks if character is in permitted operators
    :param _chr:
    :return: bool
    """
    return _chr in permitted_operators()


def is_symbol_permitted_equation(_str):
    """
    checks if equation String consists only permitted characters
    :param _str:
    :return: bool
    """
    allowed_chars = 0
    for _chr in permitted_symbols() + permitted_operators():
        allowed_chars += _str.count(_chr)
    return len(_str) == allowed_chars


def has_edge_operator(_str):
    """

    :param _str:
    :return: bool
    """
    return is_operator(_str[0]) or is_operator(_str[-1])


def is_correct_sequence(_str):
    """
    Checks Sequence of Operators
    :param _str:
    :return: bool
    """
    for i in range(1, len(_str)):
        if is_operator(_str[i]) and is_operator(_str[i - 1]):
            return False
    return True


def calculate(equation):
    """
    Calculates The Final Result
    :param equation:
    :return:
    """
    if len(equation) == 0:
        return CalcError.FormatError.value
    if not is_symbol_permitted_equation(equation):
        return CalcError.SymbolError.value
    if has_edge_operator(equation):
        return CalcError.FormatError.value
    if not is_correct_sequence(equation):
        return CalcError.FormatError.value
    equation_parser = EquationParser(equation)
    equation_parser.build()
    res = equation_parser.calculate()
    if res[0] == "error":
        return res[1].value
    return str(res[1])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        eq = sys.argv[1]
        print(calculate(eq))
    else:
        print("(Error: Please Enter the Equation in Correct Format)")
