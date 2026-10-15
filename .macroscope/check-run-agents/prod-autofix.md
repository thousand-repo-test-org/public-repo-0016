---
title: "Prod residency autofix probe"
model: gpt-6-luna
reasoning: high
effort: low
tools:
  - modify_pr
include:
  - "quota.py"
authors:
  - chenruichou
targets:
  - only_default_branch
---

`Quota.remaining` can return a negative number when a tenant has over-consumed.
Fix it by clamping the result at zero, editing `quota.py` directly with your
modify_pr tool. Do not merely describe the fix — apply it.
