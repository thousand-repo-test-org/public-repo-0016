"""Token-bucket rate limiting helpers."""

import time


class TokenBucket:
    """Refills at `rate` tokens per second, capped at `capacity`."""

    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.rate = rate
        self.tokens = capacity
        self.updated_at = time.monotonic()

    def _refill(self):
        now = time.monotonic()
        self.tokens = min(self.capacity, self.tokens + (now - self.updated_at) * self.rate)
        self.updated_at = now

    def allow(self, cost=1):
        self._refill()
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False


def retry_after(bucket, cost=1):
    """Seconds to wait before `cost` tokens will be available."""
    if bucket.tokens >= cost:
        return 0
    return (cost - bucket.tokens) / bucket.rate
