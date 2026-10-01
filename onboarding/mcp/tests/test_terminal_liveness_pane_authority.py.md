# mcp/tests/test_terminal_liveness_pane_authority.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Falsifiable proof of one authority boundary: pane classification is **diagnostic-only** and may never
authorize readiness, delivery, terminal outcome/identity, interruption origin, or state-signal
eligibility. `PaneDiagnosticAuthorityTests` drives the real `TerminalCatalogLivenessSweeper.refresh`
and `observe_terminal_liveness` over temporary catalogs with the shared `_Clock`/`_FakeHost`/
`_entry`/`_snapshot`/`_ready_snapshot` helpers imported from
[test_terminal_liveness.py](test_terminal_liveness.py.md) — no parallel harness is built here. It is
the executable half of the `LOCR-R27@v1` contract that
[terminal_liveness.py](../src/agents_remember/serving/terminal_liveness.py.md) implements.

## Code Commentary

### Logic

The module is a **preservation** proof: it changes no production byte. Its subject is the separation
`terminal_liveness.py` already maintains — a pane reading's only sink is `control_raw["paneDiagnostic"]`
while turn truth comes from `snapshot_turn_state` or the literal `"stale"`.

The ten cases each pin a distinct clause of that contract:

1. **Contradiction, both directions.** `test_pane_and_adapter_disagreement_keeps_turn_truth_adapter_owned`
   runs two connected rows whose pane reading contradicts the adapter snapshot: the pane reads
   `turn-ended` under a running adapter turn, and `working` under a settled one. Each row keeps the
   adapter's `turn_state` while the pane's own reading survives as `paneDiagnostic`.
2. **Readiness.** `test_a_pane_reading_cannot_authorize_readiness_over_the_adapter` drives
   `AdapterSnapshot(control="disconnected" | "failed")` — both production-reachable `ControlState`
   values — with a pane capturer returning `CODEX_WORKING_PANE`. The persisted `control_state` is the
   adapter's value, `control_activity`/`control_acceptance` stay `unknown`, the turn claim stays the
   non-terminal `stale`, and `paneDiagnostic` is `working`. This is the case that pins the clause a
   pane reading can never authorize a dispatch-ready seat over a bridge the adapter reported gone.
3. **Below threshold.** `test_connected_row_keeps_its_control_and_turn_truth_below_the_read_threshold`
   fails the bridge read one and two times and asserts the retained control state, activity, turn
   state, its timestamp, and the incrementing `controlReadFailures` counter.
4. **Threshold ownership.** `test_the_failure_threshold_owns_the_stale_transition_not_the_pane` shows
   the third consecutive failure, not the pane content, owns the `disconnected`/`stale` transition.
5. **Starting rows.** `test_alive_starting_row_keeps_its_prior_turn_truth_through_any_read_failure`
   holds `starting` and the prior turn truth across repeated failures.
6. **Legacy rows.** `test_legacy_row_without_a_control_endpoint_projects_stale_for_any_pane` projects
   `unsupported`/`stale` for a row with no `control_endpoint` under both pane directions, and its
   `_forbidden_control_read` reader raises if the control surface is consulted at all — the transition
   is authorized by the missing control surface, not by pane text.
7. **Failed terminal page.** `test_failed_terminal_read_advances_no_terminal_truth_but_keeps_turn_truth`
   advances no outcome/identity while the separately successful canonical snapshot still projects
   non-terminal turn truth.
8. **Both observer phases.** `test_startup_prime_and_steady_pass_share_one_pane_diagnostic_boundary`
   asserts `host.calls == 3`, which discriminates the two-row starting fast path from a three-row full
   sweep, so the row it reports really came through the prime path.
9. **Pane independence.** `test_no_pane_reading_changes_a_turn_or_terminal_field` sweeps four pane
   readings (`turn-ended`, `working`, `awaiting-input`, `stale`) against one identical row and asserts
   the authoritative tuple is unchanged, with a non-vacuity check that all four readings classified.
10. **Negative source guard.** `test_no_source_write_can_make_a_pane_reading_authoritative` asserts
    `_pane_authority_offenders(terminal_liveness.py source) == []` and that each injected leak is
    caught.

