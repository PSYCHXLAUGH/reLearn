import re

text = "hello re"
match = re.findall(r"\w", text)

print(match)