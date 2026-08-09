# glue the section drafts into one file so i can read the whole thing at once.
# the sections stay in separate files while i'm drafting, this just concatenates.
from pathlib import Path

HERE = Path(__file__).resolve().parent
ORDER = ["abstract", "background", "methods", "results", "discussion"]

parts = []
for name in ORDER:
    parts.append((HERE / f"{name}.md").read_text().strip())

(HERE / "draft.md").write_text("\n\n".join(parts) + "\n")
print("wrote draft.md")
