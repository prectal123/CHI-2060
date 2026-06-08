import os
import re

files = ['index_ide.html', 'index_dandy.html', 'index_minimal.html', 'index_dump.html', 'index_ferrous.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r') as file:
        content = file.read()
    
    # Replace Human Seeder Name
    content = re.sub(r'Human Seeder Name(?=</label>)', 'name of human researcher', content)
    
    # Replace Nationality
    content = re.sub(r'Nationality(?=</label>)', 'nationality of human researcher', content)
    
    # Replace Primary Area of Interest -> Wickathon registration
    content = re.sub(r'Primary Area of Interest(?=</label>)', 'Wickathon registration', content)
    
    # Replace the options
    options_pattern = re.compile(r'<select id="reg-interest"[^>]*>.*?</select>', re.DOTALL)
    
    new_options = '''<select id="reg-interest" class="form-input">
                        <option value="climate">Climate Change</option>
                        <option value="mental_health">Mental Health</option>
                        <option value="inequality">Inequality</option>
                      </select>'''
    
    # In index_ferrous.html, the class might be different, let's keep the existing opening tag.
    def replacer(match):
        select_open = re.search(r'<select[^>]*>', match.group(0)).group(0)
        return f'''{select_open}
                        <option value="climate">Climate Change</option>
                        <option value="mental_health">Mental Health</option>
                        <option value="inequality">Inequality</option>
                      </select>'''

    content = options_pattern.sub(replacer, content)
    
    with open(f, 'w') as file:
        file.write(content)

print("Registration form update done.")
