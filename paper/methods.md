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

outline for the rest:
- using the measured cohesion instead (compaction risk)
- calibrating plant stress against pH
- putting the two into one score
- checking the ranking holds up
