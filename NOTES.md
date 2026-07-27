# notes

## done so far
- repo set up, config, listed the data sources
- cleaned the cohesion values (ranges into one number)
- computing d10 / d50 / d90 from the sieve curves (had a bug where they came out
  backwards, fixed by sorting the sieve sizes first)
- built a first stage A table: cohesion + bulk density + grain size
- tried predicting cohesion with a random forest, and it does not work
- switched to just using the measured cohesion for the simulants and ranking them
  by it (crusting risk), capped the top outlier, saved it, made a bar chart

## the model does not work
- once I group by mission the R2 goes negative, worse than guessing the average
- cohesion barely correlates with density (spearman 0.13, p 0.22)
- the cohesion numbers come from different tests, they do not sit on one curve

## about the ranking
- right now this is basically sorting the simulants by cohesion, which is honest
  but a bit thin. friendliest are LSS-ISAC-1, EAC-1A, MLS-1 and the riskiest are
  IGG-01 and NAO-1
- it does not use the plant chemistry (pH / CEC) yet

## next
- bring in the OSD-670 plant data and add a chemistry side
- figure out how to combine cohesion and chemistry into one score

## questions
- what do I do about simulants with no measured pH?
