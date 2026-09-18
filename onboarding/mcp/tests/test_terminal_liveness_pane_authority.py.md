# mcp/tests/test_terminal_liveness_pane_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_terminal_liveness_pane_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T13:36+02:00 |
| lastVerifiedCommitHash | `a135150459f8499ba309faf0373cc3b4bf7ff852` |
| lastVerifiedCommitDate | 2026-09-18T19:58:12+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured in the resolved memory root, and these claims concern
this repository's own test fixtures and assertions, so the exact retained source is the direct
evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The production module whose authority boundary this suite pins; imports `record_turn_projection` and writes pane readings only to `control_raw["paneDiagnostic"]`. | `_observe_alive`; `_observe_control_read_failure`; `_record_adapter_turn_state` | mcp/src/agents_remember/serving/terminal_liveness.py:370-452; mcp/src/agents_remember/serving/terminal_liveness.py:472-529; mcp/src/agents_remember/serving/terminal_liveness.py:585-622 |
| The shared fixtures this module imports instead of rebuilding — clock, host double, row builder, adapter snapshots. | `_Clock`; `_FakeHost`; `_entry`; `_snapshot`; `_ready_snapshot` | mcp/tests/test_terminal_liveness.py:44-104 |
| The canonical adapter snapshot contract whose `ControlState` includes the `disconnected`/`failed` values the readiness case drives. | `AdapterSnapshot`; `ControlState` | mcp/src/agents_remember/models/conversations/control_wire.py:19-19; mcp/src/agents_remember/models/conversations/control_wire.py:126-151 |
| The non-pane compatibility projection the legacy case pins (control `unsupported`, activity `unknown`, acceptance `unsupported`). | `legacy_control_unsupported_entry` | mcp/src/agents_remember/serving/hosted_control_projection.py:72-83 |
| The pane classifier whose output may only become a diagnostic. | `classify_turn_state` | mcp/src/agents_remember/serving/turn_state.py:159-174 |
| The state-signal eligibility rule the suite leaves dependent on canonical outcome plus a non-null terminal-evidence identity. | `_state_signal_finding` | mcp/src/agents_remember/serving/state_signals.py:237-260 |
| The lane registration the fail-closed manifest requires for this module. | "mcp/tests/test_terminal_liveness_pane_authority.py" | mcp/tests/test-evidence-lanes.toml:219-219 |
| The pane-authority requirement this suite is the executable evidence for. | "Pane classification stays diagnostic-only for turn and terminal truth." | mcp/tests/test_terminal_liveness_pane_authority.py:1-7 |

## Cross-Repo References

This card establishes in-repository test behavior, not a separate cross-repository protocol or live
installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:218-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `AdapterSnapshot`; `ControlState` repointed to mcp/src/agents_remember/models/conversations/control_wire.py:126-151; mcp/src/agents_remember/models/conversations/control_wire.py:19-19. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_state_signal_finding` repointed to mcp/src/agents_remember/serving/state_signals.py:237-260. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:217-217. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-15T13:36+02:00 — 260831-LOCR-L27 curator (uncommitted change set on `ar/260831-locr-l27`,
  base `b368b661`): created this card for the new module. `LOCR-R27@v1` is a **preservation**
  obligation — its own Deliverable Evidence asks for the diagnostic/turn-authority separation to be
  proved *unchanged* — so the leaf's delivery is evidence-only and no production file moved; the
  card's current contract records the boundary and the two pane-independent transitions rather than a
  code change. Two limits are recorded deliberately. First, the split from
  `test_terminal_liveness.py` (574 lines, byte-unchanged) is a size-doctrine decision, not an
  accident: extending it in place reached 1094 lines, inside the coding-guidelines 900-1200
  "do not add without extracting" band, so the module was split out and **must not be merged back**.
  Second, the negative source guard's measured reach is recorded exactly as probed — it catches
  direct-value, keyword, dict-literal and attribute-store forms and is blind to an enclosing-`if`
  constant, positional writer arguments, and `CatalogTurnEvidence(state=…)`; those shapes stay
  behaviour-pinned, so no clause rests on the guard alone. The readiness half of the authority clause
  was the one clause found unpinned in the baseline review, and case 2 above is its fix, so the
  readiness fields are named in the contract with their production-reachable `disconnected`/`failed`
  inputs rather than left implicit. Verification metadata stays pinned until closeout stamps the leaf
  code commit.
