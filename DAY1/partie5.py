import sys

def list_discovery() -> list:
    if len(sys.argv) < 7:
        args = ["10", "20", "30", "40", "50", "hello"]
    else:
        args = sys.argv[1:7]

    numbers = [int(x) for x in args[:5]]

    numbers.sort(reverse=True)

    numbers.pop()

    print(f"Numbers has {len(numbers)} elements and the sum of them all is {sum(numbers)}.")

    numbers.append(args[5])

    return numbers

print(list_discovery())






import sys

def dict_creation() -> dict:

    args = sys.argv[1:] or ["nom", "Lexie", "age", "27", "ville", "Paris"]
    return dict(zip(args[::2], args[1::2]))


def dict_display(my_dict: dict):
    for key in my_dict.keys():
        print(key)

    for value in my_dict.values():
        print(value)

    for key, value in my_dict.items():
        print(f"Key: {key} - Value: {value}")


res = dict_creation()
dict_display(res)





def tuple_discovery(a, b, c, d) -> tuple:
    return (d, c, b, a)


def tuple_display(tpl: tuple):
    for element in tpl:
        print(element)


tpl = tuple_discovery(1, 2, 3, 4)
tuple_display(tpl)

try:
    tpl[0] = 99
except TypeError as e:
    print("Erreur :", e)








    def set_discovery(l1: list, l2: list) -> tuple[set, set, set, set]:
        set1 = set(l1)
        set2 = set(l2)

        union_result = set1 | set2

        intersection_result = set1 & set2

        difference_result = set1 - set2

        sym_diff_result = set1 ^ set2

        return (union_result, intersection_result, difference_result, sym_diff_result)


    l1 = [1, 2, 3, 4, 5]
    l2 = [10, 2, 4, 8, 12]

    res = set_discovery(l1, l2)

    for elem in res:
        print(elem)







def power_via_comprehension(numbers: list[int]) -> list[int]:
    return [n**2 if n < 0 else -n for n in numbers]

l = [1, -2, -3, 4, -5]
print(power_via_comprehension(l))





