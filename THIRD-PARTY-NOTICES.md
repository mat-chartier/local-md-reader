# Third-Party Notices

`index.html` bundles the following third-party libraries **inline** (vendored,
no CDN). Their license headers are preserved verbatim inside the file.

---

## marked

- **Version:** 13.0.1
- **License:** MIT
- **Copyright:** © 2011–2024 Christopher Jeffrey and contributors
- **Homepage:** https://github.com/markedjs/marked
- **SHA-384 (of the exact bundled bytes):**
  `sha384-rsHQN9cWjVomCl6G/DKSg/7NAxlGLQ18RgAK8nNytMFlpz+JMgE8PDSpJrjgGDOU`

```
The MIT License (MIT)

Copyright (c) 2018+, MarkedJS (https://github.com/markedjs/)
Copyright (c) 2011-2018, Christopher Jeffrey (https://github.com/chjj/)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## DOMPurify

- **Version:** 3.0.9
- **License:** Apache-2.0 **OR** MPL-2.0 (dual-licensed; you may choose either)
- **Copyright:** © Cure53 and other contributors
- **Homepage:** https://github.com/cure53/DOMPurify
- **Full license:** https://github.com/cure53/DOMPurify/blob/3.0.9/LICENSE
- **SHA-384 (of the exact bundled bytes):**
  `sha384-3HPB1XT51W3gGRxAmZ+qbZwRpRlFQL632y8x+adAqCr4Wp3TaWwCLSTAJJKbyWEK`

DOMPurify is distributed under a dual license. This project redistributes the
unmodified `dompurify@3.0.9` bundle; its license header is preserved inline in
`index.html`. The full Apache-2.0 and MPL-2.0 texts are available at the URL
above.

---

## Mermaid

- **Version:** 11.17.2
- **License:** MIT
- **Copyright:** © Knut Sveidqvist and Mermaid contributors
- **Homepage:** https://github.com/mermaid-js/mermaid
- **Full license:** https://github.com/mermaid-js/mermaid/blob/master/LICENSE
- **SHA-384 (of the exact bundled bytes):**
  `sha384-EOXBFmc3gx5mb+vn0vPvvGqACToJD24hhacX5Yx+8NUUQrHIle/Qi5Bg9o3zKwW2`

Renders ` ```mermaid ` fenced code blocks (flowchart, sequence, class, state, ER,
gantt, pie, gitgraph…) to SVG **entirely client-side** — no network requests, in
keeping with the app's offline model. Initialized with `securityLevel: 'strict'`,
and the produced SVG is re-sanitized with DOMPurify (`SVG_SANITIZE`) before it is
inserted into the document. The upstream build ships without a license header
comment, so an MIT header is prepended to the inline `<script>` block.

---

## Updating a vendored library

1. Download the exact minified build you want to pin, e.g.
   `https://cdnjs.cloudflare.com/ajax/libs/marked/<version>/marked.min.js`.
2. Verify its SHA-384:
   `curl -sfL <url> | openssl dgst -sha384 -binary | openssl base64 -A`
3. Replace the corresponding inline `<script>…</script>` block in `index.html`,
   **keeping the library's license header comment intact**.
4. Update the version and SHA-384 recorded above.
