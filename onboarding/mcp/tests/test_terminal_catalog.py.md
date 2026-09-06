# test_terminal_catalog.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal_catalog.py`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash |  `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate |  2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks terminal catalog durability: landed state stays landed, dispatch-brief receipts are idempotent and reject replacement, torn extra data refuses without erasure, concurrent upserts preserve rows, and cross-instance termination cannot be resurrected. Temporary catalog instances exercise durable state rather than a pure in-memory substitute.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

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
| Landed state round trips and is not reanimated | `test_landed_state_round_trips_and_is_not_reanimated` | mcp/tests/test_terminal_catalog.py:59-85 |
| Dispatch brief receipts are idempotent and refuse a second receipt | `test_dispatch_brief_receipts_are_idempotent_and_refuse_a_second_receipt` | mcp/tests/test_terminal_catalog.py:87-103 |
| Read refuses torn extra data without erasing evidence | `test_read_refuses_torn_extra_data_without_erasing_evidence` | mcp/tests/test_terminal_catalog.py:105-112 |
| Concurrent upserts do not lose or corrupt rows | `test_concurrent_upserts_do_not_lose_or_corrupt_rows` | mcp/tests/test_terminal_catalog.py:114-137 |
| Cross instance termination is sticky and never resurrected | `test_cross_instance_termination_is_sticky_and_never_resurrected` | mcp/tests/test_terminal_catalog.py:139-162 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: added reviewer parent
  serialization and address-bound lifetime forcing. Verification remains closeout-owned.

- 2026-08-26T16:03+02:00 — Post-failure repair: rebound receipt assertions to the dedicated
  `DispatchBriefReceiptStore`, including the missing-row result and second-receipt refusal. No
  certifying test execution is claimed.


- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2 final curation: corrected the governing tests
  overview and kept this unit's receipt claim limited to idempotent same-generation binding plus
  second-receipt refusal; cross-address movement is forced in the succession suite. No test
  execution is claimed.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: added private receipt round-trip/idempotency and
  staged-heir promotion coverage. Verification remains closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `test_terminal_catalog.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 2 citation claims; scoped result 0 findings.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: documented additive control metadata
  round-trip and legacy omission coverage.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T18:30+02:00 — 260707-HFX2-L18: added one complete optional-field projection and
  round-trip regression covering role/provenance, tuples, paths, liveness, retirement/landing,
  labels, and turn state. Existing omission/legacy cases remain the complementary absent-field
  proof; other diffs are formatting only. Verification metadata remains pinned until closeout
  stamps the eventual L18 code commit.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added durable seat-role migration and pair-lookup
  regressions, including stable in-place catalog rewrite.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: added dispatch-provenance round-trip and lock-safe
  log-binding race coverage. Verification metadata remains pinned until closeout stamps the eventual
  L15 code commit.

- 2026-07-09T14:05+02:00 — HFX2-L11 (landed chat archive): added 46 lines of coverage for the new
  `status:"landed"` state — `mark_landed`/`with_landing` provenance round-trip, and confirms landed
  is preserved (never reverted) across `with_attachment`, `with_liveness_success`, and `mark_exited`
  (the terminal-forward guarantee the reviewer's D-3 probe and delta-verify both confirmed). Verification
  metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-06T23:58:48+02:00 — 260703-L14 (visual hierarchy + chat grouping): added
  `test_spawn_role_round_trips_and_is_omitted_when_unset` — the `spawn_role` column serializes as
  `spawnRole` when set, is omitted when unset, and reads back migration-safe (mirrors the L5
  `leaf_key` cases). Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-03T12:50+02:00 — No content impact: L15 hoisted a function-local `import threading` to module top for the PLC0415 gate; no test logic change.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: `active_for_leaf` coverage is now role-aware — `_entry` takes a `kind`
  (harness ⇒ chat, terminal), `test_active_for_leaf_returns_running_owner` pins the default `"chat"` role,
  and `test_active_for_leaf_is_scoped_by_role` seeds a chat + a terminal on one leaf and asserts each role
  resolves independently. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added `leaf_key` coverage — round-trip + omit-when-unset + legacy
  row→`None` (migration-safe), `with_leaf_key` bind/unbind, and `active_for_leaf` returning the single
  running owner (not exited/terminated/other-keyed rows). Verification metadata pinned until closeout
  stamps the L5 commit.
- 2026-06-27T00:22+02:00 — Task 22 follow-up: added coverage that `mark_exited` cannot downgrade an
  explicitly terminated catalog row, matching the browser `End` behavior.
- 2026-06-26T23:05+02:00 — Created for task 22: covers catalog path, JSON schema/order, default
  terminated-row filtering, exited-row visibility, termination timestamps, and attach restoring running
  status. Verification metadata pinned until closeout stamps the task-22 code commit.
