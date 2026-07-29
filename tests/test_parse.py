import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from harmonize import parse_num


def test_parse_num():
    assert parse_num("1.5") == 1.5
    assert parse_num("0.15 - 0.7") == 0.425   # range -> midpoint
    assert parse_num("1.5*") == 1.5           # star gets stripped
    assert parse_num("NA") is None
    assert parse_num("") is None


if __name__ == "__main__":
    test_parse_num()
    print("ok")
