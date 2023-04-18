import re

string = "I love love to eat pizza but too much pizza gives me me a stomach ache"
result = re.sub(r'\b(\w+)\s+\1\b', r'\1', string)

print(result)
