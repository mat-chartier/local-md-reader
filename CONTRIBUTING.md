# Contributing to Local Markdown Reader

Thank you for considering contributing! This guide will help you understand our process.

---

## Code of Conduct

Be respectful, inclusive, and constructive. We're here to build a better tool together.

---

## Ways to Contribute

### 🐛 Report Bugs
Found a bug? [Open an issue](../../issues/new) with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Browser/OS info
- Screenshots if helpful

### 💡 Suggest Features
Have an idea? [Start a discussion](../../discussions) or [open an issue](../../issues/new) with:
- What problem does it solve?
- Why is it important?
- How might it work?
- Any examples or mockups?

### 📖 Improve Documentation
- Fix typos in README, SECURITY.md, etc.
- Clarify confusing sections
- Add examples
- Translate to other languages

### 🔒 Security Reports
**Do NOT open public issues for security vulnerabilities.**

See [SECURITY.md](SECURITY.md) for responsible disclosure guidelines.

### 💻 Code Contributions

---

## Development Setup

### Prerequisites
- A text editor or IDE (VS Code, Sublime, etc.)
- Firefox or Chrome for testing
- Git

### No Build Process
This project uses **vanilla JavaScript with no build tools**. Just edit files and test in your browser.

### Local Testing
```bash
# Option 1: Direct file
open index.html

# Option 2: Simple server
python3 -m http.server 8000
# Visit http://localhost:8000
```

### File Structure
```
.
├── index.html              # Main app (all HTML/CSS/JS in one file)
├── README.md              # User guide
├── SECURITY.md            # Security details
├── SECURITY_TESTING_GUIDE.md
├── SECURITY_ANALYSIS_FINAL.md
├── CONTRIBUTING.md        # This file
├── LICENSE                # MIT license
├── .gitignore
└── generate_sri_checksums.py  # Utility script
```

---

## Development Workflow

### 1. Fork & Clone
```bash
git clone https://github.com/mat-chartier/local-md-reader.git
cd local-md-reader
```

### 2. Create a Branch
```bash
git checkout -b feature/my-feature
# or
git checkout -b fix/bug-description
```

### 3. Make Changes
Edit `index.html` directly. Keep it as **a single file** (no splitting into separate files).

### 4. Test Thoroughly
```bash
# Test in multiple browsers (Firefox, Chrome, Safari, Edge)
# Open DevTools Console (F12) to check for errors
# Test with various markdown files (with accents, links, etc.)
```

### 5. Commit & Push
```bash
git add .
git commit -m "feat: Add feature XYZ" # or "fix: ..." or "docs: ..."
git push origin feature/my-feature
```

### 6. Open a Pull Request
On GitHub, create a PR with:
- Clear title describing the change
- Description of what/why/how
- Link to related issues if applicable
- Screenshots for UI changes

---

## Code Style

### JavaScript
- Use `const` and `let`, not `var`
- Arrow functions for simple callbacks
- Comments for complex logic
- Descriptive variable names

### Bad Example:
```javascript
const x = () => {
  const a = document.getElementById('viewerContent');
  a.innerHTML = h;
};
```

### Good Example:
```javascript
const renderTabContent = () => {
  const viewerContent = document.getElementById('viewerContent');
  viewerContent.innerHTML = sanitizeHtml(html);
};
```

### Security Rules (Non-Negotiable)
- ❌ **Never** directly set `.innerHTML` without sanitization
- ✅ Use `DOMPurify.sanitize()` for untrusted content
- ❌ **Never** use `eval()` or `Function()`
- ✅ Use CSP-compliant patterns
- ❌ **Never** make outbound network requests without `connect-src` adjustment
- ✅ Keep `connect-src 'none'` whenever possible

---

## Testing Guidelines

### Manual Testing Checklist
- [ ] Open a folder with various .md files
- [ ] Click files → they open in tabs
- [ ] Navigate between tabs
- [ ] Close tabs
- [ ] Resize the splitter
- [ ] Test internal anchor links
- [ ] Test cross-document links
- [ ] Test with accented characters (français)
- [ ] Test dark mode toggle
- [ ] Open DevTools → no errors in console
- [ ] Test in Firefox, Chrome, Safari

### Security Testing
See [SECURITY_TESTING_GUIDE.md](SECURITY_TESTING_GUIDE.md) for detailed procedures.

Key tests:
- [ ] XSS test: Try opening a `.md` with `<script>` tags → should be sanitized
- [ ] CSP test: Try `fetch()` in console → should be blocked
- [ ] Link test: Try `javascript:` links → should be ignored

---

## Commit Message Format

Use clear, descriptive commit messages:

```
feat: Add search functionality across documents
fix: Correct anchor link handling for accented headings
docs: Update security guidelines
test: Add XSS security test case
refactor: Simplify file tree rendering
chore: Update dependencies
```

---

## Pull Request Guidelines

### Before Submitting
- [ ] Test in multiple browsers
- [ ] No console errors/warnings
- [ ] No security issues introduced
- [ ] Commit messages are clear
- [ ] Docs updated if needed
- [ ] Changes are focused (one feature/fix per PR)

### What We're Looking For
✅ Clear explanation of changes  
✅ Security-conscious code  
✅ Well-tested  
✅ Consistent with existing code style  
✅ Doesn't break existing functionality  

### What Might Delay Review
❌ No explanation of changes  
❌ Multiple unrelated changes in one PR  
❌ Security concerns not addressed  
❌ No testing info provided  
❌ Formatting inconsistencies  

---

## Feature Ideas Welcome

Interested in working on something from the roadmap?

### High Priority
- 🔍 Full-text search across files
- 🎨 Theme selector UI
- 📊 Syntax highlighting

### Medium Priority
- 📑 Table of contents generator
- 🔖 Bookmarks/favorites
- 📄 Recent files list

### Low Priority (Nice to Have)
- 🌐 Remote markdown sources
- 📱 Mobile-specific UI
- ⌨️ Keyboard shortcuts guide

Before starting, **open an issue first** to discuss the approach.

---

## Questions?

- 💬 [Start a Discussion](../../discussions)
- 📖 Check existing [Issues](../../issues)
- 🔒 Security: See [SECURITY.md](SECURITY.md)

---

## Review Process

1. **Maintainer Review** (1-3 days)
   - Check code quality
   - Verify security
   - Test functionality

2. **Feedback** (if needed)
   - Discuss changes
   - Request modifications
   - Answer questions

3. **Approval & Merge**
   - After approval, your PR is merged
   - Changelog updated
   - Next release includes your contribution

---

## Licensing

By contributing, you agree that your code will be licensed under [MIT License](LICENSE).

---

## Recognition

Contributors are recognized in:
- README.md contributors section
- GitHub contributors graph
- Release notes

---

**Thank you for helping improve Local Markdown Reader!** 🎉

---

Last Updated: 2026-08-11
