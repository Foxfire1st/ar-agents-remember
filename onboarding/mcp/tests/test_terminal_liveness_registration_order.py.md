# mcp/tests/test_terminal_liveness_registration_order.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_terminal_liveness_registration_order.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T13:20+02:00 |
| lastVerifiedCommitHash | `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| lastVerifiedCommitDate | 2026-09-18T07:49:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

This hermetic unit-regression module is the falsifiable proof of the terminal liveness sweeper's
**registration-before-compaction** contract: a due full sweep commits its observation batch, then
enumerates terminated rows with `include_terminated=True`, offers exactly that set to the
execution-evidence registrar, and hands **only the registrar's returned proved-id set** to
`catalog.compact(...)`. It adds no production behavior — the order already holds in
`terminal_liveness.py` — so it is a regression fence over an existing contract, not new relay
behavior. Two adjacent properties ride the same five cases: an absent registrar must yield an empty
proved set rather than assumed registration, and the starting-row fast path must do neither stage.

## Code Commentary

### Logic

`test_due_sweep_registers_committed_terminated_rows_before_compaction` is the ordering case, and it
instruments the **enumeration itself** rather than a downstream consumer. `TerminalCatalog.batch` is
wrapped to record `batch-enter`/`batch-exit`, and `TerminalCatalog.list` is wrapped so the
`include_terminated=True` read appends an event carrying the batch-commit state observed *at the
read*. The case then asserts the exact chain
`batch-enter → batch-exit → enumerate[include_terminated=True, batch=closed] → register → compact`.
Recording the read's own batch state is what makes a relocation of the terminated-row read visible
instead of inferred from the registrar's call site: an enumeration moved inside the batch would
report `batch=open`, and one moved ahead of the batch would land at chain position 0. The case's
second phase runs a sweeper with **no** registrar over a second catalog and asserts `compact`
receives `frozenset()`. No registrar means no proof, so a task-bound leaf row survives its expired
retention window.

`test_partial_registration_compacts_only_the_proven_rows` offers two terminated task-bound rows and
has the registrar prove one. Compaction receives the singleton `frozenset({"proven"})`, the proved row
is gone, and `unproven` is still `terminated` — the retention predicate is genuinely engaged, not
vacuous.

`test_registration_failure_prevents_compaction_and_leaves_rows_retryable` makes the registrar raise.
The exception escapes the pass, `compact` is never called (`arguments == []`), and both rows remain
present and `terminated`.

`test_restart_after_registration_before_compaction_reregisters_and_loses_nothing` crashes `compact`
after a successful registration, proves both rows survive, then builds a fresh `TerminalCatalog` over
the same file plus a fresh sweeper: registration runs again with both rows and only then does
compaction reclaim them, so a crash between the two stages loses no terminal evidence.

`test_starting_fast_path_neither_registers_nor_compacts_while_the_due_sweep_does` enters the
rate-limited branch through the sweeper's in-memory cadence seam, asserts zero registrar and zero
`compact` calls, and then advances the clock past the sweep interval so the same wiring fires on the
next due sweep — both directions, so the case cannot pass by the wiring being dead.

### Conventions

- The module drives the real `TerminalCatalog` over a `tempfile` directory and the real
  `TerminalCatalogLivenessSweeper.refresh`, and pins `sys.path` to this checkout's `mcp/src` so the
  tree under test is the tree on disk (proved by mutation response, not by import inspection).
- The registrar and the compactor are the module's owned stand-ins for the task-owned execution
  registrar: the registrar records the rows it was offered and returns only the ids it proved, and
  the compactor records the proved set it received before delegating to the real `compact`. They are
  doubled so a case can choose partial proof, failure and crash; the catalog, the sweeper, the batch
  and the retention predicate are all real.
- Rows are built by a typed `_row(...)` base plus `dataclasses.replace(...)` variants, so the module
  is Pyright-clean without a `# type: ignore` suppression; the harness `unittest` style and the
  movable `_Clock` match the sibling terminal-liveness modules.
- Assertions and docstrings state the technical contract only; the sample `TaskDocumentRef` path a
  terminated row carries is fixture data that engages the retention predicate, not a real task
  binding.
- The module is classified in the repository's `unit-regression` evidence lane
  (`mcp/tests/test-evidence-lanes.toml:119`), the same lane as its sibling
  `test_terminal_liveness_deferred_work.py`, because it is hermetic: temporary catalogs, in-process
  `unittest` classes, no `worktree_services`.

### Invariants And Boundaries

- Registration precedes compaction, and the terminated-row enumeration sits between the batch commit
  and registration. Reordering any of the three stages is the defect this module exists to catch.
- The registration callback is the **only** authority that proves an execution id registered; only the
  set it returns reaches `compact`. An absent callback is an empty proved set, never an assumed
  registration.
- A raising registrar fails the pass before compaction and leaves the terminal rows retryable; a crash
  after registration but before compaction is safe because the next pass re-registers idempotently.
