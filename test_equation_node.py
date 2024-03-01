"""
tests for EquationNode Class
"""
from equation_node import EquationNode
from equation_enums import CalcOperators


def test_constructor():
    """
    test for EquationNode constructor
    """
    parent_node = EquationNode(None, None, None, CalcOperators.Equality)
    left_node = EquationNode(parent_node, None, None, CalcOperators.Addition)
    assert parent_node.operator == CalcOperators.Equality
    assert left_node.parent == parent_node
    assert left_node.operator == CalcOperators.Addition


def test_setters_and_getters():
    """
    test for equation getter and setter functions
    """

    parent_node = EquationNode(None, None, None, CalcOperators.Equality)
    left_node = EquationNode(None, None, None, None)
    right_node = EquationNode(None, None, None, None)

    left_node.set_operator(CalcOperators.Addition)
    assert left_node.operator == CalcOperators.Addition
    right_node.set_operator(CalcOperators.Subtraction)
    assert right_node.operator == CalcOperators.Subtraction

    left_node.set_parent(parent_node)
    assert left_node.parent == parent_node
    right_node.set_parent(parent_node)
    assert right_node.parent == parent_node

    parent_node.set_left(left_node)
    assert parent_node.left == left_node
    parent_node.set_right(right_node)
    assert parent_node.right == right_node

    assert parent_node.get_left() == left_node
    assert parent_node.get_right() == right_node
    assert parent_node.get_operator() == CalcOperators.Equality
    assert left_node.get_parent() == parent_node
    assert right_node.get_parent() == parent_node
