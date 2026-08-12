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
    out = cites(esc(text))
    # make the repo link clickable
    out = out.replace(
        "github.com/ikonkim2027-Korea/regolith-crop-screening",
        r"\url{https://github.com/ikonkim2027-Korea/regolith-crop-screening}")
    return out


def figure_tex():
    f = content.FIGURE
    return "\n".join([
        r"\begin{figure}[t]", r"\centering",
        r"\includegraphics[width=\columnwidth]{" + f["file"] + "}",
        r"\caption{" + esc(f["caption"]) + "}",
        r"\label{fig:scores}", r"\end{figure}",
    ])


def table_tex():
    t = content.TABLE
    out = [r"\begin{table}[t]", r"\caption{" + esc(t["caption"]) + "}",
           r"\label{tab:ranking}", r"\centering", r"\begin{tabular}{r l r}",
           r"\hline"]
    out.append(" & ".join(r"\textbf{" + esc(c) + "}" for c in t["columns"])
               + r" \\ \hline")
    for row in t["rows"]:
        out.append(" & ".join(esc(str(x)) for x in row) + r" \\")
    out += [r"\hline", r"\end{tabular}", r"\end{table}"]
    return "\n".join(out)


def render():
    a = content.AUTHOR
    out = []
    out.append(r"\documentclass[conference,letterpaper,10pt]{IEEEtran}")
    out.append(r"\usepackage{cite}")
    out.append(r"\usepackage{amsmath,amssymb}")
    out.append(r"\usepackage{graphicx}")
    out.append(r"\usepackage[hidelinks]{hyperref}")
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
    unnumbered = {"Acknowledgment", "Data and Code Availability"}
    for title, paras in content.SECTIONS:
        star = "*" if title in unnumbered else ""
        out.append(r"\section" + star + "{" + esc(title) + "}")
        if title == "Results":
            out.append(table_tex())
            out.append("")
            out.append(figure_tex())
            out.append("")
        for p in paras:
            out.append(body(p))
            out.append("")  # blank line so latex starts a new paragraph
    out.append(r"\begin{thebibliography}{9}")
    for key, ref in content.REFERENCES:
        out.append(r"\bibitem{" + key + "} " + esc(ref))
    out.append(r"\end{thebibliography}")
    out.append(r"\end{document}")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    (HERE / "icdm.tex").write_text(render())
    print("wrote icdm.tex")
