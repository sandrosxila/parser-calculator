"""
Tests for calculator
Made by Sandro Skhirtladze
"""
import calc


def test_permitted_operators():
    """
    test for permitted operators
    """
    assert calc.permitted_operators() == ['+', '-', '*', '/']


def test_permitted_symbols():
    """
    test for permitted symbols
    """
    assert calc.permitted_symbols() == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def test_is_operator():
    """
    test for operator checker
    """
    assert calc.is_operator('+')
    assert calc.is_operator('-')
    assert calc.is_operator('*')
    assert calc.is_operator('/')
    assert not calc.is_operator('9')
    assert not calc.is_operator('&')
    assert not calc.is_operator('(')
    assert not calc.is_operator(')')
    assert not calc.is_operator('a')
    assert not calc.is_operator('//')
    assert not calc.is_operator('95')
    assert not calc.is_operator('&^()')


def test_is_symbol_permitted_equation():
    """
    test for permitted symbol checker
    """
    assert calc.is_symbol_permitted_equation('+')
    assert calc.is_symbol_permitted_equation('-')
    assert calc.is_symbol_permitted_equation('*')
    assert calc.is_symbol_permitted_equation('/')
    assert calc.is_symbol_permitted_equation('9')
    assert calc.is_symbol_permitted_equation('95')
    assert calc.is_symbol_permitted_equation('9+5')
    assert not calc.is_symbol_permitted_equation('%')
    assert not calc.is_symbol_permitted_equation('&')
    assert not calc.is_symbol_permitted_equation('(')
    assert not calc.is_symbol_permitted_equation(')')
    assert not calc.is_symbol_permitted_equation('a')
    assert not calc.is_symbol_permitted_equation('9a')
    assert calc.is_symbol_permitted_equation('//')
    assert calc.is_symbol_permitted_equation('9//5')
    assert not calc.is_symbol_permitted_equation('9&5')
    assert not calc.is_symbol_permitted_equation('&^()')


def test_has_edge_operator():
    """
    test for unwanted characters at the edges
    """
    assert calc.has_edge_operator("+9")
    assert calc.has_edge_operator("9+")
    assert calc.has_edge_operator("+9+")
    assert calc.has_edge_operator("+9+6")
    assert calc.has_edge_operator("8+9+")
    assert not calc.has_edge_operator("8+9+25")


def test_is_correct_sequence():
    """
    test for sequence checker
    """
    assert calc.is_correct_sequence("8+9+25")
    assert calc.is_correct_sequence("8+9-25/99*5")
    assert not calc.is_correct_sequence("8+9++25")
    assert not calc.is_correct_sequence("8+9+-25")
    assert not calc.is_correct_sequence("8+9/-25")


def test_calculate():
    """
    tests for calculator
    """
    assert calc.calculate("") == "( Error: Please Enter the Equation in Correct Format )"
    assert calc.calculate("10+5") == str(15)
    assert calc.calculate("10-5") == str(5)
    assert calc.calculate("10*3") == str(30)
    assert calc.calculate("10/5") == str(2)
    assert calc.calculate("10/3") == str(3)
    assert calc.calculate("9/10") == str(1)
    assert calc.calculate("10/4") == str(3)
    assert calc.calculate("10/0") == "(Error: divide by 0)"
    assert calc.calculate("10.4+3.5") == "( Error: Equation Contains Unpermitted Symbol )"
    assert calc.calculate("abcd+efg") == "( Error: Equation Contains Unpermitted Symbol )"
    assert calc.calculate("a10+3b") == "( Error: Equation Contains Unpermitted Symbol )"
    assert calc.calculate("10++3") == "( Error: Please Enter the Equation in Correct Format )"
    assert calc.calculate("-10+5") == "( Error: Please Enter the Equation in Correct Format )"
    assert calc.calculate("1+5+1") == str(7)
    assert calc.calculate("1+5+1-2") == str(5)
    assert calc.calculate("3+10/3+13/3") == str(11)
    assert calc.calculate("10/2*3") == str(2)
    assert calc.calculate("10/2*3+3") == str(5)
    assert calc.calculate("10/2*3+-3") == "( Error: Please Enter the Equation in Correct Format )"
    assert calc.calculate("10/(2*3+3)") == "( Error: Equation Contains Unpermitted Symbol )"

    # my tests:
    assert calc.calculate("+10") == "( Error: Please Enter the Equation in Correct Format )"
    assert calc.calculate("10") == str(10)
    assert calc.calculate("10-") == "( Error: Please Enter the Equation in Correct Format )"
    assert calc.calculate("-10/3") == "( Error: Please Enter the Equation in Correct Format )"
    assert calc.calculate("25/5++6") == "( Error: Please Enter the Equation in Correct Format )"
    assert calc.calculate("23+26a-8501t") == "( Error: Equation Contains Unpermitted Symbol )"
    assert calc.calculate("205+6-9/0") == "(Error: divide by 0)"
    assert calc.calculate("39/16-21-20/0*22+9+32/28*33*2-8+36+40/40") == "(Error: divide by 0)"
    assert calc.calculate("39/16-21-20/39*22+9+32/28*0*2-8+36+40/40") == "(Error: divide by 0)"
    assert calc.calculate("39/16-21-20/39*22+9+32/28*55*0-8+36+40/40") == "(Error: divide by 0)"
    assert calc.calculate("39/16-21-20/39*22+9+32/28*55*12-8+36+40/0") == "(Error: divide by 0)"
    assert calc.calculate("10/3+10/3") == str(7)
    assert calc.calculate("3+2") == str(5)
    assert calc.calculate("3-2") == str(1)
    assert calc.calculate("3*2") == str(6)
    assert calc.calculate("3/2") == str(2)
    assert calc.calculate("32-52") == str(-20)
    assert calc.calculate("39/16-21-20/39*22+9+32/28*33*2-8+36+40/40") == str(19)
    assert calc.calculate("2-39-37-26*21/9+37-14+25-30/29+23/22/30/12") == str(-88)
    assert calc.calculate("16348-35509+12833/19037+13798-4346-25849*" +
                          "6087*11668-4769-9605+13934/26324/27774-20032") == str(-1835876569598)
    assert calc.calculate("16348-35509+12833/19037+13798-4346-25849*" +
                          "6087*11668-4769-9605+13934/26324/27774-20032-1/2") == str(-1835876569599)
    assert calc.calculate(
        "191*83+250-164/88/88+44-215*236*132*94*354/79" +
        "-153/181*62-384+55-128/77/188+187/372-346/315-189*73+267+227/71" +
        "+309*152/182*264-237/72+217-393+124-317-50*203-336" +
        "*121/173/313/12-303+157/154/164-219-356/388-99*286+162*282" +
        "*181*189+292-201/140+246*50/395/8/232/251-144-289/261+301" +
        "*219-48+1+10/301*306*44*105/8/164/22*296*225*280" +
        "+359+234-395*305*52+389-192/196-233/20/68+207+337") == str(-1264594822)
