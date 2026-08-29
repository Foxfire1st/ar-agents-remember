# mcp/src/agents_remember/mcp/registration

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `mcp/src/agents_remember/mcp/registration`       |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-08-29T08:52+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview      | `../../../../../overview.md`                     |

## IAS Worktree Advertisement

The worktree surface advertises contract-addressed source reconciliation as an operation an agent can
start, observe, continue after resolving a retained conflict, or cancel. The public shape carries
the chosen memory-sync policy and explicit resolution action, never a private journal key or Git-ref
capability. Start/attach selecting paths can return the same reconciliation guidance instead of
exposing an uncurrent atomic master.

Task-document authoring remains independently advertised and wholly upstream. No queue/activation
lock field or whitelist is added to its schema. Exact parameter descriptions and response-state
vocabulary are reconciled to the frozen implementation; commit verification remains closeout-owned.

## Purpose

`mcp/registration/` is the **advertised MCP tool surface**: every `@server.tool()`
declaration in this repository lives here, one module per tool family. It was carved out of
`mcp/server.py` in 260731-EFA-L2; `server.py` kept only process wiring (compact-content shim,
ambient lifecycle, the `FastMCP` instance) and now loops over `TOOL_REGISTRARS` from this
package's `__init__.py`.

Most tools retain the flat-schema rule established by EFA. DAGQC L2 introduces one deliberate
model-typed exception: `memory_quality_check(request=...)` publishes a strict discriminated
sync/start/poll object because mutual exclusion between execution and poll fields is the public
contract. Task-addressed lifecycle operations still keep private operation identity off the wire.

Each module exposes exactly one `register_<family>_tools(server, config) -> None`, declares its
tools as nested functions decorated with `@server.tool()`, and forwards each call to one payload
builder in `mcp/tools/`. Nothing else belongs here.

## The Defining Contract: The Signature IS The Published Schema

**FastMCP derives each tool's published JSON input schema from the Python signature.** A flat
parameter list publishes flat properties; a model-typed parameter republishes the tool as a single
nested object. Measured against the installed mcp 1.28.1 and recorded verbatim in `pyproject.toml`:

```
def flat(repo_id, task_name, leaf_id)  -> properties: [repo_id, task_name, leaf_id]; no $defs
def nested(args: SomeModel)            -> properties: [args];                        has $defs
```

So changing a flat structural signature such as `dispatch_agent(task_document_ref, role, brief)`
into one model-typed argument is not an internal refactor: it republishes the MCP input schema as a
nested object. Structural vocabulary and flatness are both part of the registered contract.

That is why these modules — and only these — are exempt from `PLR0913` (the ≤5-argument rule that
260731-EFA-L2 armed at full strength across the rest of the tree, refactoring 274 of 293 offenders
into 163 parameter objects rather than listing them). The exemption is a single per-file-ignore in
`pyproject.toml`:

```toml
"mcp/src/agents_remember/mcp/registration/*.py" = ["PLR0913"]
```

The remaining long signatures in the repository are `@server.tool()` declarations under this path.
There is no ratchet, baseline, grandfather list or burn-down behind it — the
developer ruled all four forbidden — and no `noqa` anywhere holds an argument-count finding down.

**Do not turn either shape into a habit.** Flatness remains the default; a model parameter requires
an explicitly approved public nested contract, as memory quality now has. The carve-out is held shut by
`mcp/tests/test_code_quality_check.py::ToolSignatureExemptionTests`, which:

- asserts `PLR0913` is selected and neither globally ignored nor softened by a `max-args` override;
- asserts the exempted-pattern set equals exactly `{"mcp/src/agents_remember/mcp/registration/*.py"}`
  — a second exemption anywhere, or a widened pattern, fails;
- walks the AST of every file the pyproject pattern actually matches and fails if any function in
  them is anything but a `@server.tool()` declaration or the registrar that hosts them;
- runs Ruff over the tracked tree with `--ignore-noqa --select PLR0913` and requires exit 0, so a
  line-level suppression cannot hide a finding the gate would otherwise see.

