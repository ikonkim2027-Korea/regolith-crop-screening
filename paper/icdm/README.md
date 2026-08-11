# icdm paper

The submission version of the paper, formatted for the IEEE Computer Society
proceedings look (US Letter, two column, 10pt Times).

`content.py` holds the whole paper as plain text in one place. Two little renderers
read it so the LaTeX and Word versions never drift apart:

```
python make_fig.py   # -> fig_scores.png  (the score distribution)
python to_tex.py     # -> icdm.tex   (IEEEtran, compile on Overleaf)
python to_docx.py    # -> icdm.docx  (python-docx, opens in Word)
```

For the LaTeX version I compile `icdm.tex` on Overleaf with the IEEE template, since
I don't have a TeX setup locally. The bibliography is inlined in the .tex so it
builds in one pass without bibtex. The Word version needs `python-docx`.

## ICDM Teen Research Symposium rules I'm building to

- up to 5 pages including figures, tables, and references
- IEEE Computer Society proceedings format
- single-blind, so my name stays on it
- the first author affiliation has to say "High School Student" (it does)
- deadline is 20 August 2026

## formatting, checked against the IEEE CS 8.5x11 guidelines

the docx follows the measured numbers from the guidelines:

- page: US Letter, 8.5 x 11 in
- print area: 6.875 in wide (matches the spec exactly)
- margins: top 1.0 in, bottom 1.125 in, left and right 0.8125 in
- two columns with a 5/16 in (0.3125 in) gap
- body: 10pt Times New Roman, single spaced, fully justified
- title 24pt, abstract and index terms 9pt, section headings 10pt roman numerals
- no page numbers or running header/footer, same as the IEEE template

the latex version uses the standard IEEEtran conference class (letterpaper, 10pt),
which is the accepted IEEE format; i did not override its geometry because the
class is meant to be used as is. so the two files are laid out by their own
templates and both come out to 4 pages, under the 5 page limit.

## still to do before submitting

- confirm the name in the acknowledgment reads right
