# mcp/src/agents_remember/serving/seat_turn_truth.py

| Field                  | Value                                                      |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                            |
| path                   | `mcp/src/agents_remember/serving/seat_turn_truth.py`       |
| doc_type               | `file-level-onboarding`                                    |
| lastUpdated            | 2026-08-09T03:51+02:00|
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                                    |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                              |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The catalog write surface for seat-turn truth (260713-TES-L2): module-level free functions
over `TerminalCatalog`'s public atomic `get`+`upsert` seams that persist the lifted terminal
outcome, the terminal-evidence cursors, the interrupt-request provenance stamp, and the
state-signal/non-reaction/compound-idle dedupe markers. The frozen `TerminalCatalogEntry` and
the catalog classes carry a strict surface budget, so this module exists instead of growing new
catalog methods.

## Code Commentary

### Logic

The `with_*` copiers cit:([`with_turn_evidence`], mcp/src/agents_remember/serving/seat_turn_truth.py:23-78) are pure `dataclasses.replace` copies: `with_turn_evidence`
sets the seat state plus one terminal observation, preserving `turn_state_changed_at` when the
state did not actually transition; `with_state_signal_emitted`/`with_non_reaction_emitted`
stamp one evidence/row episode; `with_compound_idle_emitted` stamps one compound-idle episode
signature; `with_interrupt_request` stamps developer provenance; `with_terminal_cursors`
advances only the supplied cursors.

The `record_*` helpers cit:([`record_turn_projection`, `record_compound_idle_emitted`], mcp/src/agents_remember/serving/seat_turn_truth.py:73-88; mcp/src/agents_remember/serving/seat_turn_truth.py:155-166) are the locked-style write points: read the current row via
`catalog.get`, apply the copier, and `catalog.upsert` only when the row actually changed;
unknown session ids return `None`/no-op; re-recording the same compound signature is a no-op
(the already-emitted guard). `record_terminal_cursors` is called by the liveness
sweep ONLY after a successful terminal-evidence read — a failed read never advances the
cursors (the F2 no-loss fix).

### Conventions

One write path for the relay and liveness projection: no caller mutates catalog fields
directly; every terminal-truth mutation rides `get`+`upsert` through this module.

### Invariants And Boundaries

- The turn-state timestamp is preserved when the state is unchanged (a no-op observation must
  not mint a boundary transition).
- Signal markers are idempotent: re-recording the same evidence id is a no-op; the
  compound-idle marker is signature-keyed (`compound_idle_emitted_for`), so re-recording the
  same episode signature is a no-op and a NEW episode (signature change) overwrites the marker
  — that is the re-arm (260713-TES-L3).
- Cursors advance only on success; the snapshot pointer and terminal cursors are independent
  positions.
- The module never posts inbox rows, never classifies, and never decides delivery — it only
  persists catalog truth.

### Todos

None for this module.

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the
write semantics are same-repository runtime behavior proven by source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines these catalog writes; the atomic seam contract is the source of truth. | `record_turn_projection` | mcp/src/agents_remember/serving/seat_turn_truth.py:73-86 |

## Repo-Internal References

The module consumes `TerminalCatalog`/`TerminalCatalogEntry`/`CatalogTurnEvidence` and is
called by the liveness sweep and the interrupt route and the state-signal actions.

| Finding | Anchor | Source |
| --- | --- | --- |
| The frozen catalog row, evidence stamp, and public get/upsert seams it writes through. | "class TerminalCatalogEntry:"; "class CatalogTurnEvidence:"; "class TerminalCatalog:" | mcp/src/agents_remember/models/terminal_catalog.py:68-72; mcp/src/agents_remember/models/terminal_catalog.py:42-50; mcp/src/agents_remember/serving/terminal_catalog.py:48-92 |
| The liveness sweep's read-before-projection ordering that calls `record_terminal_cursors`. | `_observe_alive` | mcp/src/agents_remember/serving/terminal_liveness.py:343-426 |
| The interrupt route stamping developer provenance after an accepted interrupt. | `conversation_interrupt` | mcp/src/agents_remember/serving/conversation/control/api.py:151-187 |
| The state-signal/non-reaction action markers. | `_emit_state_signal`; `_emit_non_reaction` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:421-480; mcp/src/agents_remember/serving/_agent_notifier_actions.py:542-599 |
| The compound-idle action-time marker write (ask + marker share the fresh signature). | `_emit_compound_idle` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:483-539 |


## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes these catalog writes. | — | — |

## Update History

- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: refreshed the body and citations for the current
  `TerminalCatalogEntry`/`CatalogTurnEvidence` model move; verification metadata remains pinned
  until closeout.

- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: added the compound-idle write helpers
  (`with_compound_idle_emitted` / `record_compound_idle_emitted`), the signature-keyed
  idempotent-marker invariant, and the emitter citation. Verification metadata pinned until
  closeout stamps the 260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the new
  seat-turn-truth write module (get+upsert helpers for turn evidence, cursors, interrupt
  provenance, and signal markers; no-loss cursor rule). Verification metadata pinned to the leaf base `1c1629fc` until closeout stamps the 260713-TES-L2 commit.
