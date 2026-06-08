import re

# We will base it on index_minimal.html to get the basic rendering loop, 
# but we will replace the CSS, the body structure, and the header completely.
with open('index_minimal.html', 'r') as f:
    content = f.read()

# 1. Replace CSS
new_css = """
    :root {
      --font-sans: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
      --font-heading: 'Roboto', 'Helvetica Neue', Helvetica, Arial, sans-serif;
      --bg-body: #f7f7f7;
      --bg-content: #ffffff;
      --text-main: #333333;
      --text-secondary: #555555;
      --color-primary: #0055A4; /* ACM Blue */
      --color-primary-hover: #003d7a;
      --color-border: #dddddd;
    }
    body {
      margin: 0; padding: 0; font-family: var(--font-sans); background: var(--bg-body); color: var(--text-main); line-height: 1.6;
    }
    a { color: var(--color-primary); text-decoration: none; }
    a:hover { text-decoration: underline; }
    
    /* Header & Navigation */
    .classic-header { background: #ffffff; border-bottom: 3px solid var(--color-primary); }
    .header-top { display: flex; justify-content: space-between; align-items: center; padding: 1rem 2rem; max-width: 1200px; margin: 0 auto; }
    .header-logo { font-family: var(--font-heading); font-weight: 700; font-size: 2rem; color: var(--color-primary); }
    
    .nav-bar { background: var(--color-primary); color: #fff; }
    .nav-container { max-width: 1200px; margin: 0 auto; display: flex; }
    .nav-item { padding: 1rem 1.5rem; cursor: pointer; font-weight: 600; text-transform: uppercase; font-size: 0.9rem; }
    .nav-item:hover, .nav-item.active { background: var(--color-primary-hover); }
    
    /* Subnav */
    .subnav-bar { background: #eeeeee; border-bottom: 1px solid var(--color-border); }
    .subnav-container { max-width: 1200px; margin: 0 auto; display: flex; gap: 1rem; padding: 0.5rem 2rem; }
    .subnav-item { padding: 0.5rem 1rem; cursor: pointer; font-size: 0.9rem; color: var(--text-secondary); border-radius: 4px; }
    .subnav-item:hover, .subnav-item.active { background: #dddddd; color: var(--text-main); font-weight: 600; }
    
    /* Layout */
    .main-wrapper { max-width: 1200px; margin: 2rem auto; display: grid; grid-template-columns: 3fr 1fr; gap: 2rem; padding: 0 2rem; }
    .content-area { background: var(--bg-content); padding: 2rem; border: 1px solid var(--color-border); box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .sidebar-area { background: var(--bg-content); padding: 1.5rem; border: 1px solid var(--color-border); }
    
    /* Content Blocks */
    .content-block { margin-bottom: 2rem; }
    .block-title { font-family: var(--font-heading); font-size: 1.5rem; color: var(--color-primary); border-bottom: 2px solid var(--color-border); padding-bottom: 0.5rem; margin-bottom: 1rem; }
    .block-description { font-style: italic; color: var(--text-secondary); margin-bottom: 1.5rem; }
    
    /* Tables */
    .dense-table { width: 100%; border-collapse: collapse; margin-bottom: 1.5rem; }
    .dense-table th, .dense-table td { border: 1px solid var(--color-border); padding: 0.75rem; text-align: left; }
    .dense-table th { background: #f9f9f9; font-weight: 600; }
    
    /* Forms & Buttons */
    .classic-input { width: 100%; padding: 0.75rem; border: 1px solid var(--color-border); border-radius: 4px; margin-bottom: 1rem; font-family: var(--font-sans); }
    .classic-btn { background: var(--color-primary); color: #fff; border: none; padding: 0.75rem 1.5rem; font-weight: 600; cursor: pointer; border-radius: 4px; }
    .classic-btn:hover { background: var(--color-primary-hover); }
    
    /* Sponsors */
    .sponsor-tier-label { font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-secondary); margin: 1.5rem 0 1rem; border-bottom: 1px solid var(--color-border); padding-bottom: 0.25rem; }
    .sponsor-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 1rem; }
    .sponsor-card { border: 1px solid var(--color-border); padding: 1rem; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; background: #fafafa; }
    .sponsor-card img { max-width: 100%; max-height: 60px; object-fit: contain; }
    
    .sidebar-widget-title { font-family: var(--font-heading); font-size: 1.2rem; color: var(--color-primary); border-bottom: 2px solid var(--color-border); padding-bottom: 0.5rem; margin-bottom: 1rem; margin-top: 2rem; }
    .sidebar-widget-title:first-child { margin-top: 0; }
"""

