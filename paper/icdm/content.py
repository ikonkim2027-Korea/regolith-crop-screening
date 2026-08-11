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
    "affiliation": ["High School Student", "St. Mark's School",
                    "ikonkim2027@gmail.com"],
    "email": "ikonkim2027@gmail.com",
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
    ("Data", [
        "Three public datasets are used. The Gasteiner open database {gasteiner} "
        "has measured cohesion, friction angle, and bulk density for lunar "
        "regolith and simulants across many missions and lab studies. PlanetGSD "
        "{planetgsd} gives grain-size curves, and the OSD-670 study {russell} "
        "supplies the plant side, with soil pH and cation exchange capacity for "
        "each peat and simulant mixture. Nothing here is an original experiment; "
        "all of it is reused public data, with sources and licenses logged in the "
        "repository.",

        "The cohesion values needed cleaning first, because older reports give "
        "ranges such as \"0.15 - 0.7\" rather than a single number, so the "
        "midpoint of each range is taken. From the sieve curves, d10, d50, and "
        "d90 are computed per sample by sorting sizes, normalizing the weights, "
        "and interpolating the cumulative passing curve. After joining, 23 "
        "simulants carry a usable measured cohesion and enter the ranking.",
    ]),
    ("Method", [
        "The first idea was to predict cohesion from grain size and bulk density "
        "with a random forest, to fill in simulants with no measured cohesion. To "
        "keep the test honest, cross validation is grouped by mission, so the "
        "model never trains on a soil from the same body it is tested on. It does "
        "not work: the grouped-CV R2 comes out below zero, worse than predicting "
        "the mean. Cohesion barely correlates with density here (Spearman about "
        "0.13). The likely cause is that the cohesion numbers come from very "
        "different tests, from spacecraft landing estimates to lab shear boxes, so "
        "they do not fall on one clean curve. This is reported rather than hidden.",

        "Since the model does not work, the measured cohesion is used directly for "
        "the simulants that have it. Higher cohesion means a soil holds together "
        "harder and is more likely to crust, so a rescaled cohesion is treated as "
        "a crusting risk in [0, 1]. One simulant, NAO-1, sits far above the rest "
        "near 95 kPa, so the scale is capped at the 95th percentile before "
        "rescaling, otherwise it flattens everything else into one narrow band.",

        "For the chemistry side the OSD-670 data {russell} is used. As the "
        "simulant fraction rises, soil pH rises and radish biomass drops. The drop "
        "is measured as a deficit against the all-peat control and fit against pH "
        "with a straight line, giving deficit = 0.351 pH - 1.675. The fit is tight "
        "(R2 = 0.975) but rests on only four points, so it is treated as a rough "
        "calibration, not a validated model. The four mixtures span pH 4.7 to "
        "7.0, so applying the line to JSC-1A at pH 9.6 reaches well past the "
        "fitted range and pins its chemistry term at the ceiling.",

        "The index combines the two. Where a simulant has a measured pH, the score "
        "is 0.4 times the crusting risk plus 0.6 times the calibrated chemistry "
        "stress; where it does not, and most do not, the score falls back to the "
        "crusting risk alone. In practice only one ranked simulant (JSC-1A) has a "
        "published pH, so the chemistry term moves that single row and the ranking "
        "is otherwise driven by compaction. The two sides do not yet carry equal "
        "weight, and the paper does not pretend they do.",
    ]),
    ("Results", [
        "The index runs over the 23 simulants with a measured cohesion, listed in "
        "Table I. Each gets a score in [0, 1], where 0 is friendliest to plants "
        "and 1 is riskiest. "
        "The scores are not evenly spread (Fig. 1): most simulants sit below "
        "about 0.5 and "
        "only a handful reach the risky end, so the ranking is about picking out "
        "the few problem soils rather than splitting a smooth gradient. At the "
        "friendly end are LSS-ISAC-1 (0.00), EAC-1A (0.00), and MLS-1 (0.02), with "
        "LHS-1 (0.07) close behind. At the risky end IGG-01 and NAO-1 reach 1.00, "
        "with OB-1A (0.79) and PolyU-1 (0.71) just below; NAO-1 carries the very "
        "high measured cohesion and was always going to land here.",

        "JSC-1A is the informative case, as the only simulant in the table with a "
        "published pH and therefore the only score carrying the chemistry term. "
        "Its compaction alone is low (0.08), but the high pH raises the chemistry "
        "stress and the combined score reaches 0.63, moving it into the risky "
        "half. This matches the plant studies, and shows how much one row can move "
        "once its pH is known.",

        "Two simulants have published plant results to check against. JSC-1A, "
        "which the index places in the risky half at rank 19, is reported to cut "
        "germination and biomass {duri}. LHS-1, placed in the friendlier half at "
        "rank 7, does sustain limited growth in the same line of work. On the two "
        "soils with plant data the direction of the ranking agrees. Two points is "
        "a sanity check, not a validation, but it is reassuring that the ranking "
        "does not point the wrong way.",

        "To test stability, every cohesion value was jittered by up to 20 percent "
        "and the compaction ranking rebuilt 2000 times. The friendliest three simulants "
        "stayed in the friendly group in about 78 percent of runs and the riskiest "
        "three in about 67 percent, with a median Kendall tau of 0.95 against the "
        "original order. The order barely moves overall; where it moves is the "
        "middle, where several simulants sit within a few hundredths and swap "
        "places. So the two ends are solid and the middle band should not be read "
        "as an exact order. This test moves the compaction scores only, so it "
        "does not probe JSC-1A, the single row the chemistry term adjusts.",

        "It is worth being clear about what the ranking is. For 22 of the 23 "
        "simulants the score is driven entirely by compaction, because they have "
        "no published pH. So this is mostly a physical, soil-structure ranking "
        "with a chemistry correction that so far touches one row. It is a "
        "screening tool, a way to point at the simulants most likely to crust and "
        "stress plants before anyone spends months on a growth trial, not a "
        "prediction of exact biomass.",
    ]),
    ("Discussion", [
        "The main point is that a useful first pass at which simulants will be "
        "hard to grow in is possible without running a single growth trial. The "
        "measured properties already exist and carry enough signal to separate "
        "loose, friendly soils from dense, crust-prone ones. Because trials are "
        "slow and expensive and there are far more candidate simulants than any "
        "lab can test, a screen that puts likely problem soils at the top lets "
        "people spend trial time where it counts. Notably, the simple physical "
        "measure did most of the work; the chemistry probably matters more in "
        "reality, but compaction is what public data let me measure across the "
        "whole set, which is itself a finding.",

        "The limits are worth naming. The chemistry calibration rests on four "
        "points from one study, so the pH-to-stress line is a rough guide. Only "
        "one ranked simulant has a published pH, so the chemistry term hardly "
        "touches the ranking. The cohesion values come from very different tests, "
        "which is exactly why the random forest could not fit them. That same "
        "spread shows up across properties: cohesion, friction angle, and bulk "
        "density barely correlate here (Spearman weak and not significant), so "
        "ranking by another mechanical property would not reproduce this order. The score reflects "
        "cohesion specifically, the property Russell tied to crusting, rather than "
        "a general strength axis. And the plant check covers only two soils. None "
        "of these break the screen, but they set a ceiling on how much weight the "
        "exact scores can carry. The clearest next step is more pH and CEC values, "
        "though published measurements for these simulants are scarce, so filling "
        "that column may mean measuring them rather than mining papers.",
    ]),
    ("Conclusion", [
        "This work asked whether public soil data alone can flag which regolith "
        "simulants are likely to crust and stress plants, without growing "
        "anything. It can, at least for the two ends of the ranking. A rescaled "
        "cohesion picks out the soils that pack down hardest, a four-point pH "
        "calibration adds a chemistry correction where the data allows, and a "
        "jitter test shows the friendly and risky groups are stable while the "
        "middle is not. The negative modeling result is reported alongside the "
        "positive screen. For a first pass at a hard problem, pointing at the "
        "likely trouble soils before anyone plants a seed is already useful.",
    ]),
    ("Acknowledgment", [
        "The author thanks Seo Ho Song for guidance, and the teams behind the "
        "Gasteiner database, PlanetGSD, and the OSD-670 study for making their "
        "measurements public.",
    ]),
    ("Data and Code Availability", [
        "Every input used here is public and cited above. The code that cleans "
        "the data, builds the score, and runs the checks is available at "
        "github.com/ikonkim2027-Korea/regolith-crop-screening.",
    ]),
]

