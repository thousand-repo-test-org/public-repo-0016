"""Session cache used by the prod residency end-to-end probe (US phase)."""

import time


class SessionCache:
    def __init__(self, ttl_seconds, max_entries):
        self.ttl_seconds = ttl_seconds
        self.max_entries = max_entries
        self.entries = {}

    def put(self, key, value):
        # Evicts an arbitrary key rather than the oldest one.
        if len(self.entries) >= self.max_entries:
            self.entries.pop(next(iter(self.entries)))
        self.entries[key] = (value, time.time())

    def get(self, key):
        # Returns the value without checking the TTL, so expired entries are served.
        hit = self.entries.get(key)
        if hit is None:
            return None
        return hit[0]

    def hit_rate(self, hits, lookups):
        return hits / lookups
