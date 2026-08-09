# abstract + intro (draft)

## abstract

Growing crops on the Moon or Mars will mean growing them in regolith, and testing
whether plants tolerate a given simulant takes a full multi week growth trial, so
only a few of the many simulants have been tested. This work asks whether published
soil measurements alone can screen simulants for how hard they will be on plants,
without a growth trial. I join three public datasets, engineering properties, grain
size and plant results, into one table. A random forest to predict cohesion from
the other properties fails on mission grouped cross validation (R2 below zero),
which I report rather than hide, since it reflects how noisy pooled cohesion data
is. Instead I build a screening score from measured cohesion and a small pH to
stress calibration, and rank 23 simulants. The ranking agrees with the two soils
that have published growth results, and a jitter test shows the friendly and risky
ends are stable while the middle is not.

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
part of the story here, not something I cut out to make the paper look cleaner.

# background / related work (draft)

## growing food off Earth

Long missions cannot carry all their soil up from Earth, so crops will eventually
have to grow in the local regolith, which is a poor growth medium. The regolith
tested for plants so far is alkaline, holds very few nutrients, and compacts into a
surface crust that keeps water from the roots [russell].

## what people have grown so far

A handful of groups have actually put plants in regolith simulant. Wamelink and
coworkers [wamelink] got seeds to germinate in diluted Mars and Moon simulants,
though the plants stayed small. Eichler [eichler] found the opposite: on plain
Martian simulant with no amendment, almost nothing grew. The most useful study
for this project is Russell [russell], who grew lettuce, radish and pepper in a
carbonaceous asteroid simulant mixed with peat and watched growth fall as the
simulant fraction rose. Radish suffered the most, and the authors blamed
compaction and crusting rather than missing nutrients. A recent review [duri]
pulls these together and points out that lunar simulants in particular are
alkaline and nutrient poor, with JSC-1A giving poor growth and LHS-1 managing a
little.

## the soil side

On the engineering side there is a lot of measured data that never gets used for
plant questions. Gasteiner and coworkers [gasteiner] recently put together an open
database of lunar regolith and simulant properties, with cohesion, friction angle
and bulk density across many missions and simulants. PlanetGSD [planetgsd] does
something similar for grain size across Earth, the Moon and Mars, and there have
been attempts to relate cohesion to bulk density for compacted simulants [dotson].
These are exactly the numbers that describe whether a soil will compact and crust,
but they sit in a separate literature from the plant work.

## the gap

So there are two piles of data about the same soils. One measures how the soil
behaves mechanically, the other measures how plants do in it, and the two almost
never appear together. Screening indices are common in soil and materials science,
but I did not find one that combines engineering and biology measurements to pick
a soil for space crops. Treating this as a data integration problem [doan], and
being upfront about which parts of the model work and which do not [gundersen], is
the angle this project takes.

## references

- [russell] Russell et al. 2022, Planetary Science Journal 3(7), 155
- [wamelink] Wamelink et al. 2014, PLOS ONE 9(8), e103138
- [eichler] Eichler et al. 2021, Icarus 354, 114022
- [duri] Duri et al. 2022, Frontiers in Astronomy and Space Sciences 8, 747821
- [gasteiner] Gasteiner, Murdoch and D'Angelo 2026, arXiv:2602.03829
- [planetgsd] PlanetGSD 1.0, 2026, Earth System Science Data / figshare
- [dotson] Dotson et al. 2024, Icarus 411, 115943
- [doan] Doan, Halevy and Ives, Principles of Data Integration, 2012
- [gundersen] Gundersen and Kjensmo, AAAI 2018

# methods (draft)

## the data

Three public datasets go into this. The Gasteiner open database [gasteiner] has
measured cohesion, friction angle and bulk density for lunar regolith and for
simulants, across a lot of missions and lab studies. PlanetGSD [planetgsd] gives
grain size curves, and the OSD-670 study [russell] has the plant side, with soil
pH and CEC for each peat and simulant mixture. The cohesion values needed cleaning
first, because the older reports give ranges like "0.15 - 0.7" instead of a single
number, so I took the midpoint of each range. For grain size I read the sieve
curves and computed d10, d50 and d90 for each sample.

