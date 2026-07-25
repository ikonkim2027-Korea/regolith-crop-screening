# notes

## done so far
- repo set up, config, listed the data sources
- cleaned the cohesion values (ranges into one number)
- computing d10 / d50 / d90 from the sieve curves (had a bug where they came out
  backwards, fixed by sorting the sieve sizes first)
- built a first stage A table: cohesion + bulk density + grain size
- tried predicting cohesion with a random forest, and it does not work

## the model does not work
- random split looked ok-ish in log space (R2 ~0.07) but that was leaking, the
  same core ends up on both sides
- once I group by mission the R2 goes negative (about -0.06), so it is worse than
  just guessing the average
- cohesion barely correlates with density anyway (spearman 0.13, p 0.22)
- gradient boosting was even worse, so it is not the model, it is the data
- the cohesion numbers come from totally different tests (landing estimates,
  penetrometer, lab), so they probably do not sit on one curve

## idea
- maybe I do not need to predict cohesion. the simulants I actually care about
  already have measured cohesion, so I could just use that directly and skip the
  ML part

## next
- pull the simulant list with their measured cohesion
- then figure out how to connect cohesion to plant stress

## questions
- what do I do about simulants with no measured pH?
