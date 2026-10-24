# mcp/src/agents_remember/application/memory_tools.py

## Governing Overview

[Application layer overview](overview.md)

## Purpose

`memory_tools.py` is the typed application entry point surface for onboarding drift, citation work,
route-index refresh, memory initialization, baseline adoption, and memory carryover. Memory-quality
scope, execution, and async control now belong to the dedicated typed controller.

Provides the memory-facing application entry points and the ordinary leaf writer guard. Citation fixing and route-index apply also share one measured pre-baseline admission on the configured converted memory root.

`memory_init_tool` scaffolds the memory root and reports the measured knowledge state; it does not author
knowledge. For a complete resolved tree reported as `not-recorded` or `recorded`, the next action names
that state and asks the developer to start the Architect, which runs the foundation as a regular task
with a Curator. A nonlegacy `PublishedIntentUnavailable` answer retains its measured state, dataset path,
code and detail and uses the same handover. This can include `unusable` from unavailable publication; it
is distinct from a resolved partial index, whose next action remains to repair the named knowledge files
and rebuild their derived index. Admission failures keep their own next action, and legacy-format
publication keeps conversion guidance. The handover neither invokes a role nor retires the separately
registered knowledge-bootstrap CLI.

## Code Commentary

### Logic

`drift_check_tool` binds the application-owned converted base when the call names a contract, so a leaf
that deleted a file carries that anchor as carried and stale rather than refusing it as newly written;
without a contract the base is the memory checkout's converted `HEAD`, as the converted check already
does. On an existing unconverted directory, `drift_check_tool` returns `ok=false`,
`status: "error"` and the shared `legacy_format_refusal` message before measuring drift.
`memory_baseline_status_tool` reports `ok=false` for `blocked-drift`, `blocked-invalid`,
`blocked-legacy-cards`, `unavailable` and `legacy-format`.
The baseline owner returns `unavailable` when an existing memory HEAD resolves but its Git
attribution history cannot be read. An unborn converted repository can remain `ready`
under the existing drift rules; an existing unconverted directory receives `legacy-format` first. This adapter preserves the owner's state and details; cache-file availability does
not become a new admission requirement.

`CarryoverApplyOptions` contains the approval intent and explicit review selections, not a memory commit subject. The apply adapter forwards those fields to the converted worktree import and sets `ok` from whether its state is `refused`. Carryover creates no commit and refreshes no ledger; baseline adoption remains the separate attributed-commit producer.

The module defines three parameter objects for separate application contracts: `MemoryBranches` carries optional source/work branch overrides for baseline adoption; `CarryoverSelection` carries the repository, exact target contract, memory/code refs, base and replacement choice; `CitationOperationScope` carries only `document` or `documents`. `intent_note` remains a separate apply approval argument.

`CitationOperationScope.documents` admits a finite fix list beside singleton `document`. Both selectors together, an empty list and a list over `MAX_CURATOR_SOURCE_CANDIDATES` refuse before resolving trees; that shared constant is the only list bound. Only fix passes `allow_documents=True`; check rejects a multi-card selector. Each fix member has singleton authoring/refresher semantics, and a refused member does not prevent other named cards from being processed. No snapshot or caller-exclusion operand remains. Unconverted check/fix refuse instead of acquiring or repairing legacy citations.

Converted fixing forwards each selected document to card authoring and reference repair, excluding authoring-refused sidecars from mechanical refresh. This internal exclusion set protects refused cards; it is not a caller-glob interface. The removed `_citation_trees`, citation source-index build and internal citation migration helpers supply no fallback.

Citation selection is application-owned. The CLI and registered fixer construct the same document-only scope; converted reference authoring and mechanical refresh remain distinct stages. Neither public surface exposes legacy snapshot, caller-exclude, source-index-build or migration operands.

Memory-quality resolution, checklist composition, sync/start/poll control, and public run outcomes
were extracted to `application/memory_scope.py` and `application/memory_quality/controller.py`.
This module no longer implements or wraps that failure family. Its remaining operations retain
their existing configured-authority and typed parameter-object boundaries.

`route_index_refresh_tool` then forwards the resolver-owned code root, onboarding root, repository
identity and storage authority into `build_route_indexes`.
Ordinary drift reads file no temp report (`DriftSummaryOutput(write_report=False)`). The curator checklist is the
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
`document` needs no `expected_snapshot`: `CitationOperationScope.validate(allow_documents=True)` admits the fixer selection; check uses the default single-document validation. Source-index and internal migration operations are removed. An unconverted
tree receives `ok=false`, `code: "legacy-format"` and the shared conversion guidance from
`legacy_format_refusal` for both check and fix, including fix dry runs. There is no legacy
citation-table check/fix fallback. Route-index apply also refuses unconverted memory;
its `dry_run=true` preview is preserved. These refusals do not depend on converted memory
elsewhere. The existing contractless pre-baseline admission still requires a converted root.

