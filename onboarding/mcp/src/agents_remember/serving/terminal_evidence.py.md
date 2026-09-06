# mcp/src/agents_remember/serving/terminal_evidence.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/serving/terminal_evidence.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-09T01:21+02:00                                        |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                                    |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The daemon-side terminal-evidence lift for the worker→manager state-signal relay
(260713-TES-L2). It reuses the conversation layer's per-vendor projectors over the
control-plane evidence page (codex/claude) or pi durable-entry pages, maps the newest
`MappedTurnOutcome` into a `TurnTerminalEvidence` the catalog seat truth can persist, and
returns the next cursor only on a successful read. This is the projection lift (G1): the
canonical per-vendor outcome becomes catalog turn truth instead of being discarded before
the catalog.

## Code Commentary

### Logic

`read_entry_terminal_evidence` cit:([`read_entry_terminal_evidence`], mcp/src/agents_remember/serving/terminal_evidence.py:145-160) is the per-row entry point: non-harness,
harness-less, or endpoint-less rows return no claim and no advance; pi rows go through
`_read_pi_terminal_evidence`; all other harnesses read one evidence page after the persisted
`terminal_evidence_sequence` and map it with `latest_terminal_evidence` cit:([`latest_terminal_evidence`], mcp/src/agents_remember/serving/terminal_evidence.py:63-100). The
mappers reuse `projector_for(harness_id)` and the same `map_evidence_frame`/`map_native_frame`
contract the active conversation slice consumes — there is deliberately no second adapter
interpretation of vendor shapes.

`_read_pi_terminal_evidence` cit:([`_read_pi_terminal_evidence`], mcp/src/agents_remember/serving/terminal_evidence.py:163-190) walks from the persisted `terminal_native_cursor` to
the tail in 200-entry pages, bounded by `MAX_NATIVE_LIFT_PAGES = 8` (≤1600 entries per
sweep), keeps the newest terminal outcome across pages, and returns the last processed
`native_id` as the next cursor. An empty page breaks without advancing, so a no-progress read
is idempotent; longer histories continue on the next sweep, level-triggered.

`TerminalEvidenceRead` cit:(["class TerminalEvidenceRead:"], mcp/src/agents_remember/serving/terminal_evidence.py:50-50) is the no-loss contract: `projection` plus the optional
`evidence_sequence`/`native_cursor`. Cursors are returned only when the read succeeded, so a
failed read leaves the catalog row at the pre-window position and the next sweep re-reads the
same evidence — never a skipped window.

`interrupted_origin` cit:([`interrupted_origin`], mcp/src/agents_remember/serving/terminal_evidence.py:193-206) attributes an interrupted outcome: `developer` only when the
dashboard interrupt action stamped `interrupt_requested_by="developer"` and (when the evidence
carries a turn id) that request names the same turn; everything else is `unknown`. The relay
carries the fact only — hold-off/resume policy is the manager's.

### Conventions

Deferred conversation imports (function-local, `# noqa: PLC0415`) keep the module free of the
conversation-package import cycle that `hosted_control_projection` already documents. The
lift never interprets raw pane/log content; it maps only the same bounded evidence/native
surfaces the projectors already consume.

### Invariants And Boundaries

- Cursors advance ONLY on a successful read; a failed or evicted read yields no claim AND no
  advance (no-loss retry).
- Unknown harness/projector, unmappable native frames, and empty pages produce no terminal
  claim.
- The lift is additive: it never changes the snapshot pointer or any control projection; the
  snapshot and terminal cursors are separate positions.
- The relay never judges: no stale/suspect classification, no respawn trigger, no
  expectation-overdue reasoning lives here.

### Todos

None for this module.

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the
per-vendor outcome mapping is same-repository runtime behavior proven by source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this lift; the projectors and control-plane evidence pages are the source of truth. | `read_entry_terminal_evidence` | mcp/src/agents_remember/serving/terminal_evidence.py:145-160 |

## Repo-Internal References

The lift consumes the conversation projectors (`projector_for`, `map_evidence_frame`,
`map_native_frame`) and the control-plane evidence reads (`read_control_evidence`,
`read_control_native_page`); the catalog row carries the outcome fields and cursors it
persists through `seat_turn_truth`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The per-vendor projector registry the lift reuses. | `projector_for` | mcp/src/agents_remember/serving/conversation/projectors/__init__.py:122-123 |
| The bounded evidence-page and native-page read seams. | `read_control_evidence`; `read_control_native_page` | mcp/src/agents_remember/serving/harness_control_client.py:351-371; mcp/src/agents_remember/serving/harness_control_client.py:375-407 |
| The catalog row fields this module reads and the liveness sweep that calls it (read-before-projection). | "class TerminalCatalogEntry:"; `_observe_alive` | mcp/src/agents_remember/models/terminal_catalog.py:68-72; mcp/src/agents_remember/serving/terminal_liveness.py:343-426 |


## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local evidence lift. | — | — |

## Update History

- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the new
  terminal-evidence lift module (per-vendor projection reuse, dedicated cursors,
  `MAX_NATIVE_LIFT_PAGES = 8` pi tail walk, no-loss read contract, interrupt-origin
  attribution). Verification metadata pinned to the leaf base `1c1629fc` until closeout stamps
  the 260713-TES-L2 commit.


