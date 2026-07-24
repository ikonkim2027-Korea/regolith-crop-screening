"""Cleaning up the cohesion numbers first. A lot of the older reports give a
range like "0.15 - 0.7" or put a star on estimated values, so I need to turn
those into plain numbers before I can do anything with them."""
import re


def parse_num(x):
    if x is None:
        return None
    s = str(x).strip().replace("*", "")
    if s in ("", "NA", "N/A", "-"):
        return None
    nums = re.findall(r"-?\d+\.?\d*", s)
    if not nums:
        return None
    # if it is a range, just take the midpoint for now
    return sum(float(n) for n in nums) / len(nums)


if __name__ == "__main__":
    for v in ["1.5", "0.15 - 0.7", "1.5*", "NA", "30 - 40"]:
        print(v, "->", parse_num(v))

# TODO: load the simulant table, compute d10/d50/d90 from the sieve curves,
# then join everything on mission/sample
