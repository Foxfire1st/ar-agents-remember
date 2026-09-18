# mcp/src/agents_remember/application/ - MCP Application Layer Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/application/`     |
| doc_type               | `route-local-overview`                     |
| lastUpdated | 2026-09-17T03:15+02:00 |
| lastVerifiedCommitHash | `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| lastVerifiedCommitDate | 2026-09-18T04:45:39+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l08` uncommitted source; base `1ff1893f44d875073d58af863238501a6be35288` |
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## IAS Per-Contract Activation Application Boundary

The application layer composes selecting operations around one per-contract activation authority.
An atomic master is not exposed merely because its series contract exists: activation becomes
`reconciling`, that contract's exact code/external-memory bases are synchronized, and only an
exact-current result becomes `active`. The record is keyed by the canonical series contract, not the
protected source pair, so two atomic masters commanded by one sprint and sharing its code/memory
source branches hold independent records: the only activation waiting reason is
`atomic-series-reconciling` for a contract's own in-flight reconciliation, and a foreign master is
never a reason to wait. A retained conflict returns agent-owned continue/cancel guidance and leaves
the integration lock free between calls.

Status observes the stable enclosure-root sync journal independently from task-document health.
Application adapters translate failures into bounded tool results; they do not recreate the journal
from task prose, queue rows, or ambient Git. Task-document mutation remains an upstream application
flow: it publishes canonical truth, invalidates projections for semantic/readiness mutations, and never asks queue or
activation state for permission.

## 260831-LOCR-L37 The Stop-Only Application Boundary

This route gained one application entry point and no authority. `worktree_tools.py::worktree_pause_tool`
admits the configured contract through the shared gate (projecting a refusal under the operation name
`worktree_pause`), builds the same typed `WorktreeArgs` the other contract-addressed entry points build
— the contract path plus `config.orchestration.gate_policy` — and delegates to
`git_worktree_manager.pause_result`. It performs no Git, moves no ref, creates no commit, lands
nothing, writes no ledger row, and runs no auto-land seat hook, because nothing is retired and nothing
is finished.

That shape is the boundary. Every other mutating entry point on this route hands work to a worktree
owner that may publish; this one hands work to a route whose publication modules are structurally
unreachable (see `worktrees/modules/pause.py.md` and `mcp/tests/test_pause_is_not_publication.py`). The
application layer therefore does not decide whether to publish — there is no such decision on this
path to make.

`worktree_pause_tool` is the counterpart of `worktree_checkpoint_landing_tool` on the same file and the
opposite side of it: the checkpoint is the explicitly requested **publication** of an unfinished
master's accumulated line, and the pause is the stop that publishes nothing. Two entry points, two
registered tools, neither reachable from the other.

## CCR-R25 Actionable Refusal Boundary

`worktree_tools.py` routes the existing `RouteReviewError` through one pure refusal projector at
start/admission and direct closeout. With an exact contract the response carries only the
contract-bound `task_doc` operation and arguments; the required review payload remains caller input.
Certification admission preserves every original finding while promoting a route-review finding
through the same projector. These application paths report observed gate outcomes and do not create
reviews, mutate task documents, or provide a fallback authority.

## Current Structural Application Boundary

`application/structural/` translates ambient caller intent and document+role targets into authorized
plane-owned dispatch, messaging, seat management, and gate mutations. Runtime correlations remain
inside the transaction. Ordinary messages are replacement-aware; the initial dispatch brief is the
sole exact-pinned exception. Failed briefing retires a child only when the matching generation is
positively proven unbriefed; unreadable, missing, or contradictory evidence refuses reconciliation
without cleanup. Since 260821-ARSPAWN-L1
`dispatch_agent` resolves the caller by kind (plane seat vs ambient launcher resolved from the
process environment), keeps the plane structural path unchanged, and records caller-kind provenance
(`caller_kind` `plane`/`ambient`) through the `application/terminal_tools.py` spawn primitive onto
the catalog row and the `spawnedByKind` wire field.

ARSPAWN-L2 keeps that public surface but makes its seat transaction idempotent. The structural
child route now composes `dispatch_transaction.py` with the serving-owned per-seat lock and durable
brief evidence. Ordinary messages derive parent/child addresses without requiring a live occupant;
private occupant ids remain an execution detail and are never persisted into a complete structural
destination.

## Durable Lifecycle Application Boundary — detached worker removed

This section previously described `lifecycle/lifecycle_operation_worker.py` as the detached
application owner for closeout and integration, with its own packaged CLI composition root, the
explicit `lifecycle-operation` execution mode, and heartbeat/progress/terminal publication. That
module was deleted by the de-entanglement cut (commit `173bb01e`, "delete the detached lifecycle
worker and drive every fixture on the synchronous path"): the MCP tools now drive
`worktree_closeout_apply` and `worktree_integrate` in-process, and the record advance moved into
`worktrees/integration/lifecycle/lifecycle_operation_store.py`. The `application/closeout_door.py`
door adapter and the `application/lifecycle/legacy_operation_tool.py`,
`lifecycle_enclosure_tools.py` and `lifecycle_status_wait.py` entry points were deleted by the same
cut. There is no detached worker composition root or worker-execution mode on this route.

## Purpose

`application/` owns operation-level MCP composition. Application entry points translate
trusted MCP runtime config plus typed tool arguments into package service calls
and JSON-compatible payload dictionaries. Domain placement follows what a tool
operates on: `task_reopen_tool` cit:([`task_reopen_tool`], mcp/src/agents_remember/application/task_docs/task_reopen.py:20-41) sits beside the task_doc application entry point because it
reopens a task, while worktree_tools keeps only genuine worktree operations (its
abandon now also ends the ambient lifecycle it anchors).

## Hot Path Summary

`worktree_tool_requests.py` carries only code/memory commit messages and landed commits. `worktree_tools.py` forwards that pair unchanged; `memory_tools.py` exposes baseline/carryover cache observations without a ledger commit argument. Adapters do not recreate retired guards or synthesize a third output.

## Detailed Route Context

This route owns the single closed configured-contract admission result/projector and the task-addressed application adapters over lifecycle location, controls, adoption, direct landing, and degraded status. The legacy-repair adapter and the closeout-door adapter were deleted as capabilities by the de-entanglement cut.

For 260731-EFA-L21, `runtime/startup.py` is the trusted MCP declaration boundary: it declares MCP
execution before loading runtime configuration. Dashboard foreground, daemon, and reload-worker
entry paths make the corresponding dashboard declaration in their CLI route. Undeclared linked
worktree entry paths therefore cannot inherit the deployed coordination root.

The current operation surfaces include `context_packet.py` and `coordination_tools.py` for context
assembly and resolver calls; `memory_scope.py` plus `memory_quality/controller.py` and
`memory_quality/runs.py` for canonical quality authority, execution, and bounded run retention;
`memory_tools.py` for drift, citations, route-index, init, baseline, and
carryover; `gate_tools.py` and `hosted_readiness.py` for gate/readiness operations;
`lifecycle/lifecycle_tools.py`, `operator_inbox_tools.py`, and `orchestration_tools.py` for lifecycle, inbox,
and orchestration operations; `runtime/startup.py` and `terminal_tools.py` for startup and terminal
operations; `provider_tools.py` for provider operations; `worktree_tools.py` for worktree operations;
`benchmark_tools.py`, `runtime/install.py`, and `runtime/skills.py` for benchmark, install, and skill
surfaces; `task_docs/task_doc_tools.py` for JSON-primary task-document authoring; `tool_response.py` for response
completion; `worktree_status.py` for status packets; and `read_files.py` for paired source/onboarding
reads. Route-index refresh still resolves context first and forwards repository/storage authority to
the deterministic builder.
Context and worktree application entry points forward `parent_task`/`leaf_id` into the source resolver, and task-doc
authoring writes `seriesContractPath` plus `enclosures[]` instead of the retired `contractPath`.

Contract-scoped memory quality is the curator's pre-closeout worklist over the leaf's dirty code and
memory worktrees. `memory_scope.py` resolves and freezes the exact leaf authority, code/onboarding
roots, and temporary code-base provenance; `memory_quality/controller.py` uses that identity for
both sync and bounded async execution. A bare repository-scoped call still targets official memory
and supplies no invented provenance; commit-derived verification stamps remain closeout-owned.
The `memory_quality/` package is a behavior-preserving ownership split of the former flat
controller and run-registry modules; it creates no facade, compatibility reader, or second quality
API.
**260707-HFX2-L11**: `worktree_tools.py`'s `worktree_integrate_tool`/
`lifecycle_finalize_task_tool` now compose completion-edge landing — after a successful non-dry-run
edge, when `config.retirement.auto_land_on_integration`/`auto_land_on_finalize` is on (both default
ON), `_auto_land_completed_seats` resolves the qualified leaf key and calls
`serving.landing.land_seats_for_leaf` for the edge's own role set (worker/reviewer at integrate,
manager/reviewer at finalize). Matching sessions are marked `status:"landed"` with provenance and
returned as `autoLandedSeats`; tmux sessions are not killed, so the dashboard can show an inspectable
landed archive. The helper body remains best-effort (`except Exception: return []`) so a catalog
fault can never fail an already-succeeded edge — landing is archive bookkeeping riding the edge,
never a gate on it.

## Parameter Objects: This Route Owns The Concepts

260731-EFA-L2 armed `PLR0913` (≤5 arguments) at full strength with no ignore and no `max-args`
override, and this route absorbed a large share of the resulting refactor. An application entry point's arguments
are now named concepts, defined **beside the application entry point that takes them** and imported by the
payload builder and the tool declaration:

| Module | Selected types it defines |
| --- | --- |
| `task_docs/task_ref.py` | `TaskRef` — the repo plus whichever locator a caller holds; shared by `resolve_context_tool`, `worktree_attach_tool`, `worktree_status_tool`. |
| `worktree_tool_requests.py` | `TaskIdentity`, `TaskBases`, `StartExecution`, `OperationControlRequest`, `CloseoutCommitMessages`, `CloseoutApproval`, `FinalizeTaskDocs` (+ `DEFAULT_TASK_BASES`, `DEFAULT_START_EXECUTION`, `PREVIEW_ONLY`, `NO_TASK_DOCS`). `worktree_tools.py` consumes these types and owns operation composition. |
| `memory_tools.py` | `MemoryBranches`, `CarryoverSelection`, `CarryoverCommitMessages` (+ their defaults). |
| `task_docs/task_doc_tools.py` | `TaskDocTarget`, `TaskDocEdit` (+ `NO_EDIT`). |
| `benchmark_tools.py` | `BenchmarkSelection`, `BenchmarkPreparation`, `CodexBenchmarkRun` (+ `ALL_CASES`, `DEFAULT_PREPARATION`, `DEFAULT_RUN`). |
| `provider_tools.py` | `ProviderQueryScope`, `GrepaiRepoScope`, `GrepaiSearchQuery`, `GrepaiTraceQuery` (+ `WORKSPACE_QUERY_SCOPE`, `ALL_INDEXED_REPOS`). |
| `runtime/` | Groups MCP startup, typed runtime-install delegation, and skill deployment without a package facade. |

This is a selected, not exhaustive, inventory. Other direct application-level request/target objects
are defined beside the gate, hosted-readiness, lifecycle, operator-inbox, orchestration, server-startup,
terminal, tool-response, and worktree-status entry points.

Two splits are load-bearing rather than cosmetic and must survive future edits: `CloseoutApproval`
stays separate from `CloseoutCommitMessages` (folding them would let a dry run read as an approved
apply), and `intent_note` stays outside `CarryoverSelection` (it is the approval, not part of what
is carried).

Application-only packing types stop at this boundary. Most MCP declarations keep flat published
signatures and build those objects in their bodies. Memory quality is the deliberate exception: its
strict discriminated request is itself the public contract, so FastMCP publishes one nested
sync/start/poll object and Pydantic rejects mixed mode fields.

## Route Model

- MCP transport lives in `mcp/registration/` (the `@server.tool()` declarations) and the
  `mcp/tools/` package (the payload builders); `mcp/server.py` is process wiring only.
- Application entry points should remain typed operation facades, not generic command
  runners.
