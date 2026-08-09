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

ABSTRACT = ""

KEYWORDS = []

# (title, [paragraph, paragraph, ...])
SECTIONS = []

# (key, formatted reference string), in order of first appearance
REFERENCES = []
