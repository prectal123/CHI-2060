import re

with open('specifications.js', 'r') as f:
    content = f.read()

content = re.sub(r'desc: "Suitable for ', 'desc: "This subcommittee is suitable for ', content)

with open('specifications.js', 'w') as f:
    f.write(content)

print("Fixed suitable.")
