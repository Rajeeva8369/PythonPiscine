def fix_ip(ip: str) -> str | None:
    parts = ip.split('.')

    if len(parts) != 4:
        return None

    try:
        nums = [int(p) for p in parts]

        if any(n < 0 or n > 255 for n in nums):
            return None

        return '.'.join(str(n) for n in nums)

    except ValueError:
        return None


print(fix_ip('0.0.0.0'))
print(fix_ip('156.183.193.1'))
print(fix_ip('010.184.00242.056'))
print(fix_ip('000010.00000.0295.10'))
print(fix_ip('0.0.0.324'))
print(fix_ip('0.0.0.0.0'))





import re

def simple_pattern_search(phrase: str) -> bool:
    return bool(re.search(r'eggs\d+', phrase))


print(simple_pattern_search("I love eggs203, can I have some please ?"))
print(simple_pattern_search("I love eggs, can I have some please ?"))
print(simple_pattern_search("No eggs123 here"))
print(simple_pattern_search("Nothing to see here"))





import re

def extract_emails(phrase: str) -> list[str]:
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, phrase)

text = "Please contact us at support@example.com or sales@example.org."
emails = extract_emails(text)
print(emails)




import re

def extract_hashtags(message: str) -> list[str]:
    pattern = r'#\w+'
    return re.findall(pattern, message)

msg = "Loving the #Python and #regex exercises from #EDS #DataPoolDigi2!"
hashtags = extract_hashtags(msg)
print(hashtags)




import re

def split_on_pattern(message: str) -> list[str]:
    pattern = r'\d+\.\n'
    return re.split(pattern, message)


msg = "Today, Leah is 25 years old. Meaning she was born in 1994.\nMaybe I have to check my maths !"
parts = split_on_pattern(msg)
print(parts)






import re


def date_conversion(text: str) -> str:
    pattern = r'(\d{4})-(\d{2})-(\d{2})'

    return re.sub(pattern, r'\3/\2/\1', text)


text = "Today's date is 2024-01-15 and tomorrow will be 2024-01-16."
converted_text = date_conversion(text)
print(converted_text)




