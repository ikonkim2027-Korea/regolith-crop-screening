# notes

## done so far
- repo set up, config, listed the data sources
- cleaned the cohesion values (ranges into one number)
- computing d10 / d50 / d90 from the sieve curves (had a bug where they came out
  backwards, fixed by sorting the sieve sizes first)
- built a first stage A table: cohesion + bulk density + grain size
- tried predicting cohesion with a random forest, and it does not work
- ranked the simulants by measured cohesion (crusting risk), capped the outlier
- added the osd-670 mixture chemistry and radish biomass (digitized from the
  paper). radish stress lines up with pH almost perfectly (deficit = 0.351*pH -
  1.675, R2 0.975), but it is only 4 points so I am not reading too much into it

## the model does not work
- once I group by mission the R2 goes negative, worse than guessing the average
- the cohesion numbers come from different tests, they do not sit on one curve

## next
- combine the cohesion risk and the pH stress into one score
- problem: most simulants have no measured pH, only a few do, so I need to figure
  out how to handle the ones that are missing it

## questions
- how do I combine two scores when only some simulants have both?
