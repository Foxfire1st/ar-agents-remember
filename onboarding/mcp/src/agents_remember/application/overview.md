# mcp/src/agents_remember/application/ - MCP Application Layer Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/application/`     |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-08-13T08:47+02:00 |
| lastVerifiedCommitHash | `28a66feae742bf02fe4b647388b220f921cc7007` |
| lastVerifiedCommitDate | 2026-08-15T03:44:49+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Current Structural Application Boundary

`application/structural/` translates ambient caller intent and document+role targets into authorized
plane-owned dispatch, messaging, seat management, and gate mutations. Runtime correlations remain
inside the transaction. Ordinary messages are replacement-aware; the initial dispatch brief is the
sole exact-pinned exception and failed briefing retires the unbriefed child.

## Durable Lifecycle Application Boundary

`lifecycle_operation_worker.py` is the detached application owner for closeout and integration.
Its packaged CLI entry is also the operation process's composition root: it builds and binds the
default `WorktreeServices` before dispatch, so installed workers use the real adapters without
requiring an ambient MCP server binding.
Before that service/config load, the entry declares the explicit `lifecycle-operation`
execution mode. This admits only the detached plane-owned task worker to live operation authority;
it does not claim MCP or dashboard daemon ownership and does not weaken ordinary checkout CLI
isolation.
It loads the task contract and durable accepted input, reconstructs the captured gate policy and
candidate identity, delegates to the existing synchronous lifecycle implementation, and publishes
heartbeat/progress/terminal evidence. Recovery stays attached to the same accepted operation after
agent or process replacement; callers never supply the private operation key or worker PID.

## Purpose

`application/` owns operation-level MCP composition. Application entry points translate
trusted MCP runtime config plus typed tool arguments into package service calls
and JSON-compatible payload dictionaries. Domain placement follows what a tool
operates on: `task_reopen_tool` cit:([`task_reopen_tool`], mcp/src/agents_remember/application/task_doc_tools.py:1006-1027) sits beside the task_doc application entry point because it
reopens a task, while worktree_tools keeps only genuine worktree operations (its
abandon now also ends the ambient lifecycle it anchors).

## Hot Path Summary

For 260731-EFA-L21, `runtime/startup.py` is the trusted MCP declaration boundary: it declares MCP
execution before loading runtime configuration. Dashboard foreground, daemon, and reload-worker
entry paths make the corresponding dashboard declaration in their CLI route. Undeclared linked
worktree entry paths therefore cannot inherit the deployed coordination root.

The current operation surfaces include `context_packet.py` and `coordination_tools.py` for context
assembly and resolver calls; `memory_tools.py` for drift, memory quality, route-index, init, baseline,
and carryover; `gate_tools.py` and `hosted_readiness.py` for gate/readiness operations;
`lifecycle_tools.py`, `operator_inbox_tools.py`, and `orchestration_tools.py` for lifecycle, inbox,
and orchestration operations; `runtime/startup.py` and `terminal_tools.py` for startup and terminal
operations; `provider_tools.py` for provider operations; `worktree_tools.py` for worktree operations;
`benchmark_tools.py`, `runtime/install.py`, and `runtime/skills.py` for benchmark, install, and skill
surfaces; `task_doc_tools.py` for JSON-primary task-document authoring; `tool_response.py` for response
completion; `worktree_status.py` for status packets; and `read_files.py` for paired source/onboarding
reads. Route-index refresh still resolves context first and forwards repository/storage authority to
the deterministic builder.
Context and worktree application entry points forward `parent_task`/`leaf_id` into the source resolver, and task-doc
authoring writes `seriesContractPath` plus `enclosures[]` instead of the retired `contractPath`.

Contract-scoped memory quality is the curator's pre-closeout worklist over the leaf's dirty code and
memory worktrees. `memory_tools.py` supplies the contract's code-base commit only as temporary
comparison provenance for unstamped cards, so changed claims reopen before a real code commit exists.
A bare repository-scoped call still targets official memory and supplies no invented provenance;
commit-derived verification stamps remain closeout-owned.
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
| `task_ref.py` (new) | `TaskRef` — the repo plus whichever locator a caller holds; shared by `resolve_context_tool`, `worktree_attach_tool`, `worktree_status_tool`. |
| `worktree_tools.py` | `TaskIdentity`, `TaskBases`, `StartExecution`, `CloseoutCommitMessages`, `CloseoutApproval`, `FinalizeTaskDocs` (+ `DEFAULT_TASK_BASES`, `DEFAULT_START_EXECUTION`, `PREVIEW_ONLY`, `NO_TASK_DOCS`). |
| `memory_tools.py` | `MemoryBranches`, `CarryoverSelection`, `CarryoverCommitMessages` (+ their defaults). |
| `task_doc_tools.py` | `TaskDocTarget`, `TaskDocEdit` (+ `NO_EDIT`). |
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

**These types stop at this boundary.** The MCP tool declarations in `mcp/registration/` keep flat
published signatures and build these objects in their bodies, because FastMCP derives each tool's
JSON schema from the Python signature — a model-typed tool parameter would republish the tool as a
nested object for every client.

## Route Model

- MCP transport lives in `mcp/registration/` (the `@server.tool()` declarations) and the
  `mcp/tools/` package (the payload builders); `mcp/server.py` is process wiring only.
- Application entry points should remain typed operation facades, not generic command
  runners.
- Domain behavior belongs in service modules such as `providers`,
  `worktrees`, `memory_quality`, `memory`, `benchmarks`, and `install`.
- Response shape validation happens after application entry point return through the model
  registry (`models/tool_registry.py`), applied by the `mcp/tools/` payload
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
| The two MCP payload builders are declared at these entry points. | "def skills_install_payload("; "def task_reopen_payload(" | mcp/src/agents_remember/mcp/tools/core.py:144-144; mcp/src/agents_remember/mcp/tools/task_doc.py:33-33 |
| `ResponseModel` is the public response-model base. | `ResponseModel` | mcp/src/agents_remember/models/base.py:41-60 |
| `TOOL_RESPONSE_MODELS` is the registry of public response models. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:116-179 |
| Leaf memory scope carries the optional unstamped comparison base; the contract path supplies the leaf's real code base while bare official scope leaves it absent. | "class MemoryScope:"; "def _leaf_memory_scope(" | mcp/src/agents_remember/application/memory_tools.py:42-57; mcp/src/agents_remember/application/memory_tools.py:120-178 |
| `memory_quality_check_tool` passes that comparison provenance into the full quality runner without changing verification metadata. | `memory_quality_check_tool` | mcp/src/agents_remember/application/memory_tools.py:217-292 |
| `route_index_refresh_tool` resolves context and supplies repository/storage authority. | `route_index_refresh_tool` | mcp/src/agents_remember/application/memory_tools.py:438-460 |
| `build_route_indexes` is the deterministic route-index builder. | `build_route_indexes` | mcp/src/agents_remember/kernel/route_index.py:182-230 |
| `worktree_status_packet` returns the `WorktreeSummary` the context packet embeds directly, so the state machine's output is checked at the producer. | `worktree_status_packet` | mcp/src/agents_remember/application/worktree_status.py:21-56 |
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
repos plus a `ledgerMapsCodeHead` mapping check; the default stays
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

## Update History

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
