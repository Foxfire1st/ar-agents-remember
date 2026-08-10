# test_seat_lifecycle.py

| Field                  | Value                                     |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                               |
| path                   | `mcp/tests/test_seat_lifecycle.py`            |
| doc_type               | `file-level-onboarding`                       |
| lastUpdated            | 2026-08-10T06:28+02:00 |
| lastVerifiedCommitHash |  `b537abe20cf2498ef38e86e29ca586b5eec38466`|
| lastVerifiedCommitDate |  2026-08-10T08:37:35+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_seat_lifecycle.py` is the failing-first + regression suite for seat lifecycle behavior:
retirement authority/manual retire, automatic completion cleanup, live identity/rename, and
live turn-state. It covers the retire authority matrix, the `session_retire`/`session_rename` MCP
tools end-to-end, turn-state classification from scripted pane fixtures, the terminal-mark vs.
liveness-hysteresis interplay, and the `worktree_integrate`/`lifecycle_finalize_task` close-or-land
hooks. Dedicated failure/race containment moved to `test_completion_cleanup.py` with its source
owner; this suite retains successful integration/finalization wiring and role/report selection.

## Code Commentary

### 260707-HFX2-L18 Pair Retirement Regressions

The authority matrix now uses binding leaf/role, covers manager retirement of own-master pipeline
roles, and proves an unbound failed dispatch resolves its master through `replacementForLeaf`.
Owner-never-self-retires and portfolio authority remain pinned.

### Logic

Shared fixtures: `_config(root, **retirement_overrides)` builds a minimal `McpRuntimeConfig` with
an overridable `RetirementSettings`; `_entry(session_id, *, leaf_key, spawn_role)` builds one
fixed shape — a `running` `harness` `TerminalCatalogEntry` — and every rarer shape (a
`terminated` row, a plain `terminal` row, an unbound `replacement_for_leaf`) is a
`dataclasses.replace(...)` on the frozen row rather than another builder parameter; `_get`
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
- **`TurnStateSweepWiringTests`** — `observe_terminal_liveness` with the capturer injected through
  `probe=LivenessProbe(hysteresis=TerminalCatalogLivenessConfig(), pane_capturer=…)`: an alive
  `kind="harness"` row gets classified AND `turn_state_changed=True` on first
  classification; a `kind="terminal"` (plain shell) row — built as
  `replace(_entry(...), kind="terminal", harness=None)` — is NEVER classified: asserts `turn_state`
  stays `None` and the capturer is never even called (`calls == []`), proving the "plain terminals
  are never classified" invariant at the capture-call level, not just the result level.
- **`TerminalMarkVsLivenessInterplayTests`** — a retired row stays `status="terminated"` after a
  SUBSEQUENT alive `record_liveness_probe` (hysteresis never resurrects a retire); retiring an
  already-`terminated` row (via a plain `/terminate`, i.e. `mark_terminated`, not a prior retire)
  never back-fills retroactive retirement provenance — `retired_at` stays `None`.
- **`LandSeatsForLeafTests`** — `land_seats_for_leaf(catalog, SeatClosure(reason, edge, at), *,
  leaf_key, roles)` role/leaf-key scoping: lands only rows
  matching BOTH `leaf_key` and `roles`, leaves a manager row and a different-leaf worker row
  untouched, records the landing provenance carried by `SeatClosure`, and skips
  already-terminated seats.
- **`AutoLandHookIntegrationTests`** — ARG-L1 completion-edge wiring around a fake contract and
  fake terminal host. Exact-session/exact-leaf durable reports close worker/reviewer/curator via
  normal retirement, prove tmux termination/catalog auto-close provenance, and leave a seeded
  transcript unchanged; manager/orchestrator remain running. Missing and wrong-leaf reports defer;
  `autoCloseCompletedSeats=false` lands all three leaf roles; edge-off and dry-run do nothing;
  finalization retries late subordinate cleanup without touching the manager.
- **`RetirementSettingsConfigTests`** — all three `RetirementSettings()` fields default `True`.

### Conventions

Plain `unittest.TestCase` classes (not pytest fixtures), matching the repo's dominant test style.
Each stateful test class uses a `tempfile.TemporaryDirectory()` per test in `setUp`/`tearDown`
rather than a shared fixture, so catalog file state never leaks between tests.

### Invariants And Boundaries

This file tests behavior across the seat lifecycle source files (`retire_policy.py`, `retire.py`,
`landing.py`, `turn_state.py`, `terminal_catalog.py`, `terminal_liveness.py`, and
`application/worktree_tools.py`'s close-or-land hooks) plus the `session_retire`/`session_rename` MCP
tool payloads and `RetirementSettings` config parsing.

### Todos

No known follow-up in this file.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation; this is a
same-repository unit/integration test file with no external-standard dependency.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document governs this test shape; the leaf task doc's failing-first requirement list is the source of truth for coverage scope. | "class RetirePolicyMatrixTests" | mcp/tests/test_seat_lifecycle.py:112-112 |

## Repo-Internal References

This suite directly exercises five source files and the leaf task doc's requirement list.

| Finding | Anchor | Source |
| --- | --- | --- |
| `RetirePolicyMatrixTests` exercises `check_retire_authority`/`master_of`/`RetirePolicyError` directly. | `RetirePolicyMatrixTests` | mcp/tests/test_seat_lifecycle.py:112-180 |
| `LandSeatsForLeafTests` exercises `land_seats_for_leaf` directly. | `LandSeatsForLeafTests` | mcp/tests/test_seat_lifecycle.py:593-643 |
| `TurnStateClassificationTests` exercises `classify_turn_state` directly. | `TurnStateClassificationTests` | mcp/tests/test_seat_lifecycle.py:383-475 |
| `TurnStateSweepWiringTests` exercises `observe_terminal_liveness`'s alive-classification path with an injected `pane_capturer`. | `TurnStateSweepWiringTests` | mcp/tests/test_seat_lifecycle.py:476-546 |
| `TerminalMarkVsLivenessInterplayTests` exercises `mark_retired`/`record_liveness_probe` interplay on `TerminalCatalog` directly. | `TerminalMarkVsLivenessInterplayTests` | mcp/tests/test_seat_lifecycle.py:547-592 |
| `AutoLandHookIntegrationTests` exercises both successful completion edges, exact report ordering, all three subordinate roles, owner exclusions, retire provenance, transcript retention, opt-out landing, edge-off, and dry-run behavior. | `AutoLandHookIntegrationTests` | mcp/tests/test_seat_lifecycle.py:645-869 |
| `RetirementSettingsConfigTests` exercises all `RetirementSettings` defaults (parsing is covered separately in `test_config.py::RetirementSettingsTests`). | `RetirementSettingsConfigTests` | mcp/tests/test_seat_lifecycle.py:870-878 |
| `SessionRetireToolTests`/`SessionRenameToolTests` exercise `session_retire_payload`/`session_rename_payload` end-to-end. | `SessionRetireToolTests`; `SessionRenameToolTests` | mcp/tests/test_seat_lifecycle.py:181-327; mcp/tests/test_seat_lifecycle.py:328-382 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is exercised by this local test suite. | — | — |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History

- 2026-08-10T06:28+02:00 — Moved completion-cleanup failure/race cases to the dedicated
  `test_completion_cleanup.py` suite and reconciled all class ranges. This file now owns successful
  edge wiring; the dedicated suite owns containment. Verification metadata remains blank until
  closeout stamps the code commit.

- 2026-08-10T05:45+02:00 — 260805-ARG-L1: replaced completion-edge landing expectations with
  exact-report-gated worker/reviewer/curator retirement, tmux/provenance/transcript proofs,
  manager/orchestrator exclusion, deferral, opt-out landing, and failure-containment coverage.
  Verification metadata remains pinned until closeout stamps ARG-L1.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: corrected the shared-fixture and injection-seam
  descriptions, which the leaf made false. `_entry` lost three parameters — its documented
  signature `(session_id, *, leaf_key, spawn_role, status, kind)` is now
  `(session_id, *, leaf_key, spawn_role)` and it always mints a `running` `harness` row; the
  terminated row, the plain-terminal row and the unbound `replacement_for_leaf` row are now
  `dataclasses.replace(...)` on the frozen entry, so the "sane defaults" wording was describing
  defaults that no longer exist as parameters. `TurnStateSweepWiringTests` now injects the
  capturer through `probe=LivenessProbe(hysteresis=TerminalCatalogLivenessConfig(),
  pane_capturer=…)` rather than the two loose keywords, and `land_seats_for_leaf` takes a
  positional `SeatClosure(reason, edge, at)` ahead of `leaf_key`/`roles`; both bullets were
  rewritten to match. The whole-module citation in Docs References moved from L1-L743 to L1-L832.
  No test class or method was added, removed or renamed and no assertion changed, so the coverage
  claims themselves are unaffected.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

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
