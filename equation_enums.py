"""
Author: Sandro Skhirtladze
"""
import enum


class CalcOperators(enum.Enum):
    """
    Enums for Arithmetic Operations
    """
    Equality = int(0)
    Addition = int(1)
    Subtraction = int(2)
    Division = int(3)
    Multiplication = int(4)
