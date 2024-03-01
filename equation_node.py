"""
Author: Sandro Skhirtladze
"""


class EquationNode:
    """
    Class for Equation Parser Tree Node
    """

    def __init__(self, parent, left, right, operator):
        """
        Constructor For Multiple Assignments
        :param parent:
        :param left:
        :param right:
        :param operator:
        """
        self.parent = parent
        self.left = left
        self.right = right
        self.operator = operator

    def set_parent(self, parent):
        """
        :param parent:
        :return:
        """
        self.parent = parent

    def get_parent(self):
        """
        :return:
        """
        return self.parent

    def set_left(self, left):
        """

        :param left:
        :return:
        """
        self.left = left

    def get_left(self):
        """

        :return:
        """
        return self.left

    def set_right(self, right):
        """

        :param right:
        :return:
        """
        self.right = right

    def get_right(self):
        """

        :return:
        """
        return self.right

    def set_operator(self, operator):
        """

        :param operator:
        :return:
        """
        self.operator = operator

    def get_operator(self):
        """

        :return:
        """
        return self.operator
