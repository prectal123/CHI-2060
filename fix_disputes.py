import os
import re

files = ['index_ide.html', 'index_dandy.html', 'index_minimal.html', 'index_dump.html', 'index_ferrous.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r') as file:
        content = file.read()
    
    # 1. Remove upvote badge
    content = re.sub(r'<span class="badge-tag \${d\.badgeClass}">\${d\.badge}</span>\s*', '', content)
    
    # 2. Replace activity metrics
    pattern = r'<div class="board-reply">\s*<div class="board-reply-hdr">\s*<ion-icon name="[^"]+"></ion-icon>\${d\.replyHeader}\s*</div>\s*<p class="board-reply-text">\${d\.replyText}</p>\s*</div>'
    replacement = r'<div style="margin-top: 1rem;"><p class="board-reply-text" style="font-style:italic;">${d.replyText}</p></div>'
    content = re.sub(pattern, replacement, content)
    
    with open(f, 'w') as file:
        file.write(content)

print("Python script done.")
