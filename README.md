# Local Markdown Reader

A lightweight, offline markdown explorer. Browse local markdown files with a split-pane interface, internal/cross-document anchors, and multiple tabs. **100% client-side, no server needed.**

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Security: Hardened](https://img.shields.io/badge/Security-Hardened-green.svg)
![Vanilla JS](https://img.shields.io/badge/Stack-Vanilla%20JS-blue.svg)

---

## Features

- 📁 **File Explorer** — Real folder tree: every sub-folder is shown (even ones with no `.md`) and read **lazily**, only when you expand it — no slow up-front scan (Chromium browsers; see note below)
- 🔄 **Refresh** — Re-scan the current folder to pick up new/changed files without re-selecting it (Chromium browsers; see note below)
- 📄 **Live Preview** — Renders markdown to HTML with proper formatting
- 🔗 **Smart Navigation** — Jump between documents with internal and cross-document anchors
- 📑 **Multi-Tab Support** — Open multiple files at once, cached for performance
- 📏 **Resizable Panes** — Drag the splitter to adjust explorer/viewer width
- 🌙 **Dark Mode** — Auto-adapts to system theme
- 🇫🇷 **Unicode-Friendly** — Handles accents and special characters in anchor links
- ⚡ **Lightweight & self-contained** — marked.js + DOMPurify vendored inline in one HTML file; no build step, no server, no network
- 🔒 **Security-Hardened** — XSS protection, strict CSP, sanitization, file validation, zero external requests

---

## Quick Start

### 1. Download
Download `index.html` from the [main branch](https://raw.githubusercontent.com/mat-chartier/local-md-reader/main/index.html).

Or: Open index.html directly from the [repository](https://github.com/mat-chartier/local-md-reader/blob/main/index.html).

Or: Access on [github pages](https://mat-chartier.github.io/local-md-reader/)

### 2. Open
Open the file directly in your browser (Firefox, Chrome, Safari, Edge).

### 3. Browse
Click "📁 Open Folder" and select a folder containing `.md` files.

### 4. Read
Click any `.md` file to view it rendered.

---

## Usage

### Keyboard & Mouse

- **📁 Open Folder** → Pick a folder of `.md` files
- **🔄 Refresh** → Re-scan the current folder for new/changed files (see caveat below)
- **Click folder** → Expand/collapse
- **Click file** → Open in new tab
- **Click tab** → Switch between files
- **× on tab** → Close tab
- **Drag splitter** → Resize panes
- **⬆ Top button** → Scroll to top
- **Links** → Click to navigate (same doc, other docs, external URLs)
- **Anchors** → `[text](#heading)` or `[text](other.md#heading)` work

> **Explorer & refresh caveat:** the lazy folder tree and silent re-scanning both rely on the [File System Access API](https://developer.mozilla.org/docs/Web/API/File_System_API), available in **Chromium browsers (Chrome/Edge)**. There you get the full experience: every sub-folder is shown and read only when expanded, and Refresh re-reads the same folder in place, preserving your open tabs and expanded folders. On **Firefox/Safari** (which lack the API) the app falls back to a one-time flat listing of your `.md` files via the native picker. There, Refresh re-opens the picker so you re-pick the folder — but it **preserves your open tabs and expanded folders** and re-reads file contents, so it's a real reload rather than a fresh start. The app shows a hint suggesting Chrome/Edge on those browsers.

### Markdown Features Supported

✅ Headings (h1–h6)  
✅ Lists (ordered, unordered)  
✅ Code blocks with syntax highlighting  
✅ Inline code  
✅ Blockquotes  
✅ Tables  
✅ Images  
✅ Links  
✅ Bold, italic, strikethrough  
✅ Horizontal rules  

### Folder Structure

```
my-docs/
├── README.md
├── guide/
│   ├── getting-started.md
│   └── advanced.md
└── api/
    ├── endpoints.md
    └── authentication.md
```

**Open root folder** → See entire structure  
**Navigate via links** → `[See API](api/endpoints.md#authentication)`

---

## Security Features

🔒 **XSS Protection** — HTML sanitized with DOMPurify  
🔒 **Content Security Policy** — Blocks data exfiltration  
🔒 **File Validation** — Extension & size checks (max 10MB)  
🔒 **Link Validation** — Dangerous protocols blocked  
🔒 **Debug Isolation** — No sensitive data in console  
🔒 **Zero external requests** — `marked.js` and `DOMPurify` are **vendored inline** (no CDN), so the page makes **no network requests at all**  

> **Truly offline & private:** everything — reading, parsing, rendering, and both libraries — is contained in the single `index.html`. The page issues **zero outbound network requests**, on `file://` and on GitHub Pages alike. No file content, and no metadata (not even your IP to a CDN), ever leaves your device. Enforced by CSP (`default-src 'none'; connect-src 'none'; img-src 'self' data:`) plus DOMPurify sanitization. See [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) for the bundled libraries and their licenses.

See [SECURITY.md](SECURITY.md) for detailed threat model, attack scenarios, and deployment guidelines.

---

## Local Deployment

### Option A: Direct File
```bash
# Just download index.html and open in browser
open index.html
```

### Option B: Local Server (Python)
```bash
python3 -m http.server 8000
# Visit http://localhost:8000
```

### Option C: Local Server (Node.js)
```bash
npx http-server .
# Visit http://localhost:8080
```

---

## Advanced: Updating the Vendored Libraries

`marked.js` and `DOMPurify` are **bundled inline** in `index.html` (no CDN, no
Subresource Integrity needed since nothing is fetched at runtime). To bump a
version, download the exact minified build, verify its SHA-384, and replace the
matching inline `<script>` block — keeping its license header comment intact.
Full step-by-step and the pinned checksums are in
[THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

---

## Technical Stack

- **Vanilla JavaScript** (single self-contained `index.html`, no build tools)
- **Marked.js** (vendored inline) for markdown rendering
- **DOMPurify** (vendored inline) for XSS prevention
- **File System Access API / File API** for local file access (no backend)
- **CSS Grid & Flexbox** for responsive UI

---

## Browser Compatibility

| Browser | Status | Note |
|---------|--------|------|
| Firefox | ✅ Full | webkitdirectory supported since v50 |
| Chrome | ✅ Full | Recommended |
| Safari | ✅ Full | iOS/macOS supported |
| Edge | ✅ Full | Chromium-based |
| IE 11 | ❌ Not supported | Use modern browser |

---

## Use Cases

### 📚 Personal Knowledge Base
Browse local markdown notes offline, organized in folders.

### 🏢 Professional Documentation
View internal docs, wikis, runbooks in a secure, fast interface.

### 🗃️ Digital Archive
Read Vitam-exported documents with full-text navigation.

### 📖 Book/Course Materials
Study markdown-formatted textbooks with cross-references.

### 🛠️ Developer Docs
Navigate API documentation, changelogs, guides.

---

## Limitations

❌ No external markdown processing (only client-side)  
❌ No file editing (read-only)  
❌ No sync to cloud  
❌ No search across files (future enhancement)  
❌ No file upload via UI (use native file picker)  

---

## Performance

| Metric | Value |
|--------|-------|
| Initial Load | <100ms (no network — everything is inline) |
| File Open | <50ms (from cache) |
| Render | <200ms (marked + DOMPurify) |
| Memory (10 files) | ~5MB |
| Memory (100 files) | ~30MB |

---

## Troubleshooting

### Issue: Nothing renders / blank page
**Check DevTools Console (F12).** The app needs **no network** — `marked.js` and `DOMPurify` are bundled inside `index.html`. If the page is blank, make sure the file was downloaded whole (≈100 KB) and not truncated.

### Issue: Markdown doesn't render
**Check DevTools Console (F12)** for CSP violations or script errors.

### Issue: Links don't work
**Verify path:** 
- Same folder: `other.md`
- Parent: `../other.md`
- Absolute: Full path from root

### Issue: Slow on large files (>5MB)
**Note:** Each .md file is fully loaded into memory. Consider splitting very large documents.

---

## Contributing

Contributions welcome! Areas of interest:

- 🔍 Full-text search across files
- 🌐 Remote markdown sources (URL input)
- 📊 Syntax highlighting improvements
- 🎨 Theme customization
- ♿ Accessibility enhancements
- 📱 Mobile UI improvements

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Security & Privacy

**No telemetry.** No cookies. No tracking. All data stays on your device.

For detailed security analysis, threat model, and deployment recommendations, see [SECURITY.md](SECURITY.md).

---

## License

MIT License — See [LICENSE](LICENSE) file for details.

**In short:** Use freely for any purpose, commercial or personal, with attribution.

---

## Support

- 📖 [SECURITY.md](SECURITY.md) — Security details & deployment guide
- 🧪 [SECURITY_TESTING_GUIDE.md](SECURITY_TESTING_GUIDE.md) — How to test security features
- 🐛 [GitHub Issues](../../issues) — Report bugs
- 💬 [Discussions](../../discussions) — Ask questions

---

## Roadmap

- [x] Fully offline / vendored build (marked.js + DOMPurify bundled inline, no CDN)
- [ ] Full-text search
- [ ] Export to PDF
- [ ] Print-friendly view
- [ ] Syntax highlighting (code blocks)
- [ ] Table of contents generator
- [ ] Keyboard shortcuts guide
- [ ] Bookmarks/favorites
- [ ] Recent files list
- [ ] Theme selector UI

---

## Thanks

Built with:
- [marked.js](https://marked.js.org/) — Markdown parser
- [DOMPurify](https://cure53.de/purify) — XSS prevention
- No other dependencies! 🎉

---

**Made with ❤️ for secure, offline document browsing.**

Last updated: 2026-08-11
