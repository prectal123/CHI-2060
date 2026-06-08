const fs = require('fs');
const files = ['index_ide.html', 'index_dandy.html', 'index_minimal.html', 'index_dump.html', 'index_ferrous.html'];

for (const file of files) {
  let content = fs.readFileSync(file, 'utf8');
  
  // Remove badge
  content = content.replace(/<span class="badge-tag \${d\.badgeClass}">\${d\.badge}<\/span>\s*/g, '');
  
  // Replace reply box
  const replyBoxRegex = /<div class="board-reply">\s*<div class="board-reply-hdr">\s*<ion-icon name="[^"]+"><\/ion-icon>\${d\.replyHeader}\s*<\/div>\s*<p class="board-reply-text">\${d\.replyText}<\/p>\s*<\/div>/g;
  
  content = content.replace(replyBoxRegex, '<p class="board-reply-text" style="font-style:italic;"><em>${d.replyText}</em></p>');
  
  fs.writeFileSync(file, content);
}
console.log("Done");
