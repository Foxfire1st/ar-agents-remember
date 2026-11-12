# mcp/tests/test_reference_anchor_integration_owners.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_reference_anchor_integration_owners.py` carries MIK-R198 to the actual integration owners: `integrate_result`, the closeout's early recovery gate, and the checkpoint, final and recorded series publications. The fault is one tiny citation — README's first line — recorded before only the containing blob moves, with no publication gate patched, so a refusal that names only R198 is attributable to the anchor and a repair must publish.

## Code Commentary

The native checkpoint fixture supplies real enclosure and branch authority, and the queue fixture supplies the master/leaf pair; `_cite` writes one line-range anchor over `README.md` at the code worktree's own bytes. The first case takes a passing full-quality check over the healthy pair, persists it as a receipt, then moves the cited source: both dry and real integration refuse with `knowledge-gate-refused` naming only the rule, every ref and the receipt bytes are unchanged, and after `fix_references` re-records one anchor the same entry integrates and records the repaired memory-content commit. The recovery case resumes an interrupted closeout whose commits already exist, fixes the live tree, and still refuses the immutable recovered commit — `require_gated_recovery` is called once with the exact commits while `refuse_ungated_candidate` is never reached, which is the point that preflight must not shadow the exact gate. The series case is parametrized over the three publishing owners; each refuses the synced debt with only the rule named and unchanged refs after a source sync, and then publishes the state its own owner names once a fresh child leaf repairs the inherited citation.

## Evidence

- Leaf integration rejudges the pair despite an old full-quality receipt, and lands after the anchor repair [1]
- Early closeout recovery judges the immutable output through the exact gate, never the preflight [2]
- Checkpoint, final and recorded series publications refuse synced anchor debt and publish a real leaf repair [3]
