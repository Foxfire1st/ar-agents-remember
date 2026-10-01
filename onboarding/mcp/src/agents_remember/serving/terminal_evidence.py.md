# mcp/src/agents_remember/serving/terminal_evidence.py

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

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the
per-vendor outcome mapping is same-repository runtime behavior proven by source and tests.

- No external/domain document defines this lift; the projectors and control-plane evidence pages are the source of truth. [1]

### Repo-Internal References

The lift consumes the conversation projectors (`projector_for`, `map_evidence_frame`,
`map_native_frame`) and the control-plane evidence reads (`read_control_evidence`,
`read_control_native_page`); the catalog row carries the outcome fields and cursors it
persists through `seat_turn_truth`.

- The per-vendor projector registry and strict `HarnessProjector` protocol the lift reuses. [2]
- The bounded evidence-page and native-page read seams. [3]
- The catalog cursor fields and liveness failure containment this module feeds. [4]
- The focused tests pin the no-loss envelope, unsupported-harness, bounded-Pi, and failure-containment cases. [5]


### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary owns or consumes this local evidence lift.
