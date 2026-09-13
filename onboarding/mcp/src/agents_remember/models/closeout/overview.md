# Closeout Projection Models Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/models/closeout` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1ddf7fdac40fa3e9c30b8ded693d440e07d6a8b6`|
| lastVerifiedCommitDate |  2026-09-13T22:07:53+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Models overview](../overview.md)

## What This Area Is

Strict wire and persistence models for closeout inputs, door sources, disposable queue
projections, and task-publication effects.

`input.py` is the route's message-bearing contract and, since 260913-LCA-L1, the one definition of the
attribution a memory commit carries. `EffectiveCloseoutInput.memory_content_message(code_commit)`
returns the closeout's own message verbatim plus exactly one final-paragraph `Code-Commit: <sha>`
trailer naming the code commit that same closeout landed; both sanctioned closeout routes — worktree
closeout in `worktrees/modules/closeout_external.py` and branch-addressed direct landing in
`worktrees/integration/direct_landing/direct_landing_execution.py` — render their memory-content commit
message through it, and `message_for` stays the raw public echo that the ledger leg still uses.

## Hot Path Summary

`projection.py` defines the `valid-built` / `invalid-empty` state machine and bounded member,
source-problem, invalidation, rebuild, and task-doc effect payloads.

## Local Invariants And Traps

- A projection is disposable scheduling state, never lifecycle/commit evidence.
- Invalid means empty; stale rows are not transitioned into a second lifecycle database.
- Text and population bounds are enforced at model construction.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `projection.py` | [projection.py.md](projection.py.md) | covered |

## Docs And Boundary References

No configured external source applies. Queue producers and application consumers are documented
through same-repository source references.

## Update History

- 2026-09-13T21:42+02:00 — 260913-LCA-L1 (uncommitted change set on `ar/260913-lca-l1-ar`): recorded
  that `input.py` now owns the single rendering of the memory-content commit message —
  `CODE_COMMIT_TRAILER_KEY` plus `EffectiveCloseoutInput.memory_content_message(code_commit)`, the
  closeout's own body with exactly one final-paragraph `Code-Commit: <sha>` trailer naming the code
  commit the same closeout landed — and that both closeout routes render through it while the
  `memory.md`-only ledger leg keeps plain `message_for("ledger")` and no trailer. This route's file-level
  map still lists only `projection.py`; that gap predates this change and was left alone.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-08-25T15:44+02:00 — Created for the disposable projection contract introduced by the
  closeout-lifecycle reform. Verification remains closeout-owned.