# the score distribution figure, rendered into the Results section.
FIGURE = {
    "file": "fig_scores.png",
    "caption": "Distribution of screening scores across the 23 simulants. Most "
               "sit at the low, plant-friendly end, with only a few reaching the "
               "risky end.",
}

# the ranking table. rendered into the Results section by both renderers.
TABLE = {
    "caption": "The 23 simulants ranked by screening score (0 = friendliest to "
               "plants, 1 = riskiest).",
    "columns": ["Rank", "Simulant", "Score"],
    "rows": [
        [1, "LSS-ISAC-1", "0.00"],
        [2, "EAC-1A", "0.00"],
        [3, "MLS-1", "0.02"],
        [4, "CAS-1", "0.04"],
        [5, "JSC-1", "0.04"],
        [6, "BP-1", "0.04"],
        [7, "LHS-1", "0.07"],
        [8, "KLS-1", "0.08"],
        [9, "LMS-1", "0.19"],
        [10, "TLS-01", "0.25"],
        [11, "CUG-1A", "0.25"],
        [12, "OPRL2N", "0.36"],
        [13, "NU-LHT-4M", "0.42"],
        [14, "FJS-1", "0.42"],
        [15, "WHU-1", "0.52"],
        [16, "CSM-LHT-1", "0.63"],
        [17, "CSM-LMT-1", "0.63"],
        [18, "OPRH3N", "0.63"],
        [19, "JSC-1A", "0.63"],
        [20, "PolyU-1", "0.71"],
        [21, "OB-1A", "0.79"],
        [22, "IGG-01", "1.00"],
        [23, "NAO-1", "1.00"],
    ],
}

