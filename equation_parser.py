"""
Author: Sandro Skhirtladze
"""
from equation_node import EquationNode
from equation_enums import CalcOperators
from calc_error import CalcError


class EquationParser:
    """
    Class for Parser Tree
    """

    def __init__(self, _str):
        """
        initialize Parser Tree
        :param _str:
        """
        self.equation = _str
        self.stack = [EquationNode(None, None, None, CalcOperators.Equality)]

    def undermine(self):
        """
        splitting the equation input into the list that \n
        contains either the strings having only numbers or \n
        the sequence of the symbols that doesn't contain digits
        :return: List[str]
        """
        equation_parts = []
        equation_part = ""
        for i in self.equation:
            if (
                    (len(equation_part) == 0)
                    or
                    (i.isdigit() and equation_part[-1].isdigit())
                    or
                    not (i.isdigit()) and not (equation_part[-1].isdigit())
            ):
                equation_part += i
            else:
                equation_parts.append(equation_part)
                equation_part = i
        equation_parts.append(equation_part)
        return equation_parts

    def get_parent(self, priority):
        while priority <= self.stack[-1].get_operator().value:
            self.stack.pop()
        return self.stack[-1]

    def make_node(self, _chr, _num):
        """
        Node Creator Dispatcher
        :param _chr:
        :param _num:
        :return:
        """
        _dispatch = {
            '+': CalcOperators.Addition,
            '-': CalcOperators.Subtraction,
            '*': CalcOperators.Multiplication,
            '/': CalcOperators.Division
        }
        _operation = _dispatch.get(_chr)
        parent = self.get_parent(_operation.value)
        new_node = EquationNode(parent, parent.get_right(), _num, _operation)
        parent.set_right(new_node)
        self.stack.append(new_node)

    def build(self):
        """
        Parser Tree Builder
        :return:
        """
        equation_parts = self.undermine()
        self.stack[0].set_right(float(equation_parts[0]))
        operator_index = 1

        while operator_index < len(equation_parts):
            operator_symbol = equation_parts[operator_index]
            self.make_node(operator_symbol, float(equation_parts[operator_index + 1]))
            operator_index += 2

    def calc(self, _current):
        """
        Calculator
        :param _current:
        :return:
        """
        if isinstance(_current, float):
            return ["success", _current]
        # if _current.get_left() is None:
        #     return ["success", _current.get_right()]
        # if _current.get_right() is None:
        #     return ["success", _current.get_left()]

        left = self.calc(_current.get_left())
        right = self.calc(_current.get_right())

        if (
                left[1] == CalcError.DivisionError or
                right[1] == CalcError.DivisionError or
                (_current.get_operator() == CalcOperators.Division and right[1] == float(0))
        ):
            return ["error", CalcError.DivisionError]

        dispatch = {
            CalcOperators.Addition: ["success", left[1] + right[1]],
            CalcOperators.Subtraction: ["success", left[1] - right[1]],
            CalcOperators.Multiplication: ["success", left[1] * right[1]],
            CalcOperators.Division: ["success", left[1] / right[1] if right[1] != 0 else left[1]]
        }

        return dispatch.get(_current.get_operator())

    def calculate(self):
        """
        public Calculator
        :return: result of Equation
        """
        res = self.calc(self.stack[0].get_right())
        if res[0] != "error":
            res[1] = int((res[1] / abs(res[1])) * int(abs(res[1]) + 0.5))
        return res
