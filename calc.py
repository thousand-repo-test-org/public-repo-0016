"""Small numeric helpers used by the residency E2E probe."""


def mean(values):
    """Arithmetic mean of a sequence of numbers."""
    return sum(values) / len(values)


def percentile(values, p):
    """Return the p-th percentile (0-100) using nearest-rank."""
    ordered = sorted(values)
    rank = int(len(ordered) * p / 100)
    return ordered[rank]


def running_total(values):
    """Running totals, one entry per input value."""
    total = 0
    out = []
    for v in values:
        total += v
        out.append(total)
    return out
