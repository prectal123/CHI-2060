import re
import os

with open('specifications.js', 'r') as f:
    spec = f.read()

logos = re.findall(r'logo:\s*"([^"]+)"', spec)
missing = []
for logo in logos:
    if not os.path.exists(logo):
        missing.append(logo)

print("Missing logos:", set(missing))
