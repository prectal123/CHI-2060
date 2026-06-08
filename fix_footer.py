import os
import re

files = ['index_ide.html', 'index_dandy.html', 'index_minimal.html', 'index_dump.html', 'index_ferrous.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r') as file:
        content = file.read()
    
    # 1. Replace copyright text
    content = re.sub(r'© 2060 ACM CHI Steering Committee[^<]*', '© 2060 • ACM SIGCHI', content)
    
    # 2. Delete inquiries text
    inquiry_pattern = r'For general inquiries.*?Hosted on the Somatic Agentic Node Network\.'
    content = re.sub(inquiry_pattern, '', content, flags=re.DOTALL)
    
    with open(f, 'w') as file:
        file.write(content)

print("Footer updated.")
