# renders content.py into a Word .docx laid out to the IEEE Computer Society
# proceedings look (US Letter, Times 10pt, numbered references).
# needs python-docx: pip install python-docx
import re
from pathlib import Path

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

import content

HERE = Path(__file__).resolve().parent

# {key} citations become [n] in order of the reference list
NUM = {k: i + 1 for i, (k, _) in enumerate(content.REFERENCES)}


def cite_sub(text):
    def repl(m):
        keys = re.findall(r"\{([a-z]+)\}", m.group(0))
        return "[" + ", ".join(str(NUM[k]) for k in keys) + "]"
    return re.sub(r"(\{[a-z]+\})+", repl, text)


def add_body(doc, text, size=10, justify=True):
    p = doc.add_paragraph()
    run = p.add_run(cite_sub(text))
    run.font.size = Pt(size)
    if justify:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(0)
    return p


def render():
    doc = Document()
    normal = doc.styles["Normal"].font
    normal.name = "Times New Roman"
    normal.size = Pt(10)

    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    sec.top_margin, sec.bottom_margin = Inches(0.75), Inches(1.0)
    sec.left_margin, sec.right_margin = Inches(0.625), Inches(0.625)

    # title
    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run(content.TITLE)
    r.bold = True
    r.font.size = Pt(18)

    # author with the required high-school affiliation
    a = content.AUTHOR
    au = doc.add_paragraph()
    au.alignment = WD_ALIGN_PARAGRAPH.CENTER
    au.add_run(a["name"] + "\n" + "\n".join(a["affiliation"]))

    # abstract
    ab = doc.add_paragraph()
    run = ab.add_run("Abstract—")
    run.bold = True
    run.italic = True
    run.font.size = Pt(9)
    r2 = ab.add_run(cite_sub(content.ABSTRACT))
    r2.italic = True
    r2.font.size = Pt(9)
    ab.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    kw = doc.add_paragraph()
    run = kw.add_run("Index Terms—")
    run.bold = True
    run.italic = True
    run.font.size = Pt(9)
    kw.add_run(", ".join(content.KEYWORDS)).font.size = Pt(9)

    # sections, numbered with roman numerals
    romans = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    for i, (title, paras) in enumerate(content.SECTIONS):
        h = doc.add_paragraph()
        h.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = h.add_run(f"{romans[i]}.  {title.upper()}")
        run.bold = True
        run.font.size = Pt(10)
        for p in paras:
            add_body(doc, p)

    # references
    h = doc.add_paragraph()
    run = h.add_run("REFERENCES")
    run.bold = True
    run.font.size = Pt(10)
    for i, (_key, ref) in enumerate(content.REFERENCES):
        p = doc.add_paragraph()
        p.add_run(f"[{i + 1}] {ref}").font.size = Pt(8)
        p.paragraph_format.space_after = Pt(0)

    return doc


if __name__ == "__main__":
    render().save(HERE / "icdm.docx")
    print("wrote icdm.docx")
