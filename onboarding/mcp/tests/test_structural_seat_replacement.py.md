# mcp/tests/test_structural_seat_replacement.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_structural_seat_replacement.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T12:00+02:00 |
| lastVerifiedCommitHash |  `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces ARSPAWN-L2 canonical-seat idempotency, bounded recovery, vacancy-safe addressing, and mixed
ambient/plane replacement behavior.

## Code Commentary

### Logic

The suite builds real sprint/master/leaf task documents, a durable terminal catalog and inbox, and
a synchronized fake host. It then exercises same-seat concurrency, different-seat concurrency,
contradictory evidence refusal, receipt repair, inbox-compaction recovery, lock failure, crash-
stranded generation replacement, actual queued-message delivery after manager replacement, and
staged-heir promotion.
The fake-host setup sets the dispatch readiness wait to zero: these tests prove serialization and
durable queued-brief convergence, not a real adapter startup delay. Lock contention patches the
transaction-owned `exclusive_structural_dispatch_lock` boundary.

### Conventions

Assertions inspect private ids only inside the forcing harness. Public dispatch and message payloads
must remain structural and are checked for runtime-id absence.

### Invariants And Boundaries

- Same-seat concurrent dispatch produces one host and one brief.
- Different seats do not serialize behind a global lock.
- Distinct seats create at most two zero-length files in the fixed hash-stripe namespace.
- Forced `flock` acquisition failure returns the typed serializer refusal before spawn; no fallback runs.
- One failed/unbriefed generation can be retired and replaced; contradictory evidence cannot.
- A vacancy-time message remains document-and-role addressed and reaches the next manager.
- A staged replacement becomes current only after the incumbent leaves.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite is the focused ARSPAWN-L2 forcing matrix. | `StructuralSeatReplacementTests` | mcp/tests/test_structural_seat_replacement.py:63-540 |
| Same-seat dispatch converges while different seats remain concurrent. | `test_concurrent_repeated_dispatch_converges_on_one_briefed_ambient_seat`; `test_different_canonical_seats_do_not_share_a_global_dispatch_lock` | mcp/tests/test_structural_seat_replacement.py:173-218; mcp/tests/test_structural_seat_replacement.py:219-251 |
| Recovery refuses contradictions, repairs receipts, survives compaction, and has no lock fallback. | `test_dispatch_refuses_contradictory_brief_evidence_without_leaking_the_occupant`; `test_repeated_dispatch_repairs_a_missing_catalog_receipt_from_the_durable_brief`; `test_repeated_dispatch_trusts_the_catalog_receipt_after_inbox_compaction`; `test_dispatch_lock_failure_is_a_typed_refusal_without_a_spawn_fallback` | mcp/tests/test_structural_seat_replacement.py:252-265; mcp/tests/test_structural_seat_replacement.py:266-282; mcp/tests/test_structural_seat_replacement.py:283-295; mcp/tests/test_structural_seat_replacement.py:296-312 |
| Positive unbriefed evidence permits replacement of one crash-stranded generation. | `test_crash_stranded_unbriefed_ambient_child_is_retired_and_replaced` | mcp/tests/test_structural_seat_replacement.py:313-340 |
| The mixed flow delivers vacancy-time canonical messages to successive replacement managers without durable runtime ids. | `test_ambient_and_plane_flow_keeps_a_queued_message_canonical_across_manager_replacement` | mcp/tests/test_structural_seat_replacement.py:341-488 |
| A staged heir becomes current only after the incumbent retires, and duplicate dispatch still refuses. | `test_staged_replacement_becomes_the_only_current_occupant_after_retire` | mcp/tests/test_structural_seat_replacement.py:489-540 |

## Cross-Repo References

No cross-repository dependency governs this unit.

## Update History

- 2026-08-31T12:00+02:00 — A005 aligned concurrency forcing with the extracted transaction-owned
  serializer and removed two artificial ten-second fake-adapter waits without weakening the durable
  queue/one-seat assertions. Verification remains closeout-owned.

- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2 final curation: reconciled the complete
  544-line candidate, moved repository evidence out of Domain Documentation, and refreshed every
  forcing anchor. No test execution is claimed.

- 2026-08-25T20:58+02:00 — ARSPAWN-L2 failure-family hardening: the refusal forcing now fails
  actual `flock` acquisition, proving the serializer owns the translation and spawn never runs.
  Verification remains closeout-owned.

- 2026-08-25T20:39+02:00 — ARSPAWN-L2 boundedness pass: the different-seat forcing now proves
  concurrent seats create at most two zero-length files in the fixed hash-stripe namespace.
  Verification remains closeout-owned.

- 2026-08-25T20:31+02:00 — ARSPAWN-L2 quality pass: simplified the concurrent-dispatch forcing
  assertions below complexity 10 and returned the file to 597 lines without weakening its
  one-seat/one-brief proof. Citations were regenerated; verification remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: created as the focused replacement and idempotency
  forcing suite. Verification remains closeout-owned.
