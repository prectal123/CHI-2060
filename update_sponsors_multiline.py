import os
import re

files = ['index_ide.html', 'index_dandy.html', 'index_minimal.html', 'index_dump.html', 'index_ferrous.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r') as file:
        content = file.read()
    
    # 1. Update sidebarSponsors rendering (multiline or singleline)
    sidebar_pattern = r'<div class="sponsor-sidebar-card">\s*<div class="sponsor-side-name">\$\{s\.name\}</div>\s*<div class="sponsor-side-desc">\$\{s\.desc\}</div>\s*</div>'
    new_sidebar = '<div class="sponsor-sidebar-card" style="padding: 10px; text-align: center;"><img src="${s.logo}" alt="${s.name}" title="${s.name}" style="max-width:100%; max-height:40px; display:block; margin:0 auto; object-fit:contain;"></div>'
    content = re.sub(sidebar_pattern, new_sidebar, content)

    # 2. Update sponsor_block rendering in Ferrous
    ferrous_pattern = r'<div class="sponsor-card">\s*<div class="sponsor-name">\$\{sp\.name\}</div>\s*<div class="sponsor-desc">\$\{sp\.desc \|\| [^}]+\}</div>\s*</div>'
    new_ferrous = '<div class="sponsor-card" style="padding: 10px; text-align: center;"><img src="${sp.logo}" alt="${sp.name}" title="${sp.name}" style="max-width:100%; max-height:60px; object-fit:contain; display:block; margin:0 auto;"></div>'
    content = re.sub(ferrous_pattern, new_ferrous, content)
    
    with open(f, 'w') as file:
        file.write(content)

print("Sponsors updated multiline.")
