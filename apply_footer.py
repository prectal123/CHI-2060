import re

AGENT_VIEW_HTML = """
  <!-- Agent Raw View (hidden until toggled) -->
  <section id="agent-raw-view" style="display:none; position:fixed; top:0; left:0; width:100vw; height:100vh; background:#000000; color:#00ff00; z-index:9999; overflow:auto; padding:2rem; font-family:monospace; font-size:0.85rem; line-height:1.4; cursor:pointer;" onclick="toggleAgentView()">
    <div style="margin-bottom:1rem; border-bottom:1px solid #00ff00; padding-bottom:0.5rem; font-weight:bold;">
      <span>SOMATIC PERSONAL AGENT CLIENT // TRACE DATA STREAM</span>
    </div>
    <pre id="agent-raw-pre" style="white-space:pre-wrap; word-break:break-all; color:#00ff00;"></pre>
  </section>
"""

FOOTER_HTML = """  <footer class="academic-footer">
    <div>&copy; 2060 &bull; ACM SIGCHI</div>
    <div style="font-size:0.65rem; color:#999; margin-top:0.5rem; cursor:pointer;" onclick="toggleAgentView()">
      Powered by Somatic Personal Agent
    </div>
  </footer>
"""

TOGGLE_JS = """
    let _agentViewOpen = false;
    function toggleAgentView() {
      _agentViewOpen = !_agentViewOpen;
      const el = document.getElementById('agent-raw-view');
      if (!el) return;
      if (_agentViewOpen) {
        el.style.display = 'block';
        const pre = document.getElementById('agent-raw-pre');
        if (pre) pre.textContent = JSON.stringify({ CHI2060_SPEC, CHI2060_PAPERS }, null, 2);
      } else {
        el.style.display = 'none';
      }
    }
"""

for fname in ['index_classic.html', 'index_grid.html']:
    with open(fname, 'r') as f:
        content = f.read()

    # Remove existing plain footer
    content = re.sub(
        r'\s*<footer class="academic-footer">.*?</footer>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove existing agent-raw-view if present
    content = re.sub(
        r'\s*<section[^>]*id="agent-raw-view"[^>]*>.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove existing toggleAgentView / _agentViewOpen if present
    content = re.sub(
        r'\n\s*let _agentViewOpen.*?}\s*\n',
        '\n',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'\n\s*function toggleAgentView\(\).*?}\s*\n',
        '\n',
        content,
        flags=re.DOTALL
    )

    # Inject agent-raw-view before </body>
    content = content.replace('</body>', AGENT_VIEW_HTML + '\n' + FOOTER_HTML + '\n</body>')

    # Inject JS function before window.addEventListener('DOMContentLoaded'
    content = content.replace(
        "window.addEventListener('DOMContentLoaded', init);",
        TOGGLE_JS + "\n    window.addEventListener('DOMContentLoaded', init);"
    )

    with open(fname, 'w') as f:
        f.write(content)
    print(f"Done: {fname}")
