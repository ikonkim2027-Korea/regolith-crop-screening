import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from harmonize import _percentiles


def test_percentiles_ordered():
    # a simple curve: most of the weight in the middle sizes
    sizes = [1, 10, 100, 1000]
    weights = [10, 40, 40, 10]
    d10, d50, d90 = _percentiles(sizes, weights)
    assert d10 <= d50 <= d90


if __name__ == "__main__":
    test_percentiles_ordered()
    print("ok")
