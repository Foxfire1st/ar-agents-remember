# mcp/src/agents_remember/serving/harness_terminal_surface.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_terminal_surface.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Draft and transcript models. | `UncommittedDraft` | mcp/src/agents_remember/serving/harness_control_models.py:110-119 |
| Shared queue owner. | `HarnessControlBridge` | mcp/src/agents_remember/serving/harness_control_bridge.py:77-543 |
| R11 scenarios. | `test_ambiguous_draft_submission_retains_human_text` | mcp/tests/test_harness_control_conformance_1.py:230-244 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:29+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 3 citation rows with exact anchors (`UncommittedDraft`/`TranscriptEntry` model extents, `HarnessControlBridge`, and the draft-custody test block 551-618 containing `test_ambiguous_draft_submission_retains_human_text`) and ledger-verified ranges. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for normalized transcript
  rendering and the R11 surface-owned uncommitted-draft guarantee.
