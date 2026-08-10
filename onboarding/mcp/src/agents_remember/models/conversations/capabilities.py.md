# mcp/src/agents_remember/models/conversations/capabilities.py

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| repository             | agents-remember                                                  |
| path                   | `mcp/src/agents_remember/models/conversations/capabilities.py`    |
| doc_type               | `file-level-onboarding`                                          |
| lastUpdated            | 2026-08-08T14:38+02:00                                           |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                       |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                    |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/capabilities.py` (260731-EFA-L9, moved from
`serving/conversation/_models_status.py`) owns the fixture-evidence-bound capability contract:
exact evidence products gate `supported`/`partial` claims.

## Code Commentary

### Logic

`CapabilityEvidence` (cit:(["class CapabilityEvidence"], mcp/src/agents_remember/models/conversations/capabilities.py:11-11)) requires the exact runtime-fixture
evidence product; `FeatureCapability` (cit:(["class FeatureCapability"], mcp/src/agents_remember/models/conversations/capabilities.py:18-18)) carries the deliberate
no-version-demotion NOTE — the contract is the only gate and runtime/helper versions are
informational metadata only; `ConversationCapabilities` (cit:(["class ConversationCapabilities"], mcp/src/agents_remember/models/conversations/capabilities.py:102-102)) aggregates the live, history,
attachment, control, and telemetry slices.

### Invariants And Boundaries

- `supported`/`partial` capability claims require exact runtime-fixture evidence and a fixture id;
  fixture evidence itself has `enablesCapabilities=false`.
- Do not reintroduce version-string demotion (L5F R4).

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
| Fixture evidence never enables capabilities. | `test_installed_runtime_fixtures_are_allowlisted_evidence_not_enablement` | mcp/tests/test_conversation_foundation.py:163-188 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the capabilities module moved from
  `serving/conversation/_models_status.py`. Verification metadata pinned until closeout stamps
  the L9 code commit.
