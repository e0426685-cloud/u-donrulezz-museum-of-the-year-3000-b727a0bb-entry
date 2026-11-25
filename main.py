"""Museum of the Year 3000 — one-line museum label entry.

Writes the museum label to /output/entry.txt (stdlib only).
"""

import os

LINE = "Smoke alarm. Screamed at toast; silent during fires. Humans removed its battery and called this 'fixing it'."

def validate(line):
    """Check the label meets the gate: 1-200 chars, one line, not blank."""
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if not line.isprintable():
        raise ValueError("entry must contain only printable characters")
    return line


validate(LINE)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod("/output/entry.txt", 0o644)

with open("/output/entry.txt", "r", encoding="utf-8") as f:
    written = f.read()
if written != LINE:
    raise ValueError("round-trip check failed: entry.txt does not match the label")
