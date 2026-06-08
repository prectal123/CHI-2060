import re

with open('index_classic.html', 'r') as f:
    content = f.read()

# 1. Add chi2060_papers.js
content = content.replace('<script src="specifications.js"></script>', '<script src="chi2060_papers.js"></script>\n  <script src="specifications.js"></script>')

# 2. Add global variables
globals_js = """
    let currentTab = "home";
    let currentSubtab = "intro";
    let paperTrack = "all";
    let paperQuery = "";
    let paperSubcommittee = "";
"""
content = re.sub(r'let currentTab = "home";\s*let currentSubtab = "intro";', globals_js, content)

# 3. Add papers catalog rendering logic inside renderContent() loop
old_if_chain = r'} else if \(block.type === "blog_list" \|\| block.type === "qa_board_block"\)'
new_papers_logic = """} else if (block.type === "papers_catalog") {
          html += `
            <div style="margin-bottom:1.5rem; display:flex; gap:0.5rem; border-bottom:1px solid var(--color-border); padding-bottom:1rem;">
              <button class="markdown-btn" style="border-radius:4px; padding:0.4rem 1rem; ${paperTrack === 'all' ? 'background:var(--color-primary-hover);' : 'background:#888;'}" onclick="setPaperTrack('all')">All Papers</button>
              <button class="markdown-btn" style="border-radius:4px; padding:0.4rem 1rem; ${paperTrack === 'conference' ? 'background:var(--color-primary-hover);' : 'background:#888;'}" onclick="setPaperTrack('conference')">Conference Track</button>
              <button class="markdown-btn" style="border-radius:4px; padding:0.4rem 1rem; ${paperTrack === 'journal' ? 'background:var(--color-primary-hover);' : 'background:#888;'}" onclick="setPaperTrack('journal')">Journal Track</button>
            </div>
            <div style="margin-bottom:1.5rem; display:flex; gap:1rem;">
              <input type="text" style="flex:1; padding:0.6rem; border:1px solid #ccc; font-family:var(--font-sans);" placeholder="Search title, authors, ID..." value="${paperQuery}" oninput="setPaperQuery(this.value)">
              <select style="padding:0.6rem; border:1px solid #ccc; font-family:var(--font-sans);" onchange="setPaperSubcommittee(this.value)">
                <option value="">All Subcommittees</option>
                ${getUniqueSubcommittees().map(sub => `
                  <option value="${sub}" ${paperSubcommittee === sub ? 'selected' : ''}>${sub}</option>
                `).join("")}
              </select>
            </div>
            <div class="papers-list-feed">
              ${renderFilteredPapersList()}
            </div>
          `;
        } else if (block.type === "blog_list" || block.type === "qa_board_block")"""

content = re.sub(old_if_chain, new_papers_logic, content)

# 4. Add the helper functions to the script
js_helpers = """
    function cycleTheme() {
"""
new_js_helpers = """
    function getUniqueSubcommittees() {
      const subs = new Set();
      if (typeof CHI2060_PAPERS !== 'undefined' && CHI2060_PAPERS.conference_papers && CHI2060_PAPERS.journal_papers) {
        CHI2060_PAPERS.conference_papers.forEach(p => subs.add(p.subcommittee));
        CHI2060_PAPERS.journal_papers.forEach(p => subs.add(p.subcommittee));
      }
      return Array.from(subs).sort();
    }

    function setPaperTrack(track) {
      paperTrack = track;
      renderContent();
    }

    function setPaperQuery(query) {
      paperQuery = query;
      const feed = document.querySelector(".papers-list-feed");
      if (feed) feed.innerHTML = renderFilteredPapersList();
    }

    function setPaperSubcommittee(sub) {
      paperSubcommittee = sub;
      renderContent();
    }

    function renderFilteredPapersList() {
      if (typeof CHI2060_PAPERS === 'undefined' || !CHI2060_PAPERS.conference_papers || !CHI2060_PAPERS.journal_papers) return '<p>Loading papers...</p>';
      let list = [];
      if (paperTrack === "all" || paperTrack === "conference") {
        list = list.concat(CHI2060_PAPERS.conference_papers.map(p => ({ ...p, track: "Conference" })));
      }
      if (paperTrack === "all" || paperTrack === "journal") {
        list = list.concat(CHI2060_PAPERS.journal_papers.map(p => ({ ...p, track: "Journal" })));
      }
      if (paperQuery) {
        const q = paperQuery.toLowerCase();
        list = list.filter(p => p.title.toLowerCase().includes(q) || p.id.toLowerCase().includes(q) || p.authors.some(a => a.human.toLowerCase().includes(q) || a.agent.toLowerCase().includes(q)));
      }
      if (paperSubcommittee) {
        list = list.filter(p => p.subcommittee === paperSubcommittee);
      }
      if (list.length === 0) return '<p style="padding:1.5rem; text-align:center; color:#888;">No publications found.</p>';

      return list.map(p => {
        const badge = p.award ? `<span style="background:#ffc107; color:#000; padding:0.1rem 0.4rem; font-size:0.7rem; font-weight:700; border-radius:3px; margin-left:0.5rem;">${p.award}</span>` : '';
        const auths = p.authors.map(a => `${a.human} (<span style="color:var(--color-primary);">${a.agent}</span>) [${a.contribution_pct}%]`).join(", ");
        return `
          <div style="border:1px solid #eee; margin-bottom:1rem; padding:1.2rem; background:#fff;">
            <div style="font-size:0.8rem; color:#666; margin-bottom:0.5rem; display:flex; justify-content:space-between;">
              <span><strong>${p.id}</strong> // TRACK: ${p.track.toUpperCase()}</span>
              <div>
                <span style="font-weight:700; border:1px solid #ccc; padding:0.1rem 0.4rem; border-radius:3px;">${p.subcommittee}</span>
                ${badge}
              </div>
            </div>
            <h4 style="margin:0 0 0.5rem 0; font-size:1.15rem; color:#111;">${p.title}</h4>
            <div style="font-size:0.9rem; color:#444; margin-bottom:0.8rem;"><strong>Seeders:</strong> ${auths}</div>
            <div style="font-size:0.8rem; color:#888; display:flex; gap:1.5rem;">
              <span>FILE: <a href="#download" style="font-weight:600;" onclick="alert('Downloading: ${p.file}')">${p.file}</a> (${p.file_size_mb} MB)</span>
              <span>COMPATIBILITY: ${p.compatible_agent_version} (${p.compatible_os.join(", ")})</span>
            </div>
          </div>
        `;
      }).join("");
    }

    function cycleTheme() {
"""
content = content.replace(js_helpers, new_js_helpers)

with open('index_classic.html', 'w') as f:
    f.write(content)

print("Papers logic added to classic.")
