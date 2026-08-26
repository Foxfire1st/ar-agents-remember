# mcp/src/agents_remember/application/structural/dispatch_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/structural/dispatch_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T16:03+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structural application services](overview.md)

## Purpose

Owns the idempotent spawn-and-brief transaction for one canonical
`(task_document_ref, role)` seat.

## Code Commentary

### Logic

`execute_dispatch_transaction` admits a first spawn, recognizes an already occupied seat, and
reconciles that occupant against its durable catalog receipt and exact-pinned inbox brief. A viable
brief converges on the existing generation. A missing catalog receipt is repaired from the brief;
a retained catalog receipt survives bounded inbox compaction. A generation proven to have failed
before briefing is retired and retried once. Contradictory, unreadable, or otherwise ambiguous
evidence refuses without retirement. Receipt repair is delegated to `DispatchBriefReceiptStore`,
which composes with the terminal catalog atomic lock/read/write unit without widening the general
`TerminalCatalog` lifecycle surface.

### Conventions

The transaction receives typed owners and callbacks. It may inspect a private occupant id while
reconciling, but all returned payloads contain only the structural document-and-role address.

### Invariants And Boundaries

- One invocation performs at most one replacement retry.
- A manual or unattributed live occupant is never retired merely because it lacks dispatch evidence.
- A catalog receipt and a present pinned brief must agree.
- A successful retry never exposes the replaced or current runtime id.
- `None` from evidence reconciliation is positive proof of no viable brief; exceptions and
  contradictions are unknown state and cannot authorize rollback.
- Serialization is supplied by `serving/structural_dispatch.py`; this module owns reconciliation,
  not lock implementation.

### Todos

None.

## Docs References

No Domain Documentation source is configured; this repository-owned transaction and its forcing
suite are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| The dispatch transaction has one bounded reconciliation-and-retry loop. | `execute_dispatch_transaction` | mcp/src/agents_remember/application/structural/dispatch_transaction.py:54-88 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Existing generation evidence is loaded, repaired, and classified before retirement. | `reconcile_dispatch_evidence`; `_load_dispatch_evidence`; `_dispatch_evidence_outcome` | mcp/src/agents_remember/application/structural/dispatch_transaction.py:124-142; mcp/src/agents_remember/application/structural/dispatch_transaction.py:145-169; mcp/src/agents_remember/application/structural/dispatch_transaction.py:172-215 |
| Contradictory evidence produces the stable typed reconciliation refusal. | `_reconciliation_refusal` | mcp/src/agents_remember/application/structural/dispatch_transaction.py:218-230 |
| Concurrent, retry, compaction, and replacement behavior is forced end to end. | `StructuralSeatReplacementTests` | mcp/tests/test_structural_seat_replacement.py:63-540 |

## Cross-Repo References

No cross-repository dependency governs this unit.

## Update History

- 2026-08-26T16:03+02:00 — Post-failure repair: documented the dispatch-specific receipt-store
  collaborator and rechecked the explicitly bounded two-attempt reconciliation loop. Verification
  remains closeout-owned.


- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2 final curation: made the positive-proof versus
  unknown-state rollback boundary explicit and refreshed every final candidate citation.
  Verification remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: created for canonical-seat dispatch
  reconciliation. Verification remains closeout-owned.