## Layout

| Module              | Family                                                                    |
| ------------------- | ------------------------------------------------------------------------- |
| `__init__.py`       | `TOOL_REGISTRARS` (the ordered tuple `create_server` loops over) and the `ToolRegistrar` alias. |
| `core.py`           | `ping`, `server_info`, `context_packet`, `read_ar_files`, `resolve_context`, `runtime_install`, `skills_install`. |
| `sessions.py`       | `dispatch_agent`, `retire_child`, `rename_child`, `rename_self`; `dispatch_agent` accepts both plane-hosted and ambient (no plane identity) callers, with the caller-kind matrix documented in its published description; runtime allocation stays plane-owned. |
| `memory.py`         | `drift_check`, strict discriminated-request `memory_quality_check`, `route_index_refresh`, `memory_init`, `memory_baseline_status`, `memory_baseline_adopt`, `memory_carryover_plan`, `memory_carryover_apply`; full contract-scoped quality also publishes its digest-bound structured attestation. |
| `providers.py`      | `provider_status`, `provider_diagnostics`, `provider_watchers`.            |
| `code_search.py`    | `grepai_search`, `grepai_trace`, and the six `cgc_*` graph tools.          |
| `worktrees.py`      | `worktree_start`, `worktree_attach`, `worktree_status`, `worktree_sync` — the working half of a task. |
| `closeout.py`       | `worktree_closeout_preview`, `worktree_closeout_apply`, `worktree_integrate`, `worktree_cleanup`, `worktree_abandon` — the landing half. |
| `tasks.py`          | `task_reopen`, `lifecycle_finalize_task`, `task_doc`, `closeout_queue`; task-doc advertises the judgment-provenanced `author_execution_graph` mutation batch (which also bootstraps a graph-less sprint — the first `add_node` batch creates the graph), the classification/wave previews, and the policy-gated `branch_addressed` direct-execution mode (L16-R6), while closeout-queue mutations use a strict action-specific request and the hosted seat or — when none exists — a request-carried declared caller (L16-R2). |
| `benchmarks.py`     | `codex_benchmark_prepare`, `codex_benchmark_run`.                          |
| `lifecycle.py`      | The six session-lifecycle signals: `lifecycle_start`, `lifecycle_resume`, `lifecycle_turn_end_notification`, `lifecycle_end`, `switch_lifecycle`, `lifecycle_phase`. |
| `gates.py`          | Structural `lifecycle_gate`, `gate_decide`, `gate_list`; an ambient caller with no plane seat declares `caller` (role + task_document_ref) on each (L16-R3); public gate/lifecycle ids are absent. |
| `orchestration.py`  | `message_parent`, `message_child`; ordinary whole-message traffic resolves current structural occupants. |

Twelve registrars, 59 advertised tools (260815-DAG-L16 added `direct_landing`) — the same 59
names `mcp/tools/base.py::PUBLIC_TOOLS` lists, which `mcp/tests/test_tools.py` checks against a
live server's `list_tools()`.

## Hot Path Summary

Registration publishes the task-addressed lifecycle-control, explicit enclosure-adoption, and bounded legacy-operation schemas while keeping operation identity private.

A tool body usually packs flat MCP arguments into the parameter objects the payload builder and its
application entry point take, then returns the builder's result unchanged. Memory quality instead
dispatches its already validated request DTO by mode and returns the matching builder result. Packing is
the whole content — `TaskRef`, `SpawnSeat`, `GateVerdict`, `CarryoverSelection`,
`CloseoutCommitMessages`, `TaskIdentity`/`TaskBases`/`StartExecution`, `BenchmarkSelection`/
`BenchmarkPreparation`/`CodexBenchmarkRun`, `TaskDocTarget`/`TaskDocEdit`, `InboxAddress`/
`InboxMessage`/`InboxPoster`, `NudgeTarget`/`NudgeSubject`, `GrepaiSearchQuery`/`GrepaiRepoScope`/
`ProviderQueryScope`.

