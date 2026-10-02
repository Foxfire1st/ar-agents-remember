# mcp/src/agents_remember/application/memory_tools.py

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
`reference_state.check_references` or, for the fixer, `_converted_citation_fix` instead of building citation
`Trees`. A stale reference is reported (report-only), never a gate finding. Since L37 (fix round P1b)
`_converted_citation_fix` does two things: it authors the cards' citation rows into resolved sidecar
references (`memory/conversion/card_authoring.author_card_references`), then re-records the anchors whose
bytes moved mechanically (`reference_state.fix_references`). With one `document` named, both steps touch
that card and its sidecar only, and the result is `ok` only when no card was refused. On converted memory a
`document` needs no `expected_snapshot`: `CitationOperationScope.validate(document_alone=True)` admits it,
and every legacy operation still validates strictly before it does any work. An unconverted tree takes the legacy citation-table path
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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; this card is grounded in the
package application entry point and resolver contracts.

No configured domain documentation could be checked.

### Repo-Internal References

- Baseline status reports unsuccessful `ok` for unavailable Git history as well as blocked drift, while preserving the owner's payload. [1]
- The baseline owner distinguishes unreadable attribution behind a resolvable HEAD from an unborn repository, retaining the existing drift decision. [2]
- Carryover has one memory subject and forwards it without a ledger-message option. [3]
- Canonical quality scope is owned by the focused scope module. [4]
- Typed quality execution and public run translation are owned by the controller. [5]
- The route-index application entry point forwards resolver-owned authority. [6]
- The route-index builder. [7]
- The route-index builder receives storage authority explicitly in its typed signature. [8]
- The apply entry point that forwards that subject and nothing else. [9]
- Baseline status reports unsuccessful `ok` for unavailable Git history as well as blocked drift, while preserving the owner's payload. [10]
- The baseline owner distinguishes unreadable attribution behind a resolvable HEAD from an unborn repository, retaining the existing drift decision. [11]
- Carryover has one memory subject and forwards it without a ledger-message option. [12]
- The apply entry point that forwards that subject and nothing else. [13]
- Canonical quality scope is owned by the focused scope module. [14]
- Its resolver, which binds a repository to the scope the quality surface runs against. [15]
- The one execution path both the report and the closeout gate run through. [16]
- The curator worklist publication that follows a full scoped call. [17]
- On a converted tree the citation check reports the sidecar references' state instead of reading citation tables. [18]
- On a converted tree the citation fixer authors the cards' citation rows into sidecar references, then re-records mechanically moved anchors; one named document scopes both. [19]
- The one construction point that carries a caller's excludes into all four citation operations. [20]
- The scope object the caller's excludes ride with, validated at construction. [21]
- The refusal rule for a caller exclude that cannot mean anything. [22]
- **The memory initializer now reports the knowledge foundation beside the memory root it scaffolds (`ICR-R29@v1`).** [23]
- **The admission whose location this block reports, so the location a curator is told to populate is the one the bootstrap publishes to.** [24]
- The read that decides the block's state, and the unavailable form its states come from. [25]

- One document with no frozen generation is admitted for converted memory; legacy operations validate strictly. [26]

### Cross-Repo References

The application entry point can target configured sibling repositories, but no external implementation governs
this package-local dispatch contract.

No meaningful cross-repo references found.

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

## 260928-MIK-L37 The Card Writers Stay Unlocked On An Unconverted Line

`citation_fix_tool`, `citation_migrate_tool` and `route_index_refresh_tool` do not ask the cutover lock. They write
onboarding cards and route indexes into a leaf's working tree, never knowledge records and never the database, and
they commit nothing; the closeout that would commit their edits is locked. The decision record DEC-VMMJDN states
this exception to MIK-R24 rule 9 and is linked to the three functions, so a change to one of them raises the
decision's rejected alternative (lock the three tools like every other write) for reconsideration.

- The three card writers, which ask no cutover lock. [27]
