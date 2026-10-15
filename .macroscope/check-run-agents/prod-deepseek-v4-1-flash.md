---
title: "Prod residency probe deepseek-v4-1-flash"
model: deepseek-v4-1-flash
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

Post an issue comment saying exactly: "prod-residency-probe deepseek-v4-1-flash ok".