- Domain behavior belongs in service modules such as `providers`,
  `worktrees`, `memory_quality`, `memory`, `benchmarks`, and `install`.
- Response shape validation happens after application entry point return through the model
  registry (`models/tools/tool_registry.py`), applied by the `mcp/tools/` payload
  builders. That is the LAST line of defence, not the only one: when a collaborator
  already returns a model or a `TypedDict`, an application entry point passes it through rather than
  re-validating an untyped dump (260731-EFA-L4) — a `ValidationError` raised at
  `model_validate` inside an application entry point lands on the tool path, where nothing catches it,
  whereas a type mismatch at the producer is a pyright error before the code ships.
- A vocabulary an application entry point decides is declared in the owning model/module and imported
  by the consumer, not retyped there (260731-EFA-L4; `FileReadStatus` is the worked example).
  cit:(["FileReadStatus = Literal["], mcp/src/agents_remember/models/read_files.py:20-32; mcp/src/agents_remember/application/read_files.py:44-46)

## Invariants And Boundaries

- Application entry points resolve repo IDs through `McpRuntimeConfig`; they should not
  accept arbitrary source or coordination roots from tool callers.
- Route-index application entry points must pass the resolver-owned repository identity and storage/path-rule
  settings into the kernel builder explicitly; the builder does not infer write authority from a
  filesystem location.
- Contract-scoped quality must measure the leaf memory tree against the leaf code worktree and pass
  the leaf base as unstamped comparison provenance. It must not stamp the dirty tree or give an
  official-memory call a synthetic comparison base.
- Provider, benchmark, and worktree application entry points should call package services
  directly rather than CLI `main(argv)` wrappers.
- Keep each application entry point file scoped by domain; do not rebuild the former
  `runtime/skills.py` focused entry point.
- Launch-capable provider operations re-read the on-disk authority fail-closed
  (containment R1, 260707-HFX-L1); application entry points must never launch providers off
  the boot-snapshot config, while stop/status/cleanup stay ungated.

L14: the task-doc application entry point accepts the additive `orchestrates` field (master-only) through create/set_field, feeding the dashboard's command hierarchy; docs without it are untouched.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two MCP payload builders are declared at these entry points. | "def skills_install_payload("; "def task_reopen_payload(" | mcp/src/agents_remember/mcp/tools/core.py:148-148; mcp/src/agents_remember/mcp/tools/task_doc.py:35-35 |
| `ResponseModel` is the public response-model base. | `ResponseModel` | mcp/src/agents_remember/models/base.py:66-88 |
| `TOOL_RESPONSE_MODELS` is the registry of public response models. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:116-179 |
| Canonical memory scope freezes official/leaf authority, both trees, and optional unstamped comparison provenance. | `MemoryScopeIdentity`; `resolve_memory_scope`; `resolve_leaf_memory_scope` | mcp/src/agents_remember/application/memory_scope.py:27-143 |
| The typed quality controller owns sync/start/poll execution and checklist publication without changing verification metadata. | `run_memory_quality_request`; `start_memory_quality_request`; `poll_memory_quality_request`; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_quality/controller.py:110-120; mcp/src/agents_remember/application/memory_quality/controller.py:111-143; mcp/src/agents_remember/application/memory_quality/controller.py:146-208; mcp/src/agents_remember/application/memory_quality/controller.py:363-441 |
| `route_index_refresh_tool` resolves context and supplies repository/storage authority. | `route_index_refresh_tool` | mcp/src/agents_remember/application/memory_tools.py:254-290 |
| `build_route_indexes` is the deterministic route-index builder. | `build_route_indexes` | mcp/src/agents_remember/kernel/route_index.py:182-230 |
| `worktree_status_packet` returns the `WorktreeSummary` the context packet embeds directly, so the state machine's output is checked at the producer. | `worktree_status_packet` | mcp/src/agents_remember/application/worktree_status.py:61-143 |
| `DriftSummaryPacket`, the typed drift seam `_drift_packet` returns. | "class DriftSummaryPacket(TypedDict):" | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:11-11 |
| `FileReadStatus` is defined in the models type. | `FileReadStatus` | mcp/src/agents_remember/models/read_files.py:29-29 |
| The application read-files entry point imports the wire type and decides the read status. | "from agents_remember.models.read_files import FileReadStatus"; "def _resolve_onboarding(" | mcp/src/agents_remember/application/read_files.py:52-52; mcp/src/agents_remember/application/read_files.py:218-218 |