The published docstring is the model-visible description of the tool and is checked for presence by
`test_tools.py`; it is the only place a caller learns the semantics, so it carries the refusal
vocabulary and the act-by-default `dry_run` contract in prose.

For `author_execution_graph`, that description names the exact mutation cells (node, edge with
predecessor/successor/reason, leaf move, nature set with its judgment row), the graph-less
bootstrap, and the structured classifications and derived waves returned by preview; callers do not
have to infer the shape from prose examples. The `closeout_queue` description likewise carries the
degraded `status` readout (mode/registers/laneOwner/legalNextOperations) and the sync-first
`worktree_sync` recovery naming for stale-base refusals.

Structural tool registration fixes attribution and caller identity in the plane: a hosted seat wins,
an ambient caller with no plane seat declares `caller` (role + task_document_ref) and the same
authorization validates it exactly like a seat (L16-R3). `dispatch_agent` is the one public spawn
tool for both caller kinds: since 260821-ARSPAWN-L1 an ambient caller (no `AR_HOSTED_SESSION_ID`) is
resolved from the process environment rather than request data, spawns with the pinned brief + the
same rollback, has no parent seat (so seat-authority and child-scope checks do not apply), and still
gets role-altitude validation — the published description documents the caller-kind matrix. Gate
decisions use the ambient or declared caller for authority; message tools derive the sender from the
hosted context. No agent-facing signature accepts an actor/session/lifecycle/inbox/gate id.

`register_lifecycle_tools` takes `_config` and does not use it: its six payloads act on the
process-wide ambient lifecycle rather than on resolved settings. The parameter stays so every
module in the package has the one registrar signature `TOOL_REGISTRARS` is typed against.

## Invariants And Boundaries

- **Never give a tool function a model-typed parameter.** The signature is the published schema;
  a parameter object here is a breaking wire change for every client. This is the reason for the
  `PLR0913` exemption and the reason nobody may "tidy" these functions.
- Keep bodies to packing + one forwarded call. Any ordinary logic added under this path fails
  `ToolSignatureExemptionTests::test_every_function_in_the_exempted_path_is_a_published_tool_declaration`.
- Do not add a second `PLR0913` exemption or widen the existing pattern; both fail the same suite.
- A new tool means editing one family module and appending to `PUBLIC_TOOLS`, the response-model
  registry, and `docs/reference/mcp-tools.md`; a new family means a new module plus one entry in
  `TOOL_REGISTRARS`. `create_server` itself should not grow a special case.
- Registration order in `TOOL_REGISTRARS` is the order the server advertises tools in; the
  `PUBLIC_TOOLS` equality check is set-based for `list_tools()` but exact-list for `server_info`.
- Request validation belongs in the payload builders and application entry points; response validation belongs
  to `base._tool_payload`. This layer validates nothing.
- Do not add a raw shell or arbitrary-command tool to this surface.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `create_server` loops over `TOOL_REGISTRARS` and owns nothing else about the tool surface. | `create_server` | mcp/src/agents_remember/mcp/server.py:32-44 |
| The payload builders every declaration forwards to. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:77-79 |
| `PUBLIC_TOOLS` — the advertised name list this package must match. | `PUBLIC_TOOLS` | mcp/src/agents_remember/mcp/tools/base.py:10-69 |
| The `PLR0913` per-file-ignore and the reasoning recorded beside it. | "mcp/src/agents_remember/mcp/registration/*.py" | pyproject.toml:38-38 |
| The AST suite that holds the exemption to published tool declarations only. | `test_every_function_in_the_exempted_path_is_a_published_tool_declaration` | mcp/tests/test_code_quality_tool_signature_exemption.py:60-70 |
| What each declaration hands its payload builder, proved through a live FastMCP instance. | `RegistrationWiringTests` | mcp/tests/test_mcp_registration_wiring.py:61-116 |
| The advertised-name and docstring-presence checks against a live server. | `test_every_public_tool_has_a_description` | mcp/tests/test_tools.py:138-152 |
| `TaskRef` — the shared task locator three read-side tools pack. | `TaskRef` | mcp/src/agents_remember/application/task_docs/task_ref.py:14-28 |

