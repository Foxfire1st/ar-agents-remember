# mcp/src/agents_remember/serving/terminal_evidence.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/serving/terminal_evidence.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-09-08T14:39+02:00                                        |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634`                                    |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The daemon-side terminal-evidence lift for the worker→manager state-signal relay.
It reuses the conversation layer's per-vendor projectors over the control-plane evidence
page (codex/claude) or pi durable-entry pages, maps the newest `MappedTurnOutcome` into
catalog seat truth, and returns a cursor only for a successfully inspected window. Deque
pages are validated before mapping: eviction gaps, stale frames, empty truncated pages, and
incoherent complete envelopes fail closed, while a truncated page advances only to its last
returned frame. Unsupported harnesses are rejected before either evidence surface is read.

## Code Commentary

### Logic

`read_entry_terminal_evidence` cit:([`read_entry_terminal_evidence`], mcp/src/agents_remember/serving/terminal_evidence.py:187-208) is the per-row entry point: non-harness,
harness-less, endpoint-less, or unsupported-projector rows return no claim and no advance;
pi rows go through `_read_pi_terminal_evidence`; all other supported harnesses read one
evidence page after the persisted `terminal_evidence_sequence`. `_validated_evidence_cursor`
cit:([`_validated_evidence_cursor`], mcp/src/agents_remember/serving/terminal_evidence.py:46-76)
checks the eviction floor and every returned sequence before `latest_terminal_evidence`
maps any frame. A truncated page returns its final frame sequence, a complete non-empty page
must reach `latest_sequence`, and a coherent empty page retains the persisted cursor.

`latest_terminal_evidence` cit:([`latest_terminal_evidence`], mcp/src/agents_remember/serving/terminal_evidence.py:107-143)
and `latest_native_terminal_evidence` cit:([`latest_native_terminal_evidence`], mcp/src/agents_remember/serving/terminal_evidence.py:146-184)
reuse the canonical projector registry and map only its `MappedTurnOutcome` outputs. There
is deliberately no second adapter interpretation of vendor shapes.

`_read_pi_terminal_evidence` cit:([`_read_pi_terminal_evidence`], mcp/src/agents_remember/serving/terminal_evidence.py:211-238) walks from the persisted `terminal_native_cursor` to
the tail in 200-entry pages, bounded by `MAX_NATIVE_LIFT_PAGES = 8` (≤1600 entries per
sweep), keeps the newest terminal outcome across pages, and returns the last processed
`native_id` as the next cursor. An empty page retains the prior cursor; a later page failure
propagates to the liveness containment boundary so no cursor or projection is persisted.

`TerminalEvidenceRead` cit:(["class TerminalEvidenceRead:"], mcp/src/agents_remember/serving/terminal_evidence.py:94-104) is the no-loss contract: `projection` plus the optional
`evidence_sequence`/`native_cursor`. Cursors are returned only when the read succeeded, so a
failed read leaves the catalog row at the pre-window position and the next sweep re-reads the
same evidence — never a skipped window.

`interrupted_origin` cit:([`interrupted_origin`], mcp/src/agents_remember/serving/terminal_evidence.py:241-254) attributes an interrupted outcome: `developer` only when the
dashboard interrupt action stamped `interrupt_requested_by="developer"` and (when the evidence
carries a turn id) that request names the same turn; everything else is `unknown`. The relay
carries the fact only — hold-off/resume policy is the manager's.

### Conventions

Deferred conversation imports (function-local, `# noqa: PLC0415`) keep the module free of the
conversation-package import cycle that `hosted_control_projection` already documents. The
lift never interprets raw pane/log content; it maps only the same bounded evidence/native
surfaces the projectors already consume.

### Invariants And Boundaries

- Cursor validation precedes canonical mapping for deque reads. A failed, evicted, or
  incoherent read yields no claim AND no advance (no-loss retry).
- Unknown harness/projector rows are rejected before any evidence/native page read.
- Unmappable native frames and coherent empty pages produce no terminal claim but are still
  considered inspected; successful reads advance through the inspected boundary.
- The lift is additive: it never changes the snapshot pointer or any control projection; the
  snapshot and terminal cursors are separate positions.
- Pi paging remains bounded at 200 entries per page and eight pages per observer call; this
  module has no deep-history fallback or second cursor store.
- The relay never judges: no stale/suspect classification, no respawn trigger, no
  expectation-overdue reasoning lives here.

### Todos

None for this module.

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the
per-vendor outcome mapping is same-repository runtime behavior proven by source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this lift; the projectors and control-plane evidence pages are the source of truth. | `read_entry_terminal_evidence` | mcp/src/agents_remember/serving/terminal_evidence.py:187-208 |

## Repo-Internal References

The lift consumes the conversation projectors (`projector_for`, `map_evidence_frame`,
`map_native_frame`) and the control-plane evidence reads (`read_control_evidence`,
`read_control_native_page`); the catalog row carries the outcome fields and cursors it
persists through `seat_turn_truth`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The per-vendor projector registry and strict `HarnessProjector` protocol the lift reuses. | `class HarnessProjector`; `projector_for` | mcp/src/agents_remember/serving/conversation/projectors/__init__.py:26-47; mcp/src/agents_remember/serving/conversation/projectors/__init__.py:115-123; mcp/src/agents_remember/serving/conversation/projectors/__init__.py:136-137 |
| The bounded evidence-page and native-page read seams. | `read_control_evidence`; `read_control_native_page` | mcp/src/agents_remember/serving/harness_control_client.py:351-371; mcp/src/agents_remember/serving/harness_control_client.py:375-407 |
| The catalog cursor fields and liveness failure containment this module feeds. | `terminal_evidence_sequence`; `terminal_native_cursor`; `_terminal_evidence` | mcp/src/agents_remember/models/terminal_catalog.py:182-183; mcp/src/agents_remember/serving/terminal_liveness.py:455-469 |
| The focused tests pin the no-loss envelope, unsupported-harness, bounded-Pi, and failure-containment cases. | `ReadEntryTerminalEvidenceTests`; `PiCursorContinuationTests` | mcp/tests/test_terminal_evidence_cursors.py:153-360 |


## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local evidence lift. | — | — |

## Update History
- 2026-09-11T22:39:01+00:00: Generated citation repair: `terminal_evidence_sequence`; `terminal_native_cursor`; `_terminal_evidence` repointed to mcp/src/agents_remember/models/terminal_catalog.py:182-182; mcp/src/agents_remember/models/terminal_catalog.py:183-183; mcp/src/agents_remember/serving/terminal_liveness.py:455-469. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-08T14:39+02:00 — 260831-LOCR-L20 curator reconciliation: refreshed the current
  no-loss cursor contract, exact envelope validation order, unsupported-harness refusal, and
  bounded Pi continuation against the uncommitted candidate. Added the focused regression
  route citation; verification metadata remains pinned until governed closeout stamps the
  candidate code commit.

- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the new
  terminal-evidence lift module (per-vendor projection reuse, dedicated cursors,
  `MAX_NATIVE_LIFT_PAGES = 8` pi tail walk, no-loss read contract, interrupt-origin
  attribution). Verification metadata pinned to the leaf base `1c1629fc` until closeout stamps
  the 260713-TES-L2 commit.