### Conventions

Application entry points translate validated tool arguments into service calls and JSON-compatible payloads.
Path confinement and repository authorization use the shared `kernel/authority` helpers
(`require_repo`, `require_within_coordination`) rather than local
filesystem checks.

### Invariants And Boundaries

- Tool callers cannot supply arbitrary source, onboarding, coordination, or storage roots.
- Memory quality must route through the dedicated scope/controller API; this general memory module
  must not re-grow quality scope, registry, or checklist implementations.
- Route-index refresh must forward resolver-owned repository and storage authority explicitly; it
  must not reconstruct path rules from directory layout or parser defaults.
- A drift read is read-only content and files no per-call report; it must not re-grow quality scope, registry, or checklist implementations.
- Effectful refresh/init/baseline operations act by default and expose `dry_run` for preview;
  carryover remains an explicit plan/apply operation.

### Todos

None known for the MX-FIX-4 application entry point boundary.

### Role Runtime and Scope

When a task-scoped config has replaced repo.memory_root with a leaf root, `_refuse_official_memory` obtains the original configured repository only after `require_configured_contract_repositories` proves repository lineage and candidate worktree identity. That guard remains the ordinary leaf route. Without a contract, the existing fixer and route-index apply admit only a declared repository whose resolved memory root is the declared converted root, has no attributed baseline, and has no linked memory worktree. An unreadable worktree list refuses. The result names `admission: pre-baseline`; a failed condition writes nothing.
Unconverted format names the shared conversion procedure; other admission failures
retain their missing-condition and leaf-route guidance. Once a baseline exists the contractless write is refused. This is a card/index admission, not permission to author knowledge or to commit.

Both converted fixer admissions use the same authoring and mechanical-refresh composition. Sidecars of cards refused by authoring are excluded from mechanical refresh, so neither stage changes that card or its sidecar. Successful siblings may still be authored; a refused run is not a claim that the whole bootstrap is complete.

## MIK-R46 R8: refusal envelope at the application boundary

The shared `_carryover_legacy_refusal` accepts an operation name (default `memory_carryover_apply`) and uses generic unconverted-memory guidance for either source or target. The MCP plan adapter supplies `memory_carryover_plan`; the lower application plan retains its raised format refusal. This changes envelope labeling, not layout admission, guards or commit authority.

`memory_carryover_apply_tool` catches only a `RuntimeError` recognized by `is_legacy_format_refusal`; other runtime errors are re-raised. `_carryover_legacy_refusal` returns `ok=false`, `state=refused`, code `legacy-format`, one short refusal `message`, full rule text in logged `detail`, and conversion/retry guidance in `nextAction`/`nextStep`. Matching converted source/target versions now enable carryover through the exact recovery-leaf authority route. Format mismatches and unrelated authority errors are not this recognized legacy refusal and still raise; the adapter reports `ok=false` for a returned `state=refused`. This is not a catch-all error envelope or a new commit producer.

The unconverted `citation_fix_tool` whole result now explicitly carries `nextAction=citation_fix`, matching its delivered projection. It still refuses before citation authoring/refresh; the converted card-writer and pre-baseline admissions retain their boundaries.


## Evidence

Inherited numbered findings [3], [12], [9], [13], [36], [20], [21], [26], [27] retain their separate historical custody; no currentness is inferred from those inherited targets. The source-bound account below distinguishes surviving owners from the legacy implementation removed by this task. Removed projection, source-index and prepared-continuation captions are not retained as executable behavior.

- Carryover options forward approval intent and explicit review selection without a commit subject. [37]

- The carryover adapter forwards converted worktree import, derives ok from refused state and translates only the recognized legacy RuntimeError. [38]

- Converted fixing authors selected cards then refreshes references, excluding authoring-refused sidecars. [39]

- The document-only scope refuses conflicting, empty or oversized selections; only fix admits a multi-card list. [40]

- The converted fixer and route-index apply retain ordinary leaf and measured pre-baseline admissions. [41]


### Docs References

No Domain Documentation source is configured for this repository; this card is grounded in the
package application entry point and resolver contracts.

No configured domain documentation could be checked.

### Repo-Internal References





### Cross-Repo References

The application entry point can target configured sibling repositories, but no external implementation governs
this package-local dispatch contract.

No meaningful cross-repo references found.

### Runtime Source References


## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-DAGQC-L2 Quality Ownership Extraction

The quality-specific authority, complete execution identity, bounded registry orchestration, and
checklist publication moved to `memory_scope.py` and `memory_quality/controller.py`. This leaves
`memory_tools.py` focused on the other memory operations and prevents each transport/application
caller from reimplementing the controller's failure vocabulary.

