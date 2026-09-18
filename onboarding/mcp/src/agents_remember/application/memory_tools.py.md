# mcp/src/agents_remember/application/memory_tools.py

| Field                  | Value                                                      |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                            |
| path                   | `mcp/src/agents_remember/application/memory_tools.py`       |
| doc_type               | `file-level-onboarding`                                    |
| lastUpdated | 2026-09-15T01:13+00:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00 |
| governingOverview      | `overview.md`                                              |

## Governing Overview

[Application layer overview](overview.md)

## Purpose

`memory_tools.py` is the typed application entry point surface for onboarding drift, citation work,
route-index refresh, memory initialization, baseline adoption, and memory carryover. Memory-quality
scope, execution, and async control now belong to the dedicated typed controller.

## Code Commentary

### Logic

`memory_baseline_status_tool` reports `ok=false` for both `blocked-drift` and `unavailable`.
The baseline owner returns `unavailable` when an existing memory HEAD resolves but its Git
attribution history cannot be read. An unborn repository can remain `ready` under the existing
drift rules. This adapter preserves the owner's state and details; cache-file availability does
not become a new admission requirement.

`CarryoverCommitMessages` contains only the memory-content subject. The apply adapter forwards
that subject to `CarryoverApplyOptions`; the carryover owner attributes the memory commit and may
refresh the consumer ledger cache. No ledger subject or third commit intent crosses this boundary.

The module defines four parameter objects for separate application contracts:
`MemoryBranches` carries optional source/work branch overrides for baseline adoption
(`mcp/src/agents_remember/application/memory_tools.py:336-348`);
`CarryoverSelection` carries the repository, memory/code refs, base, and replacement choice for
carryover planning/apply (`mcp/src/agents_remember/application/memory_tools.py:349-368`);
`CarryoverCommitMessages` carries the memory-content commit subject for apply
(`mcp/src/agents_remember/application/memory_tools.py:369-376`); and since 260915-CAPS-L14
`CitationOperationScope` carries the per-call citation selection **including the caller's own
excludes** (`mcp/src/agents_remember/application/memory_tools.py:44-55`).
`intent_note` remains a separate apply approval argument.

**One construction point serves all four citation operations.** `_citation_trees` builds the
citation `Trees` for `citation_check_tool`, `citation_source_index_build_tool`, `citation_fix_tool`
and `citation_migrate_tool`
(`mcp/src/agents_remember/application/memory_tools.py:140-156`). It validates the caller's excludes
through `validate_caller_excludes` and hands them to `Trees`, so a caller-supplied exclude and the
memory layer's `system/settings.json` register are read at one place rather than four. `Trees` takes
the excludes as a value: two operations over one root may carry different caller excludes and neither
changes the other's population. A caller that adds excludes is asserting a **narrower** population
than the register alone, and a pattern that cannot mean anything is refused by name.

Memory-quality resolution, checklist composition, sync/start/poll control, and public run outcomes
were extracted to `application/memory_scope.py` and `application/memory_quality_controller.py`.
This module no longer implements or wraps that failure family. Its remaining operations retain
their existing configured-authority and typed parameter-object boundaries.

`route_index_refresh_tool` then forwards the resolver-owned code root, onboarding root, repository
identity, and storage authority into `build_route_indexes`
(`mcp/src/agents_remember/application/memory_tools.py:279-315`).
Ordinary drift artifacts stay under the coordination temp root. The curator checklist is the
explicit enclosure-local exception and remains outside both Git worktrees. Baseline and carryover
entry points preserve their separate service contracts.

### Conventions

Application entry points translate validated tool arguments into service calls and JSON-compatible payloads.
Path confinement and repository authorization use the shared `_guards` helpers rather than local
filesystem checks.

### Invariants And Boundaries

- Tool callers cannot supply arbitrary source, onboarding, coordination, or storage roots.
- Memory quality must route through the dedicated scope/controller API; this general memory module
  must not re-grow quality scope, registry, or checklist implementations.
- Route-index refresh must forward resolver-owned repository and storage authority explicitly; it
  must not reconstruct path rules from directory layout or parser defaults.
- Drift reports are temporary coordination artifacts, not durable onboarding content.
- Effectful refresh/init/baseline operations act by default and expose `dry_run` for preview;
  carryover remains an explicit plan/apply operation.

### Todos

None known for the MX-FIX-4 application entry point boundary.

## Docs References

