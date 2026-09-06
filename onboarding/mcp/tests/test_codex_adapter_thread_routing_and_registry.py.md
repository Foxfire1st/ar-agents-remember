# mcp/tests/test_codex_adapter_thread_routing_and_registry.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/tests/test_codex_adapter_thread_routing_and_registry.py` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                   |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Codex seat policy and thread-identity routing tests.

## Code Commentary

### Logic

Unset policies are omitted from turn/start; configured sandbox mappings become copied JSON data. An unsolicited turn/started on the seat thread makes it busy and blocks preflight. A sub-agent settings frame crosses as raw evidence without changing the seat, while identical drift on the seat thread fails the bridge.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Thread identity, not payload shape, determines settings authority. The removed partial-collab registry tests must not be described as current coverage here.

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
| Turn start sends only the policies the seat configured. | `test_turn_start_sends_only_the_policies_the_seat_configured` | mcp/tests/test_codex_adapter_thread_routing_and_registry.py:58-108 |
| A turn the seat did not dispatch still makes it busy. | `test_a_turn_the_seat_did_not_dispatch_still_makes_it_busy` | mcp/tests/test_codex_adapter_thread_routing_and_registry.py:112-143 |
| A sub agents settings frame is evidence not the seats settings. | `test_a_sub_agents_settings_frame_is_evidence_not_the_seats_settings` | mcp/tests/test_codex_adapter_thread_routing_and_registry.py:147-197 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T11:15+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 6 assigned citation findings (3 missing anchors and 3 malformed sources); final scoped check is clean.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new Codex
  thread-routing / registry-binding suite. Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
