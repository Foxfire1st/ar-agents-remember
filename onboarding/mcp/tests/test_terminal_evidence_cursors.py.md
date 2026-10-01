# mcp/tests/test_terminal_evidence_cursors.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Focused unit protection for the no-loss terminal-evidence cursor contract. The module exercises
the Codex/Claude deque envelope rules, unsupported-harness refusal, bounded Pi continuation, and
the liveness boundary that suppresses cursor persistence after a `HarnessControlError`.

## Code Commentary

### Logic

`ReadEntryTerminalEvidenceTests` builds typed evidence pages and proves that a truncated page
advances only to its last returned sequence, a coherent complete page advances to its final
frame, and a coherent empty page retains its persisted cursor. Eviction floors, stale frames,
tail mismatches, empty-ahead pages, and empty truncated pages raise before mapping; the
unsupported-harness case proves neither evidence surface is read.

`PiCursorContinuationTests` supplies typed native pages to the existing reader. It covers empty
page retention, forward reads after a persisted native cursor, the eight-page bound,
forward progress over unmappable/non-terminal frames, and a later-page failure that returns no
result through `_terminal_evidence` and leaves the original cursor unchanged.

### Conventions

The helpers create protocol-shaped `EvidencePage` and `NativeEvidencePage` values and use
`unittest.mock` at the existing read seams. The tests are serial focused development checks in
the `unit-regression` lane; they do not mint Dagger or closeout authority.

### Invariants And Boundaries

- A deque cursor records the last frame proved inspected, never the daemon tail from an
  incoherent or truncated envelope.
- Any supported read failure leaves the persisted catalog cursor at its pre-read value.
- Unsupported harnesses do not receive a speculative read or projection.
- Pi remains bounded at 200 entries per page and `MAX_NATIVE_LIFT_PAGES` pages per call.
- These tests cover R20 cursor and envelope behavior only; canonical mapping, terminal identity,
  catalog batching, and certification remain owned by their existing routes.

### Todos

None for this module.

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the tests
exercise repository-owned evidence-page and cursor contracts.

- No external/domain document defines this local cursor contract. [1]

### Repo-Internal References

The test module drives the production reader, liveness containment, typed evidence models, and
the explicit evidence lane declaration.

- Deque envelope validation, unsupported-projector gating, and candidate cursor selection. [2]
- Pi paging remains bounded and returns the last inspected native id. [3]
- Liveness contains the harness read failure and suppresses cursor persistence. [4]
- Evidence and native-page models define the typed page envelopes under test. [5]
- This focused module is classified as unit-regression. [6]

### Cross-Repo References

No cross-repository implementation participates in these local unit tests.

No external or sibling-repository boundary is exercised.