## 260731-EFA-L17 Change

The closeout-family docstrings now state the quality altitude ladder: preview/apply name the
leaf change-set-scoped contract (`--targeted`: changed files + reverse-import closure + derived
test subset, mandatory CRAP over changed modules) and say the full wrapper is NOT a leaf gate;
`worktree_integrate` states it runs the altitude-routed gate itself before any merge (leaf
targeted; master full with host-managed RAM/swap by default and an optional
`orchestration.qualityGate.memoryCapBytes`). The L8
bare-`*` keyword-only remediation is completed here: `worktree_cleanup` and `worktree_abandon`
now carry the separator too, so every `@server.tool()` declaration in the module is
keyword-only. The registered tool surface is unchanged.

L22 applies the same Python-only keyword boundary to `message_child`'s content fields. FastMCP
continues publishing the identical named JSON fields; no agent-visible address or payload changes.

## 260731-EFA-L9 Route Impact — Caller Re-Points

The registration callers were rewritten by the L9 caller wave: conversation/evidence/control-wire models now import from `models/conversations/`, the runtime config record from `kernel/primitives/runtime_config.py`, and the terminal-catalog row vocabulary from `models/terminal_catalog.py`. Registration/tool wiring behavior is unchanged.

## L23 Closeout Registration Composition

`closeout.py` still owns one public closeout tool family, but its internal wiring is divided among
`_register_closeout_command_tools`, `_register_integration_command_tools`, and
`_register_reclamation_command_tools`. Their `_tools` suffix keeps the route's narrow structural
exemption attributable exactly to tool declarations and registrar helpers. Published signatures
and descriptions stay at the registration boundary while the public tool names, arguments, and
model-visible authority remain unchanged.

## R39 Registration Route

The integration tool contract now reports leaf acceptance as certified at closeout rather than
rerunning targeted mode. Master integration remains the sole full acceptance owner and always uses
the pinned Dagger executor.

## 260815-DAG-L3 Closeout Queue Route

`tasks.py` now advertises `closeout_queue` beside the task-document and lifecycle-finalization
surfaces. The published request is deliberately one strict action-discriminated model: status has
no mutation fields; every mutation carries a stable request id and expected revision; manager
declaration cannot smuggle a grade; and blocker, admission, grading, selection, and release fields
are legal only for their owning action. The caller is the plane-injected hosted seat when one
exists; an ambient caller with no plane seat declares `caller` (role + task_document_ref) instead
(260815-DAG-L16, L16-R2) — the declaration is validated like a seat and grants no authority beyond
the same role/document pair. No actor, session, lifecycle, operation key, or arbitrary queue id
enters the wire contract.

The tool description makes the detection/judgment boundary explicit. It reports recomputed
mechanical facts and deterministic order, while priority and blocker exceptions must resolve to
exact canonical sprint register rows. The same route binds the structured memory-quality
attestation, whose Markdown report digest and exact source-change dispositions are published only
by a full contract-scoped `memory_quality_check`. Public registration remains packing plus one
payload builder; queue logic stays in the application/worktree/control-plane owners.

## 260815-DAG-L4 L4 Public Lifecycle Surface

Registered worktree and memory tools expose journaled closeout/integration and read-only conflict/carryover planning while keeping protected writes behind configured authority. Response schemas and next-tool literals match the executable registration surface.

## 260815-DAG-L14 Task-Doc Registration

`mcp/registration/tasks.py` documents the sprint linkage operations (`attach_master`,
`detach_master`, `linkage_report`) on the `task_doc` tool.

## 260815-DAG Master Full-Gate Repair Route Impact

Registration modules import the moved `application/task_docs/*`; `registration/tasks.py` extracts the `task_doc` description constant; `registration/closeout.py` renames the direct-landing helper.

