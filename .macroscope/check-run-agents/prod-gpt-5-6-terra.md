---
title: "Prod residency probe gpt-5-6-terra"
model: gpt-5-6-terra
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

Post an issue comment saying exactly: "prod-residency-probe gpt-5-6-terra ok".
