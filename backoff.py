"""Exponential backoff helpers for retrying flaky calls."""

import random


def backoff_delays(attempts, base=0.5, cap=30.0, jitter=True):
    """Yield the delay to wait before each retry attempt."""
    for attempt in range(attempts):
        delay = min(cap, base * (2 ** attempt))
        if jitter:
            delay = random.uniform(0, delay)
        yield delay


def total_backoff(attempts, base=0.5, cap=30.0):
    """Worst-case total seconds spent sleeping across `attempts` retries."""
    return sum(min(cap, base * (2 ** a)) for a in range(attempts))


def should_retry(status_code, attempt, attempts):
    """Whether a response with `status_code` warrants another attempt."""
    if attempt >= attempts:
        return False
    return status_code >= 500 or status_code == 429
