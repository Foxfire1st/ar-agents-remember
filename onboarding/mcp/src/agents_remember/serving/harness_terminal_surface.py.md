# mcp/src/agents_remember/serving/harness_terminal_surface.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_terminal_surface.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:00+02:00 |
| lastVerifiedCommitHash | `409891a4bea54f3b6c3a125611afe54c41cca661` |
| lastVerifiedCommitDate | 2026-07-14T10:43:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Renders the normalized transcript and input surface for a hosted harness while routing terminal and
automated messages into the bridge's shared ordered queue.

## Code Commentary

The surface owns `UncommittedDraft`: only draft update and draft submit operations touch it. A
durable delivery is a separate whole message and cannot inject into, submit, or discard draft text.
Immediate/queued acceptance clears only the submitted draft revision; ambiguous acceptance retains
the draft for reconciliation. Pane content remains a readable projection, not authority.

## Invariants And Boundaries

- Human draft custody belongs to the surface, not the adapter or durable delivery path.
- Transcript rendering is derived from normalized bridge state.
- No native vendor full-screen TUI is driven concurrently with the bridge.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Draft and transcript models. | [harness_control_models.py](harness_control_models.py) |
| Shared queue owner. | [harness_control_bridge.py](harness_control_bridge.py) |
| R11 scenarios. | [test_harness_control.py](../../../tests/test_harness_control.py) |

## Update History

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for normalized transcript
  rendering and the R11 surface-owned uncommitted-draft guarantee.
