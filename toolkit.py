import re

text = """
- White: hsl(0, 0%, 100%)
- Pale blue: hsl(221, 100%, 96%)
- Light lavender: hsl(241, 100%, 89%)
- Dark gray blue: hsl(224, 30%, 27%)
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