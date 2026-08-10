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

## still to do before submitting

- fill in my email in the author block
- double-check the reference details (volumes, DOIs) against the originals
