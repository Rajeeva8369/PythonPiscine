
from operations import basic_ops
from operations import advanced_ops

def do_op(a: int, b: int, op: str) -> float | int | None:
    match op:
        case '+':
            return basic_ops.add(a, b)
        case '-':
            return basic_ops.subtract(a, b)
        case '*':
            return advanced_ops.multiply(a, b)
        case '/':
            return advanced_ops.safe_divide(a, b)
        case _:
            print(f"Opération '{op}' non reconnue")
            return None

# Tests
print(do_op(1, 1, '+'))  # 2
print(do_op(1, 1, '-'))  # 0
print(do_op(11, 11, '*')) # 121
print(do_op(2, 2, '/'))   # 1.0
print(do_op(2, 0, '/'))   # Impossible de diviser par zéro, retourne None

