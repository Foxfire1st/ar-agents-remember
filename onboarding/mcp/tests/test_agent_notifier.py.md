# test_agent_notifier.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_agent_notifier.py`             |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Disposable terminal-row and delivery doubles for notifier consumers.

## Code Commentary

### Logic

The fixed NOW clock, _entry builder, reachable _FakeHost and accepted paster establish fixture inputs. _entry supplies seat identity; consumers use the catalog row own with_turn_state and dataclasses.replace for other fields. This file contains no retained test methods.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

A successful fake paste is fixture behavior, not proof of hosted delivery. Do not infer predicate, escalation or heartbeat protection from this helper module.

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
| Entry. | `_entry` | mcp/tests/test_agent_notifier.py:31-55 |
| Fakehost. | `_FakeHost` | mcp/tests/test_agent_notifier.py:58-65 |
| Fake paster. | `_fake_paster` | mcp/tests/test_agent_notifier.py:68-83 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-26T12:30+02:00 — 260821-ARSPAWN-L2 semantic re-read: retained the fact-predicate, action-dispatch,
  and sweep-owner claim after verifying current `evaluate_predicates` composes the same fact-only
  routes with per-row structural containment; regenerated its source ranges.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_agent_notifier.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the deletion of the
  expectation/ladder predicate test classes and the fact-only inbox-predicate surface.
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the `ExpectationPredicateTests`
  fixture kind swap from `ack-by` to `verdict-by` (ack-by retired with N16; verdict-by remains
  an active expectation kind). Verification metadata pinned until closeout stamps the
  260713-TES-L4 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the expectation-fixture rename
  (ack-by), the deletion of the turn-report staleness tests, and the new
  `RetiredDispatchExpectationTests` silence pins. Verification metadata pinned until closeout
  stamps the 260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T12:41:53+00:00 — 260731-EFA-L6 S18-B09 curator: split terminal-catalog aliases from the consuming supervisor fixture builder; the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2: recorded the `_entry` rewrite this leaf already made to
  the body. The fixture no longer mirrors `TerminalCatalogEntry`'s shape, so its `turn_state`,
  `turn_state_changed_at` and `liveness_failures` parameters (and the `SeatTurnState` import) are
  gone; callers now use the row's own `with_turn_state(state, changed_at=…)` or `replace(...)`. The
  rest of the source diff is parameter-object adoption at fixture call sites —
  `Expectation`/`ExpectationSubject` for expectation rows, `InboxMessage`/`InboxRouting`/
  `InboxAddress`/`InboxPoster`/`InboxSubject` for `create_operator_inbox_entry`, and
  `schedule=EscalationSchedule(...)` for `evaluate_escalation_findings` — plus `ruff format`
  reflow. Every class and every test name is identical and no predicate, ladder, respawn or sweep
  assertion changed, but the file lost 24 lines, so both in-file citations were re-anchored (the F1
  pin L759-L789 → L747-L777 and the HFX2-L9 sweep block L531-L636 → L526-L621).
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T19:49+02:00 — Positional 260707-HFX2-L19 F1: documented the public-boundary
  regression that keeps a past-SLA `no-hosted-session` row silent below
  `PERSISTENT_FAILURE_ATTEMPTS` and emits only the exhausted counterpart. Recorded why the
  no-catalog fixture mutation-pins `_delivery_failure_still_retrying`. Verification metadata remains
  pinned until manager-owned closeout stamps the eventual L19 code commit.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: covered pair-scoped findings/coalescing/routing and
  sweep-clock delivery; recorded the bounded O4 fixed-point adjustment.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: covered replacement-leaf progress suppression and the
  one-row redelivery budget on the log-confirmed delivery path. Verification metadata remains pinned
  until closeout stamps the eventual L15 code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: added chain-progress suppression,
  rung-floor/same-sweep guard, and current-manager dead-upstream regressions; recorded the unbound-
  worker S1 follow-up. Verification metadata remains pinned until closeout stamps the eventual L13
  code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: added supervisor regressions for one signal per cooldown,
  mid-turn pane-signal suppression with no owner inbox row, restart/backlog non-burst before the
  900-second floor, and one-second sweeps that tick heartbeat without minting per-second signal
  rows. Verification metadata pinned until closeout stamps the 260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm, R1/R2/R4/R6): added terminal-ladder
  predicate/integration tests proving dead/no-hosted-session terminal-rung rows become
  `ladder-resolved` and are not redelivered, plus a redeliver-budget integration proving attempts are
  capped per sweep while heartbeat backlog/duration metrics advance. Verification metadata pinned
  until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 (escalation ladder + dead-man respawn, R2-R6): added
  `EscalationPredicateTests` (SLA-due/not-yet-due), `DeadUpstreamPredicateTests` (dead-owner fires,
  live-owner and no-provenance stay silent), and `LadderWalkIntegrationTests` — the R6 fixtures: a
  silent seat climbing all three rungs then hitting the rung-3 ceiling, a dead intermediate manager
  skipped at rung 2, a dead manager with live workers triggering respawn + orphan surfacing (workers
  themselves asserted unchanged), and the dead-upstream sweep signaling the grandparent. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T18:45+02:00 — Created for 260707-HFX2-L2 (supervisor sweep + predicates, R2-R6):
  sixteen tests — one per predicate family (pane/expectation/turn-report/inbox/seat-liveness, each
  with its fire + silent + edge-case variants), one seeded-drift sweep integration test asserting
  the full finding→action→heartbeat chain, a no-routable-owner edge case, and two heartbeat-specific
  cases (zero-drift still ticks; sweep count increments). Documents the fake-paster
  monotonic-chip-counter fix (a live F-V/N1 instance found while writing this suite) as a preserved
  invariant for future test additions. Verification metadata pinned until closeout stamps the
  260707-HFX2-L2 commit.
