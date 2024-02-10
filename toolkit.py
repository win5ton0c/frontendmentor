import re

text = """
- Light slate blue (background): hsl(252, 100%, 67%)
- Light royal blue (background): hsl(241, 81%, 54%)
- Violet blue (circle): hsla(256, 72%, 46%, 1)
- Persian blue (circle): hsla(241, 72%, 46%, 0)
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