def change_separator(base_str: str, split_str: str, join_str: str) -> str:
    parts = base_str.split(split_str)

    middle_parts = parts[1:-1]

    return join_str.join(middle_parts)


print(change_separator(
    'Hello, world, my name is Leah, how are you ?',
    ', ',
    ' - '
))




def sub_index(base_str: str, sub_str: str) -> str:
    idx = base_str.find(sub_str)

    return base_str[idx + len(sub_str):] if idx != -1 else base_str


print(sub_index(
    'Hello, world, my name is Leah, how are you ?',
    'my name is '
))





def replace_str(base_str: str, sub_str: str) -> str:
    return base_str.replace(sub_str, "Egg and Spam")


print(replace_str(
    'Hello Leahh, my name is Leah, how are you ?',
    'Leah'
))






def normalize_input(base_str: str) -> (str, str):
    return base_str.lower(), base_str.upper()


print(normalize_input('Hello LeAh, hOW aRE YOu ?'))





def remove_white_spaces(base_str: str) -> (str, str, str):

    return base_str.strip(), base_str.lstrip(), base_str.rstrip()


print(remove_white_spaces(' \t\tMy name is Leah.\t\t\t \t'))
