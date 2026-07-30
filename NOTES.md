# notes

## done so far
- repo set up, config, listed the data sources
- cleaned the cohesion values (ranges into one number)
- computing d10 / d50 / d90 from the sieve curves (had a bug where they came out
  backwards, fixed by sorting the sieve sizes first)
- built a first stage A table: cohesion + bulk density + grain size
- tried predicting cohesion with a random forest, and it does not work
- ranked the simulants by measured cohesion (crusting risk), capped the outlier
- calibrated radish stress against pH (deficit = 0.351*pH - 1.675, R2 0.975, 4 pts)
- combined the compaction risk and the pH stress into one index

## the model does not work
- grouped by mission the R2 goes negative, worse than guessing the average
- the cohesion numbers come from different tests, they do not sit on one curve

## about the index
- only JSC-1A has a measured pH (1 of 23), so the chemistry only moves that one
  row and the ranking is basically still compaction
- friendliest come out LSS-ISAC-1, EAC-1A, MLS-1 and the riskiest are IGG-01, NAO-1

## sanity check
- compared the ranking to what the papers report (validate.py). JSC-1A lands in
  the risky half and it does grow badly in the studies; LHS-1 is in the friendlier
  half and it does grow a bit. so the direction lines up, which is reassuring
- only had solid published numbers for those two though

## next
- find pH for more simulants so the chemistry side actually does something
- the ranking is still basically compaction, need to be honest about that

## questions
- is a 0.4 / 0.6 split between compaction and chemistry reasonable, or arbitrary?

## checking (came back to it)
- reran all the scripts, everything still works
- added a test for parse_num, it passes
- cleaned up a couple of unused bits (config TARGET, a stray import in model.py)
- tried a 50/50 weight but went back to 40/60, it only changes the one row anyway
