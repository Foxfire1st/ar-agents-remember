# mcp/src/agents_remember/serving/turn_state.py

| Field                  | Value                                              |
| ---------------------- | ----------------------------------------------------- |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/serving/turn_state.py`         |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-08T02:43+02:00                                  |
| lastVerifiedCommitHash | `a3e43cb0877c18b9d2b0e6ada4eb5719a01f251f`|
| lastVerifiedCommitDate | 2026-08-06T05:49:07+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`turn_state.py` classifies captured tmux pane text into a diagnostic turn-state (260707-HFX-L8,
issue #4): `working | turn-ended | awaiting-input | stale`. It is observation evidence for the
liveness path, not authoritative readiness, delivery, liveness, or action state; adapter snapshots
and catalog state remain the authority a reader sees.

## Code Commentary

### Logic

`classify_turn_state(pane_text, *, harness=None)` returns a `TurnStateClassification(state,
evidence)` frozen dataclass. Precedence, checked in order, first match wins:
1. **Blank/`None` pane_text → `stale`, `evidence=None`.** The same evidence-less case the
   spawn-delivery paster already treats specially — nothing to read a turn signal off of.
2. **Working (busy)** — `_WORKING_PATTERNS`: `"esc to interrupt"`, `"esc to cancel"`, `"thinking"`,
   `"generating"` (all word-boundary, case-insensitive), and a braille spinner glyph range
   (`[⠁-⣿]`, common TUI spinner block). Checked FIRST among the content patterns so a transient busy
   marker inside an otherwise-idle-looking pane never misclassifies as turn-ended.
3. **Awaiting-input (blocked-on-you)** — `_AWAITING_INPUT_PATTERNS`: `"do you want to"`, `"(y/n)"`,
   `"allow...?"`, `"proceed?"`, `"press enter to continue"`. Distinct from "turn ended with nothing
   further expected".
4. **Turn-ended (idle-ready)** — `_TURN_ENDED_PATTERNS`: a bare `>` prompt line (with or without a
   box-drawing `│` border), or the word `"ready"`.
5. **Fallback → `stale`.** No marker matched at all — an unrecognized pane shape, not necessarily an
   error.

Each pattern family has a matching empty per-harness override dict
(`_HARNESS_WORKING_PATTERNS`/`_HARNESS_AWAITING_INPUT_PATTERNS`/`_HARNESS_TURN_ENDED_PATTERNS`,
keyed by `Harness.id`) checked BEFORE the shared generic patterns for that family — currently empty
for every known harness (every harness classifies off the shared markers), wired and ready for a
future harness with a distinctive pane shape to add its own table without touching the classifier
itself.

### Conventions

Deliberately marker-based (regex `.search()` over captured text), not a terminal-control-sequence
parser — cheap enough to run on the EXISTING L5 liveness-sweep cadence, never a new hot loop or a
new tmux round-trip. Per-harness marker tables are declared HERE, not in `harnesses.py`: they are
pane-TEXT patterns, an orthogonal concern to that registry's launch-argv/knob-mapping tables.

### Invariants And Boundaries

- Fail-safe by construction: every code path returns a `TurnStateClassification`, never raises —
  blank/unreadable/unrecognized input all resolve to `stale` rather than propagating an exception
  into the L5 sweep.
- Classification is stateless and pure (no I/O, no catalog access) — the caller
  (`terminal_liveness.py::_observe_alive`) is responsible for capturing the pane text and persisting
  the result.
- Pane markers are diagnostic only: they cannot authorize boot readiness, delivery, liveness,
  or actions, and adapter snapshots remain authoritative for those decisions.

### Todos

**Diagnostic boundary (HFX-L8 doctrine review F1/F2):** the liveness caller may provide a
history-inclusive capture, so marker matches are evidence only and must not authorize readiness,
delivery, liveness, or actions. Harness-specific tail-sensitive handling and adapter snapshots
remain the authority for live decisions; marker calibration is a separate follow-up.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
turn-state-classification-specific behavior; this file is same-repository runtime plumbing, and the
marker regexes are a first-cut internal heuristic (see Todos), not derived from an external spec.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

`classify_turn_state` is called from exactly one place — the L5 liveness sweep's alive-observation
path — with pane text captured by `terminal_paste.capture_pane`.

| Finding | Anchor | Source |
| --- | --- | --- |
| `_observe_alive` records the pane classification; adapter snapshots remain authoritative for persisted state. | `_observe_alive` | mcp/src/agents_remember/serving/terminal_liveness.py:327-393 |
| The terminal-paste module defines the shared history-inclusive `capture_pane` wrapper and its bounded history argv supplying classifier input. | "def capture_pane"; `_capture_pane_argv`; `_CAPTURE_HISTORY_LINES` | mcp/src/agents_remember/serving/terminal_paste.py:40-40; mcp/src/agents_remember/serving/terminal_paste.py:181-182; mcp/src/agents_remember/serving/terminal_paste.py:201-201 |
| The classification result is persisted via `TerminalCatalog.record_turn_state`, with `with_turn_state` producing the catalog copy. | `record_turn_state`; `with_turn_state` | mcp/src/agents_remember/serving/terminal_catalog.py:419-423; mcp/src/agents_remember/serving/terminal_catalog.py:714-728 |
| The per-harness marker override tables are keyed by the supplied harness id in `turn_state`, with keyed lookups tried before shared patterns. | `_classify_by_marker_tables`; "key = harness or \"\""; "_HARNESS_WORKING_PATTERNS.get(key,"; "_HARNESS_AWAITING_INPUT_PATTERNS.get(key,"; "_HARNESS_TURN_ENDED_PATTERNS.get(key," | mcp/src/agents_remember/serving/turn_state.py:140-154 |
| Tests cover classification precedence, marker families, and the empty per-harness override fallback from scripted pane-text fixtures. | `TurnStateClassificationTests` | mcp/tests/test_seat_lifecycle.py:374-464 |
| The adapter exposes diagnostic `blocked_reason`; pane classification does not provide a boot-readiness authority method. | `HarnessAdapter`; `blocked_reason` | mcp/src/agents_remember/serving/harness_adapters.py:14-25 |
| Adapter tests pin stable known/generic classification and keep `blocked_reason` diagnostic-only. | `test_known_and_generic_adapters_are_stable`; `test_blocked_reason_is_failure_diagnostic_only` | mcp/tests/test_harness_adapters.py:11-15; mcp/tests/test_harness_adapters.py:18-25 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## 260731-EFA-L2 Current Delta

Classification was decomposed into named strategies, with the precedence rule stated once:

- `_first_matching_state(...)` — walk a precedence-ordered marker ladder; **the first pattern that
  fires names the state**.
- `_classify_codex_pane(pane_text)` — classify Codex off the live pane **TAIL only**.
- `_classify_by_marker_tables(pane_text, harness)` — classify any harness off the shared marker
  tables, with per-harness overrides applied first.

The marker tables, their precedence and the resulting `TurnStateClassification` values are
unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-04T14:17+02:00 — 260731-EFA-L6 S18-B13 curator: closed D11 complete marker-table lookup construct evidence for the same-reviewer residual delta.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `_first_matching_state` / `_classify_codex_pane` / `_classify_by_marker_tables` split; marker tables and precedence unchanged.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-08T22:30+02:00 — 260707-HFX2-L3 (paste injector hardening, R2): added `boot_ready`, a thin
  composition over `classify_turn_state` (ready = state != "stale") — the per-harness delivery
  adapter's boot-readiness signature. No change to `classify_turn_state` itself or its precedence;
  the accuracy-gap Todo above is unchanged/unactioned. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L3 commit.
- 2026-07-08T02:43+02:00 — Created for 260707-HFX-L8 (live identity + turn-state, issue #4): the
  marker-based turn-state classifier — `classify_turn_state`, `TurnStateClassification`, the
  precedence-ordered pattern tables (working > awaiting-input > turn-ended > stale) plus empty
  per-harness override dicts. Rides the existing L5 liveness-sweep cadence via
  `terminal_liveness.py::_observe_alive`, never a new hot loop. Doctrine-review F2 (accepted,
  deferred): the caller feeds this classifier the full 200-line history-inclusive capture rather
  than the pane tail, so scrollback text can misclassify — folded into a future calibration
  follow-up, not actionable in this leaf. Verification metadata pinned until closeout stamps the
  HFX-L8 commit.
