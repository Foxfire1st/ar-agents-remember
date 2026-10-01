# Closeout Projection Models Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/models/closeout` |

## Governing Overview

[Models overview](../overview.md)

## What This Area Is

Strict wire and persistence models for closeout inputs, door sources, disposable queue
projections, and task-publication effects.

`input.py` is the route's message-bearing contract and, since 260913-LCA-L1, the closeout-shaped way in
to the attribution a memory commit carries. `EffectiveCloseoutInput.memory_content_message(code_commit)`
returns the closeout's own message verbatim plus exactly one final-paragraph `Code-Commit: <sha>`
trailer naming the code commit that same closeout landed; both sanctioned closeout routes — worktree
closeout in `worktrees/modules/closeout_external.py` and branch-addressed direct landing in
`worktrees/integration/direct_landing/direct_landing_execution.py` — render their memory-content commit
message through it. `message_for` exposes only the accepted code or memory message; there is no ledger message field, leg or enabledness state.

**This route renders the attribution; it does not own the rendering, and it no longer owns the key.**
Since 260913-LCA-L2 the trailer key is declared once in `kernel/memory_attribution.py` — the reader of
the hashed object, one rank below `models` in `layers.toml`. Since 260913-LCA-L4 this route imports the
kernel's one renderer (`input.py:9`) and `memory_content_message` is a delegation to it, so
`grep -rn '"Code-Commit"' --include=*.py mcp/` has exactly one hit in a module that both declares **and**
interpolates the key. The direction is fixed by the
layer contract rather than by preference: a kernel module importing a model would import upward.

## Hot Path Summary

`input.py` defines exactly two public commit legs (`code`, `memory`) and rejects unknown fields. `EffectiveCloseoutInput.memory_content_message` delegates attribution rendering to the kernel; no caller supplies a third commit message.

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

## Evidence

### Docs And Boundary References

No configured external source applies. Queue producers and application consumers are documented
through same-repository source references.

### Repo-Internal References

The following current source owns the changed behavior; no external domain source is configured for this slice.

- Accepted closeout message input contains only code and memory. [1]
- The effective two-leg input renders memory attribution through the kernel. [2]
