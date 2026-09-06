# mcp/src/agents_remember/models/conversations/opening.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/models/conversations/opening.py`     |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-08T14:38+02:00                                       |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                   |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/opening.py` (260731-EFA-L9, moved from
`serving/conversation/_models_operations.py`) owns `OpenConversationOperation`, the
identity/catalog-proof open operation with phase-matching rollback.

## Code Commentary

### Logic

`OpenConversationOperation` (cit:(["class OpenConversationOperation"], mcp/src/agents_remember/models/conversations/opening.py:16-16)) validates the complete semantic
product: no-launch outcomes carry no spawned identity, and identity-bearing failures require
catalog proof plus the phase-matching rollback state.

### Invariants And Boundaries

- Open identity and catalog proof must agree exactly; do not weaken the bidirectional rollback
  product.

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

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the opening module moved from
  `serving/conversation/_models_operations.py`. Verification metadata pinned until closeout
  stamps the L9 code commit.
