import re

pattern = r"at"
text = "The cat sat on the mat."

matches = re.findall(pattern, text)
print(matches)