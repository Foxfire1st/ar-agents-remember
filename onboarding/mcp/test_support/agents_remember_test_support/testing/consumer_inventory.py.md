# mcp/test_support/agents_remember_test_support/testing/consumer_inventory.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/consumer_inventory.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Enumerates every acceptance edge that could otherwise consume evidence from the wrong authority.

## Code Commentary

`ACCEPTING_CONSUMER_INVENTORY` maps coverage, quality, retry, route review, lifecycle, closeout, and
integration to their owner, current evidence shape, candidate proof, reachability, and enforcement.
Tests compare it to the closed `EvidenceConsumer` vocabulary.

The coverage owner is `quality_plan._pytest_step`: command construction moved out of the stable
`check` execution facade during the file-size responsibility split. The inventory names the real
owner rather than preserving a compatibility fiction. That ownership move does not change the
Dagger-only evidence boundary or create another consumer.

## Invariants And Boundaries

- Every consumer except local feedback appears exactly once.
- `direct_route_reachable` remains false for all accepting consumers.
- New acceptance consumers must extend both the model enum and this forcing inventory.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The complete accepting-consumer inventory is explicit. | `ACCEPTING_CONSUMER_INVENTORY` | mcp/test_support/agents_remember_test_support/testing/consumer_inventory.py:22-79 |

## Update History

- 2026-08-28T04:48+02:00 — Corrected the coverage consumer owner to the extracted
  `quality_plan._pytest_step`; evidence authority and the closed consumer vocabulary are unchanged.
- 2026-08-26T10:44:52+02:00 — No content impact: reviewed owner-string relocations for quality and lifecycle consumers; the closed accepting-consumer inventory and evidence reachability rules are unchanged.
- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
