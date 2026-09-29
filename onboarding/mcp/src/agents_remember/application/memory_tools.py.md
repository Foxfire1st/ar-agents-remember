# mcp/src/agents_remember/application/memory_tools.py

| Field                  | Value                                                      |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                            |
| lastUpdated | 2026-09-24T09:20+02:00 |
| lastVerifiedCommitHash | `719acba61e491d0b7f1ee82dbeea5314ecec5083` |
| lastVerifiedCommitDate | 2026-09-29T20:27:14+02:00|
| path                   | `mcp/src/agents_remember/application/memory_tools.py`       |
| doc_type               | `file-level-onboarding`                                    |
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

**On a converted memory tree, `citation_check` and `citation_fix` work over sidecar references
(MIK-R24 rule 5).** Both tools first ask `memory_quality/reference_state.is_converted_memory` whether the
memory root (the onboarding root's parent) holds `knowledge/layout.json`. If it does, they return
`reference_state.check_references` or `reference_state.fix_references` instead of building citation
`Trees`. A stale reference is reported (report-only), never a gate finding, and the fixer re-records
only anchors whose bytes moved mechanically. An unconverted tree takes the legacy citation-table path
exactly as before. The source-index build and `citation_migrate` are legacy-format operations and are
not adapted.

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
| Baseline status reports unsuccessful `ok` for unavailable Git history as well as blocked drift, while preserving the owner's payload. | `memory_baseline_status_tool` | mcp/src/agents_remember/application/memory_tools.py:481-488 |
| The baseline owner distinguishes unreadable attribution behind a resolvable HEAD from an unborn repository, retaining the existing drift decision. | `ledger_status`; `baseline_status` | mcp/src/agents_remember/memory/baseline.py:258-267; mcp/src/agents_remember/memory/baseline.py:300-303 |
| Carryover has one memory subject and forwards it without a ledger-message option. | `CarryoverCommitMessages` | mcp/src/agents_remember/application/memory_tools.py:470-474 |
| Canonical quality scope is owned by the focused scope module. | `resolve_memory_scope`; `MemoryScope` | mcp/src/agents_remember/application/memory_scope.py:71-102; mcp/src/agents_remember/application/memory_scope.py:105-142 |
| Typed quality execution and public run translation are owned by the controller. | `run_memory_quality_request`; `_resolve_execution` | mcp/src/agents_remember/application/memory_quality/controller.py:254-260; mcp/src/agents_remember/application/memory_quality/controller.py:365-385 |
| The route-index application entry point forwards resolver-owned authority. | `route_index_refresh_tool` | mcp/src/agents_remember/application/memory_tools.py:254-291; mcp/src/agents_remember/application/memory_tools.py:316-352 |
| The route-index builder. | `build_route_indexes` | mcp/src/agents_remember/kernel/route_index.py:184-235 |
| The route-index builder receives storage authority explicitly in its typed signature. | `build_route_indexes` | mcp/src/agents_remember/kernel/route_index.py:184-235 |
| The apply entry point that forwards that subject and nothing else. | `memory_carryover_apply_tool` | mcp/src/agents_remember/application/memory_tools.py:568-585 |
| Baseline status reports unsuccessful `ok` for unavailable Git history as well as blocked drift, while preserving the owner's payload. | `memory_baseline_status_tool` | mcp/src/agents_remember/application/memory_tools.py:481-488 |
| The baseline owner distinguishes unreadable attribution behind a resolvable HEAD from an unborn repository, retaining the existing drift decision. | `baseline_status` | mcp/src/agents_remember/memory/baseline.py:300-303 |
| Carryover has one memory subject and forwards it without a ledger-message option. | `CarryoverCommitMessages` | mcp/src/agents_remember/application/memory_tools.py:470-474 |
| The apply entry point that forwards that subject and nothing else. | `memory_carryover_apply_tool` | mcp/src/agents_remember/application/memory_tools.py:568-585 |
| Canonical quality scope is owned by the focused scope module. | `MemoryScope` | mcp/src/agents_remember/application/memory_scope.py:71-102 |
| Its resolver, which binds a repository to the scope the quality surface runs against. | `resolve_memory_scope` | mcp/src/agents_remember/application/memory_scope.py:105-142 |
| The one execution path both the report and the closeout gate run through. | `_execute_memory_quality` | mcp/src/agents_remember/application/memory_quality/controller.py:388-462 |
| The curator worklist publication that follows a full scoped call. | `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_quality/controller.py:512-692 |
| On a converted tree the citation check reports the sidecar references' state instead of reading citation tables. | `citation_check_tool`; `is_converted_memory` | mcp/src/agents_remember/application/memory_tools.py:173-209; mcp/src/agents_remember/memory_quality/reference_state.py:40-43 |
| On a converted tree the citation fixer re-records only mechanically moved reference anchors. | `citation_fix_tool`; `fix_references` | mcp/src/agents_remember/application/memory_tools.py:233-276; mcp/src/agents_remember/memory_quality/reference_state.py:207-227 |
| The one construction point that carries a caller's excludes into all four citation operations. | `_citation_trees` | mcp/src/agents_remember/application/memory_tools.py:154-170 |
| The scope object the caller's excludes ride with, validated at construction. | `CitationOperationScope` | mcp/src/agents_remember/application/memory_tools.py:57-87 |
| The refusal rule for a caller exclude that cannot mean anything. | `validate_caller_excludes` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:171-193 |
| **The memory initializer now reports the knowledge foundation beside the memory root it scaffolds (`ICR-R29@v1`).** | `memory_init_tool`; `_knowledge_foundation_state`; `KNOWLEDGE_BOOTSTRAP_ROUTE` | mcp/src/agents_remember/application/memory_tools.py:357-360; mcp/src/agents_remember/application/memory_tools.py:363-392; mcp/src/agents_remember/application/memory_tools.py:395-434; mcp/src/agents_remember/application/memory_tools.py:340-343 |
| **The admission whose location this block reports, so the location a curator is told to populate is the one the bootstrap publishes to.** | `admit_bootstrap_context`; `BootstrapRefusal` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:118-129; mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:175-214 |
| The read that decides the block's state, and the unavailable form its states come from. | `resolve_published_intent`; `PublishedIntentUnavailable` | mcp/src/agents_remember/application/published_intent.py:265-265; mcp/src/agents_remember/application/published_intent.py:214-214 |

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

## KS-R23@v1 The Citation Responses Name Their Ruler

Both citation entry points now return the measurement's ruler beside their counts (item 26, D-33):
`citation_fix_tool` (`:212-247`) and `citation_migrate_tool` (`:250-284`) spread
`measuring_build_stamp()` — imported from `agents_remember.application.runtime.startup` at `:15` — into
their returned mapping (`:246`, `:283`), so each response says which build's rewrite rules produced the
counts it reports, rather than leaving a reader to assume they came from the candidate's own code.

That the repair engine belongs to the *measuring* machinery is the reason it is stamped at all: a count
produced by a fixed serving build while the candidate carries different code cannot show a fix to that
machinery. The field is declared on `CitationFixResponse`/`CitationMigrateResponse` rather than left to
the flexible envelope (see the `models/memory.py` card). Nothing else about these two operations moved —
the leaf-memory-writer scope guard, the one `_citation_trees` construction point and the refusal paths are
untouched.

## 260918-TSIP-L6 Branch Authority Unavailable, Answered In The Envelope

`memory_baseline_adopt_tool` (`:393-432`) now catches `BranchAuthorityUnavailable` — the typed
condition raised when a repository's default-branch authority was never **recorded** — and answers
through `_baseline_adopt_refusal` (`:433-459`) instead of letting a traceback take `ok`, `status`
and `nextAction` with it (`T34`). That is the shape its sibling `memory_baseline_status_tool`
(`:383-392`) already uses for the same repository: a memory repository that has never recorded its
default-branch authority is an ordinary precondition, not a crash.

The catch is deliberately narrow. `BranchAuthorityUnavailable` means *the authority this operation
needs was never recorded*, and its own message names the remedy (`memory_init` records it). The
other `RuntimeError`s on this path — *memory baseline adoption is a bootstrap-only exception on the
checked-out repository-default branch*, *memory root does not exist* — refuse a state the caller
must understand and change, and they keep raising: widening the catch to `RuntimeError` would hide
a misuse behind an envelope.
`mcp/tests/test_memory_branch_authority.py::test_baseline_adoption_refuses_a_branch_the_memory_repository_does_not_record`
is the case that holds that boundary, and the docstring states it.

## Update History
- 2026-09-29T18:11:04+00:00: Generated citation repair: `memory_baseline_status_tool` repointed to mcp/src/agents_remember/application/memory_tools.py:481-488. No content impact: mechanical anchor-range projection bound to citation source snapshot 704ba74355bb1716854facdd857416a0cc403be7304c687768829065b4665abc; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:11:04+00:00: Generated citation repair: `CarryoverCommitMessages` repointed to mcp/src/agents_remember/application/memory_tools.py:470-474. No content impact: mechanical anchor-range projection bound to citation source snapshot 704ba74355bb1716854facdd857416a0cc403be7304c687768829065b4665abc; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:11:04+00:00: Generated citation repair: `memory_baseline_status_tool` repointed to mcp/src/agents_remember/application/memory_tools.py:481-488. No content impact: mechanical anchor-range projection bound to citation source snapshot 704ba74355bb1716854facdd857416a0cc403be7304c687768829065b4665abc; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:11:04+00:00: Generated citation repair: `CarryoverCommitMessages` repointed to mcp/src/agents_remember/application/memory_tools.py:470-474. No content impact: mechanical anchor-range projection bound to citation source snapshot 704ba74355bb1716854facdd857416a0cc403be7304c687768829065b4665abc; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R03 moved lines in `published_intent.py`, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). The fixer also normalised passing ranges in rows that cite files this leaf did not change; those ranges are measurement-true. No claim, anchor or source file of this card changed.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): Added a Logic paragraph and two rows: on a converted memory tree (MIK-R24 rule 5), `citation_check_tool` and `citation_fix_tool` route to `memory_quality/reference_state`. Stale references are report-only, and the fixer handles mechanical moves only. The unconverted path is unchanged.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`application/published_intent.py`, `mcp/tools/knowledge.py`, `mcp/registration/knowledge.py`, `models/tools/knowledge_responses.py`, `cli/__main__.py`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the installed fixer or, for the multi-anchor rows it declined, by exact base-to-working line mapping; a per-document `memory-citations` check then reported 0 findings. No claim wording changed.

- 2026-09-24T09:20+02:00 — 260921-ICR-L29 curator (uncommitted change set on `ar/260921-icr-l29-ar`,
  base `0d7910f9d646161c414ed6543453536a3c749d49`): **the memory initializer gained the knowledge half of
  its own answer (`ICR-R29@v1`).** `memory_init_tool` now attaches a `knowledge` block
  (`:374-374`) built by `_knowledge_foundation_state` (`:378-417`), which resolves the **bootstrap's own
  admission** so the location a curator is told to populate is the location the bootstrap publishes to,
  and reports what a read of it finds now: `recorded` (with the dataset path and the dataset's own
  logical digest), the read route's own unavailable states (with its code and detail), or
  `context-not-admitted` when the admission refuses, in which case the block carries the admission's
  code, detail and named next action rather than a hopeful path. `KNOWLEDGE_BOOTSTRAP_ROUTE`
  (`:338-343`) is the one route string, named once because two blocks print it. **Nothing here writes**:
  the initializer still creates no knowledge, because an initializer that created knowledge would be
  inventing authored content — which is exactly the split this block makes readable instead of leaving
  "the initializer says nothing about knowledge" to be misread as "the product has no knowledge step".
  Three reference rows were added for the two functions, the route constant, the admission they resolve
  and the read whose states the block reports. **No verification stamp was advanced** — the candidate is
  uncommitted, so no commit holds the content a stamp would claim to have verified, and the governed
  closeout owns the real code and memory commits.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-19T19:52+02:00 — 260918-TSIP-L6 (uncommitted change set on `ar/260918-tsip-l6-ar`, base `a1351504`): recorded `T34`'s repair here — `memory_baseline_adopt_tool` answers `BranchAuthorityUnavailable` through `_baseline_adopt_refusal` instead of raising, with the catch deliberately narrowed to that one typed condition. Every citation range in this card was re-derived against the repaired file from an enumerated census. Verification metadata stays closeout-owned.
- 2026-09-18T19:55:32+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the three enforced `citation_anchor_absent_from_range` rows in this document** (three table rows). (a) The carryover-message row cited `369-376`, which ends one line above the `class CarryoverCommitMessages:` the claim names at `377`; the range was widened to `369-383`, so it also reaches `DEFAULT_CARRYOVER_MESSAGES` at `383`. (b) The baseline-status row cited `379-386`, one line above `def memory_baseline_status_tool` at `387`; widened to `379-387`. (c) The quality-run row cited `controller.py:111-133` for `run_memory_quality_request`, whose definition this leaf's changes left at `249-255`, and `308-328` for `_resolve_execution`, which had moved to `360-381`; the cell cites both definitions now. A first pass re-pointed only the range the checker named for `run_memory_quality_request` and the document's own second anchor stopped resolving — caught by re-running the check over the whole cell, which is why both ranges are re-derived here. Claims, anchors and every other range are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T19:24+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **recorded the `servingBuild` stamp this leaf's item 26 added to both citation entry points, which this card did not mention.** `citation_fix_tool` and `citation_migrate_tool` now spread `measuring_build_stamp()` into their returns (`:246`, `:283`), so the repair engine's counts name the build whose rules produced them; the section above states why, and the two response models declare the field. Read against the delivered but **uncommitted** working tree, so the verification stamp is not advanced: no commit carries these bytes and closeout owns the real stamp. Everything else this card asserts about the module — the parameter objects, the single `_citation_trees` construction point, the ownership extraction — was re-read and still holds; the reference-table ranges are left to the citation-range repair pass that owns them.
- 2026-09-18T14:05:00+02:00 — 260915-KS-L13 owning seat: re-read the `CitationOperationScope` claim against the current module: the class is declared at :44 and the cited range :44-55 still holds it, so the wording is unchanged and the range is unchanged; the construct changed structurally since 420669c4 and the claim still states it.
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

