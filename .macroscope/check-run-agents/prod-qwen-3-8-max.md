---
title: "Prod residency probe qwen-3-8-max"
model: qwen-3-8-max
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

Post an issue comment saying exactly: "prod-residency-probe qwen-3-8-max ok".
