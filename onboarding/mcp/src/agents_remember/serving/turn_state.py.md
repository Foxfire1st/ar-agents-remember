# mcp/src/agents_remember/serving/turn_state.py

| Field                  | Value                                              |
| ---------------------- | ----------------------------------------------------- |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/serving/turn_state.py`         |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-08T02:43+02:00                                  |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`|
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`turn_state.py` classifies a captured tmux pane's text into a live turn-state (260707-HFX-L8, issue
#4): `working | turn-ended | awaiting-input | stale`. This is the "the rail tells the truth about
what every seat is doing right now" primitive — the same "model ended its turn" / "waiting on you"
signal a developer would read off a raw tmux/cmux pane, surfaced onto the catalog row instead of
requiring anyone to attach.

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

**`boot_ready(pane_text, *, harness=None) -> bool`** (260707-HFX2-L3, R2): the per-harness delivery
adapter's boot-readiness signature (the P-5 window) — has the composer rendered ANY recognizable
state yet? A thin composition, not a new marker table: `True` whenever `classify_turn_state(...)
.state != "stale"` (working/awaiting-input/turn-ended all count as "the composer has mounted
something"; only `stale` — no marker matched at all — means "still booting, nothing to read yet").
Consumed by `harness_adapters.HarnessAdapter.boot_ready`.

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

### Todos

**Known accuracy gap (HFX-L8 doctrine review F1/F2 — accepted, deferred, not actionable in this
leaf):** the caller (`terminal_liveness.py::_observe_alive`) feeds this classifier the FULL
history-inclusive `tmux capture-pane -S -200` output (`terminal_paste.capture_pane`, 200 lines of
scrollback), not just the pane's current bottom. Because these are broad `.search()` regexes
matched anywhere in that window, a pane whose scrollback merely CONTAINS a marker word (e.g.
"generating" in an earlier file listing) can misclassify regardless of the seat's actual present
state — reviewer-confirmed as "systematically wrong for panes with chatty scrollback," not just
"regexes are untuned." Folded into a future live-pane calibration follow-up (classify over only the
last N/visible-viewport lines, or anchor markers to the pane tail); not this leaf's action item. The
shared marker regexes themselves are also a first-cut best-effort guess at common TUI shapes
(Design Decision 5 in the builder report), not calibrated against real captured Claude/Codex panes —
someone with live harness access should verify/tune before this ships to real dashboards.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
turn-state-classification-specific behavior; this file is same-repository runtime plumbing, and the
marker regexes are a first-cut internal heuristic (see Todos), not derived from an external spec.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines pane-marker turn-state classification; the leaf task doc's E3 example and this implementation are the source of truth. | L1-L91 | [turn_state.py](turn_state.py) |

## Repo-Internal References

`classify_turn_state` is called from exactly one place — the L5 liveness sweep's alive-observation
path — with pane text captured by `terminal_paste.capture_pane`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `_observe_alive` calls `classify_turn_state(pane_text, harness=entry.harness)` for every ALIVE `kind == "harness"` row on the existing L5 sweep cadence, feeding it `terminal_paste.capture_pane`'s history-inclusive capture (see Todos for the resulting accuracy gap). | `_observe_alive` | [terminal_liveness.py](terminal_liveness.py) |
| `capture_pane` is the shared history-inclusive `tmux capture-pane` wrapper this classifier's input comes from — the SAME view paste-verification already reads, so there is exactly one capture-command shape in the codebase. | `capture_pane` | [terminal_paste.py](terminal_paste.py) |
| The classification result is persisted via `TerminalCatalog.record_turn_state`, which returns a no-op when the state did not transition (so `_observe_alive` can detect and emit an observer event only on an actual change). | `record_turn_state`; `with_turn_state` | [terminal_catalog.py](terminal_catalog.py) |
| `Harness.id` is the key namespace the per-harness override dicts are keyed by, even though every override dict is currently empty. | `Harness` | [harnesses.py](harnesses.py) |
| Failing-first tests for classification precedence (busy > awaiting-input > turn-ended > stale), each marker family, and the empty-per-harness-override fallback, from scripted pane-text fixtures. | `TurnStateClassificationTests` | [../../../tests/test_seat_lifecycle.py](../../../tests/test_seat_lifecycle.py) |
| `boot_ready` is composed into the one delivery adapter interface's `boot_ready` method, alongside `pane_signals.composer_state`/`classify_pane_signal`. | `HarnessAdapter.boot_ready` | [harness_adapters.py](harness_adapters.py.md) |
| `classify_turn_state` is also reused by `HarnessAdapter.turn_started` (post-submit confirmation: a busy/spinner marker in the post-submit capture corroborates a turn start even before the generic pane-advance diff fires). | `HarnessAdapter.turn_started` | [harness_adapters.py](harness_adapters.py.md) |
| Boot/ready/mid-turn/chip-stacked/quota-modal fixtures for both known harnesses, exercised through the adapter (not this module directly). | `ClaudeCodeAdapterTests`; `CodexAdapterTests` | [../../../tests/test_harness_adapters.py](../../../tests/test_harness_adapters.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local turn-state classifier. | — | — |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## Update History
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
