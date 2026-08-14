# mcp/src/agents_remember/application/terminal_spawn_results.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/terminal_spawn_results.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T21:06+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[application overview](overview.md)

## Purpose

Centralizes public `spawn_agent_session` refusal construction at the application
boundary. Terminal opening can refuse before creating a host process for kind,
launch-selection, task binding, source lineage, or occupied-seat reasons; this
module translates those internal outcomes into the strict public response
without duplicating policy in the MCP declaration.

## Code Commentary

`spawn_refusal` builds the common non-opened envelope and retains a
`SourceLineageProjection` only for the two source-lineage refusal statuses.
`open_terminal_refusal` maps `OpenTerminalResult.status` values to the public
closed vocabulary. Its generator result is explicitly narrowed to
`SpawnAgentSessionStatus | None`, preventing inference from widening the public
status into an arbitrary string before it reaches `spawn_refusal`. The function
delegates ordinary refusals to that builder and preserves the distinct
occupied-seat evidence (`session`, `seatRole`, `ownerSession`, and task
reference) for `seat-taken`. Returning `None` means the outcome was not a
recognized refusal and the caller must continue its success handling.

## Invariants And Boundaries

- This module translates results; it does not decide task identity, lineage, or
  host process creation.
- Only lineage refusals carry `sourceLineage`; unrelated refusal envelopes do
  not leak a stale projection.
- Unknown `kind` values are represented as absent rather than crossing the
  validated public response vocabulary.
- `seat-taken` preserves replacement/ownership evidence and is not collapsed
  into a generic pre-spawn refusal.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Common pre-spawn refusal envelope includes optional lineage evidence. | `spawn_refusal` | mcp/src/agents_remember/application/terminal_spawn_results.py:13-31 |
| Internal opener outcomes map to public statuses and keep occupied-seat evidence distinct. | `open_terminal_refusal` | mcp/src/agents_remember/application/terminal_spawn_results.py:34-76 |

## Update History

- 2026-08-12T21:06+02:00 — 260731-EFA-L23 curator follow-up: re-read the closeout-exposed Pyright repair; `mapped` is now explicitly `SpawnAgentSessionStatus | None`, preserving the closed public refusal vocabulary without changing runtime mapping behavior. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — 260731-EFA-L23 curator: created for the centralized public spawn-refusal boundary, including fail-closed source-lineage evidence. Verification remains pinned to the leaf base until closeout assigns the dirty source a real commit identity.
