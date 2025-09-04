
def struct_index_display(elems):
    for elem_id, elem in enumerate(elems):
        print(f"{elem_id} = {elem}")


struct_index_display([1, 2, 3, 4, 5])




def combine_lists(l1: list, l2: list) -> None | list:
    if len(l1) != len(l2):
        return None

    return list(zip(l1, l2))


res = combine_lists([1, 2, 3], [4, 5, 6])
print(res)  # [(1, 4), (2, 5), (3, 6)]

res = combine_lists([1, 2], [4, 5, 6])
print(res)  # None




def display_combined_lists(l: list):
    for elem_id, (elem1, elem2) in enumerate(l):
        print(f"{elem_id} = {elem1} - {elem2}")

res = combine_lists([1, 2, 3], [4, 5, 6])
display_combined_lists(res)





def remove_negatives(numbers: list[float]) -> list[float]:
    return [n for n in numbers if n >= 0]


t = remove_negatives([-1, 2, 3, 4, -5, 6, 7])
print(t)




def keep_strings(elements: list) -> list[str]:
    return [elem for elem in elements if isinstance(elem, str)]


t = keep_strings(['Hello', 1, 3, "spam", 5.5, (1, 2)])
print(t)





def cut_in_two(numbers: list[float]) -> (list[float], list[float]):
    n = len(numbers)
    mid = n // 2
    return numbers[:mid], numbers[mid:]


t = cut_in_two([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(t)



