# mcp/src/agents_remember/observer/save_gate.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/save_gate.py`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-13T18:45+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The ambient methods that raise/consume this vocabulary (`switch`/`attach`/`promote`). | `switch`; `attach`; `promote` | mcp/src/agents_remember/observer/ambient.py:284-315; mcp/src/agents_remember/observer/ambient.py:333-370; mcp/src/agents_remember/observer/ambient.py:317-331 |
| The typed-error family base (`LifecycleError` → `AgentsRememberError`). | `LifecycleError` | mcp/src/agents_remember/observer/lifecycle_state.py:161-162 |
| The design separates fleeting and persistent sessions with a save gate and TTL. | "Fleeting vs persistent"; "save gate"; "TTL" | docs/design/observable-lifecycle.md:98-118 |

## Update History

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-06-13T18:45+02:00: Created for slice 2c — the pure save-gate vocabulary
  (`SaveDecision`, `coerce_save_decision`, `SaveGateRequired`, `compute_scope`,
  and the landing-zone scope constants `UNSCOPED_SCOPE`/`CROSS_REPO_SCOPE`).
  Verification metadata is pinned until closeout stamps the 2c code commit.