## the model that did not work

My first idea was to predict cohesion from grain size and bulk density with a
random forest, so I could fill in simulants that have no measured cohesion. To keep
it honest I grouped the cross validation by mission, so the model never trains on a
soil from the same body it is tested on. It did not work. On grouped cross
validation the R2 came out below zero, meaning the model does worse than just
guessing the average. Cohesion barely correlates with density in this data anyway
(Spearman around 0.13). The likely reason is that the cohesion numbers come from
very different tests, from spacecraft landing estimates to lab shear tests, so they
do not fall on one clean curve. I report this instead of hiding it.

## using the measured cohesion

Since the model does not work, I use the measured cohesion directly for the
simulants that have it. Higher cohesion means the soil holds together harder and is
more likely to crust, so I treat a rescaled cohesion as a crusting risk between 0
and 1. One simulant, NAO-1, sits far above the rest at 95 kPa, so I cap the top at
the 95th percentile before rescaling, otherwise it flattens everything else into
one tiny range.

## calibrating plant stress against pH

For the chemistry side I use the OSD-670 data [russell]. As the simulant fraction
goes up the soil pH rises and the radish biomass drops. I measured the drop as a
deficit against the all peat control and fit it against pH with a straight line,
which gives deficit = 0.351 pH - 1.675. The fit is tight (R2 0.975), but it rests
on only four points, so I treat it as a rough calibration and not a real model.

## putting it into one score

The index combines the two. Where a simulant has a measured pH I take 0.4 times the
crusting risk plus 0.6 times the calibrated chemistry stress. Where it does not, and
most do not, I fall back to the crusting risk alone. In practice only one of the
ranked simulants (JSC-1A) has a published pH, so the chemistry only moves that one
row and the ranking is still driven by compaction. The two sides clearly do not
carry equal weight here yet.

## checking the ranking holds up

To see whether the ranking is just noise I jittered every cohesion value by up to
20 percent and rebuilt it two thousand times. The friendliest three simulants
stayed the same in about 78 percent of runs and the riskiest three in about 67
percent, and the overall order barely changed (Kendall tau 0.95). So the two ends
of the ranking are trustworthy, but the middle, where several simulants sit close
together, shuffles around.

(reference keys like [russell] are listed in background.md, not repeating them here)

# results (draft)

## the ranking

The index runs over the 23 simulants that have a measured cohesion value. Each one
gets a score between 0 and 1, where 0 is the friendliest to plants and 1 is the
riskiest. The scores are not evenly spread. Most simulants sit in the lower half
below about 0.5, and only a handful climb into the risky end, so the ranking is
really about picking out the few problem soils rather than splitting a smooth
gradient.

## the two ends

At the friendly end the lowest scores go to LSS-ISAC-1 (0.00), EAC-1A (0.00) and
MLS-1 (0.02), with LHS-1 (0.07) close behind. These are the low cohesion soils that
should stay loose and let water and roots through. At the risky end IGG-01 and
NAO-1 both hit the ceiling at 1.00, with OB-1A (0.79) and PolyU-1 (0.71) just under
them. NAO-1 is the one with the very high measured cohesion, so it was always going
to land here.

JSC-1A is the interesting case because it is the only simulant in the table with a
published pH, so it is the only one whose score carries the chemistry term. Its
compaction on its own is low (0.08), but the high pH pushes the chemistry stress up
and the combined score lands at 0.63, which drops it into the risky half. That
matches the plant studies, which is a good sign, but it also shows how much the
chemistry term can move a single row once the pH is known.

## does it match what the studies saw

