# mcp/src/agents_remember/worktrees/integration/master_review_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/master_review_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T11:43+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634`|
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
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
| Typed blocked-integration payload projection. The former `master_route_review_block` / `master_route_review_refusal` pair is gone from this module; the refusal projection now lives in `worktrees/route_review.py` as `route_review_refusal_projection` / `route_review_refusal_fields`. | `blocked_integration_payload` | mcp/src/agents_remember/worktrees/integration/master_review_gate.py:14-39 |
| Preflight and lock-time publication paths consume the gate. | `integrate_result`; "def _publish_integration_edge("; "def publish_series_integration_under_authority[T](" | mcp/src/agents_remember/worktrees/modules/integrate.py:636-661; mcp/src/agents_remember/worktrees/modules/integrate.py:815-820; mcp/src/agents_remember/worktrees/series_closeout.py:73-73 |

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
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `_publish_integration_edge` in the row 61 of this card from mcp/src/agents_remember/worktrees/modules/integrate.py:636-661 to mcp/src/agents_remember/worktrees/modules/integrate.py:815-820, the extent of the construct the claim is about (the checker named line(s) [815] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `_publish_integration_edge` in the row 61 of this card from mcp/src/agents_remember/worktrees/modules/integrate.py:846-921 to mcp/src/agents_remember/worktrees/modules/integrate.py:815, the extent of the construct the claim is about (the checker named line(s) [815] as its live location); re-pointed `publish_series_integration_under_authority[T]` in the row 61 of this card from mcp/src/agents_remember/worktrees/series_closeout.py:74-92 to mcp/src/agents_remember/worktrees/series_closeout.py:73, the extent of the construct the claim is about (the checker named line(s) [73] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `_publish_integration_edge` in the row 61 of this card from mcp/src/agents_remember/worktrees/modules/integrate.py:610-613 to mcp/src/agents_remember/worktrees/modules/integrate.py:815-820, the extent of the construct the claim is about (the checker named line(s) [815] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `integrate_result` in the row 61 of this card from mcp/src/agents_remember/worktrees/modules/integrate.py:815-820 to mcp/src/agents_remember/worktrees/modules/integrate.py:610-613, the extent of the construct the claim is about (the checker named line(s) [610, 642] as its live location)
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-10T15:06+02:00 — No content impact: mechanical citation re-derivation of the `closeout.py` / `integrate.py` anchors after the closeout auto-carry change shifted their lines; the cited symbols and claims are unchanged.

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `dd51ab6200088274352370fc8830b1d05df291feb43f5a46f19ccd3b163efff4`, `3248` bytes, `102` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.

- 2026-09-08T19:27:46+02:00 — Final L24 identity cleanup: verified unchanged source bytes against the immutable v3 manifest (`dd51ab6200088274352370fc8830b1d05df291feb43f5a46f19ccd3b163efff4`, 3248 bytes, 102 lines); replaced the active whole-tree binding with exact source-file binding and preserved `96b94b2a1c8e57a7a37b19b08cda33db93fe81b6` as historical. Closeout-owned verification metadata and shared overviews were not edited.
- 2026-09-08T18:14:20+02:00 — CCR-L24 bounded memory-quality repair: updated the active candidate identity to frozen v2 while preserving the prior v1 history; no verification pin was fabricated.
- 2026-09-08T17:31:25+02:00 — CCR-L24 final-v2 source binding: rebased active R25/R26 citation ranges against the frozen cumulative source; verification remains closeout-owned.

- 2026-09-08T16:42+02:00 — CCR-R26 source-grounded preparation: created the card from the frozen
  worktree source. Commit-owned verification metadata remains intentionally blank until the source
  lands in Git.
