# mcp/src/agents_remember/serving/pane_signals.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/src/agents_remember/serving/pane_signals.py` |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-08-02T01:42+02:00                             |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb`         |
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`pane_signals.py` is the supervisor's narrow failure/intervention classifier. After
260707-HFX2-L15 it recognizes only `mid-turn`, `blocked`, and `normal`; empty-composer
`never-briefed`, stacked-chip `delivery-stalled`, and composer-state APIs were removed because pane
rendering is not dispatch-acceptance evidence. Submitted delivery is verified in harness JSONL.

## Code Commentary

### 260707-HFX2-L15 Current Logic

`classify_pane_signal` is pure and precedence-ordered: mid-turn markers suppress intervention,
then generic/per-harness modal markers yield `blocked`, otherwise the result is `normal`. Blank
panes are `normal` here and remain a separate liveness concern. `blocked_reason_label` maps the
already-matched modal evidence to `codex-quota-limit`, `permission-prompt`, or `modal-dialog` for
failure diagnostics. No composer, paste-chip, brief-presence, or turn-start inference remains.

### Historical Pre-L15 Logic (Superseded)

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

### Current Invariants And Boundaries

- Pane classification never grants dispatch acceptance or `submitted:true`.
- `mid-turn` and `blocked` are retained for supervisor intervention/failure labeling only.
- Empty composer, paste chips, and payload visibility are not durable workflow truth.
- Harness-log record parsing belongs to `harness_logs.py`, not this regex classifier.

### Historical Invariants And Boundaries (Superseded)

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

The retained modal/mid-turn regexes are best-effort diagnostic hints. No correctness or acceptance
claim may be added on top of them.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
pane-signal-classification-specific behavior; this file is same-repository runtime plumbing (the
leaf task doc's R2a is the source of truth), same posture as `turn_state.py`.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `evaluate_pane_findings` reads the captured pane and harness before invoking the pane classifier. | "def evaluate_pane_findings(" | mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:49-49 |
| The pane classifier used by that path is `classify_pane_signal`. | `classify_pane_signal` | mcp/src/agents_remember/serving/pane_signals.py:80-97 |
| `classify_turn_state` remains a separate classifier with its own operative call and precedence over the captured pane text. | `classify_turn_state` | mcp/src/agents_remember/serving/turn_state.py:157-171 |

| The adapter exposes `blocked_reason` for final diagnostic classification; it does not expose the stale `composer_state` field. | `HarnessAdapter`; `blocked_reason` | mcp/src/agents_remember/serving/harness_adapters.py:14-25 |
| The R1 delivery contract (`serving/injector.deliver`) reads `HarnessAdapter.blocked_reason` off the FINAL paste capture to classify a modal trap as `blocked(reason)` rather than a bare failed/delivered boolean. | `deliver` | mcp/src/agents_remember/serving/injector.py:60-134 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local pane-signal classifier. | — | — |

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History
- 2026-08-04T13:47:55+02:00 — 260731-EFA-L6 S18-B11 same-reviewer correction: narrowed pane-signal call ownership, classifier comparison, test coverage, and adapter behavior to operative source spans. Verification metadata unchanged.
- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 removal round: deleted `never-briefed`,
  `delivery-stalled`, composer-state, and paste-chip dispatch grammars. Retained only mid-turn and
  blocked diagnostics; harness logs now own acceptance. Verification metadata remains pinned until
  closeout stamps the eventual L15 code commit.

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
