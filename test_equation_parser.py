"""
tests for equation parser
"""
import collections
import pytest
from equation_parser import EquationParser, EquationNode, CalcError, CalcOperators


def compare(_x, _y):
    """
    check if two lists are identical
    """
    return collections.Counter(_x) == collections.Counter(_y)


def test_constructor():
    """
    test the constructor of EquationParser
    """
    equation_parser = EquationParser("25+7")
    assert equation_parser.equation == "25+7"
    assert equation_parser.stack[-1].operator == CalcOperators.Equality


def test__undermine():
    """
    Check for method __undermine
    """
    assert compare(EquationParser("9+16").undermine(), ['9', '+', '16'])
    assert compare(EquationParser("9-16+25").undermine(), ['9', '-', '16', '+', '25'])
    assert compare(EquationParser("24&98#89").undermine(), ['24', '&', '98', '#', '89'])
    assert compare(EquationParser("--5").undermine(), ['--', '5'])
    assert compare(EquationParser("-5+").undermine(), ['-', '5', '+'])


def test__get_parent():
    """
    check for method __get_parent
    """
    equation_parser = EquationParser("1+1")
    root = equation_parser.stack[0]
    assert equation_parser.get_parent(1) == root
    root_child = EquationNode(root, root.get_right(), 1, CalcOperators.Addition)
    equation_parser.stack.append(root_child)
    assert equation_parser.get_parent(2) == root_child
    assert equation_parser.get_parent(1) == root
    with pytest.raises(IndexError):
        equation_parser.get_parent(0)


def test__make_node():
    """
    check for method __make_node
    """
    equation_parser = EquationParser("1+2-9+12")
    root = equation_parser.stack[0]
    root.set_right('1')
    equation_parser.make_node('+', '2')
    assert root.get_right() == equation_parser.stack[-1]
    equation_parser.make_node('-', '9')
    assert root.get_right().get_right() == equation_parser.stack[-1]
    equation_parser.make_node('+', '12')
    assert root.get_right() == equation_parser.stack[-1]
    assert root.get_right().get_right() != equation_parser.stack[-1]


def test_build():
    """
    check if the method build a parser tree correctly
    """
    equation_parser = EquationParser("1+2")
    equation_parser.build()
    root = equation_parser.stack[0]
    assert root.get_right().get_left() == 1
    assert root.get_right().get_operator() == CalcOperators.Addition
    assert root.get_right().get_right() == 2

    equation_parser = EquationParser("1+2-9")
    equation_parser.build()
    root = equation_parser.stack[0]
    assert root.get_right().get_left() == 1
    assert root.get_right().get_right().get_operator() == CalcOperators.Subtraction
    assert root.get_right().get_right().get_right() == 9
    assert root.get_right().get_right().get_left() == 2

    equation_parser = EquationParser("1+2-9+12")
    equation_parser.build()
    root = equation_parser.stack[0]
    assert root.get_right().get_right() == 12
    assert root.get_right().get_left().get_operator() == CalcOperators.Addition
    assert root.get_right().get_left().get_left() == 1
    assert root.get_right().get_left().get_right().get_operator() == CalcOperators.Subtraction
    assert root.get_right().get_left().get_right().get_left() == 2
    assert root.get_right().get_left().get_right().get_right() == 9


def test__calculate():
    """
    check for recursive method __calculate
    """
    equation_parser = EquationParser("10")
    equation_parser.build()
    res = equation_parser.calc(equation_parser.stack[0].get_right())
    assert compare(res, ['success', 10])

    equation_parser = EquationParser("10/3+10/3")
    equation_parser.build()
    res = equation_parser.calc(equation_parser.stack[0].get_right())
    assert compare(res, ['success', (10 / 3) + (10 / 3)])

    equation_parser = EquationParser("10/0+10/4")
    equation_parser.build()
    res = equation_parser.calc(equation_parser.stack[0].get_right())
    assert compare(res, ['error', CalcError.DivisionError])

    equation_parser = EquationParser("191*83+250-164/88/88+44-215*236*132*94*354/79" +
                                     "-153/181*62-384+55-128/77/188+187/372-346/315-189*73+267+227/71" +
                                     "+309*152/182*264-237/72+217-393+124-317-50*203-336" +
                                     "*121/173/313/12-303+157/154/164-219-356/388-99*286+162*282" +
                                     "*181*189+292-201/140+246*50/395/8/232/251-144-289/261+301" +
                                     "*219-48+1+10/301*306*44*105/8/164/22*296*225*280" +
                                     "+359+234-395*305*52+389-192/196-233/20/68+207+337")
    equation_parser.build()
    res = equation_parser.calc(equation_parser.stack[0].get_right())
    assert compare(res, ['success', -1264594822.3354511])


def test_calculate():
    """
    test for final calculation method
    """
    equation_parser = EquationParser("10/3+10/3")
    equation_parser.build()
    res = equation_parser.calculate()
    assert compare(res, ['success', 7])

    equation_parser = EquationParser("4*9/3+10/3-1")
    equation_parser.build()
    res = equation_parser.calculate()
    assert compare(res, ['success', 14])

    equation_parser = EquationParser("10/0*6+10/4")
    equation_parser.build()
    res = equation_parser.calculate()
    assert compare(res, ['error', CalcError.DivisionError])

    equation_parser = EquationParser("10/6*0+10/4")
    equation_parser.build()
    res = equation_parser.calculate()
    assert compare(res, ['error', CalcError.DivisionError])
