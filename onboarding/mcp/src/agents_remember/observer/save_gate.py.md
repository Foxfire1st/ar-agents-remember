# mcp/src/agents_remember/observer/save_gate.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/save_gate.py`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-13T18:45+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

`save_gate.py` is the pure decision vocabulary of the **save gate** — the choice
forced when leaving a *fleeting* lifecycle (design §1.2/§1.5): **save** promotes
it to persistent so the work is not lost, **discard** ends it `abandoned`. It has
no I/O or threading, so the slice-3 projection reducer can reuse the scope rule.

## Code Commentary

`SaveDecision = Literal["save","discard"]` with `SAVE_DECISIONS = get_args(...)`;
`coerce_save_decision(value)` validates a raw tool-boundary string into a
`SaveDecision` or raises `LifecycleError`. `SaveGateRequired(LifecycleError)` is
raised when a switch/attach would abandon unsaved fleeting work and no decision
was supplied — it carries the active id and tells the caller to pass `on_unsaved`.
`compute_scope(repo_id, *, cross_repo=False)` returns the scope tag recorded on
`lifecycle.promoted`: the `repo_id` for single-repo work, `CROSS_REPO_SCOPE`
(`1_cross-repo`) for multi-repo enclosures, or `UNSCOPED_SCOPE` (`0_unscoped`)
when there is no managed-repo binding; the numeric prefixes sort above the
per-repo folders in the dashboard hangar (slice 4).

## Invariants And Boundaries

- Pure vocabulary: imports only `LifecycleError` from `lifecycle_state.py`; no
  I/O, no threading, no import from the ambient module — kept reusable by the
  projection reducer.
- The gate is **foundational, not interactive**: 2c records the decision from an
  explicit input and *blocks* (`SaveGateRequired`) when none is given; slice 06
  docks interactive resolution, a durable gate record, and enforcement onto this
  seam. There is deliberately no auto-save default.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The ambient methods that raise/consume this vocabulary (`switch`/`attach`/`promote`). | [ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The typed-error family base (`LifecycleError` → `AgentsRememberError`). | [lifecycle_state.py](agents-remember/mcp/src/agents_remember/observer/lifecycle_state.py) |
| The design's save gate, landing zones, and promotion event (§1.5, §2.2). | [docs/design/observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |

## Update History

- 2026-06-13T18:45+02:00: Created for slice 2c — the pure save-gate vocabulary
  (`SaveDecision`, `coerce_save_decision`, `SaveGateRequired`, `compute_scope`,
  and the landing-zone scope constants `UNSCOPED_SCOPE`/`CROSS_REPO_SCOPE`).
  Verification metadata is pinned until closeout stamps the 2c code commit.
