import os
import re

files = ['index_ide.html', 'index_dandy.html', 'index_minimal.html', 'index_dump.html', 'index_ferrous.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r') as file:
        content = file.read()
    
    # 1. Remove the checkbox HTML
    pattern_html = r'<div class="form-group">\s*<label class="form-checkbox-label">\s*<input type="checkbox" id="reg-check"[^>]*>\s*<span>\$\{f\.agreeLabel\}</span>\s*</label>\s*</div>'
    
    # Wait, in some templates, class could be different or there might not be a div class form-group. 
    # Just to be safe, I'll match the <label class="form-checkbox-label">...</label> part, or the entire block.
    # Actually, in Ferrous, the checkbox HTML might look slightly different:
    # let's write a flexible regex.
    pattern_html_flex = r'<div class="form-group">\s*<label class="form-checkbox-label">\s*<input type="checkbox" id="reg-check"[^>]*>\s*<span>\$\{f\.agreeLabel\}</span>\s*</label>\s*</div>'
    
    # Wait, if `f.agreeLabel` was rendered as "undefined", that's because `f` didn't have `agreeLabel`.
    # Let's just remove the `<div class="form-group">...id="reg-check"...</div>`
    content = re.sub(r'<div class="form-group">\s*<label class="form-checkbox-label">\s*<input type="checkbox" id="reg-check".*?</label>\s*</div>', '', content, flags=re.DOTALL)
    
    # Ferrous might not use form-group or form-checkbox-label exactly.
    # Let's do a broader regex if it fails. Let's first replace the common one.
    
    # 2. Update checkFormStatus JS
    content = re.sub(r'const chk = document\.getElementById\("reg-check"\)\.checked;\s*', '', content)
    content = re.sub(r'&& chk ', '', content)
    
    with open(f, 'w') as file:
        file.write(content)

print("Checkbox removal done.")