## 260821-CLIVE-L1 Tool Contract

The advertised closeout surface exposes code, memory, and ledger message observations where the route can require them, then reports `effectiveInput` or structured refusal. Optional schema fields are not defaults: enabled legs require explicit stripped nonblank messages at runtime. Direct landing exposes only memory and ledger intent because code is verified-existing/not-applicable. Validation precedes integration authority, the landing lock, and Git.

## 260821-CLIVE-L2 Current Architecture

This route composes public signatures only. It exposes the one closed application boundary and never owns configured-contract exception families, journal state, queue lifecycle, or compatibility policy.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Worktree registration composition. | `register_worktree_tools` | mcp/src/agents_remember/mcp/registration/worktrees.py:27-31 |
| Public payload builders. | `worktree_enclosure_adopt_payload` | mcp/src/agents_remember/mcp/tools/worktree.py:101-108 |

## 260821-DAGQC-L2 Published Quality Schema

`memory_quality_check` deliberately publishes one nested request discriminated by mode. Sync/start
execution fields and poll identity are mutually exclusive and extra-forbid; registration dispatches
the validated DTO and owns no compatibility reader or lower-level failure vocabulary.

## MCAR-L02 Published Coherence Surface

The task registrar advertises one `curator_coherence(request=...)` tool with four concise actions.
Its typed request publishes one nested schema rather than overlapping flat tools. The description
states that structured authority is canonical, evidence roots are explicit, identity classes stay
separate, historical Markdown is never searched, and `validate` is the shared admission check.
The memory registrar exposes raw `qualityChecklistStatus` separately from combined readiness and
documents deterministic same-input attestation behavior.

## Update History

- 2026-08-29T08:52+02:00 — MCAR-L02 A005: advertised the one structured curator-coherence API and
  combined memory-readiness contract. Verification remains closeout-owned.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of the contract-addressed sync
  advertisement and independently unlocked task-authoring surface; verification remains
  closeout-owned.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: published the one canonical discriminated memory-quality request and removed flat wait/run-id dispatch. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: route claims reconciled to accepted candidate tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 route impact: `dispatch_agent` documents the caller-kind matrix (plane seat vs ambient launcher resolved from the process environment); one public spawn tool, `spawn_agent_session` stays internal. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: registration import paths updated; `task_doc` description constant extracted; direct-landing helper renamed. Verified at code commit e5cb139f.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: memory_quality_check wait/run_id keyword-only async surface (L15-R7). Verified at code commit de3a0fd9.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16 route impact: `closeout.py` registers the
  `direct_landing` tool (L16-R8); `tasks.py`'s `task_doc` gains `branch_addressed`
  (L16-R6); `gates.py`'s structural declarations accept an optional request-carried `caller`
  (L16-R3). The advertised surface is now 59 tools. Verified at code commit a9d50e08.


- 2026-08-20T05:04+02:00 — 260815-DAG-L14 route impact: `task_doc` registration gains the sprint
  linkage operations. Verified at code commit 8071a644.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: `tasks.py`'s `task_doc` declaration no
  longer advertises the removed `migrate_execution_topology`; `author_execution_graph` is
  documented as the bootstrap seam, and the `closeout_queue` declaration documents the degraded
  `status` readout and sync-first recovery naming. The advertised surface stays 56 tools.
  Verification remains closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11 route impact: `tasks.py`'s `task_doc` declaration now
  also advertises the `author_execution_graph` operation; the advertised surface stays 56 tools
  (one new operation on an existing tool, no new tool). Verification remains closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-15T09:32+02:00 — 260815-DAG-L3 curator: documented the new strict `closeout_queue`
  registration, plane-owned caller authority, and digest-bound memory-quality attestation. The
  advertised surface is now 56 tools; registration remains a schema/forwarding boundary.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: registration now documents the exact
  nested migration graph and master-classification request/response cells rather than only naming
  the migration at a high level.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1 route impact: task registration advertises the exact
  multi-document migration request and derived-wave preview returned by the task-doc application.

