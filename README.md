# regolith-crop-screening

Figuring out which lunar and asteroid regolith simulants would stress plants the
most, using data that is already public instead of running greenhouse trials.

The pipeline runs end to end now and there is a full ranking of 23 simulants, so
this is past the setup stage. Writing it up is what is left.

## the idea

Space crops have to grow in regolith, which is rough soil: high pH, low nutrients,
and it compacts and forms a crust that dries roots out. There are a lot of
simulants and testing each one in a greenhouse takes weeks. I want to rank them
from measurements that already exist so you know which ones are worth testing.

## data

Pulling from a few public sources (see data/raw/PROVENANCE.md for the links).
Nothing here is my own experiment, it is all reused public data.

## layout

- src/ code
- data/ raw downloads (gitignored) and processed tables
- outputs/ figures and results (gitignored)

## running

```
python src/harmonize.py   # build the stage A table
python src/calibrate.py    # fit plant stress against soil pH
python src/index.py        # combine cohesion + chemistry into the index
python src/validate.py     # check the ranking against published growth
python src/robustness.py   # check the ranking is stable under noise
python src/plot.py         # bar chart of the ranking
```
