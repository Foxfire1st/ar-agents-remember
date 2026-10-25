# mcp/tests/test_reference_anchor_routes.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_reference_anchor_routes.py` holds MIK-R198 rule 5 at the boundary every leaf publication crosses. The publication routes judge a pair through one shared judgment — do this code commit and this memory commit hold together — so a reference anchor that no longer names the paired code is a fault that judgment refuses.

## Code Commentary

The case drives the same pair twice, once stale and once repaired, so the refusal is attributable to the anchor rather than to the fixture; the pair world is the closeout gate's own fixture, imported rather than copied, including its `ports` composition. A whole-file anchor is recorded at the code worktree's bytes, the cited source is then appended to and committed, and `closeout_external.leaf_pair_refusal` returns a refusal naming `R198.1-reference-anchor`. Re-recording the anchor alone, with the same code commit and one more memory commit, clears it. The module declares no fixture of its own and asserts nothing about the validator's internal API.

## Evidence

- A stale reference anchor refuses the pair the publication routes judge, and repairing that anchor alone clears it [1]
