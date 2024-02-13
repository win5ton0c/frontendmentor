import re

text = """
Bright orange: hsl(31, 77%, 52%)
Dark cyan: hsl(184, 100%, 22%)
Very dark cyan: hsl(179, 100%, 13%)
"""

lines = text.strip().split("\n")
css_variables = ":root {\n"

for line in lines:
    name, value = line.split(":")
    name = name.strip()[2:].replace(" ", "_").replace("(", "_").replace(")", "").lower()
    value = value.strip()
    css_variables += f"  --{name}: {value};\n"

css_variables += "}"

print(css_variables)