# mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pairing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pairing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash |  `806649b91bdce18f7b915bfbbf6727967f4e7a88`|
| lastVerifiedCommitDate |  2026-09-16T12:23:53+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Provides the small closeout adapter that makes preview, apply, and recovery consume one pair
validator and one current curator-coherence authority.

## Code Commentary

`accepted_closeout_memory_pair` obtains the current coherence record, its exact pair, no-impact
judgments, record digest, and delivery attempt as one value. `resolve_closeout_memory_pair`
re-proves the contract-addressed pair for initial apply acknowledgement and post-commit recovery
without requiring stale pre-commit candidate-tree evidence. `memory_candidate_pair_payload`
renders the same typed identity into public closeout results.

Internal-memory and series closeout return no pair because MCAR-R03 applies only to
worktree-backed external-memory leaves. There is no repo-id re-resolution or alternate filename
reader.

## Invariants And Boundaries

- Preview and normal closeout consume the pair from the validated coherence authority.
- Apply admission and recovery invoke the same canonical resolver against the exact contract.
- Recovery does not depend on a pre-commit report that must become stale after commits.
- This adapter does not invent curator judgments or mutate either repository.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Accepted coherence and exact pair facts are returned together. | `accepted_closeout_memory_pair` | mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pairing.py:30-41 |
| Apply/recovery re-prove the exact contract pair. | `resolve_closeout_memory_pair` | mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pairing.py:44-55 |
| Public closeout projection uses one pair payload writer. | `memory_candidate_pair_payload` | mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pairing.py:58-65 |

## Cross-Repo References

No cross-repository implementation reference applies.

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pairing.py` changed since
  the recorded verification commit. Re-read the card against the frozen on-disk source and
  re-checked its claims and cited ranges: nothing this card asserts is falsified by the change, so
  no wording changed. Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (a pure import relocation of `resolve_memory_candidate_pair`).
  Re-read the card against the current source: its three cited ranges (30-41, 44-55, 58-65) still
  hold and the prose names no import path. No wording changed; verification metadata remains
  closeout-owned.
- 2026-08-29T21:46+02:00 — MCAR-L03: created the shared preview/apply/recovery pairing adapter.
  Verification remains closeout-owned.
