# abstract + intro (draft)

## abstract

## introduction

### the problem

Any long stay on the Moon or Mars will eventually need to grow food in the local
regolith, because shipping soil from Earth does not scale. But regolith is a poor
medium: the material tested so far is alkaline, holds few nutrients, and packs into
a hard surface crust that keeps water from reaching roots [russell]. To prepare,
labs make simulants, ground rock mixtures meant to stand in for real regolith, and
there are now dozens of them. The trouble is that testing whether plants grow in a
simulant means a full growth trial that runs for weeks, so only a few simulants have
ever been grown in. There is no quick way to guess, up front, which of the many
simulants are likely to be the hardest on plants.

### the idea

The starting point for this project is that the numbers needed for a first guess may
already exist, just in the wrong place. Soil engineers have measured cohesion,
bulk density and grain size for many of these simulants [gasteiner][planetgsd], and
those are exactly the properties that decide whether a soil compacts and crusts. The
plant biologists, separately, have measured pH and growth for a few of them
[russell]. My idea is to bring the two together into one screening score, so a
simulant can be flagged as likely friendly or likely harsh from published
measurements alone, before anyone grows a single plant in it.

### what this paper does

This paper does four things. It joins three public datasets, the engineering
properties, the grain size curves and the plant results, into one table keyed by
simulant. It tests whether a machine learning model can predict cohesion from the
other properties, and reports honestly that it cannot on grouped cross validation.
It builds a screening score from the measured cohesion plus a small pH calibration,
and ranks 23 simulants from friendliest to riskiest. And it checks that ranking two
ways: against the handful of simulants with published growth results, and with a
jitter test to see which parts of the order are stable. The negative model result is
kept in on purpose, because it says something real about how noisy the pooled
cohesion data is.