There is no way to validate all 23 rankings, because most of these simulants have
never been grown in. But two of them have published plant results I could check
against. JSC-1A, which lands in the risky half at rank 19, is reported to cut
germination and biomass in the growth studies [duri]. LHS-1, which the index puts
in the friendlier half at rank 7, does sustain limited plant growth in the same
line of work. So on the two soils where I actually have plant data the direction of
the ranking agrees. That is only two points, so it is a sanity check and not a
proper validation, but it is reassuring that the ranking is not pointing the wrong
way.

## how stable the ranking is

The cohesion numbers are not precise, so I wanted to know how much the ranking
depends on their exact values. I jittered every cohesion by up to 20 percent and
rebuilt the whole index 2000 times. The friendliest three simulants stayed in the
friendly group in about 78 percent of the runs, and the riskiest three stayed risky
in about 67 percent. Across all the runs the median Kendall tau against the original
order was 0.95, so the overall order barely moves. Where it does move is the middle
of the table, where several simulants sit within a few hundredths of each other and
swap places under small perturbations. In practice that means the friendly and
risky groups are solid, while the exact order inside the middle band should not be
read too literally.

## what the ranking is and is not

I want to be clear about what this ranking actually is. For 22 of the 23 simulants
the score is driven entirely by compaction risk, because they have no published pH
and the chemistry term falls back to nothing. So this is mostly a physical, soil
structure ranking with a chemistry correction that so far only touches one row. It
is a screening tool: a way to point at the few simulants most likely to crust and
stress plants before anyone spends months on a growth trial, not a prediction of
exactly how much biomass each soil will yield. The honest next step is to pull pH
and CEC for more simulants so the chemistry side does real work across the table
instead of on a single soil.

(reference keys are in background.md)

# discussion (draft)

## what this says about screening regolith

The main point of this project is that you can get a useful first pass at which
simulants will be hard to grow in without running a single growth trial. The
measured soil properties are already published, and they carry enough signal to
separate the loose, friendly soils from the dense, crust prone ones. That matters
because growth trials are slow and expensive, and there are far more candidate
simulants than any lab can test. A screen that puts the likely problem soils at the
top of the list lets people spend their trial time where it counts.

The other thing worth saying is that the simple physical measure did most of the
work. I went in expecting the chemistry to matter more, and it probably does in
reality, but with public data the compaction side is what I could actually measure
across the whole set. That is a finding in itself, even if it is not the one I
expected.

## limitations

There are real limits here and I would rather name them than paper over them. The
biggest one is that the chemistry calibration rests on four points from a single
study, so the pH to stress line is a rough guide, not a validated model. The second
is that only one ranked simulant has a published pH, so the chemistry term hardly
touches the ranking yet. The third is that the cohesion values come from very
different tests, from lab shear boxes to landing estimates, which is exactly why the
random forest could not fit them. And the plant side check only covers two soils,
because those are the only ones with published growth results I could line up
against the ranking. None of these break the screen, but they do set the ceiling on
how much weight the exact scores can carry.

## what i would do next

The clearest next step is more pH and CEC values. If even half the simulants had a
published pH, the chemistry term would move more than one row and I could see
whether the compaction and chemistry rankings actually agree or pull in different
directions. After that I would want more than two soils with plant data, so the
cross-check becomes something closer to a real validation. A longer term idea is to
fold in a crusting measure that is not just cohesion, like a wet and dry cycle test,
since crusting in the field is about how a soil behaves when it dries, not only how
strong it is. But the honest first move is just filling in the chemistry column.

## conclusion

I set out to see whether public soil data alone could flag which regolith simulants
are likely to crust and stress plants, without growing anything. It can, at least
for the two ends of the ranking. A rescaled cohesion picks out the soils that
pack down hardest, a four point pH calibration adds a chemistry correction where the
data allows, and a jitter test shows the friendly and risky groups are stable even
though the middle is not. The result is a screening tool that is honest about its
limits: mostly a compaction ranking today, with a chemistry side that will only do
real work once more pH values exist. For a first pass at a hard problem, being able
to point at the likely trouble soils before anyone plants a seed is already useful.

(reference keys are in background.md)
