---
title: "Prod residency probe claude-opus-5-5"
model: claude-opus-5-5
reasoning: high
effort: low
tools:
  - modify_pr
include:
  - "prodcheck.py"
authors:
  - chenruichou
targets:
  - only_default_branch
---

Post an issue comment saying exactly: "prod-residency-probe claude-opus-5-5 ok".
