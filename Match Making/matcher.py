
import re

text = '$100'

def symbol(sample):
    # Find all instances of the exact match '$'
    re.findall(r'\$', sample)

print(symbol(text))
