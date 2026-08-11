# Local Markdown Reader

A single-page web app to explore and read markdown files from your local system. 
No server, no build step — just open in your browser.

## Features

- 📁 **File Explorer** — Browse local markdown files in a collapsible tree
- 📄 **Live Preview** — Renders markdown to HTML with syntax highlighting
- 🔗 **Smart Navigation** — Jump between documents with internal and cross-document anchors
- 📑 **Multi-Tab Support** — Open multiple files at once, cached for performance
- 📏 **Resizable Panes** — Drag the splitter to adjust explorer/viewer width
- 🌙 **Dark Mode** — Auto-adapts to system theme
- 🇫🇷 **French-Friendly** — Handles accents and special characters in anchor links
- ⚡ **Instant** — Zero dependencies (except marked.js for rendering), runs offline

## How to Use

1. Download `markdown_explorer.html`
2. Open in Firefox, Chrome, Safari, or Edge
3. Click "📁 Ouvrir dossier" and select a folder containing `.md` files
4. Click any `.md` file to view it
5. Use the scroll-to-top button or click links to navigate

## Deployment

Deploy to GitHub Pages:
- Live at [https://mat-chartier.github.io/local-md-reader/](https://mat-chartier.github.io/local-md-reader/)

## Technical Stack

- **Vanilla JS** (~1000 lines, no build tools)
- **Marked.js** for markdown rendering
- **File API** for local file access (no backend)
