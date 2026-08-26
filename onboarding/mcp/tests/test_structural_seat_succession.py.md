# mcp/tests/test_structural_seat_succession.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_structural_seat_succession.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T22:27+02:00 |
| lastVerifiedCommitHash |  `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate |  2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces successor re-selection and address-bound dispatch-receipt preservation for canonical seats.

## Code Commentary

### Logic

The suite proves that a dead preferred incumbent is marked exited and the live staged heir is
reselected before a third process can be admitted. It also proves a receipt survives promotion of
the same document-and-role seat, but is cleared by a cross-document or same-document role move so
stale evidence cannot satisfy reconciliation for another address.

### Conventions

Spawn succession uses the real catalog and spawn primitive with the shared fake host; receipt rules
are asserted directly on immutable catalog-row transformations and reconciliation.

### Invariants And Boundaries

- A live staged heir prevents admission of a third generation after incumbent death.
- Promotion preserves evidence only when document and role are unchanged.
- Any cross-seat or role move clears the address-bound brief receipt.
- Reconciliation never treats cleared evidence as proof for the new seat.

### Todos

None.

## Docs References

No Domain Documentation source is configured; this is repository-local succession proof.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Dead-incumbent probing reselects the staged heir before admitting another spawn. | `test_dead_incumbent_probe_reselects_live_heir_before_admitting_a_third` | mcp/tests/test_structural_seat_succession.py:50-90 |
| Same-seat promotion preserves its receipt while a cross-seat move clears it. | `test_brief_receipt_survives_same_seat_promotion_but_not_cross_seat_move` | mcp/tests/test_structural_seat_succession.py:92-127 |
| A role change on the same document also clears address-bound evidence. | `test_same_document_role_change_clears_address_bound_receipt` | mcp/tests/test_structural_seat_succession.py:129-139 |

## Cross-Repo References

No cross-repository dependency governs this test module.

## Update History

- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2: created for staged-heir re-selection and
  address-bound receipt proof. Verification remains closeout-owned.
