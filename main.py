"""Museum of the Year 3000 — one-line museum label entry.

Writes the museum label to /output/entry.txt (stdlib only).
"""

import os

LINE = "Smoke alarm. Screamed at toast; silent during fires. Humans removed its battery and called this 'fixing it'."

assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
assert LINE.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod("/output/entry.txt", 0o644)
