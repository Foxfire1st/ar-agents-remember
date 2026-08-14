# mcp/src/agents_remember/serving/degradation_delivery.py

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember                                                |
| path                   | `mcp/src/agents_remember/serving/degradation_delivery.py`       |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated            | 2026-08-08T14:38+02:00                                         |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                     |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                  |

## Governing Overview

[serving overview](overview.md)

## Purpose

`serving/degradation_delivery.py` (260731-EFA-L9) is the serving-backed implementation of the
provider degradation alert port, added when the providers→serving layering violation was removed:
providers may not import serving, so serving provides this delivery implementation behind a port.

## Code Commentary

### Logic

`DegradationAlertDelivery` (cit:(["class DegradationAlertDelivery"], mcp/src/agents_remember/serving/degradation_delivery.py:20-20)) implements the alert delivery contract used
by the degradation detector to post role-addressed inbox alerts; `__all__` exports only the class.

### Invariants And Boundaries

- Providers depend on the port; serving owns the concrete delivery. Do not move delivery into
  providers (layering rail enforced).

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The degradation detector declares the alert port this module implements. | `DegradationAlertPort` | mcp/src/agents_remember/providers/degradation.py:74-74 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the degradation alert delivery
  port implementation. Verification metadata pinned until closeout stamps the L9 code commit.
