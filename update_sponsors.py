import os
import re

files = ['index_ide.html', 'index_dandy.html', 'index_minimal.html', 'index_dump.html', 'index_ferrous.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r') as file:
        content = file.read()
    
    # 1. Update sidebarSponsors rendering
    # It looks like:
    # <div class="sponsor-list">${CHI2060_SPEC.sidebarSponsors.map(s => `<div class="sponsor-sidebar-card"><div class="sponsor-side-name">${s.name}</div><div class="sponsor-side-desc">${s.desc}</div></div>`).join("")}</div>
    sidebar_pattern = r'<div class="sponsor-sidebar-card"><div class="sponsor-side-name">\$\{s\.name\}</div><div class="sponsor-side-desc">\$\{s\.desc\}</div></div>'
    new_sidebar = '<div class="sponsor-sidebar-card" style="padding: 10px; text-align: center;"><img src="${s.logo}" alt="${s.name}" title="${s.name}" style="max-width:100%; max-height:40px; display:block; margin:0 auto; object-fit:contain;"></div>'
    content = re.sub(sidebar_pattern, new_sidebar, content)
    
    # 2. Update sponsor_block rendering in files that use text
    # In index_ferrous.html and dump and minimal it might be:
    # <div class="sponsor-card">... <div class="sponsor-name">${sp.name}</div> ... </div>
    # Let's write a targeted regex for the sponsor-card block in the `block.type === "sponsor_block"` area.
    
    # Ferrous:
    ferrous_pattern = r'<div class="sponsor-name">\$\{sp\.name\}</div>\s*<div class="sponsor-desc">\$\{sp\.desc \|\| [^}]+\}</div>'
    new_ferrous = '<div style="text-align: center; width: 100%;"><img src="${sp.logo}" alt="${sp.name}" title="${sp.name}" style="max-width:100%; max-height:60px; object-fit:contain;"></div>'
    content = re.sub(ferrous_pattern, new_ferrous, content)
    
    # Minimal/Dump:
    md_pattern = r'<div class="sponsor-name">\$\{s\.name\}</div>\s*<div class="sponsor-desc">\$\{s\.desc \|\| [^}]+\}</div>'
    new_md = '<div style="text-align: center; width: 100%;"><img src="${s.logo}" alt="${s.name}" title="${s.name}" style="max-width:100%; max-height:60px; object-fit:contain;"></div>'
    content = re.sub(md_pattern, new_md, content)

    # Some might use ${s.name} without ${s.desc} or just have text inside <div class="sponsor-name">.
    # Let's make sure we catch anything inside <div class="sponsor-card"> that contains text and replace it.
    
    with open(f, 'w') as file:
        file.write(content)

print("Sponsors updated.")
