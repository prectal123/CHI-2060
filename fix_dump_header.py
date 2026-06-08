import re

with open('index_dump.html', 'r') as f:
    content = f.read()

# 1. Update visual-header-banner CSS
# Change background to white, text to black, add bottom border
content = re.sub(r'background-image: linear-gradient[^;]+;', 'background: #ffffff; border-bottom: 1px solid var(--color-border);', content)
content = re.sub(r'color: #ffffff;', 'color: var(--text-main);', content)

# 2. Remove "CONTINUOUS DATA FEED (ALL NODES)" along with its icon and container if needed
# We can just remove the whole <div class="toolbar-info">...</div> since it only contained that text and icon
# Or just remove the text and icon.
content = re.sub(r'<div class="toolbar-info">\s*<ion-icon name="list-outline"></ion-icon>\s*<span>CONTINUOUS DATA FEED \(ALL NODES\)</span>\s*</div>', '', content)

with open('index_dump.html', 'w') as f:
    f.write(content)

print("Header banner updated.")
