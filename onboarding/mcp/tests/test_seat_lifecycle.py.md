# test_seat_lifecycle.py

| Field                  | Value                                     |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                               |
| path                   | `mcp/tests/test_seat_lifecycle.py`            |
| doc_type               | `file-level-onboarding`                       |
| lastUpdated            | 2026-07-08T02:43+02:00                        |
| lastVerifiedCommitHash | `2322ffc15ef803ea29bf900beeae84de19b43019`    |
| lastVerifiedCommitDate | 2026-07-08T03:14:39+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_seat_lifecycle.py` is the failing-first + regression suite for 260707-HFX-L8 (seat
retirement, live identity/rename, live turn-state). It covers every item in the leaf task doc's
failing-first list in one file: the retire authority matrix, the `session_retire`/`session_rename`
MCP tools end-to-end, turn-state classification from scripted pane fixtures, the terminal-mark vs.
liveness-hysteresis interplay, and the `worktree_integrate`/`lifecycle_finalize_task` auto-retire
automation hooks (including the R2/F1 exception-guard-widening regression tests).

## Code Commentary

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
- **`RetireSeatsForLeafTests`** — `retire_seats_for_leaf` role/leaf-key scoping: retires only rows
  matching BOTH `leaf_key` and `roles`, leaving a manager row and a different-leaf worker row
  untouched, and calling `host.terminate` only for the retired ids; already-terminated seats are
  skipped (never re-terminated, never re-added to the returned list).
- **`AutoRetireHookIntegrationTests`** — the completion-edge wiring in
  `controllers/worktree_tools.py`, built around a fake `WorktreeContract` and mocked
  `git_worktree_manager.integrate_result`/`finalize_result`: `worktree_integrate_tool` auto-retires
  worker+reviewer seats (manager untouched) and reports them in `autoRetiredSeats`; skipped when
  `auto_retire_on_integration=False` (key absent from the result entirely, not an empty list) or on
  a `dry_run` (same absent-key shape); `lifecycle_finalize_task_tool` auto-retires manager+reviewer
  seats; an unreadable contract (`load_contract` raising `OSError`) skips silently — `ok: True`,
  `autoRetiredSeats: []`, the edge itself unblocked. **R2/F1 regression tests** (added in the fix
  round, per the doctrine review): `test_worktree_integrate_survives_a_raising_retire_seats_for_leaf`
  and `test_lifecycle_finalize_survives_a_raising_retire_seats_for_leaf` monkeypatch
  `worktree_tools.retire_seats_for_leaf` itself to raise (`OSError` and `RuntimeError` respectively
  — deliberately two different exception types to prove the guard is genuinely `Exception`-wide, not
  narrowly typed to I/O errors), asserting the integrate/finalize call still returns `ok: True` with
  `autoRetiredSeats: []` and the seeded catalog row untouched — proving the widened guard (not just
  `load_contract`) actually catches a raise from the retire body itself.
- **`RetirementSettingsConfigTests`** — `RetirementSettings()` defaults: both
  `auto_retire_on_integration`/`auto_retire_on_finalize` default `True` (spawn/cleanup symmetry is
  the happy path).

### Conventions

Plain `unittest.TestCase` classes (not pytest fixtures), matching the repo's dominant test style.
Each stateful test class uses a `tempfile.TemporaryDirectory()` per test in `setUp`/`tearDown`
rather than a shared fixture, so catalog file state never leaks between tests.

### Invariants And Boundaries

This file tests behavior across FIVE source files (`retire_policy.py`, `retire.py`,
`turn_state.py`, `terminal_catalog.py`'s new methods, `controllers/worktree_tools.py`'s auto-retire
hooks) plus the `session_retire`/`session_rename` MCP tool payloads and `RetirementSettings` config
parsing — it is intentionally the single consolidated suite for the whole leaf rather than one file
per source module, matching the leaf task doc's own framing of the failing-first list as one set.

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
| `RetireSeatsForLeafTests` exercises `retire_seats_for_leaf` directly; `SessionRetireToolTests` exercises it indirectly through `session_retire_payload`. | `RetireSeatsForLeafTests` | [../src/agents_remember/serving/retire.py](../src/agents_remember/serving/retire.py) |
| `TurnStateClassificationTests` exercises `classify_turn_state` directly. | `TurnStateClassificationTests` | [../src/agents_remember/serving/turn_state.py](../src/agents_remember/serving/turn_state.py) |
| `TurnStateSweepWiringTests` exercises `observe_terminal_liveness`'s alive-classification path with an injected `pane_capturer`. | `TurnStateSweepWiringTests` | [../src/agents_remember/serving/terminal_liveness.py](../src/agents_remember/serving/terminal_liveness.py) |
| `TerminalMarkVsLivenessInterplayTests` exercises `mark_retired`/`record_liveness_probe` interplay on `TerminalCatalog` directly. | `TerminalMarkVsLivenessInterplayTests` | [../src/agents_remember/serving/terminal_catalog.py](../src/agents_remember/serving/terminal_catalog.py) |
| `AutoRetireHookIntegrationTests` exercises `worktree_integrate_tool`/`lifecycle_finalize_task_tool`/`_auto_retire_completed_seats` including the F1 exception-guard-widening fix. | `AutoRetireHookIntegrationTests` | [../src/agents_remember/controllers/worktree_tools.py](../src/agents_remember/controllers/worktree_tools.py) |
| `RetirementSettingsConfigTests` exercises `RetirementSettings` defaults (config parsing itself is covered separately in `test_config.py::RetirementSettingsTests`). | `RetirementSettingsConfigTests` | [../src/agents_remember/mcp/config.py](../src/agents_remember/mcp/config.py) |
| `SessionRetireToolTests`/`SessionRenameToolTests` exercise `session_retire_payload`/`session_rename_payload` end-to-end. | `SessionRetireToolTests`; `SessionRenameToolTests` | [../src/agents_remember/mcp/tools/terminal.py](../src/agents_remember/mcp/tools/terminal.py) |
| The leaf task doc's failing-first requirement list this suite implements. | Requirements | [../../../../../../../../../tasks/agents-remember/260707_hotfix-orchestration-stack/10_seat-retirement-and-chat-cleanup.md](../../../../../../../../../tasks/agents-remember/260707_hotfix-orchestration-stack/10_seat-retirement-and-chat-cleanup.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary is exercised by this local test suite. | — | — |

## Update History

- 2026-07-08T02:43+02:00 — Created for 260707-HFX-L8 (seat lifecycle: retirement + live chat
  identity, status, turn-state): the consolidated failing-first + regression suite (45 tests / 5
  subtests per the builder report) covering the retire authority matrix, `session_retire`/
  `session_rename` MCP tools, turn-state classification + L5-sweep wiring, terminal-mark vs.
  liveness interplay, and the integrate/finalize auto-retire automation hooks incl. the R2/F1
  exception-guard-widening regression tests. Verification metadata pinned until closeout stamps the
  HFX-L8 commit.