## KS-R23@v1 The Citation Responses Name Their Ruler

The surviving citation-fix entry point returns the measurement's ruler beside its counts:
`citation_fix_tool` attaches `measuring_build_stamp()` to its response, so the repair counts identify the serving ruler rather than being attributed to the candidate code. The old internal citation-migration entry point is removed.

That the repair engine belongs to the *measuring* machinery is the reason it is stamped at all: a count
produced by a fixed serving build while the candidate carries different code cannot show a fix to that
machinery. The citation-fix response retains the measuring-build identity. The ordinary leaf writer guard and measured pre-baseline admission remain; `_citation_trees` and the internal migration route do not.

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

This L37 exception is historical and superseded by MIK-R46@v2. `citation_fix_tool`
refuses unconverted memory in every mode; `route_index_refresh_tool` refuses apply
while preserving its read-only preview. The MCP `citation_migrate` tool and CLI
`memory-citations --migrate` option are unregistered; the internal migration function is now removed, not a supported workaround. The prior
DEC-VMMJDN exception does not authorize any of these writes on unconverted memory.

### Current Source-Inspection References

- Baseline status reports unsuccessful `ok` for unavailable Git history as well as blocked drift, while preserving the owner's payload. [1]
- The baseline owner distinguishes unreadable attribution behind a resolvable HEAD from an unborn repository, retaining the existing drift decision. [2]
- Carryover has one memory subject and forwards it without a ledger-message option. [3]
- Canonical quality scope is owned by the focused scope module. [4]

- Typed quality execution and public run translation are owned by the controller. [5]

- The route-index application entry point forwards resolver-owned authority. [6]

- The route-index builder uses explicit repository and storage authority. [7]


- The route-index builder receives storage authority explicitly in its typed signature. [8]

- The apply entry point that forwards that subject and nothing else. [9]
- Baseline status reports unsuccessful `ok` for unavailable Git history as well as blocked drift, while preserving the owner's payload. [10]
- The baseline owner distinguishes unreadable attribution behind a resolvable HEAD from an unborn repository, retaining the existing drift decision. [11]
- Carryover has one memory subject and forwards it without a ledger-message option. [12]
- The apply entry point that forwards that subject and nothing else. [13]
- Canonical quality scope is owned by the focused scope module. [14]
- Its resolver, which binds a repository to the scope the quality surface runs against. [15]

- This controller function revalidates the scope, calls the scoped memory-quality check and composes its result. [16]


- The controller attaches the curator checklist and enclosure-local worklist for the full scoped publication. [17]


- On a converted tree the citation check reports sidecar references instead of reading citation tables. [18]

- The shared converted fixer authors references, then refreshes mechanical moves, excluding every authoring-refused sidecar; one named document scopes both stages. [19]
- The shared construction point applies caller excludes to legacy Trees branches, not converted check/fix. [20]
- The scope object the caller's excludes ride with, validated at construction. [21]
- **The memory initializer now reports the knowledge foundation beside the memory root it scaffolds (`ICR-R29@v1`).** [23]
- **The admission whose location this block reports, so the location a curator is told to populate is the one the bootstrap publishes to.** [24]
- The read that decides the block's state, and the unavailable form its states come from. [25]
- One document with no frozen generation is admitted for converted memory; legacy operations validate strictly. [26]
- The three card writers, which ask no cutover lock. [27]
- Frozen implementation of _refuse_official_memory supporting the stated file behavior. [28]
- Frozen implementation of _leaf_memory_writer_scope supporting the stated file behavior. [29]
- The drift tool binds the leaf's converted base with a contract, else the checkout HEAD. [30]
- Contractless writes share the measured declared-root, converted-format, no-baseline and no-linked-worktree admission; every failed condition names the leaf route. [31]

- This application function selects pre-baseline admission or the ordinary leaf contract. Its pre-baseline and unconverted-refusal returns explicitly add measuring_build_stamp(); its converted-leaf return calls _citation_fix_result. [32]

- Route-index apply uses the same pre-baseline admission; scoped operations still use the resolver-owned roots and storage. [33]
- Finite fix selection is validated before reads with the shared bound. [34]

- The operation-specific shared legacy refusal preserves short-message/full-detail conversion guidance; only recognized caller RuntimeErrors are translated. [35]
- The public apply catches only the recognized legacy refusal; success and converted-target refusal remain distinct. [36]

- Memory initialization reports the foundation without authoring records. Complete resolved states and nonlegacy unavailable publication name the measured state before the Architect/regular-task/Curator handover; partial-index repair, legacy conversion and admission refusals retain their distinct next actions. [42]
