# mcp/tests/test_hosted_readiness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/tests/test_hosted_readiness.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Exact adapter-handshake hosted readiness.

## Code Commentary

### Logic

A matching structured handshake is ready without pane probing. Ready control with non-accepting submission state remains not-ready. Waiting obeys its deadline; a catalog identity change during adapter read becomes unknown-session.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Pane appearance is diagnostic only and cannot establish readiness. A readiness observation must remain tied to the same exact catalog generation.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact adapter handshake is ready and pane probes are diagnostic only. | `test_exact_adapter_handshake_is_ready_and_pane_probes_are_diagnostic_only` | mcp/tests/test_hosted_readiness.py:92-109 |
| Ready control without acceptance is not ready. | `test_ready_control_without_acceptance_is_not_ready` | mcp/tests/test_hosted_readiness.py:113-125 |
| Not ready wait is bounded. | `test_not_ready_wait_is_bounded` | mcp/tests/test_hosted_readiness.py:128-144 |
| Exact identity change during adapter read is unknown. | `test_exact_identity_change_during_adapter_read_is_unknown` | mcp/tests/test_hosted_readiness.py:147-157 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
