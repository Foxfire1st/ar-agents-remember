# mcp/src/agents_remember/serving/harness_adapters.py

| Field                  | Value                                                     |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/serving/harness_adapters.py`       |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-07-08T22:30+02:00                                      |
| lastVerifiedCommitHash | `75587f00070ae0903e42a2a677c51c3125eb7188`                  |
| lastVerifiedCommitDate | 2026-07-08T08:46:23+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Created for 260707-HFX2-L3 (paste injector hardening, R2): the ONE per-harness adapter interface
`serving/injector.py` reads through to decide whether/how to deliver a paste. Developer ruling
(2026-07-07T22:45, verbatim): "As injector we will then use the paste into chat method. It's the
one that is harness independent as long as you get its method right." This module is where "get its
method right" lives — boot-readiness, composer state, mid-turn behavior, modal dialog traps
(codex quota #20, permission prompts), and post-submit turn-started confirmation, each per-harness
(claude-code, codex) but behind one shared interface.

## Code Commentary

### Logic

`HarnessAdapter` is a frozen dataclass holding only `harness_id: str | None`; every method is a
THIN COMPOSITION over the existing pane classifiers, parameterized by that id — there is no
subclass per harness and no if/elif ladder here:

- `boot_ready(pane_text)` → `turn_state.boot_ready(pane_text, harness=harness_id)`.
- `composer_state(pane_text)` → `pane_signals.composer_state(pane_text, harness=harness_id)`.
- `mid_turn(pane_text)` → `pane_signals.classify_pane_signal(...).signal == "mid-turn"`.
- `mid_turn_behavior(pane_text)` → `"queued-next-turn"` when mid-turn, else `None` (both known
  harnesses queue a paste sent while generating as next-turn input; a typed slot for a future
  harness that behaves differently, not a branch that exists yet).
- `blocked_reason(pane_text)` → `None` unless `classify_pane_signal(...).signal == "blocked"`, in
  which case `pane_signals.blocked_reason_label(evidence)` (`"codex-quota-limit"` /
  `"permission-prompt"` / `"modal-dialog"`).
- `turn_started(capture, *, advanced)` → `True` if `advanced` (the paster's own generic pane-advance
  diff already fired), else falls back to `turn_state.classify_turn_state(capture, harness=
  harness_id).state == "working"` — a busy/spinner marker in the capture corroborates a turn start
  even in the single poll window before the byte-diff visibly fires.

`get_adapter(harness_id)` returns `GENERIC_ADAPTER` for `None`, the named `CLAUDE_CODE_ADAPTER` /
`CODEX_ADAPTER` for `"claude"`/`"codex"` (identity-preserving, useful for tests), or a fresh
`HarnessAdapter(harness_id=harness_id)` for any other id — an uncustomized/unknown harness still
classifies correctly off the shared marker tables (never a refusal).

### Conventions

Owns NO regex table of its own. Every pattern lives where the codebase's existing convention
already puts per-harness pane-text overrides: `pane_signals.py` (`_HARNESS_BLOCKED_PATTERNS`,
`_HARNESS_EMPTY_COMPOSER_PATTERNS`) and `turn_state.py` (`_HARNESS_WORKING_PATTERNS`,
`_HARNESS_AWAITING_INPUT_PATTERNS`, `_HARNESS_TURN_ENDED_PATTERNS`), both `dict[harness_id,
patterns]` checked before the shared generic patterns for that family. Adding a harness here means
the id flows through to those tables — the module docstring carries the full NEW-HARNESS CHECKLIST.

### Invariants And Boundaries

- R4 non-goals (developer-ruled): harness hooks, Agent SDK sessions, and the codex app-server
  protocol are NOT delivery channels this adapter (or `injector.py`) ever reads through.
- `HarnessAdapter` is stateless/pure — no I/O, no catalog access; every method is a function of the
  pane text (+ harness id) passed in.
- A future harness never touches this file's logic, only its pattern-table dependencies (see
  Conventions) and, optionally, `_ADAPTERS` for a named instance (not required — the fallback path
  already works).

### Todos

Same first-cut caveat as `pane_signals.py`/`turn_state.py`: the underlying marker regexes are a
best-effort guess at common TUI shapes, not calibrated against real captured Claude/Codex panes.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
per-harness delivery-adapter behavior; this file is same-repository runtime plumbing (the leaf task
doc's R2 is the source of truth), same posture as `pane_signals.py`/`turn_state.py`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines a per-harness delivery adapter; the leaf task doc (R2) and this implementation are the source of truth. | whole module | [harness_adapters.py](harness_adapters.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `get_adapter` is the sole entry point `serving.injector.deliver` calls to resolve per-harness behavior for the blocked-check and post-submit-confirmation corroboration. | `deliver` | [injector.py](injector.py.md) |
| `boot_ready`/`composer_state` compose `turn_state.classify_turn_state`/`turn_state.boot_ready` and `pane_signals.classify_pane_signal`/`pane_signals.composer_state`/`pane_signals.blocked_reason_label` — the single source of truth for every pattern table. | `classify_turn_state`; `boot_ready` | [turn_state.py](turn_state.py.md) |
| | `classify_pane_signal`; `composer_state`; `blocked_reason_label` | [pane_signals.py](pane_signals.py.md) |
| Fixtures for both harnesses across boot/ready/mid-turn/chip-stacked/quota-modal, plus the registry fallback behavior. | whole module | [../../../tests/test_harness_adapters.py](../../../tests/test_harness_adapters.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local delivery adapter. | — | — |

## Update History

- 2026-07-08T22:30+02:00 — Created for 260707-HFX2-L3 (paste injector hardening, R2): the one
  per-harness adapter interface — `HarnessAdapter` (boot_ready, composer_state, mid_turn,
  mid_turn_behavior, blocked_reason, turn_started), `get_adapter` registry with graceful fallback,
  named `CLAUDE_CODE_ADAPTER`/`CODEX_ADAPTER`/`GENERIC_ADAPTER` instances, and the NEW-HARNESS
  CHECKLIST docstring (R4: a future harness is one adapter registration, never a new delivery path).
  Composes existing classifiers only; adds no new pattern table of its own. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L3 commit.
