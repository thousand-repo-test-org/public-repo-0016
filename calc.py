"""Small utility module used to exercise automated review."""


def average(values):
    total = 0
    for v in values:
        total += v
    return total / len(values)


def percentile(values, p):
    ordered = sorted(values)
    idx = int(len(ordered) * p)
    return ordered[idx]


def normalize(values):
    hi = max(values)
    return [v / hi for v in values]
