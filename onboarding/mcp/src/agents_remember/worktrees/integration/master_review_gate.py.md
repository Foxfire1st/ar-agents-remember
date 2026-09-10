# mcp/src/agents_remember/worktrees/integration/master_review_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/master_review_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09T14:10+02:00 |
| lastVerifiedCommitHash | `6096941f41204c9a7d6ccb2b29f6b2e862ed56b4`|
| lastVerifiedCommitDate | 2026-09-10T09:57:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Integration overview](overview.md)

## Purpose

Projects master route-review currentness into the integration refusal boundary. The gate is
deliberately absent from atomic child closeout and is required for the single master-to-parent
publication edge.

## Code Commentary

### Logic

`master_route_review_block` adapts the typed currentness refusal into the integration result shape;
`master_route_review_refusal` produces the stable refusal payload and next action. The helpers retain
the canonical candidate, master scope and review evidence in the returned diagnostic so callers can
repair the exact stale edge. They do not perform publication or create a second review authority.

### Conventions

Refusals are typed, deterministic and actionable. Atomic child and non-integration paths remain
deferred or not-applicable; only the master integration seam consumes this gate.

### Invariants And Boundaries

- The gate is evaluated at the master-to-parent integration boundary, including the lock-time
  publication recheck.
- A missing, stale, mismatched or status-only master review blocks publication.
- The module projects refusal state; scope resolution and Git mutation remain owned by their callers.

### Todos

None.

## Docs References

No relevant domain documentation was configured for this repository-internal integration gate.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation source was configured for this source-owned gate. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Typed master-review refusal projection. | `master_route_review_block`; `master_route_review_refusal` | mcp/src/agents_remember/worktrees/integration/master_review_gate.py:53-95 |
| Preflight and lock-time publication paths consume the gate. | `integrate_result`; "def _publish_integration_edge("; "def publish_series_integration_under_authority[T](" | mcp/src/agents_remember/worktrees/modules/integrate.py:694-734; mcp/src/agents_remember/worktrees/modules/integrate.py:968-1033; mcp/src/agents_remember/worktrees/series_closeout.py:61-80 |

## Cross-Repo References

No meaningful cross-repo implementation reference is required for this gate card. The coordination
requirement is tracked in the task report and governs this preparation without serving as a source
citation here.

## Source File Binding

The active binding for this card is the exact current source-file bytes: SHA-256
`dd51ab6200088274352370fc8830b1d05df291feb43f5a46f19ccd3b163efff4` (`3248` bytes,
`102` lines). The immutable v3 manifest records the same path bytes. The source remains an
uncommitted preparation candidate, so verification metadata remains closeout-owned.

## Historical Candidate Binding

The predecessor v2 cumulative candidate tree was `96b94b2a1c8e57a7a37b19b08cda33db93fe81b6`,
with this file's SHA-256 recorded as
`dd51ab6200088274352370fc8830b1d05df291feb43f5a46f19ccd3b163efff4`. That whole-tree identity
is retained as historical composition evidence and is not the active identity for this card.

## Update History

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `dd51ab6200088274352370fc8830b1d05df291feb43f5a46f19ccd3b163efff4`, `3248` bytes, `102` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.

- 2026-09-08T19:27:46+02:00 — Final L24 identity cleanup: verified unchanged source bytes against the immutable v3 manifest (`dd51ab6200088274352370fc8830b1d05df291feb43f5a46f19ccd3b163efff4`, 3248 bytes, 102 lines); replaced the active whole-tree binding with exact source-file binding and preserved `96b94b2a1c8e57a7a37b19b08cda33db93fe81b6` as historical. Closeout-owned verification metadata and shared overviews were not edited.
- 2026-09-08T18:14:20+02:00 — CCR-L24 bounded memory-quality repair: updated the active candidate identity to frozen v2 while preserving the prior v1 history; no verification pin was fabricated.
- 2026-09-08T17:31:25+02:00 — CCR-L24 final-v2 source binding: rebased active R25/R26 citation ranges against the frozen cumulative source; verification remains closeout-owned.

- 2026-09-08T16:42+02:00 — CCR-R26 source-grounded preparation: created the card from the frozen
  worktree source. Commit-owned verification metadata remains intentionally blank until the source
  lands in Git.
