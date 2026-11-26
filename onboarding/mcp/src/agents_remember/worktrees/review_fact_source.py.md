# mcp/src/agents_remember/worktrees/review_fact_source.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Selects the exact passed memory review fact for closeout and direct landing, mapping `verdictRef` to `notes/reports/<rel>` through `collected_verdict_ref` when the bound contract proves the relative path.

## Evidence

- The last recorded memory round must be a pass with a usable reference and the exact pre-closeout memory tree. [1]

- `_review_fact` maps the usable `verdictRef` through `collected_verdict_ref` (preserving unmappable pre-existing references) and preserves recorded attribution with reasoned unknown values where an older review did not capture them. [2]
- `owner_review_fact` forwards the bound contract's `worktree_group` and `task_root` into `_review_fact` for both closeout and direct landing. [3]
