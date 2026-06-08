import re

new_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CHI 2060 - Classic Reimagined</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;1,400&family=Roboto:wght@400;500;700;900&display=swap" rel="stylesheet">
  <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
  <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
  <style>
    :root {
      --font-sans: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
      --font-heading: 'Roboto', 'Helvetica Neue', Helvetica, Arial, sans-serif;
      --bg-body: #ffffff;
      --text-main: #333333;
      --text-muted: #666666;
      --color-primary: #1e5a8f; /* A standard classic link blue */
      --color-primary-hover: #123759;
      --color-border: #e0e0e0;
      --nav-bg-hover: #8e3c2f; /* Brownish red from screenshot */
    }
    
    * { box-sizing: border-box; }
    body {
      margin: 0; padding: 0; font-family: var(--font-sans); background: var(--bg-body); color: var(--text-main); line-height: 1.6;
    }
    a { color: var(--color-primary); text-decoration: none; }
    a:hover { text-decoration: underline; }
    
    /* Hero Banner Area */
    .hero-banner {
      width: 100%;
      height: 300px;
      position: relative;
      background-image: url('chi2060_header.png'), linear-gradient(90deg, #1e3a5f, #2c5364);
      background-size: cover;
      background-position: center;
      background-color: #333;
      display: flex;
      flex-direction: column;
    }
    
    .hero-content {
      padding: 3rem 5% 1rem 5%;
      color: white;
      text-shadow: 1px 1px 4px rgba(0,0,0,0.7);
    }
    
    .hero-title {
      font-family: var(--font-heading);
      font-weight: 900;
      font-size: 2.8rem;
      margin: 0 0 0.5rem 0;
    }
    
    .hero-subtitle {
      font-family: var(--font-heading);
      font-weight: 500;
      font-size: 1.2rem;
      margin: 0;
    }
    
    /* Transparent Nav Bar */
    .nav-bar {
      margin-top: auto; /* Push to bottom of banner */
      display: flex;
      padding: 0 5%;
    }
    
    .nav-item {
      position: relative;
      color: white;
      font-weight: 600;
      padding: 1rem 1.5rem;
      cursor: pointer;
      font-size: 0.95rem;
      display: flex;
      align-items: center;
      gap: 0.2rem;
      text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    
    .nav-item:hover {
      background: var(--nav-bg-hover);
      text-shadow: none;
    }
    
    /* Dropdown */
    .dropdown {
      display: none;
      position: absolute;
      top: 100%;
      left: 0;
      background: var(--nav-bg-hover);
      min-width: 220px;
      z-index: 1000;
      box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    
    .nav-item:hover .dropdown {
      display: block;
    }
    
    .dropdown-item {
      padding: 0.8rem 1.5rem;
      color: white;
      font-weight: 400;
      border-bottom: 1px solid rgba(255,255,255,0.1);
      transition: background 0.2s;
    }
    
    .dropdown-item:last-child {
      border-bottom: none;
    }
    
    .dropdown-item:hover {
      background: rgba(0,0,0,0.15);
    }
    
    /* Main Layout */
    .layout-container {
      max-width: 1300px;
      margin: 3rem auto;
      display: grid;
      grid-template-columns: 260px 1fr 260px;
      gap: 3rem;
      padding: 0 2rem;
    }
    
    /* Left Column: Dates */
    .left-col h3 {
      font-family: var(--font-heading);
      font-size: 1.4rem;
      margin-top: 0;
      margin-bottom: 1.5rem;
      color: #222;
    }
    
    .date-intro {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      line-height: 1.5;
    }
    
    .date-category-title {
      background: #f1f1f1;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.5rem 0.8rem;
      margin-bottom: 0.5rem;
      margin-top: 1.5rem;
    }
    
    .date-category-title:first-of-type {
      margin-top: 0;
    }
    
    .date-item {
      font-size: 0.85rem;
      margin-bottom: 0.3rem;
      line-height: 1.4;
    }
    
    /* Center Column: Markdown Style Content */
    .center-col {
      /* No borders, just pure text flow */
    }
    
    .center-col h2.main-title {
      font-family: var(--font-heading);
      font-size: 2.2rem;
      font-weight: 700;
      color: #111;
      margin-top: 0;
      margin-bottom: 2rem;
    }
    
    .content-block {
      margin-bottom: 2.5rem;
    }
    
    .block-title {
      font-family: var(--font-heading);
      font-size: 1.6rem;
      color: #222;
      margin-bottom: 1rem;
      border-bottom: 1px solid var(--color-border);
      padding-bottom: 0.5rem;
    }
    
    .block-description {
      font-style: italic;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }
    
    .center-col p {
      margin-bottom: 1.2rem;
    }
    
    /* Center Tables */
    .classic-table {
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      font-size: 0.95rem;
    }
    .classic-table th, .classic-table td {
      padding: 0.6rem 0.8rem;
      border-bottom: 1px solid var(--color-border);
      text-align: left;
    }
    .classic-table th {
      font-weight: 600;
      color: #222;
      border-bottom: 2px solid #ccc;
    }
    
    /* Center Buttons */
    .markdown-btn {
      display: inline-block;
      background: var(--color-primary);
      color: #fff;
      padding: 0.6rem 1.2rem;
      border-radius: 20px;
      font-weight: 600;
      text-align: center;
      margin-right: 0.5rem;
      margin-bottom: 1rem;
      border: none;
      cursor: pointer;
    }
    .markdown-btn:hover {
      background: var(--color-primary-hover);
      text-decoration: none;
    }
    
    /* Right Column: Sponsors */
    .right-col h3 {
      font-family: var(--font-heading);
      font-size: 1.4rem;
      margin-top: 0;
      margin-bottom: 1.5rem;
      color: #222;
    }
    
    .sponsor-wrapper {
      margin-bottom: 2rem;
    }
    
    .sponsor-divider {
      font-weight: 700;
      font-size: 0.9rem;
      color: var(--text-muted);
      border-bottom: 1px solid var(--color-border);
      padding-bottom: 0.2rem;
      margin-bottom: 1rem;
      margin-top: 1.5rem;
    }
    
    .sponsor-divider:first-of-type {
      margin-top: 0;
    }
    
    .sponsor-logo {
      display: block;
      margin-bottom: 1.5rem;
      max-width: 100%;
      max-height: 50px;
      object-fit: contain;
    }
    
    /* Mobile Responsiveness */
    @media(max-width: 900px) {
      .layout-container {
        grid-template-columns: 1fr;
      }
      .nav-bar { flex-wrap: wrap; }
    }
  </style>
</head>
<body>
  
  <header class="hero-banner">
    <div class="hero-content">
      <h1 class="hero-title" id="banner-title">ACM CHI 2060</h1>
      <p class="hero-subtitle" id="banner-subtitle">Intelligence at Scale. Humanity in Focus. • March 29 – April 2, 2060</p>
      
      <div style="position:absolute; top: 1rem; right: 2rem;">
        <button onclick="cycleTheme()" style="background: rgba(255,255,255,0.2); color:white; border:1px solid rgba(255,255,255,0.4); padding:0.4rem 0.8rem; cursor:pointer; font-size:0.8rem;">Cycle Theme</button>
      </div>
    </div>
    
    <nav class="nav-bar" id="main-nav"></nav>
  </header>

  <div class="layout-container">
    <!-- Left Column: Important Dates -->
    <aside class="left-col">
      <h3>Important Dates</h3>
      <div class="date-intro">
        All times are in Anywhere on Earth (AoE) time zone. The submission site of each track will open approximately four weeks before its submission deadline.
      </div>
      
      <div class="date-category-title">Papers</div>
      <div class="date-item"><strong>2059-09-04</strong> Abstract/Metadata Due</div>
      <div class="date-item"><strong>2059-09-11</strong> Full Paper Due</div>
      <div class="date-item"><strong>2059-11-04</strong> Reviews Released</div>
      <div class="date-item"><strong>2059-12-04</strong> Resubmission Due</div>
      <div class="date-item"><strong>2060-01-15</strong> Decisions Notification</div>
      
      <div class="date-category-title">Posters</div>
      <div class="date-item"><strong>2060-01-22</strong> Submission deadline</div>
      <div class="date-item"><strong>2060-02-19</strong> Notification</div>
      
      <div class="date-category-title">Interactive Demos</div>
      <div class="date-item"><strong>2060-01-22</strong> Submission deadline</div>
    </aside>
    
    <!-- Center Column: Markdown Content -->
    <main class="center-col" id="main-content">
      <h2 class="main-title">Welcome to CHI 2060!</h2>
      <p>The ACM (Association for Computing Machinery) CHI conference on Human Factors in Computing Systems is the leading international conference on Human-Computer Interaction. CHI 2060 will take place in San Francisco at the <strong>Moscone Center</strong>.</p>
      <p><strong>CHI 2060 is currently at capacity.</strong> <em>No new agent registrations are available.</em></p>
      <button class="markdown-btn" onclick="document.querySelector('#main-nav .nav-item:nth-child(5) .dropdown-item:nth-child(3)').click()">See the Program at a Glance</button>
      <button class="markdown-btn" onclick="document.querySelector('#main-nav .nav-item:nth-child(5) .dropdown-item:nth-child(2)').click()">See the Full Program</button>
      
      <div id="dynamic-content-wrapper" style="margin-top: 3rem;"></div>
    </main>
    
    <!-- Right Column: Sponsors -->
    <aside class="right-col">
      <h3>Sponsors</h3>
      <div id="sidebar-sponsors"></div>
    </aside>
  </div>

  <footer style="background: #e9ecef; color: #555; padding: 2rem 0; text-align: center; margin-top: 3rem; font-size: 0.9rem; border-top:1px solid #ccc;">
    <p>&copy; 2060 • ACM SIGCHI</p>
  </footer>

  <script src="specifications.js"></script>
  <script>
    let currentTab = "home";
    let currentSubtab = "intro";

    function init() {
      // Setup dynamic banner text
      document.getElementById("banner-title").textContent = CHI2060_SPEC.conference.name;
      document.getElementById("banner-subtitle").textContent = `${CHI2060_SPEC.conference.theme} • ${CHI2060_SPEC.conference.location}, ${CHI2060_SPEC.conference.dates}`;
      
      renderSidebar();
      renderNav();
      renderContent();
    }

    function renderSidebar() {
      const sb = document.getElementById("sidebar-sponsors");
      let html = "";
      CHI2060_SPEC.sidebarSponsors.forEach(s => {
        if(s.type === "divider") {
          html += `<div class="sponsor-divider">${s.label} Sponsors</div>`;
        } else {
          html += `<a href="#" title="${s.name}"><img class="sponsor-logo" src="${s.logo}" alt="${s.name}"></a>`;
        }
      });
      sb.innerHTML = html;
    }

    function renderNav() {
      const nav = document.getElementById("main-nav");
      let html = "";
      Object.keys(CHI2060_SPEC.navigation).forEach(key => {
        const tab = CHI2060_SPEC.navigation[key];
        
        let dropdownHtml = "";
        if (tab.subtabs && Object.keys(tab.subtabs).length > 0) {
          dropdownHtml += `<div class="dropdown">`;
          Object.keys(tab.subtabs).forEach(sKey => {
            const sTab = tab.subtabs[sKey];
            dropdownHtml += `<div class="dropdown-item" onclick="event.stopPropagation(); selectTabSubtab('${key}', '${sKey}')">${sTab.label}</div>`;
          });
          dropdownHtml += `</div><ion-icon name="chevron-down-outline" style="font-size:0.8rem; margin-top:2px;"></ion-icon>`;
        }
        
        html += `<div class="nav-item" onclick="selectTabSubtab('${key}', null)">
          ${tab.label}
          ${dropdownHtml}
        </div>`;
      });
      nav.innerHTML = html;
    }

    function selectTabSubtab(tabKey, subtabKey) {
      currentTab = tabKey;
      if (subtabKey) {
        currentSubtab = subtabKey;
      } else {
        const tab = CHI2060_SPEC.navigation[tabKey];
        if (tab.subtabs && Object.keys(tab.subtabs).length > 0) {
          currentSubtab = Object.keys(tab.subtabs)[0];
        } else {
          currentSubtab = null;
        }
      }
      
      // If we clicked a nav item, scroll down to the dynamic content area
      window.scrollTo({ top: document.getElementById('dynamic-content-wrapper').offsetTop - 100, behavior: 'smooth' });
      
      renderContent();
    }

    function renderContent() {
      const container = document.getElementById("dynamic-content-wrapper");
      let contentBlocks = [];
      
      const tab = CHI2060_SPEC.navigation[currentTab];
      if (currentSubtab && tab.subtabs[currentSubtab]) {
        contentBlocks = tab.subtabs[currentSubtab].contentBlocks || [];
      } else {
        contentBlocks = tab.contentBlocks || [];
      }

      let html = "";
      contentBlocks.forEach(block => {
        html += `<div class="content-block">`;
        if (block.title) {
          html += `<h3 class="block-title">${block.title}</h3>`;
        }
        if (block.description) {
          html += `<p class="block-description">${block.description}</p>`;
        }
        
        if (block.type === "text_block") {
          block.paragraphs.forEach(p => html += `<p>${p}</p>`);
        } else if (block.type === "bullet_list") {
          html += `<ul style="padding-left:1.5rem; margin-bottom:1.5rem;">`;
          block.items.forEach(item => html += `<li style="margin-bottom:0.5rem;">${item}</li>`);
          html += `</ul>`;
        } else if (block.type === "table_block") {
          html += `<div style="overflow-x:auto;"><table class="classic-table"><thead><tr>`;
          block.headers.forEach(h => html += `<th>${h}</th>`);
          html += `</tr></thead><tbody>`;
          block.rows.forEach(row => {
            html += `<tr>`;
            row.forEach((cell, idx) => {
              if (typeof cell === 'object' && cell !== null) {
                if (cell.skip) return;
                let attrs = '';
                if (cell.rowspan) attrs += ` rowspan="${cell.rowspan}"`;
                if (cell.colspan) attrs += ` colspan="${cell.colspan}"`;
                let content = cell.text || '';
                if (idx === 0) content = `<strong>${content}</strong>`;
                html += `<td${attrs}>${content}</td>`;
              } else {
                html += idx === 0 ? `<td><strong>${cell}</strong></td>` : `<td>${cell}</td>`;
              }
            });
            html += `</tr>`;
          });
          html += `</tbody></table></div>`;
        } else if (block.type === "sponsor_block") {
          block.tiers.forEach(tier => {
            html += `<h4 style="color:var(--text-muted); font-size:1.1rem; border-bottom:1px dashed #ccc; padding-bottom:0.3rem; margin-top:2rem;">${tier.label} Sponsors</h4><div style="display:flex; flex-wrap:wrap; gap:2rem; align-items:center; margin-top:1rem;">`;
            tier.sponsors.forEach(sp => {
              html += `<div style="text-align:center;"><img src="${sp.logo}" alt="${sp.name}" style="max-height:60px; max-width:180px;"><div style="font-size:0.85rem; font-weight:600; margin-top:0.5rem;">${sp.name}</div></div>`;
            });
            html += `</div>`;
          });
        } else if (block.type === "subcommittee_list") {
          html += `<div style="display:flex; flex-direction:column; gap:1.5rem;">`;
          block.items.forEach(item => {
            html += `<div>
              <h4 style="margin:0 0 0.5rem; font-size:1.1rem; color:#111;">${item.title}</h4>
              <p style="margin:0; color:var(--text-muted);">${item.desc}</p>
            </div>`;
          });
          html += `</div>`;
        } else if (block.type === "submission_form") {
          html += `<div style="background:#fafafa; border:1px solid #ddd; padding:2rem; margin-top:1rem;">`;
          block.fields.forEach(f => {
            html += `<div style="margin-bottom:1.5rem;">`;
            if (f.label) html += `<label style="display:block; font-weight:600; margin-bottom:0.5rem; color:#333;">${f.label}</label>`;
            if (f.type === "text" || f.type === "email") {
              html += `<input type="${f.type}" style="width:100%; padding:0.6rem; border:1px solid #ccc;" placeholder="${f.placeholder || ''}">`;
            } else if (f.type === "select") {
              html += `<select style="width:100%; padding:0.6rem; border:1px solid #ccc;">`;
              f.options.forEach(opt => html += `<option>${opt}</option>`);
              html += `</select>`;
            } else if (f.type === "checkbox_group") {
              f.options.forEach(opt => {
                html += `<div style="margin-bottom:0.4rem;"><label><input type="checkbox"> ${opt}</label></div>`;
              });
            } else if (f.type === "textarea") {
              html += `<textarea style="width:100%; padding:0.6rem; border:1px solid #ccc;" rows="4" placeholder="${f.placeholder || ''}"></textarea>`;
            } else if (f.type === "drawing_signature") {
              html += `<div style="border:1px dashed #aaa; padding:2rem; text-align:center; background:#fff; color:#888;">[ Signature Canvas ]</div>`;
            }
            html += `</div>`;
          });
          html += `<button style="background:var(--color-primary); color:white; border:none; padding:0.8rem 1.5rem; font-weight:600; cursor:pointer;">Submit Application</button></div>`;
        } else if (block.type === "timeline_block") {
          html += `<div style="border-left: 3px solid #ddd; padding-left: 1.5rem; margin-left: 1rem;">`;
          block.events.forEach(ev => {
            html += `<div style="position:relative; margin-bottom:2rem;">
              <div style="position:absolute; left:-2rem; top:0.3rem; width:14px; height:14px; background:white; border:3px solid var(--color-primary); border-radius:50%;"></div>
              <div style="font-size:0.85rem; color:var(--text-muted); font-weight:600; margin-bottom:0.2rem;">${ev.date}</div>
              <div style="font-weight:700; color:#222; font-size:1.1rem; margin-bottom:0.4rem;">${ev.title}</div>
              <div style="color:#444;">${ev.description}</div>
            </div>`;
          });
          html += `</div>`;
        } else if (block.type === "blog_list" || block.type === "qa_board_block") {
          html += `<div style="padding:2rem; text-align:center; background:#fafafa; border:1px solid #eee; color:#888;">Interactive External Component: ${block.type}</div>`;
        }
        
        html += `</div>`;
      });
      
      container.innerHTML = html;
    }

    function cycleTheme() {
      location.href = "index.html"; 
    }

    window.addEventListener("DOMContentLoaded", init);
  </script>
</body>
</html>
"""

with open('index_classic.html', 'w') as f:
    f.write(new_html)

print("index_classic.html completely overhauled.")
