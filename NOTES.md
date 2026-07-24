# notes

## done so far
- repo set up, config, listed the data sources
- cleaned the cohesion values (ranges into one number)
- computing d10 / d50 / d90 from the sieve curves (had a bug where they came out
  backwards, fixed by sorting the sieve sizes first)
- built a first stage A table: cohesion + bulk density + grain size

## problem
- only 31 of the 96 cohesion rows actually have grain size that lines up. the
  sieve data is per sample and cohesion is per mission, so a lot of missions have
  no matching PSD. might have to lean on bulk density more than I wanted.

## next
- try predicting cohesion from grain size + density and see if it even works
- then figure out how to connect that to plant stress

## questions
- what do I do about simulants with no measured pH?
- is the midpoint the right way to collapse a range, or should I keep the width?
