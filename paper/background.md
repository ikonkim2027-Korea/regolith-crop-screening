# background / related work (draft)

## growing food off Earth

Long missions cannot carry all their soil up from Earth, so crops will eventually
have to grow in the local regolith. That is a hard ask. The regolith that has been
tested for plants is alkaline, holds very few nutrients, and physically it packs
down and forms a surface crust that keeps water from reaching the roots [russell].
Because a greenhouse trial on a single candidate soil takes weeks, it helps to
know ahead of time which soils are most likely to fail.

## what people have grown so far

A handful of groups have actually put plants in regolith simulant. Wamelink and
coworkers [wamelink] got seeds to germinate in diluted Mars and Moon simulants,
though the plants stayed small. Eichler [eichler] took a harder line: on plain
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
