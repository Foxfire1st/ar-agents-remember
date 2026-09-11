# mcp/tests/test_terminal_evidence_cursors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_terminal_evidence_cursors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-08T14:39+02:00 |
| lastVerifiedCommitHash |  `3fc5d7aa20095de50bc53008e9453c612532b97d`|
| lastVerifiedCommitDate |  2026-09-11T18:38:20+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the tests
exercise repository-owned evidence-page and cursor contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this local cursor contract. | `read_entry_terminal_evidence` | mcp/src/agents_remember/serving/terminal_evidence.py:187-208 |

## Repo-Internal References

The test module drives the production reader, liveness containment, typed evidence models, and
the explicit evidence lane declaration.

| Finding | Anchor | Source |
| --- | --- | --- |
| Deque envelope validation, unsupported-projector gating, and candidate cursor selection. | `_validated_evidence_cursor`; `read_entry_terminal_evidence` | mcp/src/agents_remember/serving/terminal_evidence.py:46-76; mcp/src/agents_remember/serving/terminal_evidence.py:187-208 |
| Pi paging remains bounded and returns the last inspected native id. | `_read_pi_terminal_evidence` | mcp/src/agents_remember/serving/terminal_evidence.py:211-238 |
| Liveness contains the harness read failure and suppresses cursor persistence. | `_terminal_evidence`; `HarnessControlError` | mcp/src/agents_remember/serving/terminal_liveness.py:457-471 |
| Evidence and native-page models define the typed page envelopes under test. | `EvidencePage`; `NativeEvidencePage` | mcp/src/agents_remember/models/conversations/evidence.py:79-135 |
| This focused module is classified as unit-regression. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-109 |

## Cross-Repo References

No cross-repository implementation participates in these local unit tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external or sibling-repository boundary is exercised. | — | — |

## Update History

- 2026-09-08T14:39+02:00 — 260831-LOCR-L20 curator: created the sidecar for the new focused
  terminal-evidence cursor suite. Verification metadata remains empty until governed closeout
  stamps the first candidate code commit.