- The starting-row fast path neither registers terminated rows nor compacts the catalog.
- A green run is ordering evidence for these five properties. It is not execution, certification or
  acceptance evidence, and it does not establish the catalog's retention-period values, evidence
  identity, or workspace-river compaction — those belong to their own owners.
- The module is ordinary version-controlled test source: it is not a governed evidence artifact and
  needs no entry in the evidence-lifecycle catalog.

### Todos

No additional implementation scope is opened by this card. The retention contract for non-leaf
terminated rows (reclaimed regardless of proof) is pre-existing and deliberately outside this
module's scope; any change to it belongs to the catalog's own owner.

## Docs References

No external Domain Documentation source is configured in the resolved memory root, and this module
tests repository-owned serving and catalog behavior, so no external domain claim is needed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No domain document defines the sweep's registration/compaction order; the implementation is the source of truth. | `refresh` | mcp/src/agents_remember/serving/terminal_liveness.py:174-221 |

## Repo-Internal References

The cited source declarations establish the contract this module pins; these ranges record current
source, not a recorded test execution.

| Finding | Anchor | Source |
| --- | --- | --- |
| The action bundle that carries the `register_execution_evidence` callback, and the `None` an absent registrar leaves behind. | `TerminalLivenessActions` | mcp/src/agents_remember/serving/terminal_liveness.py:137-142 |
| The ordered pass: observation batch, post-commit terminated enumeration, registration, compaction, then deferred syncs and turn-state callbacks. | `refresh` | mcp/src/agents_remember/serving/terminal_liveness.py:174-221 |
| The terminated-row read the ordering case instruments, and the `include_terminated` switch it exercises. | `list` | mcp/src/agents_remember/serving/terminal_catalog.py:80-84 |
| The observation batch whose commit boundary the order chain proves. | `batch` | mcp/src/agents_remember/serving/terminal_catalog.py:282-313 |
| The reclamation predicate that retains a task-bound leaf row until its id is proved registered. | `compact`; `_leaf_execution_entry` | mcp/src/agents_remember/serving/terminal_catalog.py:315-345; mcp/src/agents_remember/serving/terminal_catalog.py:52-62 |
| The starting-row fast path that must perform neither registration nor compaction. | `_refresh_starting_rows` | mcp/src/agents_remember/serving/terminal_liveness.py:223-268 |
| The production registrar whose result really is partial — an id is proved only when every registration result is `durable_or_irrelevant`. | `register_terminal_catalog_execution_evidence` | mcp/src/agents_remember/application/task_docs/task_execution_registration.py:353-389 |
| The app wiring that injects the real registrar into the sweeper's actions. | `create_app` | mcp/src/agents_remember/serving/app.py:253-314 |
| The sibling module that pins the same full/starting sweep order for the deferred post-commit work. | `TerminalLivenessDeferredWorkTests` | mcp/tests/test_terminal_liveness_deferred_work.py:101-366 |
| The ordering case, the partial-proof case, the failure case, the restart case and the fast-path exclusion case. | `test_due_sweep_registers_committed_terminated_rows_before_compaction`; `test_partial_registration_compacts_only_the_proven_rows`; `test_registration_failure_prevents_compaction_and_leaves_rows_retryable`; `test_restart_after_registration_before_compaction_reregisters_and_loses_nothing`; `test_starting_fast_path_neither_registers_nor_compacts_while_the_due_sweep_does` | mcp/tests/test_terminal_liveness_registration_order.py:154-246; mcp/tests/test_terminal_liveness_registration_order.py:248-278; mcp/tests/test_terminal_liveness_registration_order.py:280-310; mcp/tests/test_terminal_liveness_registration_order.py:312-358; mcp/tests/test_terminal_liveness_registration_order.py:360-403 |
| The module's own `unit-regression` lane row, added by the same change set that created it. | "mcp/tests/test_terminal_liveness_registration_order.py" | mcp/tests/test-evidence-lanes.toml:152-152 |

## Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned
unit-regression module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local serving proof. | — | — |

## Update History
- 2026-09-18T05:29:42+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:152-152. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:35+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_terminal_liveness_registration_order.py"` → `mcp/tests/test-evidence-lanes.toml:151-151`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.
- 2026-09-18T02:37:44+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:149-149. No content impact: mechanical anchor-range projection bound to citation source snapshot d211cfd02f11c0600198b11c621aa5574ac8743db6e0ca1d2c92936e561c5146; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:147-147. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:143-143. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-15T13:20+02:00 — 260831-LOCR-L23 curator: created this card for the change set's new
  ordering module (base `67b21aeb`). It records the post-commit registration-before-compaction chain
  the module asserts, the five cases and the observables they own, the fail-closed no-registrar
  default, and the starting-row fast path's exclusion — as current source ranges, without claiming
  execution, acceptance or a future commit stamp. Verification metadata remains closeout-owned.
