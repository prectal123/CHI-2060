import re

with open('index_dump.html', 'r') as f:
    content = f.read()

# 1. Fonts
content = content.replace('family=Outfit:', 'family=Inter:')
content = content.replace("'Outfit'", "'Inter'")

# 2. Colors
# Change bg-body to white, borders to black, text to black/gray
# --bg-body: #f8fafc; -> #ffffff;
# --bg-light: #f1f5f9; -> #ffffff;
content = re.sub(r'--bg-body:\s*#[a-f0-9]+;', '--bg-body: #ffffff;', content)
content = re.sub(r'--bg-light:\s*#[a-f0-9]+;', '--bg-light: #ffffff;', content)
content = re.sub(r'--color-border:\s*#[a-f0-9]+;', '--color-border: #111111;', content)
content = re.sub(r'--color-border-dark:\s*#[a-f0-9]+;', '--color-border-dark: #111111;', content)
content = re.sub(r'--text-main:\s*#[a-f0-9]+;', '--text-main: #000000;', content)
content = re.sub(r'--text-secondary:\s*#[a-f0-9]+;', '--text-secondary: #000000;', content)
content = re.sub(r'--text-muted:\s*#[a-f0-9]+;', '--text-muted: #555555;', content)
content = re.sub(r'--color-link:\s*#[a-f0-9]+;', '--color-link: #000000;', content)
content = re.sub(r'--color-link-hover:\s*#[a-f0-9]+;', '--color-link-hover: #555555;', content)

# 3. Remove border-radius and box-shadow entirely
content = re.sub(r'\s*border-radius:\s*[^;]+;', '', content)
content = re.sub(r'\s*box-shadow:\s*[^;]+;', '', content)

with open('index_dump.html', 'w') as f:
    f.write(content)

print("index_dump.html updated to minimal styling.")
