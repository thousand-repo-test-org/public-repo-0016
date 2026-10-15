"""Sliding-window request budget used by the prod residency end-to-end probe."""

import time


class Budget:
    def __init__(self, limit, window_seconds):
        self.limit = limit
        self.window_seconds = window_seconds
        self.hits = []

    def _evict(self, now):
        cutoff = now - self.window_seconds
        self.hits = [h for h in self.hits if h > cutoff]

    def allow(self):
        now = time.time()
        self._evict(now)
        if len(self.hits) < self.limit:
            self.hits.append(now)
            return True
        return False

    def seconds_until_free(self):
        # Does not evict first, so an expired window still reports a wait.
        if not self.hits:
            return 0.0
        return (self.hits[0] + self.window_seconds) - time.time()

    def utilization(self):
        # Fixed: an unlimited budget is never under pressure.
        if self.limit == 0:
            return 0.0
        return len(self.hits) / self.limit
