# mcp/tests/test_state_signal_restart_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_state_signal_restart_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T13:15+02:00 |
| lastVerifiedCommitHash | `52bee42965e9437b3692325954ca1dcac92813e6`|
| lastVerifiedCommitDate | 2026-09-15T13:39:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Forces the state-signal relay's durable order — row persisted, marker stamped, delivery attempted —
across every cut point a crash, a failed store write, or a same-seat structural rebind can produce.
Each case builds one durable world, cuts it, and then re-reads that world through brand-new
catalog/store/context objects, so recovery is proven against durable files rather than against
in-memory state. Seven retained cases.

## Code Commentary

### Logic

1. `test_marker_failure_keeps_one_unmarked_row_and_restart_retries_it` — the marker write raises
   after the row is durable: zero adapter submissions, exactly one pending row with `attemptCount=0`
   and no `nextAttemptAt`, and the seat's `state_signal_emitted_for` still unset. A restarted process
   renews that same row id, stamps `turn-9`, and delivers once; a third sweep adds nothing.
2. `test_immediate_boundary_marker_failure_is_fenced_until_the_marker_retries` — sweep two runs with
   the generic redelivery finder enabled over the generation **and** the boundary-drain finder
   yielding the same row; both findings are acted and both return `skipped` /
   `state-signal source marker not stamped` with zero submissions and no delivery-state mutation.
   State-signal recovery in that same sweep then renews the row, stamps the marker and delivers once.
3. `test_stop_after_marker_before_delivery_resumes_on_the_pending_row_path` — the process stops
   inside the delivery call after the marker callback returned: one *marked* pending row remains and
   the ordinary pending-row path lands it once on restart, with no second logical signal.
4. `test_rebind_before_marker_retry_renews_and_readdresses_the_same_row` — the same seat is rebound to
   another master's leaf and another role before the retry: the original row id is renewed and
   re-addressed to the current owner (`manager-1` → `manager-2`), never duplicated.
5. `test_two_seats_reporting_the_same_evidence_keep_distinct_rows` — two replacement seats on one leaf
   reporting the same outcome and evidence id hold two rows; each retry renews only its own row and
   stamps only its own marker.
6. `test_new_evidence_identity_rearms_and_the_older_row_still_delivers` — a later turn re-arms the seat
   as a distinct successor row while the older `turn-9` row still lands through its own drain path;
   the seat's marker ends on `turn-10`.
7. `test_other_kinds_keep_their_structural_coalescing_key` — the non-state preservation control:
   an `escalation` post renews across a *different* occupant under the same structural key, and a
   different seat role produces a second row. This is the one case that passes on the pre-change
   sources (see the falsification note below), which is exactly its job.

### Conventions

One `_World` per case, built over a temporary coordination root with a real catalog file and a real
inbox log; `_World.restarted` is the only "restart" mechanism and always constructs new store objects
over the same files. `_failed_marker_write` is scoped to the catalog's `upsert`, so the row write
stays healthy and only the marker leg fails. `StateSignalRestartRecoveryTests._submit_patch` patches
`inbox_delivery.submit_control_prompt` with an accepted receipt, so the assertions are about durable
row/marker/attempt state rather than about a live adapter. Cases drive the retained entry points
(`run_agent_notifier_sweep`, `act_on_finding`, `evaluate_state_signal_findings`,
`evaluate_boundary_drain_findings`) rather than private helpers.

### Invariants And Boundaries

- The durable inbox row — not the catalog marker — is the wake authority: every cut point leaves one
  pending row that the next sweep renews.
- Row identity is stable across a failed marker write, a stop after the marker, and a same-seat
  rebind (`state_signal_landed` and an exact row-id list are asserted, not inferred from a green run).
- A marker write that raises makes zero adapter submissions; delivery is unreachable while the exact
  source marker is unstamped.
