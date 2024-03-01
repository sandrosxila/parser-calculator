"""
Author: Sandro Skhirtladze
"""
import enum


class CalcError(enum.Enum):
    """
    Collection of Error Types
    """

    def __str__(self):
        return str(self.value)

    DivisionError = "(Error: divide by 0)"
    SymbolError = "( Error: Equation Contains Unpermitted Symbol )"
    FormatError = "( Error: Please Enter the Equation in Correct Format )"
