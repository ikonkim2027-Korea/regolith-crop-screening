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
SECTIONS = [
    ("Introduction", [
        "Any long stay on the Moon or Mars will eventually need to grow food in "
        "the local regolith, because shipping soil from Earth does not scale. "
        "Regolith is a poor medium: the material tested so far is alkaline, holds "
        "few nutrients, and packs into a hard surface crust that keeps water from "
        "reaching roots {russell}. To prepare, labs make simulants, ground rock "
        "mixtures meant to stand in for real regolith, and there are now dozens "
        "of them. Testing whether plants grow in a simulant means a growth trial "
        "that runs for weeks, so only a few have ever been grown in. There is no "
        "quick way to guess, up front, which of the many simulants are hardest on "
        "plants.",

        "The numbers needed for a first guess may already exist, just in the "
        "wrong place. Soil engineers have measured cohesion, bulk density, and "
        "grain size for many of these simulants {gasteiner}{planetgsd}, and those "
        "properties decide whether a soil compacts and crusts. Plant biologists, "
        "separately, have measured pH and growth for a few of them {russell}. "
        "This project brings the two together into one screening score, so a "
        "simulant can be flagged as likely friendly or likely harsh from "
        "published measurements alone, before anyone grows a single plant in it.",

        "The paper makes four contributions. It joins three public datasets into "
        "one table keyed by simulant. It tests whether a model can predict "
        "cohesion from the other properties, and reports honestly that it cannot "
        "under grouped cross validation. It builds a screening score from "
        "measured cohesion plus a small pH calibration and ranks 23 simulants. "
        "And it checks that ranking two ways, against the simulants with "
        "published growth results and with a jitter test for stability. The "
        "negative model result is kept as part of the story, not cut to make the "
        "work look cleaner.",
    ]),
    ("Related Work", [
        "Several groups have put plants in regolith simulant. Wamelink and "
        "coworkers {wamelink} germinated seeds in diluted Mars and Moon "
        "simulants, though the plants stayed small. Eichler {eichler} found that "
        "on plain Martian simulant with no amendment almost nothing grew. Most "
        "relevant here, Russell {russell} grew lettuce, radish, and pepper in a "
        "carbonaceous asteroid simulant mixed with peat and watched growth fall "
        "as the simulant fraction rose, with radish worst hit and compaction and "
        "crusting blamed over missing nutrients. A recent review {duri} adds that "
        "lunar simulants in particular are alkaline and nutrient poor, with "
        "JSC-1A giving poor growth and LHS-1 managing a little.",

        "On the engineering side there is measured data that is rarely used for "
        "plant questions. Gasteiner and coworkers {gasteiner} compiled an open "
        "database of lunar regolith and simulant properties, with cohesion, "
        "friction angle, and bulk density across many missions. PlanetGSD "
        "{planetgsd} does the same for grain size, and others have tried to "
        "relate cohesion to bulk density for compacted simulants {dotson}. These "
        "numbers describe whether a soil compacts and crusts, but they sit in a "
        "separate literature from the plant work.",

        "So there are two piles of data about the same soils that almost never "
        "appear together. Screening indices are common in soil and materials "
        "science, but none was found that combines engineering and biology "
        "measurements to pick a soil for space crops. Treating this as a data "
        "integration problem {doan}, and being explicit about which parts of the "
        "model work and which do not {gundersen}, is the angle taken here.",
    ]),
]

# (key, formatted reference string), in order of first appearance
REFERENCES = []
