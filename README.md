# regolith-crop-screening

Ranking lunar and asteroid regolith simulants by how likely they are to crust and
stress plants, worked out from soil numbers that are already published. The point
is to say, before any greenhouse trial, which simulants are worth the weeks a trial
takes.

## why bother

Crops on the Moon or Mars have to grow in regolith, which is harsh soil: alkaline,
short on nutrients, and it packs into a crust that keeps water off the roots. Labs
make dozens of simulants to stand in for the real thing, and the only way to know
whether plants tolerate one is to grow in it for weeks. There are far more
simulants than anyone has time to test, so guessing the bad ones up front saves
real work.

## the result

23 simulants scored from 0 (friendliest to plants) to 1 (riskiest):

| friendliest |      | riskiest |      |
|-------------|------|----------|------|
| LSS-ISAC-1  | 0.00 | NAO-1    | 1.00 |
| EAC-1A      | 0.00 | IGG-01   | 1.00 |
| MLS-1       | 0.02 | OB-1A    | 0.79 |
| CAS-1       | 0.04 | PolyU-1  | 0.71 |
| JSC-1       | 0.04 | JSC-1A   | 0.63 |

The first thing I tried, predicting cohesion from grain size and density with a
random forest, did not work: the score went negative under mission-grouped cross
validation. So the index uses the measured cohesion straight, as a crusting-risk
score, with a small pH correction where a simulant has published chemistry. A
2000-run jitter test says the top and bottom of the ranking hold while the middle
shuffles around.

## how it works

One script per step under `src/`, meant to run in this order:

1. `harmonize.py` joins the raw property tables into one row per simulant
2. `calibrate.py` fits plant stress against soil pH from the OSD-670 study
3. `index.py` turns measured cohesion into a crusting-risk score and folds in pH
4. `validate.py` checks the ranking against the two simulants with growth data
5. `robustness.py` re-runs the ranking under noise to see what holds
6. `make_table.py` writes the clean ranked table

`model.py` is the cohesion-prediction attempt that did not pan out, kept in as an
honest negative result. `plot.py` draws the bar chart. Parsing and the grain-size
math have their own checks in `tests/`.

## data

All reused public data, nothing measured here. The sources and their licenses are
listed in `data/raw/PROVENANCE.md`. Raw downloads and processed tables are
gitignored.

## paper

`paper/` holds the manuscript, one markdown file per section, stitched together in
`paper/draft.md`. The version for the ICDM Teen symposium lives in `paper/icdm/`,
built to the IEEE format as both LaTeX (for Overleaf) and Word.
