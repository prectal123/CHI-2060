import os
import re

files = ['index_ide.html', 'index_dandy.html', 'index_minimal.html', 'index_dump.html', 'index_ferrous.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r') as file:
        content = file.read()
    
    # Update sidebarSponsors rendering logic
    pattern = r's => `\s*<div class="sponsor-sidebar-card" style="padding: 10px; text-align: center;"><img src="\$\{s\.logo\}" alt="\$\{s\.name\}" title="\$\{s\.name\}" style="max-width:100%; max-height:40px; display:block; margin:0 auto; object-fit:contain;"></div>\s*`'
    
    new_map = r's => s.type === "divider" ? `<div style="text-transform:uppercase; font-size:0.75rem; font-weight:bold; color:var(--text-muted, #888); border-bottom:1px solid var(--color-border, #ccc); margin-top:1.5rem; margin-bottom:0.5rem; padding-bottom:0.25rem;">${s.label}</div>` : `<div class="sponsor-sidebar-card" style="padding: 10px; text-align: center;"><img src="${s.logo}" alt="${s.name}" title="${s.name}" style="max-width:100%; max-height:40px; display:block; margin:0 auto; object-fit:contain;"></div>`'
    
    content = re.sub(pattern, new_map, content)
    
    with open(f, 'w') as file:
        file.write(content)

print("Dividers updated.")
