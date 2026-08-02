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
swap places under small perturbations. The takeaway is to trust the two ends of the
ranking and to read the middle as a rough band rather than an exact order.

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
