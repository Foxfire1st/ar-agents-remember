# mcp/tests/test_inbox_arrival_guarantee.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_inbox_arrival_guarantee.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Scoped terminal-seat builder shared by inbox consumers.

## Code Commentary

### Logic

_seat creates a TerminalCatalogEntry from caller-supplied identity and task scope. This module now supplies the row fixture used by delivery tests and contains no retained arrival-guarantee test methods.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The old 25-case arrival, expiry and watcher matrix is historical. A fixture row does not prove that any command arrived or that a retry is authorized.

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
| Seat. | `_seat` | mcp/tests/test_inbox_arrival_guarantee.py:14-29 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T14:29+02:00 — Re-read post-time owner rebinding and regenerated the
  `_post_address`/`_is_owner_addressed` ranges around their current declarations; verification
  metadata remains unchanged for governed closeout.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the current staged inbox-arrival guarantee harness; the existing assertions remain accurate. Verification metadata remains pinned until closeout.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the nudge-store removal from the
  TTL/cap harness context. Verification metadata pinned until closeout stamps the
  260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: created this file-level onboarding card for
  the new arrival-guarantee forcing suite (25 test methods: scoped custody, post-time
  rebinding, supersession, terminal inspectability, TTL/cap eviction, settings resilience,
  relay-death watch, retire surfacing). Verification metadata pinned until closeout stamps the
  260713-TES-L4 commit.