- 2026-08-14T11:29+02:00 — R39 curator: reconciled public integration wording with the final
  altitude policy. Verification remains closeout-owned.

- 2026-08-14T06:25+02:00 — No public route impact: L23's final registrar delta narrows internal
  closeout registration composition and preserves the same task-addressed tool schemas; route-review
  and Dagger enforcement remain application/worktree responsibilities. Verification stays
  closeout-owned.

- 2026-08-13T12:26+02:00 — L23 structural-rail repair: corrected the closeout registration
  composition to the exact closeout/integration/reclamation helper names and recorded why every
  registrar ends in `_tools`; no public tool or schema changed. Verification provenance remains
  closeout-owned.

- 2026-08-13T09:05+02:00 — L23 route review: closeout registration remains one public tool family
  while its internal construction is split into cohesive preview, apply, and shared registration
  helpers. Public names/signatures and registry authority remain unchanged; final provenance
  remains closeout-owned.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: recorded the closeout route's internal split into closeout, integration, and reclamation registration groups without changing the public tool surface. Verification metadata remains closeout-owned.

- 2026-08-12T15:19+02:00 — L23 curator: recorded task-addressed lifecycle operation declarations and the guarded public citation-fix surface; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24: aligned registered
  closeout/integration descriptions with host-managed master memory and the
  optional explicit cap. Verification metadata remains pinned until closeout
  stamps L24.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: recorded `message_child`'s keyword-only Python
  boundary and unchanged named MCP schema; refreshed the shifted exemption-test citation.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: reconciled registration with the structural
  `dispatch_agent`, parent/child messaging, gate, retire, and rename surface and the removal of
  agent-visible exact-session controls.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 route impact: L9 caller/import re-points recorded and body updated.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 route impact: recorded the altitude-ladder tool
  docstrings and the completed keyword-only signatures. Verification metadata stays pinned
  until closeout stamps the 260731-EFA-L17 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: added the L8 Change section (bare-`*` keyword-only signatures). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T02:53:38+02:00 — W3-B05 curator: anchored 6 Tier-2 table citations and normalized one pre-existing transient source range with exact anchors and paths; fixer generated all ranges.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No route impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T00:00+02:00 — No route impact: 260731-EFA-L4 touches exactly one file under this
  path, `closeout.py` (+16/-7), and the change is **entirely inside two published docstrings** —
  `worktree_closeout_preview` and `worktree_closeout_apply` now describe closeout's new
  stage-before-gate step and its two refusals (not a task worktree; unresolved merge conflicts).
  Proven rather than eyeballed: I parsed the file at `abc7cbcc` and at the current revision,
  stripped every module/class/function docstring from both syntax trees, and the two dumps are
  identical — so no signature, parameter, default, annotation, return type, decorator or
  forwarding call moved. That matters here more than elsewhere, because on this route **the
  signature IS the published JSON schema**: a docstring edit changes the model-visible
  description and nothing on the wire, which is exactly the split this overview's defining
  contract describes. The two tools stay in the `closeout.py` family, `TOOL_REGISTRARS` and the
  58-name `PUBLIC_TOOLS` set are untouched, and no new function entered the `PLR0913`-exempted
  path, so `ToolSignatureExemptionTests` sees the same AST it did before. This overview's
  claim that "the published docstring … carries the refusal vocabulary … in prose" is not
  merely still true — L4 is an instance of it. Verification metadata pinned until closeout
  stamps the L4 commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: route created. The `@server.tool()` surface moved
  out of `server.py` into this package (12 family modules + `TOOL_REGISTRARS`), and the route
  records its defining contract — the signature IS the published MCP schema — together with the
  single `PLR0913` per-file-ignore that follows from it and the AST/`--ignore-noqa` suite that holds
  the carve-out shut. Verification metadata is pinned to the pre-change commit until closeout stamps
  the L2 code commit.