- Two seat ids sharing document, role, outcome and evidence id never renew one another's row.
- **Coverage limit recorded from source and from independent review (verdict observation O-4):** case 2
  obtains the two competing findings by calling the finders directly and acting each finding, because
  the sweep's generic redelivery path cannot select the row by construction —
  `state_signals.state_signal_held_on_boundary` excludes a non-landed state-signal row whose target
  seat is alive. The guard was independently shown firing inside a real sweep through the
  boundary-drain route (a subject rebound to a documentless binding), so the operation-level claim
  holds; a future touch of this module would be stronger with a real-sweep drain-fence assertion plus
  a comment naming that exclusion. No case here claims that the generic finder is the reachable route.
- This card records source inspection. It does not claim acceptance, certification, or an independent
  review result. The module is ordinary version-controlled test source: it holds no governed evidence
  registration, and the review verdict's promotion hold point is the
  `test-evidence-lanes.toml` `unit-regression` row, not a record created here.

### Todos

No additional implementation scope is opened by this memory reconciliation. The optional real-sweep
drain-fence hardening above is not authorized scope for this leaf.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own fixtures
and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A failed marker write leaves one unmarked pending row, zero submissions, and a restart that renews the same row id before delivering once. | `test_marker_failure_keeps_one_unmarked_row_and_restart_retries_it` | mcp/tests/test_state_signal_restart_recovery.py:353-388 |
| Both competing finders' findings are fenced at the shared action, and recovery in the same sweep stamps before delivering. | `test_immediate_boundary_marker_failure_is_fenced_until_the_marker_retries` | mcp/tests/test_state_signal_restart_recovery.py:390-449 |
| A stop after the marker leaves one marked pending row that the ordinary pending-row path lands once. | `test_stop_after_marker_before_delivery_resumes_on_the_pending_row_path` | mcp/tests/test_state_signal_restart_recovery.py:451-486 |
| A same-seat structural rebind renews and re-addresses the original row id rather than minting a sibling. | `test_rebind_before_marker_retry_renews_and_readdresses_the_same_row` | mcp/tests/test_state_signal_restart_recovery.py:488-527 |
| Two distinct seats reporting one evidence identity keep two rows that never renew each other. | `test_two_seats_reporting_the_same_evidence_keep_distinct_rows` | mcp/tests/test_state_signal_restart_recovery.py:529-561 |
| A later evidence identity re-arms the seat as a successor row while the older row still delivers. | `test_new_evidence_identity_rearms_and_the_older_row_still_delivers` | mcp/tests/test_state_signal_restart_recovery.py:563-608 |
| The non-state preservation control: structural coalescing across occupants, a second row on a different role. | `test_other_kinds_keep_their_structural_coalescing_key` | mcp/tests/test_state_signal_restart_recovery.py:610-652 |
| Fresh store objects over the same durable files model a restarted notifier process. | `_World`; `_World.restarted` | mcp/tests/test_state_signal_restart_recovery.py:267-305 |
| The injected durable-store fault fails only the marker leg, leaving the row write healthy. | `_failed_marker_write` | mcp/tests/test_state_signal_restart_recovery.py:332-337 |
| The accepted-receipt patch keeps delivery assertions on the shared protocol seam. | `_submit_patch` | mcp/tests/test_state_signal_restart_recovery.py:345-351 |
| The temporary world writes a real task topology before the sweep resolves structural owners. | `_write_task_topology` | mcp/tests/test_state_signal_restart_recovery.py:198-244 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-15T13:15+02:00 — 260831-LOCR-L10 curator: created this sidecar for the seven-case crash/restart recovery module (marker failure, immediate-boundary fence over both finders, stop-after-marker, same-seat rebind, two-seat collision, later-evidence re-arm, non-state preservation control). Recorded the durable row/marker/order contract it forces, the `_World.restarted` reconstruction convention, and the review verdict's coverage limit: the fence case drives the finders directly because `state_signal_held_on_boundary` excludes a live-target state-signal row from the generic finder by construction. Lane registration lives on the `test-evidence-lanes.toml` card; this module holds no governed evidence registration. Verification metadata pinned to the leaf base until closeout stamps the leaf commit.