Worktree start is async (GitHub #53): `worktree_tools.py` transfers the temp
lifecycle settings file to the background setup thread on a `starting` result,
forwards `retry_provider_setup`, and bounds worktree provider setup by
`timeoutCaps.providerSetupSeconds` instead of the docker-control default.

`context_packet.py` carries the opt-in branch-freshness section (GitHub #54):
`include_freshness`/`fetch_timeout` on the request feed
`kernel.git_freshness.read_branch_freshness` for the code and external-memory
repos plus informational computed-ledger status; the default stays
`not-checked` so everyday packets skip the remote fetch.

Gate-policy threading (260703-L8): `worktree_tools.py` resolves
`config.orchestration.gate_policy` and threads it into BOTH the closeout and the
integrate `WorktreeArgs`, so the module-level enforcement guards (closeout's
delegated-gate check, integrate's master-handover seam guard) always evaluate
the configured policy — never the all-human dataclass default. Omitting the
passthrough on either path silently reverts that guard to human-only semantics,
which is exactly the inert-consumer defect adversarial review 3 caught on the
integrate side.

Provider launch containment (260707-HFX-L1, containment R1): the provider,
worktree, and benchmark application entry points all treat the ON-DISK authority settings —
not the boot-snapshot config — as the provider launch authority.
`provider_tools.py` gates watcher `start`/`restart`/`invalidate-indexes` and
the launch-capable GrepAI/CGC query tools (one-shot runner containers) through
`require_provider_launch_authority` — fail-closed `ConfigError` when the disk
disables providers or cannot be read; `stop`/`status`/`shutdown-all` stay
legal. `worktree_tools.py` re-reads the authority before provider setup and
writes lifecycle settings from the LIVE map only when armed, attaching a
`providersAuthority` veto block to the result when the disk vetoed an armed
boot snapshot (the worktree itself is still created). `benchmark_tools.py`
passes the live authority's provider ids as `allowed_provider_ids` on both
benchmark requests, so a case manifest cannot arm providers disabled on disk.

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| Application message transport contains only code and memory. | `CloseoutCommitMessages` | mcp/src/agents_remember/application/worktree_tool_requests.py:111-115 |
| Landing input carries the actual two outputs. | `LandedCommits` | mcp/src/agents_remember/application/worktree_tool_requests.py:119-128 |

## 260731-EFA-L4 — Typed Seams Where An Application Entry Point Meets A Producer

Two application entry points stopped re-validating something a collaborator already returned in a checked
form. The rule is the same in both: a `ValidationError` from `model_validate` inside a
application entry point surfaces from inside an `@server.tool()` handler that has no `except` for one, so
where a producer can be made to hand over a typed value, the mismatch becomes a pyright error
at the producer instead.

**`context_packet.py`.** `worktree=` is now `worktree_status_packet(context.contract_path)`
directly — the projection in `application/worktree_status.py` is signed `-> WorktreeSummary` and
constructs the model itself, so the previous
`WorktreeSummary.model_validate(worktree_status_packet(...))` was validating a model's own
dump. This is the application-side half of a real defect: `models/worktree.py` had hand-copied
six contract vocabularies that had each drifted from the contract's own, and the resulting
`ValidationError` fired here, inside the tool. `test_wire_vocabulary_exhaustiveness.py` records
the measurement — 165 of the 213 `series-contract.md` files on disk (77.5%) made
`context_packet` raise, across seven independent gaps. The vocabulary fix lives in the `models/`
route; what this route contributes is that the seam is now checked at the producer rather than
at runtime here. `_drift_packet` is correspondingly annotated
`-> DriftSummaryPacket` (from `memory_quality.integrity.onboarding_drift_check.models`) instead
of `-> dict[str, Any]`, so both of its returns — `not_checked()` and `run_drift_summary(...)` —
are checked against the shape `models/drift.py` expects.

**`read_files.py`** defines `FileReadStatus` in `models/read_files.py`
(`Literal["found", "missing", "disabled", "unsupported", "not_requested"]`).
`application/read_files.py` imports that alias, and `_resolve_onboarding` is the only function that
decides the value and returns `tuple[FileReadStatus, str | None, bool]`.
cit:([`FileReadStatus`], mcp/src/agents_remember/models/read_files.py:29-29)
cit:(["from agents_remember.models.read_files import FileReadStatus"], mcp/src/agents_remember/application/read_files.py:52-52)
cit:([`_resolve_onboarding`], mcp/src/agents_remember/application/read_files.py:209-238)
`VALID_FILE_READ_STATUSES = frozenset(get_args(FileReadStatus))` is the runtime half, derived from the
alias. The import direction is application → models, so the producer uses the single declared alias
without maintaining a second copy.

The `read_ar_files` status semantics are unchanged and still worth restating, because the alias
now carries them: this is the ONBOARDING lookup outcome, never a source-read condition. Source
presence rides the independent `source` field, which is why `found` alongside a missing
`source` is not a contradiction.

## 260731-EFA-L9 Route Impact

The application layer gained the provider lifecycle runtime
(`application/provider_runtime.py`, moved from `worktrees/modules/provider_teardown.py` and
absorbing `provider_async.py`'s setup launcher/status) and the default `WorktreeServices`
composition (`application/worktree_services.py`) binding the provider, memory-quality, and
citation-guard adapters into the worktrees service ports.

## L23 Structural Admission Translation

Application facades now consume centralized terminal refusal translation and
strict source-lineage projections. Context status validates those facts instead
of retyping them, and ambient attach attribution occurs only after a real
attachment, keeping blocked lineage out of successful lifecycle history.

## 260815-DAG-L3 Ambient Queue Authority (Transitional After CLIVE L2)

`application/closeout_queue.py` remains the hosted authority adapter for the sprint closeout queue.
It resolves the live seat from the terminal catalog, requires a canonical bound task document, and
constructs the internal `QueueActor`; role/task identity is absent from the public request. This
section records the pre-CLIVE queue design. In the L2 candidate, lifecycle recovery and controls
use the root journal, while some selected/in-flight/certified queue states remain transitional.
L3 owns removing that lifecycle-shaped queue schema and completing waiting-only projection.

## 260815-DAG-L4 L4 Application Authority Boundary

Application tools now bind lifecycle requests to configured coordination, task, code-repository, and memory-repository identity before dispatch. Worktree, task-document, topology, and memory entry points route protected mutations through the queue/repository authority plane and reject preview/apply drift.

## 260815-DAG-L14 Sprint-Linkage Route

`application/task_sprint_linkage.py` is the new application owner of the sprint↔master linkage
contract: one atomic `attach_master`/`detach_master` pair, the read-only `linkage_report`
surface, and the moved `validate_completed_master_row` for typed rows. `task_doc_tools` routes
the new operations and carries `linkageFacts` on sprint gets; `task_execution_topology` exposes
the shared `verify_sprint_judgment_ids`.

## 260815-DAG-L16 Seat-Independent Application Route

`application/closeout_queue.py` gains the declared-caller fallback (L16-R2): on
`ambient-seat-unavailable` the request-carried `caller` builds the identical `QueueActor` a seat
would, and a contradicting declared caller refuses. The route-review binding machinery extracted
from `task_doc_tools.py` into `application/task_doc_route_review.py` (L16-R6/R9, facade
re-export), and `application/direct_landing.py` is the error-translating application boundary of
the direct landing operation (L16-R8).

## 260815-DAG-L12 Route Impact

All three task-document writers thread the joined graph titles into the renderer (L12-R1/R4): `task_doc_tools.py` (`_graph_titles_for`/`_batch_graph_titles`), `task_execution_topology.py` (`_authoring_batch_titles`), and `task_sprint_linkage.py` (`_batch_graph_titles`) — publish and preview both label the sprint mermaid diagram with real master/leaf titles; batches without a graph fall back to ref-key labels.


## 260815-DAG-L15 Route Impact

New `application/memory_quality_runs.py` (bounded single-flight background run registry, L15-R7); `memory_tools` gained the async start/poll wrappers (including the `ok`-envelope gate-repair fix); `task_execution_topology`/`task_sprint_linkage` hardened the authoring dialect (served-build preflight, typed judgment-required, move-retargets-edge, node-kind order, `create=False` dry-run locks).

## 260815-DAG Master Full-Gate Repair Route Impact

Seven application modules moved into the new `application/task_docs/` sub-route (task_doc_tools, task_execution_topology, task_sprint_linkage, task_ref, task_reopen, task_doc_queue_scope, task_doc_route_review); importers updated.

## 260821-CLIVE-L1 Application Boundary

Application closeout adapters now preserve raw public observations only until the shared route-aware normalizer returns typed `effectiveInput`. Worktree apply submits validated admission to the lifecycle owner; preview and direct landing return the same effective plan. Typed refusals carry invalid fields, resolved leg state, and a corrected call. The worker rehydrates only accepted effective input and repairs derived recovery projection from operation-journal evidence. Application code neither derives queue selection nor treats queue state as lifecycle evidence.

## 260821-CLIVE-L2 Current Architecture

Current-contract mutation consumers branch only on accepted versus refused admission and reuse the exact accepted contract/location observation. Expected path/read/authority failures are translated once. Degraded status and the explicit legacy bridge are separate because they intentionally inspect unreadable or pre-adoption state; they are not mutation fallbacks.

The committed route now groups these application owners under `application/lifecycle/`. This is a package move, not a second API: configured-contract admission remains the one total mutation boundary, and durable journal authority remains below it in `worktrees/integration/lifecycle/`.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Closed application admission. | `ConfiguredContractAdmission`; `admit_configured_contract`; `admit_configured_terminal_contract` | mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:90-90; mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:96-175; mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:178-273 |
| Configured degraded location projection. | `LifecycleOperationPublicAddress`; `configured_lifecycle_operation_location`; `observe_contract_read_failure`; `primary_operation_projection` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_location.py:26-194 |

## 260821-DAGQC-L2 Quality Controller And Direct-Landing Projection

Memory quality now has one focused application API: `memory_scope.py` freezes configured official
or leaf authority, and `memory_quality/controller.py` owns strict sync/start/poll execution,
complete run identity, checklist publication, capacity guidance, and nondisclosing polling.
`memory_tools.py` no longer repeats that failure family. The lifecycle direct-landing application
boundary separately keeps the closed result outcome authoritative while nesting journal recovery
state.

## 260824-PDLS Final Application Boundary

Public closeout and direct-landing adapters consume the shared configured-contract admission API,
while lifecycle worker service imports are deferred to execution. This keeps failure translation
total at one application boundary and prevents bootstrap import fan-out from pulling the service
graph into test collection.

## MCAR-L02 Structured Curator-Coherence Boundary

`curator_coherence.py` is the configured-contract application seam for the one
`status`/`prepare`/`publish`/`validate` coherence API. It delegates exact record/publication policy
to the closeout integration route and translates that complete domain failure family once. The
memory-quality controller uses the same currentness validator as closeout admission, exposing raw
quality readiness separately from combined `closeoutReady`; it cannot claim combined readiness
while the stable authority is absent or stale.

## MCAR-L03 Exact Memory-Candidate Route

The application plane now separates repository-only official diagnostics from acceptance-eligible
leaf work. Candidate memory quality admits one configured contract pair, preserves it through
async run identity and polling, revalidates around scanning/publication, and exposes the same pair
at closeout apply admission. Public refusal projection retains the named pair field and exact
contract-addressed repair arguments.

## Current CCR Composition And Remaining Authority Gaps

The task publication owner classifies exact field deltas and preflights affected scopes before canonical writes. Route-review and closeout admission now bind current normative task intent and direct evidence dependencies; typed intent refusals stay visible at the application boundary. Detached lifecycle workers and direct worktree paths preserve transaction identity and explicit approval/ref safety; normal closeout/integration do not automatically execute the repository certification profile. The default service graph still exposes explicit quality and memory tooling for callers that request it.

The full memory controller snapshots both working trees with external temporary indexes before scanning and revalidates those exact tree identities before checklist publication. Its `finalFullCatalog` reports executed catalog checks and missing authority; it explicitly supplies no affected-closure plan and cannot create R08 acceptance from checklist readiness. R05 frozen lifecycle admission/finalization, ordinary R16 durable telemetry and complete R07/R08 production orchestration remain unconstructed at this source. Terminal failure translation preserves classified organizational repair and actual Git recovery before supplying an otherwise missing typed rail failure.

## CCR-R18@v1 Task-Addressed Next-Step Bounding

260831-CCR-L18 added `bound_next_step` to `application/tool_response.py`: lifecycle tool responses omit any `nextStep` guidance whose arguments name a different task address than the response's own exact contract/enclosure path. File-level detail lives in that sidecar.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.

## CCR-R12@v5 Current Application Boundary

Application adapters expose transaction previews, applies, observation, and recovery. Normal
closeout commits code, mechanically refreshes and commits substantive external memory when needed, then refreshes the consumer ledger cache;
normal integration publishes a prepared pair under explicit handover/ref authority. Neither path
automatically runs strict code quality, memory quality, selected certification, curator coherence,
or independent review. Full suites remain an explicit developer request.


## Pull-Request Landing Records Through The Same Writer

A pull request lands code on the remote; it never moves refs locally, so `worktree_integrate` cannot
express it. `worktree_tools.py::worktree_record_landing_tool` is the application entry point for that
route. It admits the configured contract through the same refusal projector, builds a
`git_worktree_manager.WorktreeArgs` carrying `landed_code_commit` and `landed_memory_content_commit`, then
calls `git_worktree_manager.record_landing_result`. The point of the
entry point is that it shares `worktree_integrate`'s one contract write
(`worktrees/modules/landing_record.py`), so the terminal `integration` cell has exactly one
definition regardless of how the code landed; a commit that is not reachable from a landing target is
refused, so the cell cannot be set from a commit that landed nowhere.

`worktree_tool_requests.py::LandedCommits` is the parameter object that route owns: `code` is the
commit the PR landed on the protected branch, and the memory output is optional because C-11 carryover
may not have run yet when the landing is recorded — the cleanup guard checks carryover separately and
refuses until it is done.

## Checkpoint Landing Gets Its Own Application Entry Point (260831-LOCR-L30)

The application layer gained a second landing entry point beside the PR tail.
`worktree_tools.py::worktree_checkpoint_landing_tool` admits the configured contract, refuses through
the same projector, builds `WorktreeArgs` with `approved=not dry_run`, the typed `strategy` and the
configured `gate_policy` (the same master-exit seam pass-through `worktree_integrate_tool` uses), and
delegates to `git_worktree_manager.checkpoint_landing_result(args, configured.contract)`.

The entry point is deliberately as thin as its integrate sibling: eligibility, the series authority,
and the recorded state all live below it, and it runs none of the completion-edge work
`worktree_integrate_tool` performs — in particular no `auto_complete_seats` call, because a checkpoint
retires nothing. It is also the only landing entry point that does not need the master to be finished,
which is exactly why it is a separate tool rather than a flag on `worktree_integrate`: a caller that
invokes it has chosen a non-final landing on purpose.

**260831-LOCR-L34 corrected this entry point's published docstring, and the correction is
substantive.** It had said the route drops only the two "master is finished" assumptions; the route
also required a **completed closeout**, which is why it was unreachable in both directions — a partial
master could never satisfy it, and a complete one was refused by the downgrade guard. The docstring now
names the full refusal set (`worktree_integrate` proves the task document `Completed`, one landed
enclosure per canonical leaf, **and a completed closeout**) and states that the checkpoint captures the
master's own live code and memory work-branch tips and proves their Git source ancestry
before landing exactly those. Published text is the only thing a client reads, so it is contract rather
than comment. The preview/apply parity invariant that produced this repair is inventoried on the
`worktrees/overview.md` route and in `memory_quality/overview.md`.

## 260915-KS-L1 Knowledge Composition Seam

This route gained one module, `application/knowledge.py`, and no new authority. It is the composition seam between
admitted authority and the concrete knowledge store, and it is the **only** consumer of
`memory.knowledge` (rank 12) from this layer (rank 21).

What it does: `write_authorship` assigns the provenance envelope's `operation_id` and `recorded_at` rather than
accepting them; `admitted_knowledge_destination` binds a resolved path, namespace and envelope into the typed
handle a storage operation receives; `admitted_revision_request` attaches a draft to that destination so provenance
is **not** a parameter; `initialize_knowledge_namespace` refuses an occupied destination as a resume attempt;
`open_admitted_knowledge_store` opens read-only; and `create_knowledge_revision` delegates the insert and closes in
a `finally`.

What it deliberately does not do: it holds no schema and no durable state, it performs no admission check of its
own (`admitted_knowledge_destination` confers no authority by itself — it exists so the store receives a typed
handle rather than a bare path), and it exposes **no acceptance or promotion operation**. The store manufactures no
acceptance; `state_at_origin` and `acceptance_ref` remain authored data.

The direction is the point and it is what the `layers.toml` charter paragraph records: a lower-ranked owner —
`worktrees` (10) and `memory_quality` (11) among them — receives `models.knowledge` values or an already-prepared
result from this layer, and never imports the storage package.

| Finding | Anchor | Source |
| --- | --- | --- |
| The provenance envelope is assigned here, not accepted from a payload. | `write_authorship` | mcp/src/agents_remember/application/knowledge.py:102-122 |
| The admitted-destination constructor that confers no authority by itself. | `admitted_knowledge_destination` | mcp/src/agents_remember/application/knowledge.py:125-141 |
| Provenance and namespace come from the destination rather than from the request. | `admitted_revision_request` | mcp/src/agents_remember/application/knowledge.py:144-157 |
| Initialization refuses an occupied destination as a resume attempt. | `initialize_knowledge_namespace` | mcp/src/agents_remember/application/knowledge.py:160-190 |
| The read open and the delegating insert, both closing in a `finally`. | `open_admitted_knowledge_store`; `create_knowledge_revision` | mcp/src/agents_remember/application/knowledge.py:193-204; mcp/src/agents_remember/application/knowledge.py:207-221 |
| The layer charter paragraph that fixes the one-way direction this seam implements. | "[package.memory]" | layers.toml:206-222 |
| The storage operation this seam delegates to. | `create_revision` | mcp/src/agents_remember/memory/knowledge/store.py:255-289 |

## 260915-KS-L2 The Graph Operations Join The Seam

The same module gained the graph half's eight operations and eight request builders, and the seam's contract did
not change: the builders attach the destination's `authorship` and `repository_id` exactly as
`admitted_revision_request` does, and each operation opens the admitted destination, delegates to the owning graph
module and closes in a `finally`. The one builder with an extra parameter is `admitted_claim_request`, which takes
the anchor endpoint — naming an existing anchor and recording a new one in the same transaction are different
inputs, and the seam must not collapse them.

**The boundary a later reader most needs is the one that did not move: this module still has no non-test importer
in `mcp/src`.** Its only importers are `mcp/tests/test_knowledge_store.py` and
`mcp/tests/test_knowledge_relation_rules.py`, so its green composed-path test is evidence about the seam's
behaviour, not evidence that the seam is wired into any registered tool or entry point. The typed write boundary
that will consume it is `KS-R03`'s.

| Finding | Anchor | Source |
| --- | --- | --- |
| The graph request builders, all attaching the destination's provenance and namespace. | `admitted_family_request`; `admitted_anchor_request`; `admitted_member_request`; `admitted_claim_request` | mcp/src/agents_remember/application/knowledge.py:327-337; mcp/src/agents_remember/application/knowledge.py:351-360; mcp/src/agents_remember/application/knowledge.py:363-371; mcp/src/agents_remember/application/knowledge.py:374-386 |
| The eight graph operations, each open-delegate-close. | `create_knowledge_family`; `create_knowledge_anchor`; `create_knowledge_family_member`; `create_knowledge_realization_claim`; `remove_knowledge_realization_claim` | mcp/src/agents_remember/application/knowledge.py:423-432; mcp/src/agents_remember/application/knowledge.py:447-456; mcp/src/agents_remember/application/knowledge.py:471-480; mcp/src/agents_remember/application/knowledge.py:495-504; mcp/src/agents_remember/application/knowledge.py:507-516 |
| The graph modules the new operations delegate to. | `create_family_revision`; `create_source_anchor`; `create_family_member`; `create_realization_claim` | mcp/src/agents_remember/memory/knowledge/families.py:133-162; mcp/src/agents_remember/memory/knowledge/anchors.py:49-68; mcp/src/agents_remember/memory/knowledge/memberships.py:88-107; mcp/src/agents_remember/memory/knowledge/realizations.py:61-81 |
| The composed-path case that drives admit -> create -> reopen -> read through this seam. | "test_the_application_seam_authors_a_graph_through_an_admitted_destination" | mcp/tests/test_knowledge_relation_rules.py:566-680 |

## 260915-KS-L3 The Candidate-Write Boundary Joins The Seam

The same module gained the candidate-write boundary, and the seam's contract still did not change: every new
entry point opens the admitted destination, delegates and closes in a `finally`, and provenance keeps coming from
the destination rather than from the payload.

Three additions matter to a later reader:

- **`resolve_candidate_context` / `build_candidate_context` are the only way a batch's dataset precondition is
  built.** The application opens the destination read-only, reads the identity the candidate actually holds
  (`OpenedKnowledgeStore.snapshot_identity()`) and seals the whole resolution into a context digest. A caller
  therefore cannot hand-write the dataset identity its batch will be compared against — `CandidateResolution`
  deliberately has no field for it — and the operation re-derives the seal inside its own transaction.
- **`change_knowledge_candidate` passes `destination.authorship` into the operation as a keyword argument**, so no
  part of a submitted batch can become the stored author, authorization or instant. The batch is a value; the
  authority is the admission's.
- **The two label operations** (`set_knowledge_invariant_label`, `set_knowledge_family_label`) are the same
  open/delegate/close shape over the two guarded label edits.

**The boundary that did not move, and that a later reader most needs: this module still has no non-test importer
in `mcp/src`.** Adding `change_knowledge_candidate` inside `application/knowledge.py` does not give the module an
importer — a `grep` for one is still empty — so the seam's composed-path cases are behaviour evidence about the
boundary and not evidence that it is wired into any tool. The packet makes transport wiring an explicit later
extension, and the worker report's claim that `KS-R03` "resolved" that observation was withdrawn in review.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two label operations the seam exposes. | `set_knowledge_invariant_label`; `set_knowledge_family_label` | mcp/src/agents_remember/application/knowledge.py:224-238; mcp/src/agents_remember/application/knowledge.py:240-250 |
| The context resolution and its pure sealing step. | `resolve_candidate_context`; `build_candidate_context` | mcp/src/agents_remember/application/knowledge.py:252-273; mcp/src/agents_remember/application/knowledge.py:275-301 |
| The batch operation that takes its provenance from the destination. | `change_knowledge_candidate` | mcp/src/agents_remember/application/knowledge.py:303-315 |
| The resolution shape whose missing dataset-identity field makes the read the only source of that value. | `CandidateResolution`; `KnowledgeContext` | mcp/src/agents_remember/models/knowledge/candidate.py:163-414 |
| The lane rules the seam's entry point reaches, and the operation that applies them. | `change_candidate`; `require_writable_lane` | mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/memory/knowledge/candidate.py:83-102 |
| The composed-path case that drives the boundary end to end through this seam. | "test_a_late_invalid_command_rolls_back_every_earlier_insert_in_the_batch" | mcp/tests/test_candidate_batch_transaction.py:62-109 |
| The case that proves the operation refuses a context smuggled past the model seal. | "test_a_context_smuggled_past_the_model_seal_is_refused_by_the_operation" | mcp/tests/test_candidate_batch_transaction.py:1120-1160 |

## 260915-KS-L4 The Snapshot Lifecycle Joins As A Second Seam

The route gained one module, `application/knowledge_snapshot.py`, and no new authority. It is the **second
composition seam**: the candidate lifecycle (create, clone, open, disposal authorization) and snapshot publication
are a different composed operation from the single candidate write, and keeping them apart leaves each entry point
readable as one intent rather than one module with two jobs.

Three things matter to a later reader:

- **The write destination is derived, not passed twice.** `candidate_write_destination` builds the
  `AdmittedKnowledgeDestination` from the admitted candidate's own layout, so a caller cannot write into one
  database and publish another; `admitted_candidate_destination` is the typed handle the admitted-authority path
  calls after its own checks, and it **confers no authority by itself** — it exists so a deserialized request
  cannot become admitted input.
- **Two publication entry points share one contract.** `publish_knowledge_snapshot` freezes and installs one
  candidate's point, while `publish_prepared_knowledge_snapshot` installs an already-frozen stage through the
  *same* path — so a caller that produced a validated closed database (a merged result, an import, a restored
  artifact) reaches a destination atomically against an expected identity, with no second install route to keep
  correct.
- **The read-side gate is exposed, not decided.** `knowledge_publication_state` returns the comparison between a
  live candidate and the closed snapshot a read is about to answer from; the caller decides what to do about a
  difference, because publishing is an explicit operation and no read may publish rows.

**Two non-claims the ruled design made explicit are recorded here because a later reader will look for them.**
This seam **creates no Git commit** — the published snapshot is a closed file, and capturing it into a memory tree
is the existing candidate-tree owner's operation — and **no IAS landing is reachable from it**; the writable
candidate belongs to the experimental master. And the wiring boundary did **not** move: like
`application/knowledge.py`, this module has **no non-test importer in `mcp/src`**, so its composed-path cases are
behaviour evidence about the boundary and not evidence that any tool is wired to it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The admitted-destination constructor that confers no authority by itself. | `admitted_candidate_destination` | mcp/src/agents_remember/application/knowledge_snapshot.py:67-82 |
| The write destination derived from the candidate layout rather than passed twice. | `candidate_write_destination` | mcp/src/agents_remember/application/knowledge_snapshot.py:85-99 |
| The three lifecycle delegations. | `create_knowledge_candidate`; `clone_knowledge_candidate`; `open_knowledge_candidate` | mcp/src/agents_remember/application/knowledge_snapshot.py:102-107; mcp/src/agents_remember/application/knowledge_snapshot.py:110-115; mcp/src/agents_remember/application/knowledge_snapshot.py:118-123 |
| The two publication entry points that share one contract. | `publish_knowledge_snapshot`; `publish_prepared_knowledge_snapshot` | mcp/src/agents_remember/application/knowledge_snapshot.py:134-139; mcp/src/agents_remember/application/knowledge_snapshot.py:142-147 |
| The read-side publication gate exposed rather than decided. | `knowledge_publication_state` | mcp/src/agents_remember/application/knowledge_snapshot.py:150-155 |
| The storage operations the seam delegates to, including the two locks that are never nested. | `create_candidate`; `publish_candidate_snapshot`; `publish_prepared_snapshot` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:85-98; mcp/src/agents_remember/memory/knowledge/publication.py:66-111; mcp/src/agents_remember/memory/knowledge/publication.py:114-170 |
| The disposal verdict whose authority the caller owns. | `authorize_candidate_disposal` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:141-173 |
| The composed-path harness that drives the seam end to end through the public operations. | `build_case`; `publish` | mcp/tests/snapshot_lifecycle_test_support.py:177-205; mcp/tests/snapshot_lifecycle_test_support.py:357-380 |

## 260915-KS-L5 The Merge Joins As A Third Seam

The route gained one module, `application/knowledge_merge.py`, and still no new authority. It is the **third
composition seam**, and it exists for the same reason as the second: a guarded common-base merge is a different
composed operation from a single candidate write, and a different one again from the lifecycle/publication half, so
each entry point stays readable as one intent rather than one module with three jobs. The three seams now divide
this route's knowledge surface cleanly — the write, the lifecycle-and-publication, and the merge — which is why
this module was added rather than more entry points on either sibling.

Two things matter to a later reader:

- **It resolves, merges, and returns the typed value unchanged.** `resolve_knowledge_merge_base` proves the three
  input identities, their structure and the Git base claim, returning the resolution; `merge_resolved_knowledge_
  datasets` runs the guarded merge against a proven base and returns the whole structural outcome, including the
  coverage of both deltas and the publication state when a destination was named. A failure is the storage layer's
  typed refusal, so a caller composing a tool response branches on one code rather than catching an exception.
- **The adapter is callable rather than wired.** No Git merge driver is installed, no attribute is configured and
  no commit is created anywhere on this path: the module is the exact seam a later, separately reviewed change
  would call. That is the requirement's own boundary — this increment supplies evidence and a callable boundary,
  not production configuration.

The result this seam returns carries **no compatibility verdict**: a `structurally_merged` outcome is a statement
about the candidate's structure and nothing about whether the merged knowledge is correct. The wiring boundary also
did **not** move: like its two siblings, this module has **no non-test importer in `mcp/src`**, so its cases are
behaviour evidence about the boundary and not evidence that any tool is wired to it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The base-resolution entry point and its refusal-or-resolution contract. | `resolve_knowledge_merge_base` | mcp/src/agents_remember/application/knowledge_merge.py:36-52 |
| The merge entry point, including the carried statement that the result holds no compatibility verdict. | `merge_resolved_knowledge_datasets` | mcp/src/agents_remember/application/knowledge_merge.py:55-64 |
| The defect the layer below makes unreachable. | `KnowledgeMergeSeamDefect` | mcp/src/agents_remember/application/knowledge_merge.py:67-68 |
| The two storage operations this seam delegates to, in the order the seam exposes them. | `resolve_merge_base`; `require_session_capability` | mcp/src/agents_remember/memory/knowledge/merge_base.py:75-105; mcp/src/agents_remember/memory/knowledge/merge.py:131-163 |
| The vocabulary the seam takes and returns unchanged. | `MergeBaseRequest`; `MergeRequest`; `MergeOutcome` | mcp/src/agents_remember/models/knowledge/merge.py:124-154; mcp/src/agents_remember/models/knowledge/merge.py:189-215; mcp/src/agents_remember/models/knowledge/merge.py:349-391 |
| The unit node that drives the conforming merge end to end through the public operations. | "def test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate(" | mcp/tests/test_knowledge_guarded_merge.py:307-376 |
| The published-file freeze and install contract the merge's last step reuses rather than duplicating. | `freeze_closed_snapshot`; `publish_prepared_snapshot` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:66-109; mcp/src/agents_remember/memory/knowledge/publication.py:114-170 |

## 260915-KS-L6 The Portable Export/Import Joins As A Fourth Seam

The route gained one module, `application/knowledge_export.py`, and still no new authority. It is the **fourth**
composition seam over the experimental knowledge substrate, beside the single candidate write
(`knowledge.py`), the candidate-lifecycle/publication seam (`knowledge_snapshot.py`) and the guarded merge
(`knowledge_merge.py`), and it exists for the same reason as the three before it: exporting and importing a
whole dataset is a different composed operation from any of them, and keeping them apart leaves each entry
point readable as one intent.

- **It hands over and returns unchanged.** `export_knowledge_artifact` and `import_knowledge_artifact` delegate
  to `export_knowledge_dataset` / `import_knowledge_dataset` and return the storage layer's typed result as it
  is, so a caller branches on `state`/`refusal` rather than on an application-level wrapper.
- **Two halves are read-only and produce no database at all.** `validate_knowledge_artifact` answers whether an
  artifact is a complete export of a supported generation and what logical dataset it holds, and
  `canonical_body_of_artifact` returns that dataset's canonical body — **after validating it**, because a body
  is what a comparison is made of and a refused artifact has no identity to compare.
- **A refusal is a value on both halves**, including the file read: `read_knowledge_artifact` returns
  `selected_input_unavailable` for a path it cannot read and `invalid_export` for bytes that are not UTF-8,
  and nothing on this boundary raises an `OSError` or a `UnicodeDecodeError` for a caller to catch.
- **Two non-claims are carried where a reader of the artifact looks for them**: an export is **not** a filtered
  read response and **not** a Markdown projection, and an import creates **no Git commit** and restores **no
  Git ancestry**. Capturing an artifact into a memory tree, or committing a restored database, stays with the
  existing candidate-tree and closeout owner.

The wiring boundary did **not** move: like its three siblings, this module has **no non-test importer in
`mcp/src`**, so its evidence is behaviour evidence about the boundary and not evidence that any tool is wired
to it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The seam's five entry points and the non-claims it carries in its own docstring. | `export_knowledge_artifact`; `import_knowledge_artifact`; `validate_knowledge_artifact`; `read_knowledge_artifact`; `canonical_body_of_artifact` | mcp/src/agents_remember/application/knowledge_export.py:60-63; mcp/src/agents_remember/application/knowledge_export.py:66-74; mcp/src/agents_remember/application/knowledge_export.py:77-96; mcp/src/agents_remember/application/knowledge_export.py:99-109; mcp/src/agents_remember/application/knowledge_export.py:112-126 |
| The defect the layer below makes unreachable. | `KnowledgeArtifactSeamDefect` | mcp/src/agents_remember/application/knowledge_export.py:129-130 |
| The storage operations this seam delegates to. | `export_knowledge_dataset`; `import_knowledge_dataset`; `read_artifact` | mcp/src/agents_remember/memory/knowledge/export_import.py:133-192; mcp/src/agents_remember/memory/knowledge/export_import.py:195-244; mcp/src/agents_remember/memory/knowledge/export_import.py:257-290 |
| The vocabulary this seam takes and returns unchanged. | `ExportRequest`; `ExportResult`; `ImportRequest`; `ImportResult`; `PortableValidation` | mcp/src/agents_remember/models/knowledge/portable.py:36-44; mcp/src/agents_remember/models/knowledge/portable.py:101-133; mcp/src/agents_remember/models/knowledge/portable.py:47-63; mcp/src/agents_remember/models/knowledge/portable.py:136-176; mcp/src/agents_remember/models/knowledge/portable.py:66-98 |
| The nodes that drive the conforming round trip and the filtered-response refusal through the public seam. | "test_a_populated_dataset_round_trips_to_an_equal_logical_dataset"; "test_a_filtered_read_response_cannot_validate_as_a_complete_export" | mcp/tests/test_knowledge_portable_roundtrip.py:356-427; mcp/tests/test_knowledge_portable_roundtrip.py:712-739 |

## 260915-KS-L7 The Selective Read Joins As A Fifth Seam

The route gained one module, `application/knowledge_read.py`, and still no new authority. It is the **fifth**
composition seam over the experimental knowledge substrate, beside the candidate write (`knowledge.py`), the
candidate-lifecycle/publication seam (`knowledge_snapshot.py`), the guarded merge (`knowledge_merge.py`) and the
portable export/import (`knowledge_export.py`), and its subject is a different composed operation again: one
bounded, snapshot-consistent page of the recorded scope a seed names.

**Three boundaries this seam owns, each because getting it wrong is a different kind of wrong:**

- **The read is read-only, and that is how a refusal persists nothing.** The connection is opened through
  `open_read_only_database`, so the strongest statement available is a `SELECT`; "a refused read left the file
  byte-identical" is a property of the handle rather than a rollback the code remembers. `read_row_counts` is the
  measurement half — the same read-only handle, so a caller can take per-table counts before and after a refusal
  and compare.
- **A baseline read needs no task.** `task_ref=None` is served: the seam never resolves a leaf contract, never
  asks an enclosure owner for one and never fabricates a task, because planning has to be able to read recorded
  knowledge before a leaf exists.
- **A continuation is a binding, not a position.** Snapshot, context, selector, policy and schema are checked
  **before the file is opened** — a cursor binding another selection is a defect of the request and not a fact
  about the bytes, and reporting it as a snapshot problem would send the caller to re-select a dataset they
  selected correctly — while the manifest and the position are checked **after** the selection exists, before any
  page is built. No cursor refusal returns a partial page.

**The ordered sequence inside the one connection**: verify the declared snapshot through **three separate
comparisons** (namespace, schema generation, logical dataset — the schema check is its own statement rather than
a corollary of the digest, because a context can keep the file's real digest while declaring another generation);
select the scope; decide the typed absence (`registration_absent` for a path with no recorded claim,
`selector_absent` for an identity the snapshot does not hold, and a **recorded** identity with no memberships and
no claims served as an empty-but-real selection); check the continuation against the selection; cut the page; and
turn a page too small for its next item into `page_budget_too_small` with the exact minimum.

**`open_read_context` is the constructor, and it is what keeps the snapshot honest:** it opens the file
read-only, reads the logical identity the file actually holds and returns a context naming **that** snapshot, so a
caller cannot hand-write the snapshot a read will be verified against — it can only resolve one, and the read
compares that resolution again against the file it opens.

**Two non-claims are carried in the module's own docstring.** Every failure this seam models is a typed refusal
inside the result, but the one class that does **not** reach it is a caller passing an object which is not one of
the two typed models: that is a programming error at the call site rather than a modeled read failure, and the
signature is what the boundary claim rests on. And a caller whose input is rejected must be able to tell an
absence from a malformed input: the seam never reports a path absent for a spelling the read path refused.

The wiring boundary did **not** move: like its four siblings, this module has **no non-test importer in
`mcp/src`**, and the requirement's own boundary is explicit that the public tool name stays separate from the
concrete application function.

| Finding | Anchor | Source |
| --- | --- | --- |
| The seam's three entry points. | `read_knowledge_scope`; `open_read_context`; `read_row_counts` | mcp/src/agents_remember/application/knowledge_read.py:139-192; mcp/src/agents_remember/application/knowledge_read.py:103-136; mcp/src/agents_remember/application/knowledge_read.py:587-602 |
| **The read-only handle, the request-level cursor check before the file is opened, and the ordered sequence.** | `_read_inside_snapshot`; `_select_and_page` | mcp/src/agents_remember/application/knowledge_read.py:195-225; mcp/src/agents_remember/application/knowledge_read.py:228-271 |
| **The three snapshot comparisons, each naming the comparison that fired.** | `_snapshot_identity_refusal` | mcp/src/agents_remember/application/knowledge_read.py:274-313 |
| **The scope-dependent half of the binding, including a position past the end of the selection.** | `_continuation_refusal`; `_manifest_binding_mismatch` | mcp/src/agents_remember/application/knowledge_read.py:316-337; mcp/src/agents_remember/application/knowledge_read.py:496-516 |
| The two absence codes and the recorded-but-empty selection served rather than refused. | `_absence_refusal` | mcp/src/agents_remember/application/knowledge_read.py:357-389 |
| The storage layer this seam delegates to. | `select_recorded_scope`; `page_of_scope`; `anchor_resolver_for` | mcp/src/agents_remember/memory/knowledge/read.py:193-238; mcp/src/agents_remember/memory/knowledge/read.py:762-816; mcp/src/agents_remember/memory/knowledge/read_anchors.py:47-59 |
| The vocabulary this seam takes and returns. | `KnowledgeReadContext`; `KnowledgeReadRequest`; `KnowledgeReadResult`; `KnowledgeReadPage` | mcp/src/agents_remember/models/knowledge/read.py:216-263; mcp/src/agents_remember/models/knowledge/read.py:278-288; mcp/src/agents_remember/models/knowledge/read.py:485-511; mcp/src/agents_remember/models/knowledge/read.py:451-482 |
| **The nodes that drive the task-free baseline read and the binding refusals through the public seam.** | "test_a_baseline_read_serves_a_task_free_context_and_reaches_the_whole_selected_scope"; "test_a_continuation_naming_a_position_past_the_selection_refuses_rather_than_escaping" | mcp/tests/test_knowledge_read_boundaries.py:465-497; mcp/tests/test_knowledge_read_boundaries.py:725-762 |

## 260915-KS-L8 The Comparison Joins As A Sixth Seam

The route gained one module, `application/knowledge_diff.py`, and still no new authority. It is the **sixth**
composition seam over the experimental knowledge substrate, beside the candidate write, the
candidate-lifecycle/publication seam, the guarded merge, the portable export/import and the selective read,
and its subject is a different composed operation again: **one comparison of two named knowledge snapshots
and two named code trees, for one selected invariant or family.**

**Four boundaries this seam owns, each because getting it wrong is a different kind of wrong:**

- **The selection is R07's, run twice.** Each side goes through the one policy on **that side's own**
  read-only connection; the whole of this module's contribution to the selection contract is that a side may
  name its own exact revision (`seed_override`), which is what lets a before revision and an after revision
  be addressed separately.
- **A candidate change invalidates a continuation, because the binding says so.** The cursor binds a digest
  over both declared snapshots, both resolved contexts, both code trees and both selectors, so a candidate
  whose bytes changed has another `after` identity and is refused with `continuation_binding_mismatch`
  rather than continued. **The invalidation is the binding, not a check someone has to remember to write.**
- **A missing side refuses, and no `HEAD` is substituted.** An absent or unreadable database, or a side
  naming a snapshot the file does not hold, is refused by name; nothing here reaches for a working tree, a
  branch or `HEAD`, and the expansion's command names the two **requested** trees.
- **Absence on one side is reported, not raised.** A side whose own selector named nothing recorded still
  leaves the other side's union served, with that side's absence carried in `side_absences` — which is what
  "the removed before-side realization remains in the diff" means at the seam. The operation refuses
  outright only when **neither** side selected anything, and that refusal names the side that earned it.

**The ordered sequence, and the two properties that make it safe.** Both files are opened read-only; **both
sides are verified before either is selected** (namespace, schema generation, logical digest — three
separate comparisons per side, with the schema check its own statement rather than a corollary of the
digest), so a union can never be built from one verified snapshot and one file that turned out not to be the
snapshot it declared. And the **request-level** cursor bindings — policy, selector digest, display filter —
are decided **before** the comparison binding, so a caller who changed the question is told that rather than
being sent to re-select a dataset they selected correctly. No cursor refusal returns a partial page.

**`open_diff_side` is the constructor, and `diff_row_counts` is the measurement half.** A side can only be
*resolved* from the identity the file actually holds, so a caller cannot hand-write the snapshot a side is
verified against; and the row counts are taken through the same read-only handle, so "a refused comparison
persisted nothing" is measured rather than asserted. The two database paths are separate arguments from the
sides on purpose: **a side is an identity and a path is where the bytes currently are.**

**The non-claim is the module's own docstring, in the form the requirement wrote it.** The comparison reports
facts and comparisons of facts; it does not rank, score, approve, certify neutrality or decide that a change
has no consequence, and **it has no field that could** — which the boundary module measures over the
serialized response. A filtered or partial response declares its limits and cannot claim the complete
semantic review it did not perform.

The wiring boundary did **not** move: like its five siblings, this module has **no non-test importer in
`mcp/src`**, and no MCP tool name is introduced here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The seam's four entry points. | `diff_knowledge_scope`; `open_diff_side`; `git_tree_difference_probe`; `diff_row_counts` | mcp/src/agents_remember/application/knowledge_diff.py:199-253; mcp/src/agents_remember/application/knowledge_diff.py:128-159; mcp/src/agents_remember/application/knowledge_diff.py:162-196; mcp/src/agents_remember/application/knowledge_diff.py:826-841 |
| **The ordered body: verify both sides before either selection, select each side with the one policy, compare, collect absences, refuse an empty union, display, page.** | `_select_and_compare`; `_select_side` | mcp/src/agents_remember/application/knowledge_diff.py:397-460; mcp/src/agents_remember/application/knowledge_diff.py:482-498 |
| **Both sides verified before either is selected, and the three comparisons inside each.** | `_any_side_snapshot_refusal`; `_side_snapshot_refusal` | mcp/src/agents_remember/application/knowledge_diff.py:463-479; mcp/src/agents_remember/application/knowledge_diff.py:744-777 |
| **The binding computed before either file is opened, and the per-side effective selector it digests.** | `_binding`; `_effective_selector` | mcp/src/agents_remember/application/knowledge_diff.py:310-327; mcp/src/agents_remember/application/knowledge_diff.py:330-333 |
| **The cursor check order: policy, selector, filter, then the snapshot pair.** | `_cursor_mismatch` | mcp/src/agents_remember/application/knowledge_diff.py:709-741 |
| **The page arithmetic: the comparison total on every page, the cumulative returned, and the display's own two numbers beside it.** | `_page` | mcp/src/agents_remember/application/knowledge_diff.py:501-545 |
| The per-side absence vocabulary and the recorded-but-empty selection served rather than refused. | `_side_absences`; `_side_absence_refusal`; `_selector_is_recorded` | mcp/src/agents_remember/application/knowledge_diff.py:556-627 |
| The four input classes a failed read is mapped onto. | `_reading_failure` | mcp/src/agents_remember/application/knowledge_diff.py:256-279 |
| **The nodes that drive the real candidate write, the missing side, and the substituted-snapshot refusal through the public seam.** | "test_a_candidate_that_changed_after_a_continuation_refuses_the_continuation"; "test_a_missing_side_refuses_and_substitutes_no_other_snapshot"; "test_a_side_naming_another_snapshot_of_its_own_file_refuses_before_any_page" | mcp/tests/test_knowledge_diff_boundaries.py:325-363; mcp/tests/test_knowledge_diff_boundaries.py:303-322; mcp/tests/test_knowledge_diff_boundaries.py:438-475 |


## 260915-KS-L10 The Generation Registry Reaches The Seam

This leaf changed no authority in this route and added no module, but two of the helpers the seam calls now
behave differently and a reader of `application/knowledge.py` must not assume the old behaviour.
`read_row_counts` (`knowledge_read.py`) and `diff_row_counts` (`knowledge_diff.py`) previously iterated the
**pinned generation-1 table list**; they now resolve the **selected generation from the dataset they open**
(`generation_of_database`) and iterate *that* generation's tables and columns, which is what makes a
generation-2 dataset's coverage and row counts describe the dataset rather than the build. The composition
seam's own contract is unchanged: it still confers no authority, still assigns the provenance envelope rather
than accepting one, still exposes no acceptance or promotion operation, and `application` remains the only
consumer of `memory.knowledge` from this layer.

**One consequence worth stating plainly for a caller**: a dataset created through this seam now declares
**generation 2** (`CURRENT_GENERATION`), so a freshly initialized namespace is a generation-2 dataset with six
more tables than the generation-1 files earlier leaves produced. Opening either kind works — the open path
selects the generation from the file's own `PRAGMA user_version` — but an operation that compares two datasets
refuses a **mixed-generation** pair before any session exists rather than silently skipping the tables one side
lacks.

| Finding | Anchor | Source |
| --- | --- | --- |
| The read-side row counts now resolve the dataset's own generation instead of the build's table list. | `read_row_counts` | mcp/src/agents_remember/application/knowledge_read.py:587-603 |
| The diff-side row counts do the same, so coverage describes the dataset it measured. | `diff_row_counts` | mcp/src/agents_remember/application/knowledge_diff.py:826-842 |
| The generation selector both now call, and the declaration a created store makes. | `generation_of_database`; `CURRENT_GENERATION` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:282-282; mcp/src/agents_remember/memory/knowledge/schema_generations.py:310-327 |

## 260915-KS-L11 The Facet Selection Joins As A Sixth Seam

The route gained one module, `application/knowledge_facets.py` — the layer's thirty-second Python module
and the sixth seam — and no new authority. It is the **sixth composition seam** beside `knowledge.py`, `knowledge_snapshot.py`, `knowledge_merge.py`,
`knowledge_export.py` and `knowledge_read.py`, and it is a seam rather than more entry points on the read
because the facet aggregate is a **different selection**: `read_facet_scope` declares its own policy name
(`authored-judgment-facets/v1`), takes one seed and returns one complete page, and it shares no code path
with `KS-R07@v1`'s recorded-scope read.

Three boundaries the module owns, and the reason each is the shape it is:

- **The read-only handle is how "a refused facet read persisted nothing" is structural.** The connection is
  opened through `open_read_only_database`, so the strongest statement available is a `SELECT`; the property
  is a fact about the handle rather than a rollback the code has to remember.
- **The declared snapshot is verified before anything is selected, in three separate comparisons** —
  namespace binding, schema generation, logical dataset — each returning `snapshot_unavailable` with
  expected and observed as facts. A context describing another dataset is refused by name rather than
  answered from whatever bytes the path happens to hold.
- **The selection is complete or it refuses.** A selection past `FACET_SELECTION_ITEM_LIMIT` becomes the
  shipped `selection_incomplete` carrying its count and bound; there is no cursor, so a caller never
  receives a page it could read as the whole aggregate when it is not.

**One distinction a later reader must not flatten:** a seed naming nothing recorded is `selector_absent`,
while a *recorded* facet record with no attachments and no supersession edges is a real page reporting zero
counts. The module reads that fact (`seed_recorded`) rather than inferring it from an empty item list, so
"nothing is there" and "the record is there and carries nothing yet" stay different answers.

**The wiring boundary did not move:** like its five siblings this module has no non-tool importer in
`mcp/src`, so its cases are behaviour evidence about the seam rather than evidence that it is reachable from
a registered tool. `read_facet_scope` is in the module's `__all__`, and no MCP tool name was introduced.

## Update History
- 2026-09-18T02:37:44+00:00: Generated citation repair: `generation_of_database`; `CURRENT_GENERATION` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:310-327; mcp/src/agents_remember/memory/knowledge/schema_generations.py:282-282. No content impact: mechanical anchor-range projection bound to citation source snapshot d211cfd02f11c0600198b11c621aa5574ac8743db6e0ca1d2c92936e561c5146; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T00:25+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): recorded the route's **sixth composition seam**, `application/knowledge_facets.py` — one context, one seed, one complete page, under its own declared policy `authored-judgment-facets/v1`. The body states the three boundaries the module owns (the **read-only handle** that makes "a refused read persisted nothing" structural; the **three snapshot comparisons** run before any selection, each naming expected and observed; and the **complete-or-refused** selection with no cursor), the distinction a reader must not flatten (**a seed naming nothing is `selector_absent`, while a recorded record with no attachments is a real page with zero counts**, read from `seed_recorded` rather than inferred from an empty list), and gives the seam its correct position in the running count, since the module's own docstring numbers it the fifth while naming five predecessors. The wiring boundary is re-recorded because it did **not** move: no non-tool importer in `mcp/src`, no MCP tool name, and no shared code path with `KS-R07@v1`'s selection — which is why a shipped seed's serialized page stays byte-identical. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): **route meaning changed for two helpers, with no new authority.** `read_row_counts` and `diff_row_counts` no longer iterate the pinned generation-1 table list: they resolve the **selected generation from the dataset they open** and iterate that generation's tables, so a generation-2 dataset's coverage and row counts describe the dataset rather than the build. The body records that the seam's own contract is unchanged (no authority conferred, provenance assigned rather than accepted, no acceptance or promotion operation, still the only consumer of `memory.knowledge` from this layer), that a namespace initialized through this seam now declares **generation 2** so it carries six more tables than the generation-1 files earlier leaves produced, and that opening either kind works because the open path selects the generation from the file's own `PRAGMA user_version` while a **mixed-generation** comparison refuses before any session exists. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): stamped the untimestamped Update History entries with this document's own commit clock
- 2026-09-17T03:31:11+02:00 — **Historical stamp carried from the incoming official line** (merge HEAD `12bd7fd3`; the live stamp for this file is the later synced value in the metadata table above, which closeout re-stamps): `lastUpdated` 2026-09-15T00:56:17+00:00; `lastVerifiedCommitHash` `806649b91bdce18f7b915bfbbf6727967f4e7a88`; `lastVerifiedCommitDate` 2026-09-16T12:23:53+02:00; `reviewedWorkingCandidate` `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`.

- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): recorded the route's **sixth composition seam**, `application/knowledge_diff.py` — one comparison of two named knowledge snapshots and two named code trees — and the four boundaries it owns: **R07's selection run twice** with the per-side exact-revision address as the only addition to the selection contract; **the binding as the invalidation** (a candidate whose bytes moved presents another `after` identity and is refused rather than continued, so the invalidation is not a check someone has to remember to write); **a missing side refuses with no `HEAD` substituted**; and **one side's absence reported rather than raised**, with the operation refusing outright only when neither side selected anything. It records the two properties that make the ordered body safe (**both sides verified before either is selected**; the request-level cursor checks decided **before** the comparison binding, so a caller who changed the question is told that), the three separate snapshot comparisons per side, the page arithmetic that keeps the comparison total and the display's two numbers apart, the four typed failure classes the read maps, `open_diff_side` as the constructor that stops a caller hand-writing a side's identity, and `diff_row_counts` as the measurement half of the persisted-nothing property. It carries the module's own non-claim in the requirement's words — the comparison has **no field that could** rank, score, approve or decide neutrality, which the boundary module measures over the serialized response — and records that the wiring boundary did **not** move: like its five siblings the seam has **no non-test importer in `mcp/src`** and introduces no MCP tool name. Every storage-layer citation in the L7 section above was re-derived, because the L8 docstring insertion moved `read.py`'s anchors. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.

- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): recorded the route's **fifth composition seam**, `application/knowledge_read.py`, and the three boundaries it owns: the **read-only handle** that makes "a refused read persisted nothing" structural (with `read_row_counts` as the measurement half), the **task-free baseline read** that never fabricates a leaf, and the **cursor as a binding** whose request-level checks run before the file is opened while its manifest and position checks run where the selection exists — with no cursor refusal ever returning a partial page. The card records the ordered sequence and the three separate snapshot comparisons (namespace, schema generation, logical dataset) where the schema check is its own statement rather than a corollary of the digest, the two absence codes with the recorded-but-empty selection served rather than refused, and `open_read_context` as the constructor that stops a caller hand-writing the snapshot a read is verified against. It carries the seam's two non-claims in the module's own terms (every modelled failure is a typed refusal, while a caller passing a non-model object is a programming error at the call site; and a caller must be able to tell an absence from a malformed input) and records that the wiring boundary did **not** move — like its four siblings the seam has no non-test importer in `mcp/src`. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l07`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.

- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): recorded the fourth composition seam — `application/knowledge_export.py` — and why the portable export/import boundary is its own module rather than more entry points on any sibling: the four seams now divide the knowledge surface into the write, the lifecycle-and-publication, the merge, and the portable artifact, so each entry point stays readable as one intent. The card records the five entry points (two pure delegations, the read-only validation that produces **no database at all**, the value-or-refusal file reader whose two failures carry different codes, and the body that is handed out only for an artifact the validator accepted), the two non-claims the ruled intent made explicit (an export is not a filtered read response or a Markdown projection; an import creates no Git commit and restores no Git ancestry), and the wiring boundary that did **not** move: like its three siblings, this module has no non-test importer in `mcp/src`. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l06`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): recorded the third composition seam — `application/knowledge_merge.py` — and why the guarded common-base merge is its own module rather than more entry points on either sibling: the three seams now divide the knowledge surface into the write, the lifecycle-and-publication, and the merge, so each entry point stays readable as one intent. The card records the resolve-then-merge pair returning the storage layer's typed values unchanged, the carried absence of any compatibility verdict, and the non-claim the ruled design made explicit: **the adapter is callable rather than wired** — no Git merge driver, attribute or commit exists on this path, and activation is an explicit later change. The wiring boundary is re-recorded because it did not move: like its two siblings, this module has no non-test importer in `mcp/src`. Verification metadata remains closeout-owned.

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): recorded the second composition seam — `application/knowledge_snapshot.py` — and why the lifecycle/publication half is its own module rather than more entry points on `application/knowledge.py`: each entry point stays readable as one intent. The card records the derived write destination (so write and publish cannot name different files), the two publication entry points sharing one install contract, and the read-side gate being exposed rather than decided. **Two non-claims are stated rather than left to inference**: the seam creates no Git commit (capturing a published file into a memory tree is the existing candidate-tree owner's operation) and no IAS landing is reachable from it. The wiring boundary is re-recorded because it did not move: like `application/knowledge.py`, this module has no non-test importer in `mcp/src`. Verification metadata remains closeout-owned.
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base
  `27242ecb`): recorded the candidate-write boundary joining the seam — the context resolution that reads the live
  dataset identity and seals it (the only way a batch's precondition is built, because `CandidateResolution` has no
  dataset-identity field), the batch operation that takes `destination.authorship` so a payload cannot supply
  provenance, and the two label operations — and re-recorded the boundary that did **not** move: the seam still has
  no non-test importer in `mcp/src`, adding a function inside the module does not create one, and the worker
  report's "resolved" claim about that observation was withdrawn in review. Verification metadata remains
  closeout-owned.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base
  `60e0820e`): recorded the graph operations joining the seam — eight builders that attach the destination's
  provenance and namespace exactly as the revision builder does, eight open-delegate-close operations, and the one
  builder that takes the anchor endpoint because naming an anchor and recording one are different inputs — and
  recorded the boundary that did not move: the seam still has **no non-test importer in `mcp/src`**, so its
  composed-path test is behaviour evidence and not wiring evidence, and the consuming write boundary is `KS-R03`'s.
  Verification metadata remains closeout-owned.

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base
  `67b21aeb`): recorded the new `application/knowledge.py` composition seam — assigned rather than parameterized
  provenance, the typed admitted-destination handle that confers no authority, the occupied-destination refusal, the
  absent acceptance/promotion operation, and the one-way import direction the `layers.toml` charter paragraph
  fixes. Verification metadata remains closeout-owned.

- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Corrected application argument/result routing, record landing and checkpoint authority. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.

- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: added the stop-only application boundary to the body. The
  route gained `worktree_pause_tool`, which admits the configured contract, builds the same typed
  `WorktreeArgs` its siblings build and delegates to `git_worktree_manager.pause_result` — performing no
  Git, no ref move, no commit, no landing, no ledger write and no auto-land hook, because nothing is
  retired and nothing is finished. Recorded that this is the one mutating entry point here whose
  delegate cannot reach a publication module, so the application layer makes no publish-or-not decision
  on that path, and that it is the counterpart of `worktree_checkpoint_landing_tool` on the opposite
  side of the pause/publication split. Verification metadata remains closeout-owned; no acceptance
  claim.
- 2026-09-13T14:24:00+02:00 — 260831-LOCR-L36 activation re-keying: corrected the IAS application
  boundary from one source-pair activation authority to the per-contract activation record — each
  canonical series contract owns its record, sibling masters sharing a protected source pair never
  wait on one another, and the only waiting reason is `atomic-series-reconciling` — with no shipped
  document quoted by this route claim. Source documentation only; verification metadata remains
  closeout-owned and no acceptance or test claim is made.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:15+00:00 — 260831-LOCR-L34: recorded the corrected `worktree_checkpoint_landing_tool`
  docstring on this route — the published text had omitted the completed-closeout requirement, which
  was the reason the route was unreachable — and pointed to the preview/apply parity invariant
  inventory on the worktrees route overview and in `memory_quality/overview.md`. Content change, not a
  range repoint; verification metadata remains closeout-owned and no acceptance claim is made.
- 2026-09-12T02:55+02:00 — 260831-LOCR-L30 checkpoint landing: recorded the new
  `worktree_checkpoint_landing_tool` entry point on this route, its admission/argument/delegation
  shape, why it runs no completion-edge work, and why it is a separate public tool rather than a flag
  on `worktree_integrate`. Content change, not a range repoint; verification metadata remains
  closeout-owned.
- 2026-09-11T23:05:00+00:00: Pull-request landing curation: recorded the new `worktree_record_landing_tool` entry point and its `LandedCommits` parameter object, and why it shares the single landed-integration writer with `worktree_integrate` instead of writing the integration cell itself. Content change, not a range repoint.
- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: rewrote the "Durable Lifecycle Application Boundary" section from the deleted detached worker to the in-process synchronous route, removed the deleted legacy-repair and closeout-door adapters from the hot-path summary, and recorded the deletions of `application/closeout_door.py` and the `application/lifecycle/` worker, legacy-tool, enclosure-tool and status-wait entry points. Only cut-affected claims were reconciled; this route's other claims were not re-read in this pass, so verification metadata remains pinned. Source documentation only; no acceptance or certification claim.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-10T02:27:58+02:00 — CCR-L42 parity curation: No route impact: curator preparation and closeout now run the shared sidecar and route body/history validators independently; this route's ownership and source semantics remain unchanged. No acceptance claim is made.
- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: recorded the unified route-review refusal boundary across application start/admission, certification, and direct closeout. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `worktree_status_packet` repointed to mcp/src/agents_remember/application/worktree_status.py:61-143. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.



- 2026-09-05T07:22+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Corrected task/memory package paths and semantic invalidation; recorded exact tree revalidation, profile service composition, and remaining R05/R16/R07/R08 gaps. Verification records source review, not execution or acceptance.
- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: recorded the `bound_next_step` task-address guard in `tool_response.py`.


- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: re-anchored the controller row of the application overview (run/start/poll/attach to 98-108/111-143/146-208/363-441) shifted by the CCR-R08 +57-line controller insertion. Citation-only re-anchor; no content impact.


- 2026-08-29T21:46+02:00 — MCAR-L03: documented exact-pair admission, async revalidation, and
  closeout application reporting. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — MCAR-L02 A005: added the configured curator-coherence application
  boundary and shared memory/closeout readiness join. Verification remains closeout-owned.

- 2026-08-26T12:30+02:00 — 260821-ARSPAWN-L2 final curation: narrowed failed-dispatch cleanup to
  positively proven pre-brief generations and recorded unknown-state reconciliation refusal. No
  test execution is claimed.

- 2026-08-26T12:30+02:00 — 260821-ARSPAWN-L2 route impact: structural dispatch now composes one
  canonical-seat transaction with bounded evidence-based retry, and structural messages remain
  addressable through vacancies. Verification remains closeout-owned.

- 2026-08-26T08:55+02:00 — Finalized the IAS source-pair application boundary label against the
  frozen pass-13 candidate.

- 2026-08-25T17:21+02:00 — Reconciled the final admission, failure-projection, and deferred-import
  boundaries. Verification remains closeout-owned.

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: reconciled the final `memory_quality/` package split, moved the preserved sidecars, and verified the route against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is not Dagger certification.

- 2026-08-24T21:43+02:00 — File-size route refresh: extracted the worktree request/default concept
  owner from the operation facade. One model definition remains; operation behavior and public tool
  packing are unchanged. Verified at source commit `23d35f77`.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: added the canonical quality scope/controller route and authoritative direct-landing outcome projection. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: recorded the `application/lifecycle/` package layout, repointed current source evidence, and verified the governed L2 route at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: route claims reconciled to accepted candidate tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 route impact: `application/structural/agent_tools.py` resolves the dispatch caller by kind (plane vs ambient launcher from the process environment) and records caller-kind provenance through the `application/terminal_tools.py` spawn primitive (`spawnedByKind` wire field + catalog row); the plane structural path is unchanged. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: the task-doc authoring modules moved to the new `application/task_docs` sub-route. Verified at code commit e5cb139f.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: new memory_quality_runs registry, async start/poll quality wrappers, preflight + typed-refusal authoring dialect, create=False dry-run locks. Verified at code commit de3a0fd9.



- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   L12 title threading across the task-doc, topology-authoring, and sprint-linkage writers (publish + preview). Verified at code commit b7f2c8e2.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 route impact: closeout-queue application boundary gains
  the declared-caller fallback; route-review binding extracted to
  `application/task_doc_route_review.py`; `application/direct_landing.py` added. Verified at code
  commit a9d50e08.


- 2026-08-20T05:04+02:00 — 260815-DAG-L14 route impact: new `application/task_sprint_linkage.py`
  owns the atomic sprint↔master linkage operations; `task_doc_tools` routes them and carries
  `linkageFacts`; `task_execution_topology` shares the judgment verifier. Verified at code commit
  8071a644.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: `task_doc` dropped the removed
  `migrate_execution_topology` operation (`author_execution_graph` now bootstraps graph-less
  sprints), sprint creation scaffolds the empty canonical planning registers with write-time shape
  validation, and structural manager dispatch surfaces an atomic-sequential lane-blocked series
  bootstrap as a `StructuralOutcome` payload; the application-route model is unchanged.
  Verification remains closeout-owned.
- 2026-08-19T08:55+02:00 — 260815-DAG-L11 route impact: `task_reopen_tool` moved from
  `task_doc_tools.py` into the new `application/task_reopen.py` module (facade re-export keeps the
  surface stable), and `task_doc` gained the `author_execution_graph` operation dispatched to
  `task_execution_topology.py`; the application-route model is unchanged. Verification remains
  closeout-owned.
- 2026-08-18T12:00:00+00:00 — No route impact: L9 adds `inventory_execution_topology` (read-only pre-migration enumeration) to `task_execution_topology.py`; the application-route model is unchanged.
- 2026-08-18T09:10+02:00 — No route impact: renamed the atomic 'barrier' concept to 'blocker' throughout; route purpose unchanged.

- 2026-08-17T12:30+02:00 — No route impact: 260815-DAG-L5 extended the lifecycle-operation worker with repair evidence; the application-layer purpose is unchanged.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-15T11:25+02:00 — L3 static-gate route impact: extracted task-doc queue-scope
  classification into a focused application owner while retaining the dispatcher as the sole
  locked publication entry point.
- 2026-08-15T11:07+02:00 — L3 Dagger repair: task publication now derives queue governance from
  commanded graph scope while leaving genuinely standalone/light documents ungoverned; lifecycle
  diagnostics retain typed queue refusal status.
- 2026-08-15T09:10+02:00 — 260815-DAG-L3 route impact: recorded ambient queue authorization and
  lifecycle-operation correlation as application-owned translations. Verification remains
  closeout-owned.

- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: the application owner keeps
  explicit migration fail-closed and now has forcing proof for invalid migration envelopes,
  unresolved or wrong-kind targets, and out-of-repository authoring. An unreachable duplicate
  validation translation was removed rather than exempted from coverage.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: the application policy now treats
  master aliases as cross-document authority, revalidating every affected sprint on supported
  identity edits or master-kind replacement and returning structured migration classifications
  through the same owner.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1 route impact: `task_execution_topology.py` is the new
  application owner for exact cross-document topology validation and finite atomic migration;
  `task_doc_tools.py` delegates rather than duplicating that policy.
- 2026-08-14T06:25+02:00 — L23 final candidate review: task/worktree entry points now enforce
  candidate-bound route review and transitive source lineage at admission and exit while the
  detached lifecycle worker remains the sole long-operation application composition root.
  Verification provenance remains closeout-owned.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: routed startup/runtime-install/skill-install through the new cohesive `application/runtime/` child overview and preserved direct domain imports instead of a facade. Verification metadata remains closeout-owned.

- 2026-08-13T00:00+02:00 — 260731-EFA-L23 post-closeout worker-authority repair: documented the detached lifecycle-operation declaration before service/config loading and its deliberate non-daemon boundary. The owner reports 46 focused tests, Ruff clean, and diff-check clean. Verification remains closeout-owned.
- 2026-08-12T20:20+02:00 — L23 curator: documented application ownership of lineage refusal/status translation; verification remains closeout-owned.
- 2026-08-12T16:52+02:00 — 260731-EFA-L23 packaged-worker route review: the detached CLI now owns
  default worktree-service composition before task-addressed dispatch, closing the installed-worker
  unbound-service failure while preserving the application/worktree port split. Verification
  provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: added the detached durable lifecycle application owner and exact recovery boundary; verification provenance remains closeout-owned.

- 2026-08-11T14:40+02:00 — Recorded the current pre-closeout memory-quality boundary: a leaf-scoped
  call compares unstamped cards from the contract's code base against the dirty worktree, while
  official-memory calls do not invent provenance and closeout still owns real-commit stamps.

- 2026-08-10T19:57:55+02:00 — 260731-EFA-L21 route impact: recorded declaration-before-config-load
  at the MCP application startup boundary and its separation from undeclared linked-worktree CLI
  execution. Verification metadata remains pinned until closeout stamps the L21 code commit.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 route impact: recorded the provider-runtime and
  worktree-services composition additions. Verification metadata pinned until closeout stamps the
  L9 code commit.

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: corrected the task-reopen anchor, expanded the
  hot-path inventory, marked parameter examples as selected, and reversed the FileReadStatus ownership
  claim to match the model/application source split.

- 2026-08-02T20:33+02:00 — 260731-EFA-L6 curator W1-B03 final-index reconciliation: post-S31 final-index movement repaired the one stale `route_index_refresh_tool` citation range (`application/memory_tools.py:266-266` → `:288-288`) using warm snapshot `a4f8c991b75ef019cd8b5f10c1daa9d41694df6116b569453bd0815b4efa2817`; scoped fix/recheck recorded zero source reads, tokenization, parsing, and build. Verification metadata remains pinned until closeout.

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 6 citation rows and 1 prose citation with exact anchors and source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: route moved. `mcp/src/agents_remember/controllers/` was renamed to `application/` and `worktrees/status.py` moved in as `application/worktree_status.py`, so this route overview and all 14 child sidecars moved with the source. Adopted the leaf's vocabulary throughout: the package is "the application layer" and one function is "an application entry point". Route model, tool surface and behavior are unchanged — the old name was MVC vocabulary that described nothing about the contents. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:26+02:00 — 260731-EFA-L4 curator: **body corrected.** Added the route-impact
  section above for the two changed controllers, plus two invariants the route now follows but did
  not state: pass through a collaborator's already-checked value instead of re-validating its dump
  (because a `ValidationError` inside a controller lands on the uncaught tool path), and declare a
  controller-decided vocabulary in the controller and let the wire model import it. Recorded
  `context_packet.py`'s `worktree=worktree_status_packet(...)` passthrough — verified
  `worktrees/status.py:worktree_status_packet` is signed `-> WorktreeSummary` — and `_drift_packet`'s
  `-> DriftSummaryPacket` annotation. Recorded `read_files.py` as the new home of `FileReadStatus`
  and `VALID_FILE_READ_STATUSES`, with `_resolve_onboarding` typed to it, and flagged the
  models→controllers import direction explicitly with the no-cycle check I actually ran (imported
  `agents_remember.models.read_files` standalone; `controllers/read_files.py` has no
  `models.read_files` import). The 165-of-213 figure is quoted from
  `test_wire_vocabulary_exhaustiveness.py`'s module docstring, which is where it is measured; the
  vocabulary repair itself is a `models/` route fact and is documented there. Added three reference
  rows to the 2-column table. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: added the **Parameter Objects** section — the new
  `task_ref.py` module and the concept types each controller now defines — and corrected the Route
  Model's transport line: the `@server.tool()` declarations left `server.py` for the new
  `mcp/registration/` package. Verification metadata pinned until closeout stamps the L2 code
  commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: `memory_tools.py` now forwards the resolved code
  repository identity and storage/path-rule authority into deterministic route-index generation.
- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 route impact: controller overview now documents
  `_auto_land_completed_seats`, `serving.landing.land_seats_for_leaf`, the `auto_land_on_*` gates,
  and `autoLandedSeats`; successful completion lands chats for archive inspection instead of
  retiring them. Verification metadata pinned until closeout stamps the HFX2-L11 commit.
- 2026-07-08T02:43+02:00 — 260707-HFX-L8 route impact (seat lifecycle: retirement + live identity +
  turn-state, issue #12): `worktree_tools.py`'s integrate/finalize controllers gained a completion-edge
  auto-retire composition (`_auto_retire_completed_seats`, config-gated default ON, best-effort —
  the ENTIRE retire body is exception-guarded, widened in the R2/F1 fix round so a catalog I/O fault
  can never fail an already-succeeded edge) returning `autoRetiredSeats` on both tool results. The
  controller still stays a typed operation facade — retire mechanics live in `serving/retire.py`, this
  is composition only. Verification metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-07T16:50+02:00 — 260707-HFX-L1 route impact (provider containment R1): `provider_tools.py`
  gates launch-capable watcher actions and query tools on the live on-disk authority
  (`require_provider_launch_authority`, fail-closed; stop/status/shutdown-all ungated),
  `worktree_tools.py` re-reads the authority before provider setup (live-map settings when armed,
  `providersAuthority` veto block otherwise, worktree creation unaffected), and
  `benchmark_tools.py` threads the live provider-id set as `allowed_provider_ids` into both
  benchmark requests. Verification metadata pinned until closeout stamps the HFX-L1 commit.

- 2026-07-06T23:59:58+02:00 — L14 route impact (body): task_doc_tools carries the additive master-only `orchestrates` field end-to-end. Verification metadata pinned until closeout stamps the L14 commit.

- 2026-07-06T23:59:30+02:00 — 260703-L14 (visual hierarchy + chat grouping) route impact: `task_doc_tools.py` added `orchestrates` to the `set_field` whitelist (`_MUTABLE_FIELDS`) — a flat string list, master-only via the schema backstop. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T03:20+02:00 — No route impact: 260703-L9 reuses `_guards.require_repo` unchanged as the repo allow-list boundary for the new `serving/notes.py` API; no controller changed.
- 2026-07-05T19:10+02:00 — 260703-L8 route impact (cycle 6, small): `worktree_integrate_tool` now threads `config.orchestration.gate_policy` into integrate `WorktreeArgs` (mirroring the closeout path), so the integrate-side master-handover guard evaluates the configured policy instead of the all-human dataclass default. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T12:32+02:00 — No route impact: 260703-L4 only threads
  `config.orchestration.gate_policy` through `worktree_tools.py` into closeout
  args; controller boundaries and public controller responsibilities are
  unchanged. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-03T00:35+02:00 — L11 route impact: task_reopen_tool joins task_doc_tools (task domain); worktree_abandon_tool ends its anchored ambient lifecycle.
- 2026-07-02T18:35+02:00 — No route impact: operations-integration L7 fixed the native argv inside the
  typed `cgc_dependencies` wrapper (`provider_tools.py`) from the stale `analyze dependencies` to the
  current `analyze deps` subcommand. The controller surface, tool names, and response envelope are
  unchanged, so the route model this overview describes is unaffected (detail in the file sidecar).
  Verification metadata pinned until closeout stamps the L7 commit.
- 2026-06-29T22:57+02:00 — No route impact: `task_doc_tools.py` gained the `remove_subtask` op (CRUD
  delete: drop the master row + delete the leaf doc unless `keep_file`); the controller stays a typed
  operation facade, so the route model is unchanged (detail in the task_doc_tools.py file sidecar; task
  260629_post-landing-cleanup L2).
- 2026-06-29T21:24+02:00 — No route impact: `task_doc_tools.py` now refuses `kind="light"` and defaults
  an absent `kind` context-awarely (subTask under a leaf contract, else master); the controller stays a
  typed operation facade, so the route model this overview describes is unchanged (detail in the
  task_doc_tools.py file sidecar; task 260628_post-landing-cleanup).
- 2026-06-28T22:41+02:00 — No route impact: operations-integration L1 extracted `read_files.py`'s path-confinement + sidecar-pairing helpers into `kernel/sidecar_pairing.py` (behavior-preserving; `read_ar_files` re-imports them under their former private names). `read_files.py` stays a typed operation facade and no controller signature/surface changed, so the route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the L1 code commit.
- 2026-06-26T20:18+02:00 — Task 21 route impact: `task_doc_tools.py` remains the task-document authoring
  controller and now also composes same-root leaf-to-master row sync through the task service layer.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T16:15+02:00 — No route impact: re-verified `task_doc_tools.py`
  against the source-branch `replace` controller (`_replace` preserves the existing JSON path and
  refuses slug/kind path drift); lifecycle-gate API consolidation does not change the controller
  route model.
- 2026-06-26T15:33+02:00 — No route impact: task 25 preserves `task_doc_tools.py`'s
  source-branch `replace` operation; lifecycle-gate API consolidation does not change the controller
  route model, and operation-level detail remains in file sidecars. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: controllers now route `parent_task` and `leaf_id` through context/worktree operations, and `task_doc_tools.py` creates `seriesContractPath` plus `enclosures[]` references instead of the retired `contractPath`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T23:04+02:00 — Dashboard task 14 adds `lifecycle_finalize_task_tool` to `worktree_tools.py`. The controller remains a typed operation facade: it confines coordination paths, builds `FinalizeArgs`, and delegates branch-edge proof, cleanup verification, and task-document reconciliation to `worktrees/modules/finalize.py`.
- 2026-06-23T01:40+02:00 — No route impact: slice 07b v1, `read_files.py` now passes `repo.repo_id` to `emit_read_packet` so the `read.packet` carries `data.repoId`; the controller stays a typed operation facade delegating emission to the `observer` service, so the route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-23T00:53+02:00 — No route impact: slice 07 S5 retargets the `read_files.py` compact-reset docstring only — the `compact-reset.json` producer is deferred to the post-3.0 agentic-control-plane (no session-hook producer), with the consumer (`_maybe_reset_served`) + `refresh=true` kept as defensive scaffolding; no controller signature or behavior changed, so the route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-22T22:33+02:00 — Slice 07: added `read_files.py`, the `read_ar_files` controller (paired source+onboarding batch reads of ≤5 repo-relative paths, with its own path-confinement guard, route-index onboarding lookup, session-deduped overview front-door, and facts-only `read.packet`); added it to the Hot Path Summary. It stays a typed operation facade — resolution lives in the controller so a later dashboard `GET /api/files` route can reuse it — so the route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-19T07:23+02:00 — No route impact: slice 3c R5 adds a `dry_run` param + a `_preview` helper to `task_doc_tools.py` (renders + diffs the would-be doc and returns `rendered`/`diff`/`wouldLose` without writing); the controller stays a typed operation facade, so the route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:03+02:00 — No route impact: slice 3c R4 adds `statusNote` to `_MUTABLE_FIELDS` and drops the master-only guard on `set_section` (a leaf may upsert freeform sections; the schema validator backstops) in `task_doc_tools.py`; the controller stays a typed operation facade, so the route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T05:15+02:00 — No route impact: slice 3c R3 adds `codeExamplesNote` to `_MUTABLE_FIELDS` in `task_doc_tools.py` so `set_field` can record the deferred-examples note; the controller stays a typed operation facade, so the route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-14T00:16 — No route impact: slice 3c commit 3 adds master ops (`set_subtask`/`set_section`) + master `create` handling to `task_doc_tools.py`; the controllers stay typed operation facades, so the route model this overview describes is unchanged (detail in the file sidecar).
- 2026-06-13T22:34 — Slice 3c commit 1: added `task_doc_tools.py`, the op-dispatched controller behind the `task_doc` authoring tool (load/create the `ar-task-document/v1` JSON, apply one edit, re-render the markdown); added it to the Hot Path Summary. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T18:45+02:00 — No route impact: slice 2c adds the observer-attribution wiring to `worktree_tools.py` (`_attribute_start`/`_attribute_attach` driving `ambient().promote`/`attach`); the controllers stay typed facades delegating behavior to the `observer` service, so the route model this overview describes is unchanged (detail in the file sidecar).
- 2026-06-11T06:47+02:00 — Issue #62 worktree-only closeout: `worktree_tools.py` dropped the `direct_closeout_*` controllers, so the Hot Path Summary now describes it as the worktree-operations facade only.
- 2026-06-10T09:56+02:00 — No route impact: sub-task D adds `worktree_sync_tool` as another typed worktree operation facade in `worktree_tools.py` (path confinement + forwarding); the route model this overview describes is unchanged (detail in the file sidecar).
- 2026-06-10T09:30+02:00 — No route impact: sub-task B's `worktree_tools.py` change is a plumbing-only forward of `stale_base_choice` into `WorktreeArgs`; the controller surface this overview describes is unchanged (detail in the file sidecar).
- 2026-06-10T08:39+02:00 — GitHub #54 sub-task A: `context_packet.py` gained the opt-in freshness section (`include_freshness`, kernel-backed code/memory branch freshness, `ledgerMapsCodeHead`).
- 2026-06-10T07:40+02:00 — GitHub #53: `worktree_tools.py` start controller hands the temp lifecycle settings file to the background setup thread (skip-unlink on a `starting` result), forwards `retry_provider_setup`, and bounds worktree provider setup by `timeoutCaps.providerSetupSeconds` instead of the docker-control default.
- 2026-06-06T03:43: Re-verified against the current controller surface (9 files incl. `_guards.py` and per-domain tool modules); corrected `mcp/tools.py` references to the `mcp/tools/` package; re-stamped to `7123da56`.
- 2026-05-28T19:52+02:00: Created after the MCP controller surface split out of the former `skill_tools.py` mega-facade.
