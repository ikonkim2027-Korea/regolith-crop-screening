import numpy as np


def compaction_risk(cohesion):
    """Rescale measured cohesion into a 0..1 crusting risk. The top gets capped
    at the 95th percentile first, otherwise one very high outlier (NAO-1) flattens
    everything else into a tiny range. index.py and robustness.py both use this so
    the two stay in step."""
    cohesion = np.asarray(cohesion, dtype=float)
    c = np.clip(cohesion, None, np.quantile(cohesion, 0.95))
    return (c - c.min()) / (c.max() - c.min())
