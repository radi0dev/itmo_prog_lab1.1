# calculator.py

import ast
import operator as op

OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}


def help_message():
    print("calculates the value of an expression involving operations +, -, *, /")
    print("example: 2 + 3 * 4 - 1")
    print("example: (2 + 3) / 5")


def eval_expr(expr):
    node = ast.parse(expr, mode="eval")
    return _eval(node.body)


def _eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        operator = OPERATORS[type(node.op)]
        return operator(left, right)

    if isinstance(node, ast.UnaryOp):
        operand = _eval(node.operand)
        operator = OPERATORS[type(node.op)]
        return operator(operand)

    raise ValueError("unsupported expression")


def calculator():
    text = input("enter expression: ").strip()

    if text.lower() == "help":
        help_message()
        return

    try:
        result = eval_expr(text)
        print(result)
    except ZeroDivisionError:
        print("division by zero")
    except Exception:
        print("expression error")


calculator()