# (key, formatted reference string), in order of first appearance.
# double-check volumes/DOIs against the originals before submitting.
REFERENCES = [
    ("russell",
     "S. J. Russell, S. K. Fieber-Beyer, and K. A. Yurkonis, \"CI asteroid "
     "regolith as an in situ plant growth medium for space crop production,\" "
     "Planetary Science Journal, vol. 3, no. 7, art. 155, 2022, "
     "doi:10.3847/PSJ/ac74c9."),
    ("gasteiner",
     "L. Gasteiner, N. Murdoch, et al., \"An open database of lunar regolith "
     "and simulants properties,\" arXiv:2602.03829, 2026."),
    ("planetgsd",
     "A global dataset of grain-size distributions from Earth, the Moon, and "
     "Mars, Earth System Science Data, preprint essd-2026-206, 2026."),
    ("wamelink",
     "G. W. W. Wamelink et al., \"Can plants grow on Mars and the Moon: a growth "
     "experiment on Mars and Moon soil simulants,\" PLOS ONE, vol. 9, no. 8, "
     "e103138, 2014."),
    ("eichler",
     "A. Eichler et al., \"Challenging the agricultural viability of Martian "
     "regolith simulants,\" Icarus, vol. 354, art. 114022, 2021."),
    ("duri",
     "L. G. Duri et al., \"The potential for lunar and Martian regolith "
     "simulants to sustain plant growth: a multidisciplinary overview,\" "
     "Frontiers in Astronomy and Space Sciences, vol. 8, art. 747821, 2022."),
    ("dotson",
     "B. Dotson et al., \"Cohesion and shear strength of compacted lunar and "
     "Martian regolith simulants,\" Icarus, vol. 411, art. 115943, 2024."),
    ("doan",
     "A. Doan, A. Halevy, and Z. Ives, Principles of Data Integration. Morgan "
     "Kaufmann, 2012."),
    ("gundersen",
     "O. E. Gundersen and S. Kjensmo, \"State of the art: reproducibility in "
     "artificial intelligence,\" in Proc. AAAI, 2018."),
]
