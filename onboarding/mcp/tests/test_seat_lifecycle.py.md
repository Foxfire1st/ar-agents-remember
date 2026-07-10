# test_seat_lifecycle.py

| Field                  | Value                                     |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                               |
| path                   | `mcp/tests/test_seat_lifecycle.py`            |
| doc_type               | `file-level-onboarding`                       |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814`                                 |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_seat_lifecycle.py` is the failing-first + regression suite for seat lifecycle behavior:
retirement authority/manual retire, landed completion classification, live identity/rename, and
live turn-state. It covers the retire authority matrix, the `session_retire`/`session_rename` MCP
tools end-to-end, turn-state classification from scripted pane fixtures, the terminal-mark vs.
liveness-hysteresis interplay, and the `worktree_integrate`/`lifecycle_finalize_task` auto-land
hooks (including the best-effort guard that prevents a landing failure from failing an already
succeeded completion edge).

## Code Commentary

### 260707-HFX2-L17 Pair Retirement Regressions

The authority matrix now uses binding leaf/role, covers manager retirement of own-master pipeline
roles, and proves an unbound failed dispatch resolves its master through `replacementForLeaf`.
Owner-never-self-retires and portfolio authority remain pinned.

### Logic

Shared fixtures: `_config(root, **retirement_overrides)` builds a minimal `McpRuntimeConfig` with
an overridable `RetirementSettings`; `_entry(session_id, *, leaf_key, spawn_role, status, kind)`
builds a `TerminalCatalogEntry` with sane defaults (`kind="harness"`, `status="running"`); `_get`
asserts a catalog row exists and returns it; `_FakeHost` is a minimal `terminate`-capable stand-in
so retirement tests never need a real tmux server.

Test classes, in file order:

- **`RetirePolicyMatrixTests`** — pure `check_retire_authority` unit tests: manager retires own
  worker/reviewer ✓; refused against another master's worker or another manager (message contains
  `"own master"`); self-retire refused FIRST regardless of role confusion (message contains `"never
  retires itself"`); orchestrator retires any role incl. a completed manager; unprivileged role
  refused (`"no retire authority"`); `master_of` segment extraction incl. `None`/empty-string edge
  cases.
- **`SessionRetireToolTests`** — `session_retire_payload` end-to-end against a real temp-file
  catalog (patches `TerminalCatalog`/`TerminalHost` construction inside `mcp.tools.terminal`):
  unknown target/actor → `unknown-session`/`unknown-actor`; manager retires own worker → `retired`
  with full provenance persisted to the catalog row; cross-master refusal → `retire-refused`,
  target untouched (`status` stays `"running"`); self-retire refused; idempotent re-retire →
  `already-retired`, provenance from the FIRST call preserved even when a second call passes a
  different `reason`; orchestrator retires a manager.
- **`SessionRenameToolTests`** — `session_rename_payload`: unknown session refused; FIRST rename
  freezes `spawned_label` to the pre-rename label and is immediately visible via `entry.to_json()`
  (projection); SECOND rename changes `label` but never overwrites the frozen `spawned_label`;
  rename never touches `spawn_role` (L6 immutability, asserted directly on the persisted entry);
  renaming an already-`terminated` session is refused (`unknown-session`).
- **`TurnStateClassificationTests`** — `classify_turn_state` against scripted pane-text strings:
  busy marker (`"esc to interrupt"`) and spinner glyph both → `working`; confirmation prompt →
  `awaiting-input`; idle `>` prompt → `turn-ended`; empty string, `None`, and an unrecognized-shape
  string all → `stale`; a busy marker anywhere in the text wins over an idle-shaped marker
  elsewhere in the SAME capture (precedence proof).
- **`TurnStateSweepWiringTests`** — `observe_terminal_liveness` with an injected `pane_capturer`:
  an alive `kind="harness"` row gets classified AND `turn_state_changed=True` on first
  classification; a `kind="terminal"` (plain shell) row is NEVER classified — asserts `turn_state`
  stays `None` and the capturer is never even called (`calls == []`), proving the "plain terminals
  are never classified" invariant at the capture-call level, not just the result level.
- **`TerminalMarkVsLivenessInterplayTests`** — a retired row stays `status="terminated"` after a
  SUBSEQUENT alive `record_liveness_probe` (hysteresis never resurrects a retire); retiring an
  already-`terminated` row (via a plain `/terminate`, i.e. `mark_terminated`, not a prior retire)
  never back-fills retroactive retirement provenance — `retired_at` stays `None`.
- **`LandSeatsForLeafTests`** — `land_seats_for_leaf` role/leaf-key scoping: lands only rows
  matching BOTH `leaf_key` and `roles`, leaves a manager row and a different-leaf worker row
  untouched, records landing provenance, and skips already-terminated seats.
- **`AutoLandHookIntegrationTests`** — the completion-edge wiring in
  `controllers/worktree_tools.py`, built around a fake `WorktreeContract` and mocked
  `git_worktree_manager.integrate_result`/`finalize_result`: `worktree_integrate_tool` auto-lands
  worker+reviewer seats (manager untouched) and reports them in `autoLandedSeats`; skipped when
  `auto_land_on_integration=False` (key absent from the result entirely, not an empty list) or on a
  `dry_run` (same absent-key shape); `lifecycle_finalize_task_tool` auto-lands manager+reviewer
  seats; an unreadable contract (`load_contract` raising `OSError`) skips silently — `ok: True`,
  `autoLandedSeats: []`, the edge itself unblocked. Best-effort regression tests monkeypatch
  `worktree_tools.land_seats_for_leaf` itself to raise (`OSError` and `RuntimeError` respectively),
  asserting integrate/finalize still return `ok: True` with `autoLandedSeats: []` and the seeded
  catalog row untouched.
