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
for the two ends of the ranking. A rescaled cohesion picks out the dense, crust
prone soils, a four point pH calibration adds a chemistry correction where the data
allows, and a jitter test shows the friendly and risky groups are stable even
though the middle is not. The result is a screening tool that is honest about its
limits: mostly a compaction ranking today, with a chemistry side that will only do
real work once more pH values exist. For a first pass at a hard problem, being able
to point at the likely trouble soils before anyone plants a seed is already useful.

(reference keys are in background.md)