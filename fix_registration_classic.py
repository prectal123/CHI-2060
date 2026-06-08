import re

with open('index_classic.html', 'r') as f:
    content = f.read()

old_form_logic = r'\} else if \(block\.type === "submission_form"\) \{.*?(?=\} else if \(block\.type === "timeline_block"\))'
new_form_logic = """} else if (block.type === "submission_form") {
          const f = block.form || {};
          html += `<div style="background:#fafafa; border:1px solid #ddd; padding:2rem; margin-top:1rem;">
            <form>
              <div style="margin-bottom:1.5rem;">
                <label style="display:block; font-weight:600; margin-bottom:0.5rem; color:#333;">Name of human researcher</label>
                <input type="text" style="width:100%; padding:0.6rem; border:1px solid #ccc; font-family:var(--font-sans);" placeholder="e.g. Dr. Ha-Jun Kim" required>
              </div>
              <div style="margin-bottom:1.5rem;">
                <label style="display:block; font-weight:600; margin-bottom:0.5rem; color:#333;">Nationality of human researcher</label>
                <input type="text" style="width:100%; padding:0.6rem; border:1px solid #ccc; font-family:var(--font-sans);" placeholder="e.g. South Korea" required>
              </div>
              <div style="margin-bottom:1.5rem;">
                <label style="display:block; font-weight:600; margin-bottom:0.5rem; color:#333;">Wickathon Registration</label>
                <select style="width:100%; padding:0.6rem; border:1px solid #ccc; font-family:var(--font-sans);">
                  <option value="climate">Climate Change</option>
                  <option value="mental_health">Mental Health</option>
                  <option value="inequality">Inequality</option>
                </select>
              </div>
              <div style="margin-bottom:1.5rem;">
                <label style="display:block; font-weight:600; margin-bottom:0.5rem; color:#333;">Agent Model Attachment (.soma, .safetensors)</label>
                <input type="file" style="width:100%; padding:0.6rem; border:1px solid #ccc; font-family:var(--font-sans);" accept=".soma,.safetensors,.json,.zip" required>
              </div>
              <button type="button" onclick="alert('Registration feature is simplified in Classic layout.');" style="background:var(--color-primary); color:white; border:none; padding:0.8rem 1.5rem; font-weight:600; cursor:pointer;">Submit Application</button>
            </form>
          </div>`;
        """

content = re.sub(old_form_logic, new_form_logic, content, flags=re.DOTALL)

with open('index_classic.html', 'w') as f:
    f.write(content)

print("Fixed submission_form logic.")
