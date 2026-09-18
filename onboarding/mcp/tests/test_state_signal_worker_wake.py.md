# mcp/tests/test_state_signal_worker_wake.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_state_signal_worker_wake.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T21:40+02:00 |
| lastVerifiedCommitHash | `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| lastVerifiedCommitDate | 2026-09-18T07:49:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pins the wake a `worker` seat owes its manager at the end of an ordinary turn. A worker's substantive
handoff is its turn report, and it is not required to author a second completion message, so the
wake has to arrive on its own: an owned `worker` row whose **catalog terminal evidence** says
`completed` or `interrupted` becomes a state-signal finding, and the notifier persists and routes
exactly one durable row to the leaf's current manager through the existing inbox path. Seven retained
cases. The module asserts the state-signal relay's own surface only — no row, marker, document or
address outside it — and says nothing about the pre-existing dead-upstream supervision row the same
sweep separately raises.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in history
describe prior populations and must not be used to recreate removed tests or claim they still run.

1. `test_completed_worker_without_inbox_row_wakes_current_manager` — the incident shape: report
   written, turn ended, no message sent, manager woken. The whole store holds exactly one
   notifier-authored state-signal addressed to the live manager, carrying the worker seat, the leaf
   document, the role, the outcome and the terminal evidence identity; the seat's emitted marker
   advances to that identity; re-projecting the same evidence mints no second row.
2. `test_a_second_terminal_turn_for_the_same_seat_wakes_the_manager_again` — dedupe is per
   terminal-evidence identity, not per seat. A second turn on the same stored row advances the marker
   to `turn-10` and wakes the manager again, so a resumed worker whose first wake already landed still
   reaches its manager. The second turn is projected onto the **stored** row so turn 1's marker is
   still present when turn 2 is evaluated.
3. `test_failed_or_unknown_terminal_turn_never_wakes_the_manager` — `completed` and `interrupted` are
   the wake conditions, however real the evidence identity. A turn-end carrying a genuine adapter
   evidence identity but a `failed` or `unknown` outcome leaves the whole store empty, the finding
   list empty and the seat unstamped; the final leg re-reports the same seat and evidence identity as
   `completed` and requires the wake.
4. `test_interrupted_worker_wakes_manager_as_interrupted` — the recovery state travels with the wake:
   the row carries `interrupted` and its origin (`interrupted_by=developer`) and is not mislabelled as
   a completed turn.
5. `test_worker_wake_leaves_task_documents_untouched` — the signal reports a seat turn and never
   closes task work. The leaf and master documents (JSON and rendered Markdown) are captured around
   the sweep and compared byte for byte; leaf status stays `planning`, both steps stay `pending`, and
   the master's sub-task row stays `inProgress`.
6. `test_turn_end_without_terminal_evidence_identity_wakes_nobody` — a report on disk is not terminal
   evidence; the evidence identity is the discriminator. With a real worker report written and no
   evidence identity the store stays empty and the seat unstamped; stamping the adapter identity
   alone makes the next sweep wake the manager.
7. `test_worker_below_a_managerless_master_wakes_nobody_and_stays_eligible` — no derivable manager
   means no wake, no marker and no guessed global owner. The only visible manager owns a different
   master, so waking it would be the cross-master misroute the structural route forbids; the source
   stays eligible and the same seat wakes the right manager on the next sweep once that master has
   one.

### Conventions

One `unittest` case per boundary over a temporary coordination root holding real task documents, a
real `TerminalCatalog` file, a real inbox log and the real durable stores. Seats are seeded on the
catalog as adapter/catalog terminal truth (`_worker`, `_manager`, `_sprint_orchestrator`); no inbox
row is created for the worker at all, and the module asserts the **whole** store rather than its
state-signal subset, so a worker-authored row would be visible rather than filtered out.
`_RecordingHost` counts every contact the sweep makes with the terminal host: `get` is the live
terminal-session read behind the terminal-session GET route, and `has_session_calls` is populated on
the delivery path, which is what makes an empty `get_calls` a measured zero on a host the sweep
demonstrably reached rather than a host it never touched. Cases drive the retained entry points
(`run_agent_notifier_sweep`, `evaluate_state_signal_findings`) rather than private helpers.

### Invariants And Boundaries

- The eligible-outcome set is pinned from **both** sides: `completed` and `interrupted` wake the
  manager, and a turn-end whose outcome is neither must not, however real its evidence identity is.
- Per-turn dedupe is pinned in both directions: the same evidence identity projected twice mints one
  row, and a second distinct terminal turn on the same seat mints its own wake instead of being
  swallowed by the first turn's marker.
- Each positive case carries the negative half that keeps it falsifiable: the completed and
  interrupted cases each assert their own outcome and exclude the other, the task-document case
  asserts the wake happened before it asserts nothing else moved, and the no-evidence case re-runs the
  same seat with its evidence identity stamped.
- Terminal truth is adapter evidence in the catalog, never a live session this process has to ask
  for; the wake is addressed by current occupancy, so no unrelated manager is woken and no global
  owner is guessed.
- The wake never mutates a task document. Reporting a seat turn is not closing task work.
- This card records source inspection of an uncommitted, unaccepted tree. It does not claim
  execution, acceptance, certification, or an independent review result. Lane registration lives on
  the `test-evidence-lanes.toml` card.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution
evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The incident shape: a completed worker with no inbox row wakes its current manager with one durable state-signal carrying seat, leaf, role, outcome and evidence identity, and re-projection mints no second row. | `test_completed_worker_without_inbox_row_wakes_current_manager` | mcp/tests/test_state_signal_worker_wake.py:324-368 |
| Dedupe is per terminal-evidence identity, not per seat: a second turn on the same stored row wakes the manager again. | `test_a_second_terminal_turn_for_the_same_seat_wakes_the_manager_again` | mcp/tests/test_state_signal_worker_wake.py:370-421 |
| `failed` and `unknown` outcomes never wake the manager and leave the seat unstamped and eligible, however real the evidence identity. | `test_failed_or_unknown_terminal_turn_never_wakes_the_manager` | mcp/tests/test_state_signal_worker_wake.py:423-455 |
| An interrupted turn wakes the manager as `interrupted` with its origin, not as a completed turn. | `test_interrupted_worker_wakes_manager_as_interrupted` | mcp/tests/test_state_signal_worker_wake.py:457-478 |
| The wake leaves the leaf and master task documents byte-unchanged; it never closes task work. | `test_worker_wake_leaves_task_documents_untouched` | mcp/tests/test_state_signal_worker_wake.py:480-509 |
| A turn-end without a terminal evidence identity wakes nobody; stamping the adapter identity alone makes it wake. | `test_turn_end_without_terminal_evidence_identity_wakes_nobody` | mcp/tests/test_state_signal_worker_wake.py:511-535 |
| A worker below a managerless master wakes nobody, stamps no marker, guesses no global owner, and stays eligible for the next sweep. | `test_worker_below_a_managerless_master_wakes_nobody_and_stays_eligible` | mcp/tests/test_state_signal_worker_wake.py:537-574 |
| The terminal host records every contact the sweep makes, so an empty live terminal-session read is a measured zero on a host the delivery path reached. | `_RecordingHost` | mcp/tests/test_state_signal_worker_wake.py:72-89 |
| The accepted paster keeps delivery assertions on the shared protocol seam. | `_accepted_paster` | mcp/tests/test_state_signal_worker_wake.py:92-104 |
| One owned worker seat reporting canonical terminal truth from the adapter. | `_worker` | mcp/tests/test_state_signal_worker_wake.py:145-167 |
| The manager seat, addressed by current occupancy rather than by a recorded sender. | `_manager` | mcp/tests/test_state_signal_worker_wake.py:130-142 |
| The sprint-scoped orchestrator, the manager's own structural owner, present so the sweep's unrelated dead-upstream fact stays quiet and the whole store can be asserted. | `_sprint_orchestrator` | mcp/tests/test_state_signal_worker_wake.py:170-185 |
| The temporary world writes real sprint, master, leaf and unrelated-master documents before the sweep resolves structural owners. | `setUp` | mcp/tests/test_state_signal_worker_wake.py:203-277 |
| Every agent the whole store names, as address or as owner, used to prove no unrelated manager was woken. | `_addressed_agents` | mcp/tests/test_state_signal_worker_wake.py:304-312 |
| The module's `unit-regression` lane row, added by the same change set that created the module. | "mcp/tests/test_state_signal_worker_wake.py" | mcp/tests/test-evidence-lanes.toml:133-133 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History
- 2026-09-18T05:29:42+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:133-133. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:35+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_state_signal_worker_wake.py"` → `mcp/tests/test-evidence-lanes.toml:132-132`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.
- 2026-09-18T02:37:44+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:130-130. No content impact: mechanical anchor-range projection bound to citation source snapshot d211cfd02f11c0600198b11c621aa5574ac8743db6e0ca1d2c92936e561c5146; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:128-128. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:124-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-15T21:40+02:00 — 260831-LOCR-L05 curator, **re-dispatch**: created this sidecar for the seven-case worker turn owner wake module (incident-shape completed wake, second-turn re-wake, `failed`/`unknown` refusal, interrupted boundary, task-document immutability, evidence-identity discrimination, managerless-master refusal with retained eligibility). Recorded the instrument-reach convention (`_RecordingHost` counts, whole-store assertion, both-sided outcome and dedupe pins) that makes each case's negative half falsifiable. Lane registration lives on the `test-evidence-lanes.toml` card. Verification metadata pinned to the leaf candidate base `67c91534` until closeout stamps the leaf commit; no execution or acceptance claim is made.
