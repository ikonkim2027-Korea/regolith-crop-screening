# renders content.py into an IEEEtran conference .tex file.
# using an inline thebibliography instead of a .bib because i compile this on
# overleaf in one pass and don't run bibtex locally.
import re
from pathlib import Path
import content

HERE = Path(__file__).resolve().parent

# latex special characters that show up in prose. no % or & in the text right
# now but escape them anyway so a later edit doesn't break the build.
_ESC = {"&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_"}


def esc(text):
    for ch, rep in _ESC.items():
        text = text.replace(ch, rep)
    return text


def cites(text):
    # {russell} -> \cite{russell}, {a}{b} -> \cite{a,b}
    text = re.sub(r"(\{[a-z]+\})+", _merge_cite, text)
    return text


def _merge_cite(m):
    keys = re.findall(r"\{([a-z]+)\}", m.group(0))
    return r"\cite{" + ",".join(keys) + "}"


def body(text):
    return cites(esc(text))


def render():
    a = content.AUTHOR
    out = []
    out.append(r"\documentclass[conference]{IEEEtran}")
    out.append(r"\usepackage{cite}")
    out.append(r"\usepackage{amsmath,amssymb}")
    out.append(r"\usepackage{graphicx}")
    out.append(r"\begin{document}")
    out.append(r"\title{" + esc(content.TITLE) + "}")
    aff = r"\\".join(esc(x) for x in a["affiliation"])
    out.append(r"\author{\IEEEauthorblockN{" + esc(a["name"]) + "}")
    out.append(r"\IEEEauthorblockA{" + aff + "}}")
    out.append(r"\maketitle")
    out.append(r"\begin{abstract}")
    out.append(body(content.ABSTRACT))
    out.append(r"\end{abstract}")
    out.append(r"\begin{IEEEkeywords}")
    out.append(esc(", ".join(content.KEYWORDS)))
    out.append(r"\end{IEEEkeywords}")
    for title, paras in content.SECTIONS:
        out.append(r"\section{" + esc(title) + "}")
        for p in paras:
            out.append(body(p))
    out.append(r"\begin{thebibliography}{9}")
    for key, ref in content.REFERENCES:
        out.append(r"\bibitem{" + key + "} " + esc(ref))
    out.append(r"\end{thebibliography}")
    out.append(r"\end{document}")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    (HERE / "icdm.tex").write_text(render())
    print("wrote icdm.tex")
