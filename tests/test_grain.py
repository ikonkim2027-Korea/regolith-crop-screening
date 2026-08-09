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


def test_percentiles_unsorted_input():
    # this is the bug i had before: if the rows come in out of size order the
    # percentiles used to flip. the helper should sort internally now.
    sizes = [1000, 1, 100, 10]
    weights = [10, 10, 40, 40]
    d10, d50, d90 = _percentiles(sizes, weights)
    assert d10 <= d50 <= d90
    assert 1 <= d10 <= 1000


if __name__ == "__main__":
    test_percentiles_ordered()
    test_percentiles_unsorted_input()
    print("ok")
