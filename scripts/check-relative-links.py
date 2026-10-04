#!/usr/bin/env python3
"""Check that tracked Markdown links resolve to local files."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import subprocess
import sys

root = Path.cwd().resolve()
names = subprocess.check_output(["git", "ls-files", "-z", "--", "*.md"]).decode().split("\0")
broken = []
for name in filter(None, names):
    source = Path(name)
    for line_no, line in enumerate(source.read_text().splitlines(), 1):
        for match in re.finditer(r"\]\(([^)]+)\)", line):
            raw = match.group(1).strip()
            if not raw:
                continue
            url = raw[1:].split(">", 1)[0] if raw.startswith("<") else raw.split()[0]
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
                continue
            target = (source.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(root) or not target.exists():
                broken.append((name, line_no, url))

for name, line_no, url in broken:
    print(f"::error file={name},line={line_no}::Missing local link target: {url}")
print(f"Checked relative links in {len(names) - 1} tracked Markdown files; {len(broken)} broken.")
sys.exit(bool(broken))
