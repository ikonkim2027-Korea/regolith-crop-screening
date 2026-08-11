# data check

simulant table: 24 rows
- with cohesion: 23  (dropped for no cohesion: 1)
- with bulk density: 20
- duplicate simulant names: 0
- cohesion kPa: min 0.34, median 5.00, max 95.30
- above the 95th percentile (18.8 kPa), so capped in the score: IGG-01, NAO-1

calibration: 4 peat/simulant mixtures, pH 4.7 to 7.0
- two of the four biomass values were read off Russell's figure by eye
chemistry coverage: 1 of 23 ranked simulants have a published pH
ground truth for validation: 2 simulants with published growth

cross-checks
- index.csv rows: 23, equals the cohesion count: True
- ranked names missing from the source table: 0
