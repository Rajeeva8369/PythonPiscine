
def multiply(a: int, b: int) -> int:
    return a * b

def safe_divide(a: int, b: int) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Impossible de diviser par zéro")
        return None