No Domain Documentation source is configured for this repository; this card is grounded in the
package application entry point and resolver contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Baseline status reports unsuccessful `ok` for unavailable Git history as well as blocked drift, while preserving the owner's payload. | `memory_baseline_status_tool` | mcp/src/agents_remember/application/memory_tools.py:352-359; mcp/src/agents_remember/application/memory_tools.py:379-386 |
| The baseline owner distinguishes unreadable attribution behind a resolvable HEAD from an unborn repository, retaining the existing drift decision. | `ledger_status`; `baseline_status` | mcp/src/agents_remember/memory/baseline.py:236-275; mcp/src/agents_remember/memory/baseline.py:300-303 |
| Carryover has one memory subject and forwards it without a ledger-message option. | `CarryoverCommitMessages` | mcp/src/agents_remember/application/memory_tools.py:342-345; mcp/src/agents_remember/application/memory_tools.py:369-376 |
| Canonical quality scope is owned by the focused scope module. | `resolve_memory_scope`; `MemoryScope` | mcp/src/agents_remember/application/memory_scope.py:72-104; mcp/src/agents_remember/application/memory_scope.py:105-142 |
| Typed quality execution and public run translation are owned by the controller. | `run_memory_quality_request`; `_resolve_execution` | mcp/src/agents_remember/application/memory_quality/controller.py:111-133; mcp/src/agents_remember/application/memory_quality/controller.py:308-328 |
| The route-index application entry point forwards resolver-owned authority. | `route_index_refresh_tool` | mcp/src/agents_remember/application/memory_tools.py:254-290; mcp/src/agents_remember/application/memory_tools.py:279-315 |
| The route-index builder. | `build_route_indexes` | mcp/src/agents_remember/kernel/route_index.py:184-235 |
| The route-index builder receives storage authority explicitly in its typed signature. | `build_route_indexes` | mcp/src/agents_remember/kernel/route_index.py:184-235 |
| The apply entry point that forwards that subject and nothing else. | `memory_carryover_apply_tool` | mcp/src/agents_remember/application/memory_tools.py:418-435 |
| Its resolver, which binds a repository to the scope the quality surface runs against. | `resolve_memory_scope` | mcp/src/agents_remember/application/memory_scope.py:105-142 |
| The one execution path both the report and the closeout gate run through. | `_execute_memory_quality` | mcp/src/agents_remember/application/memory_quality/controller.py:331-383 |
| The curator worklist publication that follows a full scoped call. | `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_quality/controller.py:413-550 |
| The one construction point that carries a caller's excludes into all four citation operations. | `_citation_trees` | mcp/src/agents_remember/application/memory_tools.py:140-156 |
| The scope object the caller's excludes ride with, validated at construction. | `CitationOperationScope` | mcp/src/agents_remember/application/memory_tools.py:44-55 |
| The refusal rule for a caller exclude that cannot mean anything. | `validate_caller_excludes` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:171-193 |

## Cross-Repo References

The application entry point can target configured sibling repositories, but no external implementation governs
this package-local dispatch contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-DAGQC-L2 Quality Ownership Extraction

The quality-specific authority, complete execution identity, bounded registry orchestration, and
checklist publication moved to `memory_scope.py` and `memory_quality_controller.py`. This leaves
`memory_tools.py` focused on the other memory operations and prevents each transport/application
caller from reimplementing the controller's failure vocabulary.

## Update History

- 2026-09-17T12:40+02:00 — 260915-CAPS-L14 curator: recorded the module's **one citation construction point**. `_citation_trees` builds the citation `Trees` for all four citation operations and carries the caller's own excludes into it, validated through `validate_caller_excludes`; `CitationOperationScope` gained the `excludes` field, so a caller-supplied exclude and the memory layer's `system/settings.json` register are read in one place rather than four, and `Trees` takes them as a value so two operations over one root cannot change each other's population. **Flattened three tables from the legacy `| Finding | Citations | Source Path |` shape to the required `| Finding | Anchor | Source |` form** (the body also carried four inline `cit:([…], path:a-b)` cells, which are now plain `path:start-end`), and **re-derived every range**: the parameter objects cited at `:309-314` / `:322-338` / `:342-345` are now at `:336-348` / `:349-368` / `:369-376`, the route-index range at `:279-315`, and the `memory_scope` row cited a range that neither held `resolve_memory_scope` nor `MemoryScope`. Verification metadata is left at this leaf's synced base `0346da9c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code commit.

- 2026-09-15T01:13+00:00 — LCA-L9 current candidate: documented the baseline status adapter's `ok=false` result for unavailable Git attribution, preserving the unborn-repository and existing drift distinction without a cache guard. Rechecked both source owners and repaired the citation-table spacing. Existing verification commit/date and earlier history remain unchanged; no test-execution claim.

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Documented the single carryover commit-message input and the cache-only ledger boundary. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.


- 2026-09-10T04:35+02:00 — CCR-L42 final citation curation: re-anchored the quality-scope row to
  the current `resolve_memory_scope` and `resolve_leaf_memory_scope` implementations; the
  focused resolver remains the sole authority and verification metadata remains closeout-owned.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: re-anchored the controller request-surface row (67-144 to 98-208) shifted by the CCR-R08 +57-line controller insertion. Citation-only re-anchor; no content impact.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: removed memory-quality scope/controller/registry ownership from this general application module and routed that contract through focused typed APIs. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15: added the async start/poll wrappers over the bounded
  background run registry (R7) with the `ok`-header bug fixed at the gate-repair round; the
  synchronous `memory_quality_check_tool` contract is unchanged. Verified at code commit de3a0fd9.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-11T16:54+02:00 — Added the full scoped curator checklist composition and stable
  enclosure report path while keeping subset/official calls and code/memory content unchanged.
- 2026-08-11T14:58+02:00 — Made the temporary-provenance evidence one-to-one with the application
  declaration and its two exact scope regressions after preflight exposed the generic anchor's
  multiple current resolutions.
- 2026-08-11T14:40+02:00 — Documented contract-scoped temporary comparison provenance for
  unstamped dirty-tree claims, preserved closeout ownership of real verification stamps, and
  regenerated shifted application citations.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: added `MemoryBranches`, `CarryoverSelection` and
  `CarryoverCommitMessages` (plus their shared defaults) and moved the baseline-adopt and carryover
  keyword lists onto them; `intent_note` deliberately stays outside the selection. Resolver
  authority, drift artifacts and the plan/apply split are unchanged. Verification metadata pinned
  until closeout stamps the L2 code commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: documented explicit resolved repository/storage
  authority at the route-index controller boundary.
- 2026-05-31T12:30+02:00 — Repo/path guards moved to shared `_guards`
  (`require_repo`/`require_within_coordination`) raising `AuthorityError`, and
  `memory_baseline_status` now returns `ok=False` on blocked drift (1.0.0 review remediation).
- 2026-05-28T19:52+02:00 — Created when memory/onboarding MCP controllers moved into their own
  domain module.