`_pane_authority_offenders` is an AST taint analysis, not a text match: `_pane_derived_names` walks
assignments transitively, and `_keyword_writes` / `_dict_writes` / `_assign_writes` report a pane-
derived value reaching an authoritative field. `_PANE_AUTHORITY_FIELDS` is the field set;
`_PANE_WRITER_KEYWORDS` folds in `_record_adapter_turn_state`'s `state` parameter; `_PANE_CLASSIFIERS`
names the calls whose result is a captured pane reading. `_connected_entry` defaults
`control_state="ready"`, `control_activity="idle"`, `control_acceptance="immediate"`;
`_degraded_snapshot(entry, control)` projects `activity="unknown"`, `acceptance="unknown"`.

### Conventions

The module belongs to the **integration** lane in
[test-evidence-lanes.toml](test-evidence-lanes.toml.md) even though it is hermetic (temporary
catalogs, in-process `unittest`, no `worktree_services`), matching its sibling
`test_terminal_liveness.py`. Without that manifest row the module's application imports would run
inside ordinary unit collection, so a **new** module of this family needs its own lane row. Lane
membership is selection and cost classification only: it is not execution or acceptance evidence.

### Invariants And Boundaries

- A pane reading may be persisted only as `control_raw["paneDiagnostic"]`. It may never write
  `control_state`, `control_activity`, `control_acceptance`, `turn_state`, `turn_state_changed_at`,
  `terminal_outcome`, `terminal_outcome_at`, `terminal_evidence_id`, `interrupted_by`, or
  `state_signal_emitted_for`.
- The only pane-independent transitions are the R21 three-failure control-read threshold and the
  legacy no-`control_endpoint` compatibility projection. Both create no terminal outcome, terminal
  identity, or state signal.
- **This module is a deliberate split, not an accidental sibling; do not merge it back.**
  `test_terminal_liveness.py` is byte-unchanged at 574 lines, and an in-place extension would have
  pushed it to 1094 lines — inside the `system/coding-guidelines.md` 900-1200 "soft limit exceeded /
  do not add new feature logic without extracting" band. The shared helpers stayed in the original
  module and are imported.
- **The negative source guard is defence-in-depth over behaviour, never the sole pin.** Measured
  reach: it catches direct-value forms (`replace(entry, control_state=pane_diagnostic.state)`), the
  keyword form, the dict-literal form, and attribute stores. It is **blind** to a pane-derived
  constant written inside an enclosing `if` that tests the pane reading, to positional writer
  arguments (`_record_adapter_turn_state(c, e, pane_diagnostic.state, t)`), and to
  `CatalogTurnEvidence(state=<pane expression>)`. Those three shapes remain proposition-pinned by
  behaviour instead — the positional writer argument and the stamp alias are caught by the
  behavioural cases — so no clause of the contract rests on the guard alone. Closing the guards's
  blind spots would require modelling parameter ordinals and stamp-alias field names, and is
  deliberately out of scope.
- The tests assert persisted catalog rows, not call counts, except where a call count is itself the
  discriminator (the `host.calls == 3` fast-path check and the raising
  `_forbidden_control_read` reader).

### Todos

No implementation scope is opened by this module. Production source
([terminal_liveness.py](../src/agents_remember/serving/terminal_liveness.py.md)) is byte-identical to
its base; a future change there is caught by these cases rather than being required by them.

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory root, and these claims concern
this repository's own test fixtures and assertions, so the exact retained source is the direct
evidence.

No external domain claim is required.

### Repo-Internal References

- The production module whose authority boundary this suite pins; imports `record_turn_projection` and writes pane readings only to `control_raw["paneDiagnostic"]`. [1]
- The shared fixtures this module imports instead of rebuilding — clock, host double, row builder, adapter snapshots. [2]
- The canonical adapter snapshot contract whose `ControlState` includes the `disconnected`/`failed` values the readiness case drives. [3]
- The non-pane compatibility projection the legacy case pins (control `unsupported`, activity `unknown`, acceptance `unsupported`). [4]
- The pane classifier whose output may only become a diagnostic. [5]
- The state-signal eligibility rule the suite leaves dependent on canonical outcome plus a non-null terminal-evidence identity. [6]
- The lane registration the fail-closed manifest requires for this module. [7]
- The requirement contract this suite is the executable evidence for: requirement packet `LOCR-R27@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it. [8]
- The lane registration the fail-closed manifest requires for this module. [9]
- The pane-authority requirement this suite is the executable evidence for. [10]

### Cross-Repo References

This card establishes in-repository test behavior, not a separate cross-repository protocol or live
installation.

No external evidence is needed for these assertions.
