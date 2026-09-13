# Closeout Projection Models Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/models/closeout` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `5bb124d43ea7b234edd570cf3995521e708714bd`|
| lastVerifiedCommitDate |  2026-09-13T23:22:52+02:00|
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

**This route renders the attribution; it no longer owns the key.** Since 260913-LCA-L2 the trailer key
is declared once in `kernel/memory_attribution.py` — the reader of the hashed object, one rank below
`models` in `layers.toml` — and `input.py` imports it (`input.py:9`), so
`grep -rn '"Code-Commit"' --include=*.py mcp/` has exactly one hit. The direction is fixed by the
layer contract rather than by preference: a kernel module importing a model would import upward.

## Hot Path Summary

`projection.py` defines the `valid-built` / `invalid-empty` state machine and its source-problem,
invalidation, rebuild, and task-doc effect payloads. Its member list is unbounded — how many leaves a
sprint declares is not a projection-model concern.

## Local Invariants And Traps

- A projection is disposable scheduling state, never lifecycle/commit evidence.
- Invalid means empty; stale rows are not transitioned into a second lifecycle database.
- Text and payload bounds are enforced at model construction; the member population carries no ceiling
  since 260913-LCA-L6, so membership uniqueness (one row per waiting generation and task) is the guard
  that remains.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `projection.py` | [projection.py.md](projection.py.md) | covered |

## Docs And Boundary References

No configured external source applies. Queue producers and application consumers are documented
through same-repository source references.

## Update History

- 2026-09-13T23:20+02:00 — 260913-LCA-L2 route refresh (uncommitted change set on
  `ar/260913-lca-l2-ar`): corrected the ownership sentence this route inherited from 260913-LCA-L1.
  The key is no longer declared here: `CODE_COMMIT_TRAILER_KEY` lives in
  `kernel/memory_attribution.py` (the reader) and `input.py` imports it at `input.py:9`, so this route
  renders the attribution through the imported key rather than owning a literal. The direction is the
  one `layers.toml` permits — `kernel` ranks below `models`, and a kernel module importing a model
  would import upward — and `grep -rn '"Code-Commit"' --include=*.py mcp/` now has exactly one hit.
  The entry below stands as the record of what was true when L1 wrote it. Verification metadata
  remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-13T22:22+02:00 — 260913-LCA-L6 route refresh (uncommitted change set on `ar/260913-lca-l6-ar`):
  corrected the Hot Path Summary and the population-bound invariant, which claimed the projection
  models bound candidate populations. `CloseoutQueueState.members` is now `Field(default_factory=list)`
  with no `max_length`, so the route's member list is unbounded while `sourceProblems` keeps
  `MAX_CLOSEOUT_SOURCE_PROBLEMS`; membership uniqueness stays enforced by the state validator. The
  child card `projection.py.md` was updated in the same pass.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.

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