# Extract the script and logic from index_minimal.html
# We'll just build a brand new HTML using the specifications.js logic
new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CHI 2060 - Classic</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;1,400&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
  <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
  <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
  <style>
{new_css}
  </style>
</head>
<body>
  <header class="classic-header">
    <div class="header-top">
      <div class="header-logo" id="header-logo">ACM CHI 2060</div>
      <div style="text-align: right;">
        <div id="header-dates" style="font-weight: 600; color: var(--text-secondary);">March 29 – April 2, 2060</div>
        <div id="header-location" style="font-size: 0.9rem; color: var(--text-secondary);">San Francisco, CA</div>
        <div style="margin-top:0.5rem;">
          <button class="classic-btn" style="padding: 0.25rem 0.75rem; font-size: 0.8rem;" onclick="cycleTheme()">Cycle Theme</button>
        </div>
      </div>
    </div>
    <nav class="nav-bar">
      <div class="nav-container" id="main-nav"></div>
    </nav>
    <div class="subnav-bar" id="subnav-container-wrapper" style="display:none;">
      <div class="subnav-container" id="subnav-container"></div>
    </div>
  </header>

  <div class="main-wrapper">
    <main class="content-area" id="main-content"></main>
    <aside class="sidebar-area">
      <h3 class="sidebar-widget-title">Important Dates</h3>
      <ul style="padding-left: 1.2rem; font-size: 0.9rem; margin-bottom: 2rem;">
        <li><strong style="color:var(--text-main);">Abstract Deadline:</strong> Oct 15, 2059</li>
        <li><strong style="color:var(--text-main);">Paper Deadline:</strong> Oct 22, 2059</li>
        <li><strong style="color:var(--text-main);">Rebuttals:</strong> Dec 10-15, 2059</li>
        <li><strong style="color:var(--text-main);">Decisions:</strong> Jan 15, 2060</li>
      </ul>
      <h3 class="sidebar-widget-title">Sponsors</h3>
      <div id="sidebar-sponsors"></div>
    </aside>
  </div>
  
  <footer style="background: #222; color: #ccc; padding: 2rem 0; text-align: center; margin-top: 2rem; font-size: 0.9rem;">
    <p>&copy; 2060 • ACM SIGCHI</p>
  </footer>

  <script src="specifications.js"></script>
  <script>
    let currentTab = "home";
    let currentSubtab = "intro";

    function init() {{
      document.getElementById("header-logo").textContent = CHI2060_SPEC.conference.name;
      document.getElementById("header-dates").textContent = CHI2060_SPEC.conference.dates;
      document.getElementById("header-location").textContent = CHI2060_SPEC.conference.location;
      
      renderSidebar();
      renderNav();
      renderContent();
    }}

    function renderSidebar() {{
      const sb = document.getElementById("sidebar-sponsors");
      let html = "";
      CHI2060_SPEC.sidebarSponsors.forEach(s => {{
        if(s.type === "divider") {{
          html += `<div style="font-weight:bold; border-bottom:1px solid #ccc; margin-top:1.5rem; margin-bottom:0.5rem; font-size:0.8rem; color:#666;">${{s.label}}</div>`;
        }} else {{
          html += `<div style="margin-bottom:0.5rem; text-align:center;"><img src="${{s.logo}}" style="max-height:40px; max-width:100%; object-fit:contain;" alt="${{s.name}}"></div>`;
        }}
      }});
      sb.innerHTML = html;
    }}

    function renderNav() {{
      const nav = document.getElementById("main-nav");
      let html = "";
      Object.keys(CHI2060_SPEC.navigation).forEach(key => {{
        const tab = CHI2060_SPEC.navigation[key];
        const active = (key === currentTab) ? "active" : "";
        html += `<div class="nav-item ${{active}}" onclick="selectTab('${{key}}')">${{tab.label}}</div>`;
      }});
      nav.innerHTML = html;
    }}

    function renderSubnav() {{
      const wrapper = document.getElementById("subnav-container-wrapper");
      const subnav = document.getElementById("subnav-container");
      const tab = CHI2060_SPEC.navigation[currentTab];
      
      if (!tab.subtabs || Object.keys(tab.subtabs).length === 0) {{
        wrapper.style.display = "none";
        return;
      }}
      
      wrapper.style.display = "block";
      let html = "";
      Object.keys(tab.subtabs).forEach(sKey => {{
        const sTab = tab.subtabs[sKey];
        const active = (sKey === currentSubtab) ? "active" : "";
        html += `<div class="subnav-item ${{active}}" onclick="selectSubtab('${{sKey}}')">${{sTab.label}}</div>`;
      }});
      subnav.innerHTML = html;
    }}

    function selectTab(key) {{
      currentTab = key;
      const tab = CHI2060_SPEC.navigation[key];
      if (tab.subtabs && Object.keys(tab.subtabs).length > 0) {{
        currentSubtab = Object.keys(tab.subtabs)[0];
      }} else {{
        currentSubtab = null;
      }}
      renderNav();
      renderContent();
    }}

    function selectSubtab(key) {{
      currentSubtab = key;
      renderContent();
    }}

    function renderContent() {{
      renderSubnav();
      const container = document.getElementById("main-content");
      let contentBlocks = [];
      
      const tab = CHI2060_SPEC.navigation[currentTab];
      if (currentSubtab && tab.subtabs[currentSubtab]) {{
        contentBlocks = tab.subtabs[currentSubtab].contentBlocks || [];
      }} else {{
        contentBlocks = tab.contentBlocks || [];
      }}

      let html = "";
      contentBlocks.forEach(block => {{
        html += `<div class="content-block">`;
        if (block.title) {{
          html += `<h3 class="block-title">${{block.title}}</h3>`;
        }}
        if (block.description) {{
          html += `<p class="block-description">${{block.description}}</p>`;
        }}
        
        if (block.type === "text_block") {{
          block.paragraphs.forEach(p => html += `<p>${{p}}</p>`);
        }} else if (block.type === "bullet_list") {{
          html += `<ul style="padding-left:1.5rem;">`;
          block.items.forEach(item => html += `<li style="margin-bottom:0.5rem;">${{item}}</li>`);
          html += `</ul>`;
        }} else if (block.type === "table_block") {{
          html += `<table class="dense-table"><thead><tr>`;
          block.headers.forEach(h => html += `<th>${{h}}</th>`);
          html += `</tr></thead><tbody>`;
          block.rows.forEach(row => {{
            html += `<tr>`;
            row.forEach((cell, idx) => {{
              if (typeof cell === 'object' && cell !== null) {{
                if (cell.skip) return;
                let attrs = '';
                if (cell.rowspan) attrs += ` rowspan="${{cell.rowspan}}"`;
                if (cell.colspan) attrs += ` colspan="${{cell.colspan}}"`;
                let content = cell.text || '';
                if (idx === 0) content = `<strong>${{content}}</strong>`;
                html += `<td${{attrs}}>${{content}}</td>`;
              }} else {{
                html += idx === 0 ? `<td><strong>${{cell}}</strong></td>` : `<td>${{cell}}</td>`;
              }}
            }});
            html += `</tr>`;
          }});
          html += `</tbody></table>`;
        }} else if (block.type === "sponsor_block") {{
          block.tiers.forEach(tier => {{
            html += `<div class="sponsor-tier-label">${{tier.label}}</div><div class="sponsor-grid">`;
            tier.sponsors.forEach(sp => {{
              html += `<div class="sponsor-card"><img src="${{sp.logo}}" alt="${{sp.name}}"><div style="margin-top:0.5rem; font-weight:600; font-size:0.9rem;">${{sp.name}}</div></div>`;
            }});
            html += `</div>`;
          }});
        }} else if (block.type === "subcommittee_list") {{
          html += `<div style="display:flex; flex-direction:column; gap:1rem;">`;
          block.items.forEach(item => {{
            html += `<div style="border:1px solid var(--color-border); padding:1rem; border-radius:4px;">
              <h4 style="margin:0 0 0.5rem; color:var(--color-primary);">${{item.title}}</h4>
              <p style="margin:0; font-size:0.9rem; color:var(--text-secondary);">${{item.desc}}</p>
            </div>`;
          }});
          html += `</div>`;
        }} else if (block.type === "submission_form") {{
          html += `<div style="background:#f9f9f9; padding:1.5rem; border:1px solid var(--color-border); border-radius:4px;">`;
          block.fields.forEach(f => {{
            html += `<div style="margin-bottom:1rem;">`;
            if (f.label) html += `<label style="display:block; font-weight:600; margin-bottom:0.5rem;">${{f.label}}</label>`;
            if (f.type === "text" || f.type === "email") {{
              html += `<input type="${{f.type}}" class="classic-input" placeholder="${{f.placeholder || ''}}">`;
            }} else if (f.type === "select") {{
              html += `<select class="classic-input">`;
              f.options.forEach(opt => html += `<option>${{opt}}</option>`);
              html += `</select>`;
            }} else if (f.type === "checkbox_group") {{
              f.options.forEach(opt => {{
                html += `<div style="margin-bottom:0.25rem;"><label><input type="checkbox"> ${{opt}}</label></div>`;
              }});
            }} else if (f.type === "textarea") {{
              html += `<textarea class="classic-input" rows="4" placeholder="${{f.placeholder || ''}}"></textarea>`;
            }} else if (f.type === "drawing_signature") {{
              html += `<div style="border:1px dashed #ccc; padding:2rem; text-align:center; background:#fff; color:#999; margin-bottom:1rem;">[ Signature Canvas Component ]</div>`;
            }}
            html += `</div>`;
          }});
          html += `<button class="classic-btn">Submit Form</button></div>`;
        }} else if (block.type === "timeline_block") {{
          html += `<div style="border-left: 2px solid var(--color-primary); padding-left: 1rem; margin-left: 1rem;">`;
          block.events.forEach(ev => {{
            html += `<div style="position:relative; margin-bottom:1.5rem;">
              <div style="position:absolute; left:-1.45rem; top:0.25rem; width:10px; height:10px; background:var(--color-primary); border-radius:50%;"></div>
              <div style="font-size:0.8rem; color:var(--text-secondary); font-weight:600;">${{ev.date}}</div>
              <div style="font-weight:600; margin-bottom:0.25rem;">${{ev.title}}</div>
              <div style="font-size:0.9rem;">${{ev.description}}</div>
            </div>`;
          }});
          html += `</div>`;
        }} else if (block.type === "blog_list" || block.type === "qa_board_block") {{
          html += `<div style="padding:2rem; text-align:center; background:#f9f9f9; border:1px dashed #ccc;">[ Interactive Block: ${{block.type}} - Data Loaded Externally ]</div>`;
        }}
        
        html += `</div>`;
      }});
      
      container.innerHTML = html;
    }}

    function cycleTheme() {{
      location.href = "index.html"; // We route back to index.html to cycle through other themes
    }}

    window.addEventListener("DOMContentLoaded", init);
  </script>
</body>
</html>
"""

with open('index_classic.html', 'w') as f:
    f.write(new_html)

print("index_classic.html created.")
