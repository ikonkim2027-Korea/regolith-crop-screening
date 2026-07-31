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

outline for the rest:
- the machine learning test that did not work
- using the measured cohesion instead (compaction risk)
- calibrating plant stress against pH
- putting the two into one score
- checking the ranking holds up
