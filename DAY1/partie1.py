
def multiply(a: int, b: int) -> int:

    return a * b

result = multiply(2,2)
print(result)





def compare(a: int, b: int) -> int:
    if a > b:
        print (" Le premier nombre est plus grand que le second ")
    elif a < b :
            print(" Le premier nombre est plus petit que le second ")
    elif a == b:
        print(" Les deux nombres sont égaux ")

compare(1, 1)
compare(2, 1)
compare(-2,1)





def counting(x):
    print(*range(1, x + 1, 2), sep=", ")


counting(0)
counting(10)
counting(11)





def ask_user():
    while (mot := input("Entrez un mot (ou 'exit' pour quitter) : ")) != "exit":
        print(f"Vous avez entré : {mot}")

print (ask_user())




def safe_divide(a: int, b: int) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Impossible de diviser par zéro")
        return None


print(safe_divide(1, 2))
print(safe_divide(1, 0))




def display_square(size: int, char: str):
    for i in range(size):
        print(char * size)

display_square(1, '*')
display_square(5,'*')



