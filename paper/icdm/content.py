# single source for the icdm paper. both renderers (to_tex.py and to_docx.py)
# read this so the latex and word versions do not drift apart.
#
# citations in the paragraph text are written as {russell}, {gasteiner}, etc.
# each renderer swaps those for its own citation style. keep REFERENCES in order
# of first appearance so the numbers line up in both outputs.

TITLE = ("From Soil Mechanics to Crop Stress: Screening Regolith Simulants "
         "for Plant Suitability from Public Soil Data")

# icdm is single-blind and wants "High School Student" in the first author's
# affiliation line, so it goes here.
AUTHOR = {
    "name": "Ikon Kim",
    "affiliation": ["High School Student", "St. Mark's School"],
    "email": "",  # fill in before submitting
}

ABSTRACT = (
    "Growing crops on the Moon or Mars means growing them in regolith, and "
    "testing whether plants tolerate a given simulant takes a multi-week growth "
    "trial, so only a few of the many published simulants have been tested. This "
    "work asks whether public soil measurements alone can screen simulants for "
    "how hard they are on plants, before any trial. Three public datasets, "
    "engineering properties, grain size, and plant results, are joined into one "
    "table keyed by simulant. A random forest that tries to predict cohesion "
    "from the other properties fails under mission-grouped cross validation "
    "(R2 below zero); this negative result is reported because it reflects how "
    "noisy the pooled cohesion data is. In its place a screening score is built "
    "from measured cohesion and a small pH-to-stress calibration, and 23 "
    "simulants are ranked from friendliest to riskiest. The ranking agrees with "
    "the two simulants that have published growth results, and a jitter test "
    "shows the friendly and risky ends are stable while the middle is not. The "
    "result is a reproducible screen that flags likely problem soils from data "
    "that already exists.")

KEYWORDS = ["data integration", "screening index", "regolith simulants",
            "space agriculture", "ranking", "reproducibility"]

# (title, [paragraph, paragraph, ...])
SECTIONS = []

# (key, formatted reference string), in order of first appearance
REFERENCES = []
