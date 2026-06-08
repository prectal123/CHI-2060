import re

with open('index_classic.html', 'r') as f:
    content = f.read()

# 1. Replace the hardcoded Welcome section in the HTML body
old_body = r'<main class="center-col" id="main-content">.*?</main>'
new_body = """<main class="center-col" id="main-content"></main>"""
content = re.sub(old_body, new_body, content, flags=re.DOTALL)

# 2. Replace the hardcoded Important Dates in the left column
old_left = r'<aside class="left-col">.*?</aside>'
new_left = """<aside class="left-col" id="left-col-dates"></aside>"""
content = re.sub(old_left, new_left, content, flags=re.DOTALL)

# 3. Add JS function to render Important Dates dynamically
js_important_dates = """
    function renderLeftSidebar() {
      const col = document.getElementById("left-col-dates");
      if (!col) return;
      let html = `<h3>Important Dates</h3>
      <div class="date-intro">All times are in Anywhere on Earth (AoE) time zone.</div>`;
      
      CHI2060_SPEC.importantDates.forEach(sec => {
        html += `<div class="date-category-title">${sec.category}</div>`;
        sec.items.forEach(it => {
          html += `<div class="date-item"><strong>${it.date}</strong> ${it.label}</div>`;
        });
      });
      col.innerHTML = html;
    }
"""

content = content.replace('function renderSidebar() {', js_important_dates + '\n    function renderSidebar() {')
content = content.replace('renderSidebar();', 'renderLeftSidebar();\n      renderSidebar();')

# 4. Modify renderContent() to use main-content as container
content = content.replace('const container = document.getElementById("dynamic-content-wrapper");', 'const container = document.getElementById("main-content");')

# 5. Remove any dynamic-content-wrapper scrolling logic
content = content.replace("window.scrollTo({ top: document.getElementById('dynamic-content-wrapper').offsetTop - 100, behavior: 'smooth' });", "window.scrollTo({ top: 0, behavior: 'smooth' });")

with open('index_classic.html', 'w') as f:
    f.write(content)

print("Classic fixed.")
