"""Rate limiter used by the residency reversibility probe."""

import time


class RateLimiter:
    """Fixed-window rate limiter."""

    def __init__(self, limit: int, window_seconds: int):
        self.limit = limit
        self.window_seconds = window_seconds
        self.window_start = time.time()
        self.count = 0

    def allow(self) -> bool:
        now = time.time()
        if now - self.window_start > self.window_seconds:
            self.count = 0
        self.count += 1
        return self.count <= self.limit

    def retry_after(self) -> float:
        return self.window_start + self.window_seconds - time.time()
