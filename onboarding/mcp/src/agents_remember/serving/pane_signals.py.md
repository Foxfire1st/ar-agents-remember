# mcp/src/agents_remember/serving/pane_signals.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/src/agents_remember/serving/pane_signals.py` |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-07-08T18:45+02:00                             |
| lastVerifiedCommitHash | `75587f00070ae0903e42a2a677c51c3125eb7188`         |
| lastVerifiedCommitDate | 2026-07-08T08:46:23+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`pane_signals.py` is the supervisor sweep's pane-state classifier (260707-HFX2-L2, R2a): the P-15
fixture-zoo predicate that answers, mechanically, which of the pilot run's four intervention
triggers a captured harness pane shows right now — `never-briefed` (empty composer post-boot,
P-5/P-14), `delivery-stalled` (≥2 stacked un-consumed paste chips, the F-V duplicate-paste class),
`mid-turn` (an "esc to interrupt"-style marker — actively generating, do not intervene), `blocked`
(a modal confirmation/permission dialog, issue #20), or `normal` (no trigger). It is deliberately a
separate classifier from `turn_state.py`'s `classify_turn_state`: that module answers the L8
catalog's own UI question (`working`/`turn-ended`/`awaiting-input`/`stale`), while this one answers
the supervisor's distinct action-triggering question over the same raw pane text.

## Code Commentary

### Logic

`classify_pane_signal(pane_text, *, harness=None)` returns a frozen `PaneSignalClassification(signal,
evidence)`. Blank/`None` pane text classifies as `normal` (no evidence of any trigger — an
unreadable/vanished pane is a liveness concern for `evaluate_seat_liveness_findings` in
`supervisor.py`, not a pane-signal one). Precedence, first match wins:

1. **mid-turn** — `_MID_TURN_PATTERNS` ("esc to interrupt", "esc to cancel"). Checked FIRST so an
   actively-generating pane is never misread as blocked or stalled by an incidental scrollback
   marker.
2. **blocked** — `_BLOCKED_PATTERNS` ("do you want to", "(y/n)", "allow...?", "proceed?", "press
   enter to continue").
3. **delivery-stalled** — reuses `terminal_paste.count_paste_chips` (no re-implementation of chip
   counting); fires at `STACKED_CHIP_THRESHOLD` (2) or more, independent of composer prompt shape.
4. **never-briefed** — `_EMPTY_COMPOSER_PATTERNS` (a bare `>` or boxed `│ > │` prompt line with
   nothing else). Checked LAST among the marker families: a blank composer under a mid-turn or
   blocked marker is whatever fired first, not "never-briefed".
5. **normal** — nothing matched.

Per-harness override tables (`_HARNESS_MID_TURN_PATTERNS`/`_HARNESS_BLOCKED_PATTERNS`/
`_HARNESS_EMPTY_COMPOSER_PATTERNS`) mirror `turn_state.py`'s pattern exactly. 260707-HFX2-L3 (R2)
populated `_HARNESS_BLOCKED_PATTERNS["codex"]` with the issue #20 quota/rate-limit modal markers
("approaching rate limits", "switch model?", "hit your usage limit", "usage limit") — every other
family/harness combination is still empty and classifies off the shared markers; an unknown or
uncustomized harness still gets a best-effort signal via the shared tables (checked before them per
family, so a future per-harness entry can override without touching the classifier body).

**`blocked_reason_label(evidence)`** (260707-HFX2-L3, R2): a pure lookup, not a re-scan — maps the
`evidence` regex-source string a `"blocked"` classification already carries onto a structured
NEEDS-ATTENTION reason: `"codex-quota-limit"` when the evidence text mentions a rate/usage-limit
marker, else `"permission-prompt"` (or `"modal-dialog"` for `evidence=None`). Never reads pane text
again — reuses the same evidence `classify_pane_signal` already computed.

**`composer_state(pane_text, *, harness=None) -> ComposerState`** (260707-HFX2-L3, R2): the delivery
adapter's composer-state signature — `"empty"` / `"has-content"` / `"chip-stacked"`. Reuses this
module's own `STACKED_CHIP_THRESHOLD` and `_EMPTY_COMPOSER_PATTERNS`/per-harness override rather
than a second pattern table; blank/`None` text is `"empty"`.

### Conventions

Marker-based regex `.search()` over captured text, the same cheap, no-parser posture
`turn_state.py` uses — this classifier is meant to run on the supervisor's own sweep cadence
(default ~10s), not a hot loop.

### Invariants And Boundaries

- Fail-safe by construction: every input (including blank/`None`) resolves to a
  `PaneSignalClassification`, never raises.
- Pure and stateless — no I/O, no catalog access; the caller
  (`supervisor.py::evaluate_pane_findings`) captures the pane text and interprets the result.
- Precedence is load-bearing and intentionally asymmetric from `turn_state.py`'s own precedence
  (mid-turn > blocked > delivery-stalled > never-briefed > normal here, vs. working > awaiting-input
  > turn-ended > stale there) — the two classifiers answer different questions over the same text
  and must not be conflated or merged.
- Per-harness override dicts are declared HERE (pane-text patterns), not in `harnesses.py`
  (launch-argv/knob-mapping) — same separation-of-concerns rule `turn_state.py` documents for its
  own override tables.

### Todos

Same first-cut caveat as `turn_state.py`: the shared marker regexes are a best-effort guess at
common TUI shapes (builder report Design Decision 5), not calibrated against real captured
Claude/Codex panes. Whoever tunes `turn_state.py`'s markers against live harness access should tune
these alongside it, since both classifiers read the same captured text.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
pane-signal-classification-specific behavior; this file is same-repository runtime plumbing (the
leaf task doc's R2a is the source of truth), same posture as `turn_state.py`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines pane-signal classification; the leaf task doc (R2a) and this implementation are the source of truth. | L1-L101 | [pane_signals.py](pane_signals.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `classify_pane_signal` is called from exactly one place — `evaluate_pane_findings`, the R2a predicate over every `RUNNING` `kind == "harness"` catalog row, passed each row's captured pane text and `entry.harness`. | `evaluate_pane_findings` | [supervisor.py](supervisor.py.md) |
| `count_paste_chips` is the shared chip-counting helper this classifier's delivery-stalled trigger reuses rather than re-implementing (the same F-V/N1 duplicate-paste diagnostic `terminal_paste.py` already owns). | `count_paste_chips` | [terminal_paste.py](terminal_paste.py.md) |
| `classify_turn_state` is the SEPARATE L8 UI-state classifier over the same captured pane text — distinct precedence, distinct question, deliberately not merged (see Invariants). | `classify_turn_state` | [turn_state.py](turn_state.py.md) |
| Failing-first unit tests for every trigger family plus the empty-per-harness-override fallback, from scripted pane-text fixtures. | `PaneSignalClassifierTests` | [../../../tests/test_pane_signals.py](../../../tests/test_pane_signals.py.md) |
| `composer_state` and `blocked_reason_label` are composed into the one per-harness delivery adapter interface (`HarnessAdapter.composer_state` / `.blocked_reason`); `classify_pane_signal` itself is reused there too (`.mid_turn`, `.blocked_reason`). | `HarnessAdapter` | [harness_adapters.py](harness_adapters.py.md) |
| The R1 delivery contract (`serving/injector.deliver`) reads `HarnessAdapter.blocked_reason` off the FINAL paste capture to classify a modal trap as `blocked(reason)` rather than a bare failed/delivered boolean. | `deliver` | [injector.py](injector.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local pane-signal classifier. | — | — |

## Update History

- 2026-07-08T22:30+02:00 — 260707-HFX2-L3 (paste injector hardening, R2): populated
  `_HARNESS_BLOCKED_PATTERNS["codex"]` with the issue #20 quota/rate-limit modal markers; added
  `blocked_reason_label` (evidence → structured NEEDS-ATTENTION reason) and `composer_state`
  (`empty`/`has-content`/`chip-stacked`) as the two new signatures the per-harness delivery adapter
  (`harness_adapters.py`) composes. No change to `classify_pane_signal`'s own precedence or the
  existing empty per-harness tables for other families. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L3 commit.
- 2026-07-08T18:45+02:00 — Created for 260707-HFX2-L2 (supervisor sweep + predicates, R2a): the
  pane-state classifier — `classify_pane_signal`, `PaneSignalClassification`, the
  precedence-ordered marker tables (mid-turn > blocked > delivery-stalled > never-briefed > normal)
  plus empty per-harness override dicts, reusing `terminal_paste.count_paste_chips` for the
  delivery-stalled trigger. Feeds `supervisor.py::evaluate_pane_findings` on the sweep's own
  cadence, never a hot loop. Verification metadata pinned until closeout stamps the
  260707-HFX2-L2 commit.
