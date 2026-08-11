#!/usr/bin/env python3
"""
Generate SRI (Subresource Integrity) checksums for CDN resources.
Works on Windows, macOS, Linux.
"""

import urllib.request
import hashlib
import base64
import sys

def generate_sri_checksum(url: str, name: str) -> str:
    """Fetch URL and generate SHA384 SRI checksum"""
    print(f"📥 Fetching {name}...")
    
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
        
        # Calculate SHA384 hash
        sha384_hash = hashlib.sha384(content).digest()
        checksum = base64.b64encode(sha384_hash).decode('utf-8')
        
        print(f"✅ {name}:")
        print(f"   sha384-{checksum}")
        print()
        
        return checksum
    except Exception as e:
        print(f"❌ Error fetching {name}: {e}")
        return None

def main():
    print("=" * 60)
    print("🔐 SRI Checksum Generator for Markdown Explorer")
    print("=" * 60)
    print()
    
    resources = [
        ("https://cdnjs.cloudflare.com/ajax/libs/marked/13.0.1/marked.min.js", "marked.js"),
        ("https://cdn.jsdelivr.net/npm/dompurify@3.0.9/dist/purify.min.js", "DOMPurify"),
    ]
    
    print("Fetching and calculating checksums...")
    print()
    
    checksums = {}
    for url, name in resources:
        checksum = generate_sri_checksum(url, name)
        if checksum:
            checksums[name] = checksum
    
    print("=" * 60)
    print("✅ Checksums generated successfully!")
    print("=" * 60)
    print()
    
    print("📋 Add these to markdown_explorer_secure.html:")
    print()
    print("For marked.js:")
    print('  <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/13.0.1/marked.min.js"')
    if "marked.js" in checksums:
        print(f'          integrity="sha384-{checksums["marked.js"]}"')
    print('          crossorigin="anonymous"')
    print('          referrerpolicy="no-referrer"></script>')
    print()
    
    print("For DOMPurify:")
    print('  <script src="https://cdn.jsdelivr.net/npm/dompurify@3.0.9/dist/purify.min.js"')
    if "DOMPurify" in checksums:
        print(f'          integrity="sha384-{checksums["DOMPurify"]}"')
    print('          crossorigin="anonymous"')
    print('          referrerpolicy="no-referrer"></script>')
    print()
    
    print("🔒 Your app will then be fully protected with SRI!")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Cancelled by user")
        sys.exit(1)
