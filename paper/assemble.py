# glue the section drafts into one file so i can read the whole thing at once.
# the sections stay in separate files while i'm drafting, this just concatenates.
from pathlib import Path

HERE = Path(__file__).resolve().parent
ORDER = ["abstract", "background", "methods", "results", "discussion"]

TITLE = "# From Soil Mechanics to Crop Stress\n\nIkon Kim\n"

def load(name):
    text = (HERE / f"{name}.md").read_text()
    # the section files point at background.md for the refs; drop those notes
    # when everything is in one file
    keep = [ln for ln in text.splitlines() if "reference keys" not in ln]
    return "\n".join(keep).strip()

parts = [TITLE]
refs = ""
for name in ORDER:
    body = load(name)
    if name == "background":
        # the reference list lives at the bottom of background.md; pull it out
        # so it ends up at the end of the whole paper, not in the middle
        head, sep, tail = body.partition("## references")
        if sep:
            body = head.strip()
            refs = (sep + tail).strip()
    parts.append(body)

if refs:
    parts.append(refs)

(HERE / "draft.md").write_text("\n\n".join(parts) + "\n")
print("wrote draft.md")