- **`RetirementSettingsConfigTests`** — `RetirementSettings()` defaults: both
  `auto_land_on_integration`/`auto_land_on_finalize` default `True`.

### Conventions

Plain `unittest.TestCase` classes (not pytest fixtures), matching the repo's dominant test style.
Each stateful test class uses a `tempfile.TemporaryDirectory()` per test in `setUp`/`tearDown`
rather than a shared fixture, so catalog file state never leaks between tests.

### Invariants And Boundaries

This file tests behavior across the seat lifecycle source files (`retire_policy.py`, `retire.py`,
`landing.py`, `turn_state.py`, `terminal_catalog.py`, `terminal_liveness.py`, and
`controllers/worktree_tools.py`'s auto-land hooks) plus the `session_retire`/`session_rename` MCP
tool payloads and `RetirementSettings` config parsing.

### Todos

No known follow-up in this file.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation; this is a
same-repository unit/integration test file with no external-standard dependency.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document governs this test shape; the leaf task doc's failing-first requirement list is the source of truth for coverage scope. | L1-L743 | [test_seat_lifecycle.py](test_seat_lifecycle.py) |

## Repo-Internal References

This suite directly exercises five source files and the leaf task doc's requirement list.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `RetirePolicyMatrixTests` exercises `check_retire_authority`/`master_of`/`RetirePolicyError` directly. | `RetirePolicyMatrixTests` | [../src/agents_remember/serving/retire_policy.py](../src/agents_remember/serving/retire_policy.py) |
| `LandSeatsForLeafTests` exercises `land_seats_for_leaf` directly. | `LandSeatsForLeafTests` | [../src/agents_remember/serving/landing.py](../src/agents_remember/serving/landing.py) |
| `TurnStateClassificationTests` exercises `classify_turn_state` directly. | `TurnStateClassificationTests` | [../src/agents_remember/serving/turn_state.py](../src/agents_remember/serving/turn_state.py) |
| `TurnStateSweepWiringTests` exercises `observe_terminal_liveness`'s alive-classification path with an injected `pane_capturer`. | `TurnStateSweepWiringTests` | [../src/agents_remember/serving/terminal_liveness.py](../src/agents_remember/serving/terminal_liveness.py) |
| `TerminalMarkVsLivenessInterplayTests` exercises `mark_retired`/`record_liveness_probe` interplay on `TerminalCatalog` directly. | `TerminalMarkVsLivenessInterplayTests` | [../src/agents_remember/serving/terminal_catalog.py](../src/agents_remember/serving/terminal_catalog.py) |
| `AutoLandHookIntegrationTests` exercises `worktree_integrate_tool`/`lifecycle_finalize_task_tool`/`_auto_land_completed_seats` including the best-effort landing guard. | `AutoLandHookIntegrationTests` | [../src/agents_remember/controllers/worktree_tools.py](../src/agents_remember/controllers/worktree_tools.py) |
| `RetirementSettingsConfigTests` exercises `RetirementSettings` defaults (config parsing itself is covered separately in `test_config.py::RetirementSettingsTests`). | `RetirementSettingsConfigTests` | [../src/agents_remember/mcp/config.py](../src/agents_remember/mcp/config.py) |
| `SessionRetireToolTests`/`SessionRenameToolTests` exercise `session_retire_payload`/`session_rename_payload` end-to-end. | `SessionRetireToolTests`; `SessionRenameToolTests` | [../src/agents_remember/mcp/tools/terminal.py](../src/agents_remember/mcp/tools/terminal.py) |
| The leaf task doc's original failing-first requirement list this suite extends. | Requirements | [10_seat-retirement-and-chat-cleanup.md](ar-coordination/tasks/agents-remember/260707_hotfix-orchestration-stack/10_seat-retirement-and-chat-cleanup.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary is exercised by this local test suite. | — | — |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: converted retirement tests to pair identity and added
  unbound failed-dispatch manager cleanup coverage.

- 2026-07-09T13:36+02:00 — 260707-HFX2-L11 round 2: removed the direct
  `retire_seats_for_leaf` tests with the deleted helper, documented the current `LandSeatsForLeafTests`
  and `AutoLandHookIntegrationTests`, and kept manual retire/authority coverage unchanged.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-08T02:43+02:00 — Created for 260707-HFX-L8 (seat lifecycle: retirement + live chat
  identity, status, turn-state): the consolidated failing-first + regression suite (45 tests / 5
  subtests per the builder report) covering the retire authority matrix, `session_retire`/
  `session_rename` MCP tools, turn-state classification + L5-sweep wiring, terminal-mark vs.
  liveness interplay, and the integrate/finalize auto-retire automation hooks incl. the R2/F1
  exception-guard-widening regression tests. Verification metadata pinned until closeout stamps the
  HFX-L8 commit.
