import re

with open('index_dump.html', 'r') as f:
    content = f.read()

# 1. Update the block title rendering
old_title_logic = r'if \(block\.title\) \{\s*html \+= `<h3 class="block-title">\$\{block\.title\}</h3>`;\s*\}'
new_title_logic = """if (block.title) {
              if (block.title === "Full Program") {
                html += `<h3 class="block-title" style="cursor:pointer; display:flex; justify-content:space-between; align-items:center;" onclick="const content = this.nextElementSibling; const icon = this.querySelector('ion-icon'); if(content.style.display==='none'){content.style.display='block'; icon.name='chevron-up-outline';}else{content.style.display='none'; icon.name='chevron-down-outline';}">${block.title} <ion-icon name="chevron-up-outline"></ion-icon></h3><div class="full-program-collapsible">`;
              } else {
                html += `<h3 class="block-title">${block.title}</h3>`;
              }
            }"""
content = re.sub(old_title_logic, new_title_logic, content)

# 2. Add the closing div right before the end of the block loop
old_end_logic = r'(\s*html \+= `\s*</div>\s*</div>\s*`;\s*\}\);)'
new_end_logic = r"""            if (block.title === "Full Program") {
              html += `</div>`;
            }
\1"""
content = re.sub(old_end_logic, new_end_logic, content)

with open('index_dump.html', 'w') as f:
    f.write(content)

print("Accordion added.")
