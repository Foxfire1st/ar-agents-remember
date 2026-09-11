# mcp/tests/test_state_signal_relay.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/tests/test_state_signal_relay.py`                   |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `11d1ed0e5542818283bf7fb012a7bdd642aaba2e`                                    |
| lastVerifiedCommitDate | 2026-09-11T18:45:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Simulates multiple relay ticks to preserve the finished-worker signal even without an inbox row, revalidate topology and landed episodes before non-reaction actions, hold a busy manager at the boundary then land once, rebind a replaced owner, route a master-bound reviewer to the current manager, fence malformed or ambiguous topology per subject, avoid done signals for killed or hung seats, and withhold any owner wake while a seat's own turn is still open. Injected delivery and clock boundaries make these relay assertions deterministic.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

The current structural-routing cases exercise action-time replacement, missing/ambiguous parent
topology isolation, owner disappearance after finding revalidation, and action-time refusal without
publishing a row or source marker. These cases protect the R08 refusal and retry boundary while
leaving delivery/recovery and canonical seat selection to their owning modules.

The non-completion boundary also covers an open turn. A seat whose `turn_state` is still `working`
reports nothing to its owner even while stale adapter outcome fields survive on its row; the same
seat produces exactly one owner-addressed signal once its turn has ended. That case holds the
ended-turn trigger in place so the parked open-turn external-await design cannot be adopted here as
a fallback producer.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Incident 1 finished worker without inbox row still signals manager | `test_incident_1_finished_worker_without_inbox_row_still_signals_manager` | mcp/tests/test_state_signal_relay.py:264-287 |
| Non reaction action revalidates current topology and landed episode | `test_non_reaction_action_revalidates_current_topology_and_landed_episode` | mcp/tests/test_state_signal_relay.py:289-349 |
| Busy manager holds at boundary then lands exactly once | `test_busy_manager_holds_at_boundary_then_lands_exactly_once` | mcp/tests/test_state_signal_relay.py:351-417 |
| Owner rebinding after manager replacement | `test_owner_rebinding_after_manager_replacement` | mcp/tests/test_state_signal_relay.py:419-436 |
| Master-bound reviewer reaches the current manager after replacement | `test_master_exit_reviewer_signal_reaches_current_manager` | mcp/tests/test_state_signal_relay.py:438-466 |
| Missing or ambiguous parent topology fences one subject while preserving an unrelated finding | `test_topology_refusal_fences_one_subject_and_keeps_unrelated_finding` | mcp/tests/test_state_signal_relay.py:468-497 |
| Owner disappearance after finding revalidation leaves the source eligible and unmarked | `test_owner_disappearance_after_revalidation_keeps_source_eligible` | mcp/tests/test_state_signal_relay.py:499-536 |
| Action-time topology refusal fences the subject without a marker | `test_action_topology_refusal_fences_subject_without_marker` | mcp/tests/test_state_signal_relay.py:538-555 |
| No done signal for killed or hung seats | `test_no_done_signal_for_killed_or_hung_seats` | mcp/tests/test_state_signal_relay.py:557-575 |
| An open turn never wakes the owner before terminal evidence | `test_open_turn_never_wakes_the_owner_before_terminal_evidence` | mcp/tests/test_state_signal_relay.py:577-603 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-10T10:06:31+02:00 — 260831-LOCR-L25 curator: recorded the added open-turn non-wake case (`test_open_turn_never_wakes_the_owner_before_terminal_evidence`) and re-derived all ten retained case ranges against the current source on the leaf candidate base `6096941f41204c9a7d6ccb2b29f6b2e862ed56b4`; the nine pre-existing ranges had drifted and now match the source. This records source behavior, not a test execution or acceptance claim; verification metadata remains closeout-owned.

- 2026-09-08T14:22:32+02:00 — 260831-LOCR-L08 curator: reconciled the retained relay test account with the current R08 replacement, topology-refusal, owner-disappearance, and no-marker cases. The card records scenario ownership and source anchors without claiming execution or acceptance.

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-26T12:30+02:00 — 260821-ARSPAWN-L2 semantic re-read: retained the state-signal, non-reaction, and
  boundary-drain predicate claim after verifying each current implementation contains ambiguity
  to its own row and preserves the relay semantics; regenerated all three source ranges.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_state_signal_relay.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: recorded the current state-signal relay, owner, and
  metadata coverage against the staged source; verification metadata remains pinned until closeout.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: documented all-subordinate relay, action-time mutation,
  fresh-owner metadata, and timezone-naive evidence regressions. Verification metadata remains
  pinned until closeout stamps the code commit.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the nudge-store removal from the
  state-signal relay harness. Verification metadata pinned until closeout stamps the
  260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the landed-row fixtures' formal
  `state="landed"` alignment (N13/N16 migration; the by-rule pending landing no longer exists).
  Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: recorded the working-manager fixture change
  in `test_owner_rebinding_after_manager_replacement` (isolates the L2 rebinding behavior from
  the new compound-idle fact), corrected the governing-overview link, and widened the
  non-reaction invariant to include the manager→orchestrator arm. Verification metadata pinned
  until closeout stamps the 260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the new relay
  simulation suite (incident-#1, boundary hold past SLA/backoff, origin, rebinding, idle flap,
  non-reaction, drain). Verification metadata pinned to the leaf base `1c1629fc` until closeout
  stamps the 260713-TES-L2 commit.
