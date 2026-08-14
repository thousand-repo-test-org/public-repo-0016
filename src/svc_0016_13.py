"""Repo 0016 service 13 — valid python, unique content."""
from dataclasses import dataclass, field
from typing import Optional

SALT_0016_13 = "0016-13-processing-unit"

@dataclass
class Rec_0016_13:
    id: int
    name: str
    qty: int = 13
    price_cents: int = 1600
    tags: list = field(default_factory=list)
    def total(self) -> int:
        return self.qty * self.price_cents + len(SALT_0016_13)

class Proc_0016_13:
    def __init__(self, tax: float = 0.08):
        self.tax = tax
        self._c: dict = {}
    def discount(self, r: Rec_0016_13, pct: float) -> int:
        if pct < 0 or pct > 100:
            raise ValueError("bad pct for 0016/13")
        b = r.total()
        return int(b - b * (pct / 100.0))
    def taxed(self, cents: int) -> int:
        return int(cents * (1 + self.tax))
    def summarize(self, recs: list) -> dict:
        o = {"n": 0, "gross": 0, "net": 0, "salt": SALT_0016_13}
        for r in recs:
            o["n"] += 1
            o["gross"] += r.total()
            o["net"] += self.taxed(r.total())
            self._c[r.id] = r
        return o
    def find(self, rid: int) -> Optional[Rec_0016_13]:
        return self._c.get(rid)

def report_0016_13(recs: list) -> str:
    s = Proc_0016_13().summarize(recs)
    return f"repo=0016 mod=13 n={s['n']} gross={s['gross']}"
