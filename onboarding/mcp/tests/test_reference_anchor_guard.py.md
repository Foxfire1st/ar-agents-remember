# mcp/tests/test_reference_anchor_guard.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_reference_anchor_guard.py` protects MIK-R198 rule 5 in the shared knowledge validator: no memory publication while a reference anchor misses the exact paired code. The guard is driven the way the routes drive it — one memory Git tree, its paired code commit, and the validator's own refusal — so each case changes one thing in the pair and reads the sharp edge rather than re-implementing a scanner.

## Code Commentary

Cases are built from the fixture tree's own sidecars, with a single anchor field edited in place. A stale blob whose bytes still match refuses and closes the finding when only the blob is re-recorded; a matching blob with the wrong recorded content refuses on `stale:content`. The reporting dispositions are separated: a sync merge (two bases) completes and reports the rule with the wording that the next publication or landing refuses it, while a leaf publication (one base) refuses, and `writer_reported_rule_ids` carries the rule. The changed-source case builds real code and memory repositories, appends a line to the cited file outside the leaf's authored closure, and shows the refusal naming only the unrepaired sidecar until every reference is repaired. The exact-pair quality case reads `converted_knowledge_check`: a stale anchor makes the drift readiness item `fail` with `findingCount 1`, finalization ineligible and full-final required, and re-recording the blob returns both the check and the item to passing. The merge-commit case pins that a recorded landing is judged against its first parent alone, not both, so a two-parent landing cannot be read as a sync merge. The worktree-route case drives `memory_commit_refusal` with the two-base and leaf-publication shapes over the same candidate.

## Evidence

- A stale blob with identical content refuses a leaf publication and only the blob needs re-recording [1]
- A same-blob anchor with the wrong recorded content identity refuses [2]
- A sync merge reports the anchor debt while every publication refuses it [3]
- A cited source moved outside the leaf's closure refuses until every reference is repaired [4]
- A stale reference fails exact-pair quality and its readiness item, and clears when the anchor is repaired [5]
- A recorded landing of a merge commit is judged with its first parent as the one base [6]
- The worktree route reports the debt at a sync merge and refuses a leaf publication [7]
