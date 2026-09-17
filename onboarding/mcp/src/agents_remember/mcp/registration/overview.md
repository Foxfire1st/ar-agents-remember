# mcp/src/agents_remember/mcp/registration

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `mcp/src/agents_remember/mcp/registration`       |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-09-15T00:56:17+00:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| governingOverview      | `../../../../../overview.md`                     |

## Governing Overview

[overview.md](../../../../../overview.md)

## IAS Worktree Advertisement

The worktree surface advertises contract-addressed source reconciliation as an operation an agent can
start, observe, continue after resolving a retained conflict, or cancel. The public shape carries
the chosen memory-sync policy and explicit resolution action, never a private journal key or Git-ref
capability. Start/attach selecting paths can return the same reconciliation guidance instead of
exposing an uncurrent atomic master.

Task-document authoring remains independently advertised and wholly upstream. No queue/activation
lock field or whitelist is added to its schema. Exact parameter descriptions and response-state
vocabulary are reconciled to the frozen implementation; this source review grants no lifecycle acceptance.

## 260915-CAPS-L9 `experiment` On `runtime_install`

One additive, keyword-only parameter landed on the registered `runtime_install` tool:
`experiment: str | None = None`. The tool now builds the run's `RuntimeInstallRequest` itself and
hands it to the payload builder unchanged, so the parameters the public schema publishes and the
fields the application entry point reads cannot drift apart. Its docstring is the model-visible
contract and says what the owner's ruling requires: the parameter selects the experimental
instruction cutover **for this run**; it is a per-call input, **never a setting**; omitting it — with
no `AR_EXPERIMENT` in the server environment — installs the unmodified runtime; and the returned
record's `selectionSource` names which input supplied the mode. The registered tool count is
unchanged: a parameter was added to an existing declaration, not a tool.

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
an explicitly approved public nested contract, as memory quality now has. The configured exemption is scoped to the registration path. Removed signature-exemption
tests do not provide current enforcement; the public schema boundary remains the reason
for keeping registration declarations separate from implementation.

## Layout

| Module              | Family                                                                    |
| ------------------- | ------------------------------------------------------------------------- |
| `__init__.py`       | `TOOL_REGISTRARS` (the ordered tuple `create_server` loops over) and the `ToolRegistrar` alias. |
| `core.py`           | `ping`, `server_info`, `context_packet`, `read_ar_files`, `resolve_context`, `runtime_install`, `skills_install`. |
| `sessions.py`       | `dispatch_agent`, `retire_child`, `rename_child`, `rename_self`; `dispatch_agent` accepts both plane-hosted and ambient (no plane identity) callers, with the caller-kind matrix documented in its published description; runtime allocation stays plane-owned. |
| `memory.py`         | `drift_check`, `citation_fix`, strict discriminated-request `memory_quality_check`, `route_index_refresh`, `memory_init`, `memory_baseline_status`, `memory_baseline_adopt`, `memory_carryover_plan`, `memory_carryover_apply`; full contract-scoped quality also publishes its digest-bound structured attestation. |
| `providers.py`      | `provider_status`, `provider_diagnostics`, `provider_watchers`.            |
| `code_search.py`    | `grepai_search`, `grepai_trace`, and the six `cgc_*` graph tools.          |
| `worktrees.py`      | `worktree_start`, `worktree_attach`, `worktree_status`, `worktree_sync`, `worktree_pause` — the working half of a task, including the stop. |
| `closeout.py`       | `direct_landing`, `worktree_closeout_preview`, `worktree_closeout_apply`, `worktree_integrate`, `worktree_checkpoint_landing`, `worktree_record_landing`, `worktree_operation_control`, `worktree_cleanup`, `worktree_abandon` — the landing half. `worktree_legacy_operation` was removed from this registrar and exists nowhere in the tree. |
| `tasks.py`          | `task_reopen`, `lifecycle_finalize_task`, `task_doc`, `curator_coherence`, `closeout_queue`; task-doc advertises the judgment-provenanced `author_execution_graph` mutation batch (which also bootstraps a graph-less sprint — the first `add_node` batch creates the graph), the classification/wave previews, and the policy-gated `branch_addressed` direct-execution mode (L16-R6), while closeout-queue mutations use a strict action-specific request and the hosted seat or — when none exists — a request-carried declared caller (L16-R2). `closeout_door` was deleted from this registrar with the door-operation-journal cut (commit `6982c6a7`). |
| `benchmarks.py`     | `codex_benchmark_prepare`, `codex_benchmark_run`.                          |
| `lifecycle.py`      | The six session-lifecycle signals: `lifecycle_start`, `lifecycle_resume`, `lifecycle_turn_end_notification`, `lifecycle_end`, `switch_lifecycle`, `lifecycle_phase`. |
| `gates.py`          | Structural `lifecycle_gate`, `gate_decide`, `gate_list`; an ambient caller with no plane seat declares `caller` (role + task_document_ref) on each (L16-R3); public gate/lifecycle ids are absent. |
| `orchestration.py`  | `message_parent`, `message_child`; ordinary whole-message traffic resolves current structural occupants. |
| `capsule_serving.py` | `role_capsule_compile`, `skill_catalog_list`, `skill_catalog_read` — **and** the MCP resource set for the SEP-2640 skills transport (`skill://index.json` plus one resource per served skill file), plus the `io.modelcontextprotocol/skills` capability declaration and the call that installs the extension's two protocol methods. The one family that registers resources and protocol methods as well as tools. |
| `skills_extension.py` | **The SEP-2640 extension's two mandatory protocol methods** — `skills/list` and `skills/get` — added as bounded explicit method support against the SDK's own dispatch. Carries no `@server.tool()` declaration: it extends the session's request union, the server's message dispatcher, and the SDK's `request_handlers` map. |

Thirteen registrars and 66 tools registered by decorator, and the advertised tuple `PUBLIC_TOOLS` lists
the same 66 names. 260915-CAPS-L4 added the last three: `role_capsule_compile`, `skill_catalog_list` and
`skill_catalog_read`, declared by the new `capsule_serving.py` family and **appended** to both sides
(and to `TOOL_RESPONSE_MODELS`) in one change — the L29 rule applied by construction, and appending
rather than inserting so no existing tool's advertised position moved. The most recent membership
change before it was 260831-LOCR-L37's `worktree_pause`, declared by
`worktrees.py::_register_worktree_stop_tools`, which is the fourth registrar in that family. Since 260831-LOCR-L32 that tuple's one definition is
`mcp/src/agents_remember/models/tools/public_roster.py:22-90`, a zero-import `models` leaf;
`mcp/tools/base.py` re-exports the identical object, so nothing in this route changed. The two sets
are equal, and since 260831-LOCR-L29 that equality is checked
directly: `mcp/tests/test_tools.py::PublicSurfaceInventoryTests` registers every `TOOL_REGISTRARS`
entry against a probe `FastMCP` and compares the live `list_tools()` order against `PUBLIC_TOOLS`.
`mcp/public_surface.py` asserts the same live order together with response-model projection, dispatch
schema, and description, so a tool missing from that list is a surface violation until both sides
agree. The L29 repair is what made the sets agree — before it `worktree_record_landing` was
registered by `closeout.py` while absent from `PUBLIC_TOOLS` — and 260831-LOCR-L30 added
`worktree_checkpoint_landing` to both sides at once. 260831-LOCR-L34 changed only that tool's
**published docstring**: it had listed two of the three completion assumptions the checkpoint route
drops, omitting the completed-closeout requirement, which is why the route was unreachable from both
sides. A published refusal list is a promise about what will *not* happen, so it is kept complete
whenever the gate changes; the tool surface, registration order and payload owners are unchanged.

260831-LOCR-L36 corrected the same description's **name for the route**. It opened "Use this to pause
a master", which invited an agent to reach for a protected-branch publication on an ordinary stop
request: the call moves the master's committed code and memory refs onto its super branch, where every
other master sees them, under an explicitly required developer approval. It is a partial
**publication**, and the description now says so and states that pausing is a separate matter which is
NOT this call — a pause stops the master's work, publishes nothing, moves no ref, and leaves its
branch, worktrees and enclosure private, and no tool on this route performs it — at that point no tool
anywhere did, which L37 then changed by adding the stop to the sibling working-half registrar. Only the
description changed at L36: the signature, the registration order, the payload owner and `PUBLIC_TOOLS`
were untouched, and `mcp/tests/test_tools.py` pins the new wording.

260831-LOCR-L37 then **added the stop that correction pointed at**, as its own verb rather than as a
reinterpretation of the publication. `worktree_pause` lives in the working half of the surface
(`worktrees.py`), not in `closeout.py` beside the checkpoint, and its description carries the three
claims an agent needs: it **PAUSES an atomic master** and hands control back to the developer; it
**publishes NOTHING** — no ref move, no commit, no landing, no ledger row — while releasing the
master's atomic-series activation selection and leaving the master's code and memory work branches,
worktrees, enclosure and every unstarted leaf exactly as they were; and it proposes no next step, so
resuming is the ordinary attach/start route. It names `worktree_checkpoint_landing` as the separate,
explicitly requested PUBLICATION and states that pausing never does that. The two descriptions are now
a matched pair pointing at each other across the two halves, and `mcp/tests/test_tools.py` pins both:
the checkpoint's case from L36 and the pause's case from L37. Signature, family placement and the
`PUBLIC_TOOLS`/response-model rows were added together, so no advertised name is unanswerable.

## Hot Path Summary

The closeout registrar publishes only code/memory commit-message arguments. Memory registration removes ledger commit-message controls from carryover. Cache status remains consumer output, while the typed lower-layer owners enforce actual Git authority.

## Detailed Route Context

The closeout registrar accepts typed corrective catalog dispositions and forwards them to the existing application owner; registration creates no alternative approval or retry authority.

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

- **Preserve the approved public schema shape.** Flat signatures remain the default; the existing
  discriminated memory-quality, queue and coherence request contracts intentionally use model-typed parameters. This is the reason for the
  `PLR0913` exemption and the reason nobody may "tidy" these functions.
- Keep bodies to packing + one forwarded call. Any ordinary logic added under this path fails
  `ToolSignatureExemptionTests::test_every_function_in_the_exempted_path_is_a_published_tool_declaration`.
- Keep the registration exemption scoped to published declarations; helpers belong in their implementation owners.
- A new tool means editing one family module and appending to `PUBLIC_TOOLS`, the response-model
  registry, and `docs/reference/mcp-tools.md`; a new family means a new module plus one entry in
  `TOOL_REGISTRARS`.
- Registration order in `TOOL_REGISTRARS` is the order the server advertises tools in; the
  `PUBLIC_TOOLS` equality check is exact-order for both `list_tools()` and `server_info`.
- Semantic request validation belongs in payload builders and application entry points; response
  validation belongs to `base._tool_payload`. The transport boundary additionally rejects
  undeclared `dispatch_agent` inputs because FastMCP otherwise drops them silently. This narrow
  closed-schema enforcement does not duplicate registration or application behavior.
- Do not add a raw shell or arbitrary-command tool to this surface.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `create_server` loops over `TOOL_REGISTRARS` and owns nothing else about the tool surface. | `create_server` | mcp/src/agents_remember/mcp/server.py:58-70 |
| The payload builders every declaration forwards to. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:22-24 |
| `PUBLIC_TOOLS` — the advertised name list this package must match (63 names), defined in `models` and re-exported by the adapter. | "PUBLIC_TOOLS = ("; "__all__ = [\"PUBLIC_TOOLS\", \"RESERVED_TOOLS\", \"TRANSPORT\"]" | mcp/src/agents_remember/models/tools/public_roster.py:22-22; mcp/src/agents_remember/mcp/tools/base.py:19-19 |
| The `PLR0913` per-file-ignore and the reasoning recorded beside it. | "mcp/src/agents_remember/mcp/registration/*.py" | pyproject.toml:38-38 |
| `TaskRef` — the shared task locator three read-side tools pack. | `TaskRef` | mcp/src/agents_remember/application/task_docs/task_ref.py:14-28 |

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical closeout input rejects a ledger message field. | n/a | [mcp/src/agents_remember/models/closeout/input.py](mcp/src/agents_remember/models/closeout/input.py) |

## Historical 260731-EFA-L17 Change

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

## Current Closeout Tool Contract

The advertised closeout surface accepts code and memory message observations and reports `effectiveInput` or structured refusal. Optional schema fields are not defaults: enabled legs require explicit stripped nonblank messages at runtime. Direct landing exposes the memory message because its code output is verified-existing/not-applicable. No public ledger message, commit or intent remains. Validation still precedes integration authority, the landing lock and Git.

## 260821-CLIVE-L2 Current Architecture

This route composes public signatures only. It exposes the one closed application boundary and never owns configured-contract exception families, journal state, queue lifecycle, or compatibility policy.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Worktree registration composition, re-read and re-cited by the L37 curator at the current declaration. | "def register_worktree_tools(" | mcp/src/agents_remember/mcp/registration/worktrees.py:26-31 |
| Public payload builders — the enclosure-adoption payload builder was removed; this route now consumes the start, attach, status and sync builders. | "worktree_attach_payload," | mcp/src/agents_remember/mcp/registration/worktrees.py:17-22 |

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

## MCAR-L03 Memory Tool Advertisement

The memory-quality tool schema and description distinguish official diagnostics from exact leaf
candidate runs. Candidate poll carries the original contract address; the public contract does not
advertise repository id as acceptance authority.

## Status-Change Wait Registration

`worktrees.py` no longer registers `worktree_status_wait`: the wait tool, its payload builder and
its response registration were removed. `_register_worktree_observation_tools` now declares only
the read-only `worktree_status` addressing and refusal behavior, plus `worktree_sync` as the sole
pull-forward command, and no wait-specific operation key, PID, expected generation or bounded
timeout survives on this route.

| Finding | Anchor | Source |
| --- | --- | --- |
| The removed wait registration has no public replacement; the observation registration now declares read-only addressing, refusal behavior and typed request construction for `worktree_status`. | "def worktree_status(" | mcp/src/agents_remember/mcp/registration/worktrees.py:139-166 |

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.

## CCR-R12@v5 Current Registration Boundary

The closeout-family registration advertises transaction-only preview/apply/integration behavior.
Public calls preserve explicit developer approval, candidate/source checks, and ref safety, then
delegate code, external-memory or prepared-pair publication to existing owners. The
registered routes do not automatically invoke strict code quality, memory quality, selected
certification, curator coherence, or independent review; full suites are an explicit developer
request. The historical altitude-ladder section above remains context for the superseded contract.

## 260831-LOCR-L33 Step-Plane Vocabulary

`registration/tasks.py`'s `_TASK_DOC_TOOL_DESCRIPTION` now advertises the step plane split by intent:
`set_step` updates exactly one existing unit and never creates, `add_step` creates exactly one and
refuses an existing id, `remove_step` deletes exactly one behind a mandatory nonblank reason, and
`read_steps` is the read-only focused checklist read. All of them address one exact existing unit by
`step={id, parent?}`, where `parent` selects the namespace. The description also states the two
developer rulings: a reasoned `remove_step` may remove a `done` unit and may operate on a `Completed`
document.

Nothing else on this route moved. `operation` is a plain `str`, not an enum and not a schema member,
so the operation vocabulary exists **only** in this description text — the change touched no
signature, no `PUBLIC_TOOLS` entry, and no response model, and the tool count and registration order
are unchanged. A reader looking for the operation set in the published schema will not find it;
the description is the contract.

## 260915-CAPS-L4 The Capsule And Skill-Serving Family — Tools Plus Resources

This route gained a thirteenth family module, `capsule_serving.py`, registering three tools and, for
the first time on this route, an MCP **resource set**. Two things about it are route-level facts rather
than file-local detail:

**1. A family module may now register resources, and that does not change what "registered" means
here.** The SEP-2640 skills transport serves each skill file as an MCP resource read with
`resources/read`, alongside this server's own `skill://index.json` resource and the
`io.modelcontextprotocol/skills` capability declared in the `initialize` result. A live server now
advertises 85 resources (one per file of the 14 shipped skills, plus the index) alongside its 66 tools.
`skill_catalog_list` and `skill_catalog_read` are this server's own tool reads over the same registry
for a client that is not resource-aware.

**1b. And it installed the extension's two mandatory protocol methods — the first time this route has
carried a protocol method rather than a tool.** `skills_extension.py` registers `skills/list` and
`skills/get` against the SDK's own dispatch as **bounded explicit method support**, because the pinned
`mcp==1.29.1` has no skills affordance: zero case-insensitive `skill` matches, no `extensions` field on
`ServerCapabilities`, and an unmodelled method refused `-32602`. Three additive changes, nothing else:
the session's request-validation union gains the two request types, the server's message dispatcher
recognises them as requests (without that hook a request is *silently dropped* and the call hangs
rather than failing), and the two handlers join the SDK's own `request_handlers` map. Both handlers
answer from the same catalog the resources are registered from.

**2. The declaration, the methods and the resources are installed together in one function.**
`declare_skills_extension(server)` and `install_extension_methods(server._mcp_server)` are adjacent
calls in `_register_skill_resources`, right after the catalog proves servable. That adjacency is the
contract, not a convenience: SEP-2640 §Capability Declaration says *"declaring the extension itself
commits the server to `skills/list` and `skills/get`"*, so a server may not advertise the capability and
answer neither. The leaf's seeded-mutation probe removes the declaration coupling (`M5`) and the live
exchange case fails on the missing `extensions` key; the round-1 candidate failed on exactly the
opposite side of this pairing, which is why the two install together.

**3. This server's own index resource is not the extension's enumeration surface.**
`skill://index.json` keeps the Agent Skills well-known-discovery shape and its wire description says so;
SEP-2640 enumerates through `skills/list`, whose entries carry verbatim frontmatter and per-file digests.

The three advertised names were **appended** to `TOOL_REGISTRARS` and to `PUBLIC_TOOLS` together with
their `TOOL_RESPONSE_MODELS` rows. Appending matters on this route: the tuple's order is the advertised
order, so a registrar inserted in the middle would renumber every later position and both
order-comparing surfaces would report a violation that is really a reordering.

The registered signatures stay flat, as this route's defining contract requires — `skill_catalog_read`
publishes only `uri`, and the corpus `origin`/`root` overrides its payload builder accepts are
deliberately absent from the wire.

## 260915-CAPS-L14 The Citation Tool Gains A Caller Exclude

`memory.py`'s registered `citation_fix` gained one **optional, keyword-only** parameter:

```
exclude: list[str] | None = None
```

It is additive and scoped to one call. Caller-supplied, code-root-relative globs narrow **that
call's** citation acquisition on top of the register every call already honours — the memory layer's
`settings.json → onboarding.pathRules.exclude` and the code repository's `.gitignore` — so a caller
repairing one document cannot change the population another document's repair sees. The globs are
packed onto `CitationOperationScope.excludes` and validated at that boundary: empty, absolute, or
`..`-escaping patterns are refused **by name** rather than quietly matching nothing.

Two route-level facts follow. **Keyword-only means no existing call changes meaning**, so this is a
pure addition to the advertised schema rather than a signature change. And the register's rule set
is reported in the result, so a reader can still see which patterns produced the population even
when a caller narrowed it.

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: recorded the additive keyword-only `experiment` parameter on
  the registered `runtime_install` tool in the new section above, including that it is a per-call
  input and never a setting, and that the registered tool count is unchanged. Verification
  metadata is left at its recorded value; the candidate is deliberately uncommitted.
- 2026-09-17T11:55+02:00 — 260915-CAPS-L14 curator:
- 2026-09-17T11:55+02:00 — 260915-CAPS-L14 curator: recorded the additive `exclude` parameter on the registered `citation_fix` tool and what it does at this route's altitude (a per-call narrowing on top of the shared register, validated and refused by name, keyword-only so no existing call changes meaning), in the new section above. The file card for `memory.py` gained the matching service section, a corrected reference table and its own history entry. Verification metadata is left at its recorded value; the candidate is deliberately uncommitted, so the governed closeout stamps the real code commit.

- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass** (uncommitted change set on
  `ar/260915-caps-l4`, base `b00a4ac2`): refreshed this route section against the settled candidate.
  **Removed the round-1 rejection banner** and recorded the settled transport instead: the route now
  carries the SEP-2640 extension's **two mandatory protocol methods** (`skills/list`, `skills/get`) from
  the new `skills_extension.py`, added as bounded explicit method support against the SDK's dispatch,
  with the three additive changes and the load-bearing dispatcher hook stated, and with the declaration,
  the methods and the resources installed together because the declaration is itself the commitment.
  Kept and sharpened the distinction that this server's own `skill://index.json` is a convenience
  resource and **not** the extension's enumeration surface. Added the `skills_extension.py` row to the
  layout. The 13-registrar / 66-tool census and the append-only ordering rule are unchanged. Earlier
  entries in this card's history remain as their own leaves' as-of records. Verification metadata
  remains closeout-owned; no acceptance claim.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator (uncommitted change set on `ar/260915-caps-l4`, base
  `b00a4ac2`): added the `capsule_serving.py` row to the layout and recorded the second family-module
  form on this route — a module that registers an MCP **resource set** as well as tools. Corrected the
  route census from twelve registrars / 63 tools to **thirteen / 66**, named the three appended
  advertised names, and stated why appending (not inserting) is the route's ordering rule. Recorded
  that the extension declaration and the resource registration are coupled in one function with the
  mutation-probe entry that makes the coupling executable, and that the new tools' published signatures
  stay flat with the corpus
  overrides kept off the wire. Repointed the roster's single-definition range to
  `models/tools/public_roster.py:22-90`. Earlier counts in this card's dated sections remain as their
  own leaves' as-of records. Verification metadata remains closeout-owned; no acceptance claim.

- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Aligned advertised tool contract with two input legs and informational cache outputs. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.

- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 citation review (curator-authored, not a mechanical
  projection): re-read the worktree-registration claim against the current source and re-cited it to the
  declaration itself, `"def register_worktree_tools("` at
  `mcp/src/agents_remember/mcp/registration/worktrees.py:26-31`. The construct the range now covers is
  the function the claim names, and the wording holds unchanged. Recorded because the previous range
  arrived from a generated anchor-range projection, which is not evidence that a claim still holds.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 route impact: recorded the new `worktree_pause`
  declaration in `worktrees.py::_register_worktree_stop_tools` (the family's fourth registrar), the
  advertised count moving 62 -> 63 on both sides together, the description's three claims and its
  naming of `worktree_checkpoint_landing` as the separate publication, and the fact that the two
  descriptions now point at each other across the two halves of the surface. The family table and the
  count line were corrected; verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T17:44+02:00 — 260831-LOCR-L36 route impact: the published description of
  `worktree_checkpoint_landing` now names the route a partial **publication** and denies it is the
  pause. The old opening ("Use this to pause a master") invited an agent to publish unfinished work
  for an ordinary stop request, because the call moves the master's committed code and memory refs
  onto its super branch under explicit developer approval. Recorded in the public-surface section
  that only the description changed — signature, registration order, payload owner and `PUBLIC_TOOLS`
  are untouched — and that `mcp/tests/test_tools.py` pins the new wording. Verification metadata
  remains closeout-owned; no acceptance claim.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:15+00:00 — 260831-LOCR-L34: recorded that this route's only change is the corrected
  published docstring for `worktree_checkpoint_landing` — it had listed two of the three completion
  assumptions the checkpoint route drops, omitting the completed-closeout requirement that made the
  route unreachable — plus the rule that a published refusal list stays complete. Tool surface,
  registration order and payload ownership are unchanged. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded the new step-plane vocabulary the
  `task_doc` description advertises (`add_step`/`remove_step`/`read_steps`, `set_step` update-only,
  `add_step` create-only, `remove_step` delete-only with a mandatory reason, one exact addressing
  rule, and the `done`-unit / `Completed`-document rulings) and that the vocabulary exists only in
  the description because `operation` is a plain `str`. No registrar, family module, tool name,
  signature, or registration order changed.
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: no route impact on registration behavior;
  `PUBLIC_TOOLS` moved its definition out of `mcp/tools/base.py` into the zero-import `models` leaf
  `models/tools/public_roster.py` (L22-L85) and is re-exported unchanged, so the exact-order
  comparison this route documents still compares the same object. Corrected the census prose and the
  reference row that named `mcp/tools/base.py::PUBLIC_TOOLS` as the definition site. No registrar,
  family module, tool name, or registration order changed.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `_tool_payload` repointed to mcp/src/agents_remember/mcp/tools/base.py:22-24. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: added `worktree_checkpoint_landing` to the
  `closeout.py` registrar row, and corrected the route census to the measured state — 12 registrars,
  62 decorator-registered tools, 62 names in `PUBLIC_TOOLS`, the two sets equal. The previous count
  line still described the pre-L29 gap (`worktree_record_landing` registered but unadvertised,
  `task_doc` helper-registered), which the L29 repair closed. Re-derived the shifted reference ranges.
  Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T23:20:00+00:00: Route inventory corrected against the current registrars. The `closeout.py` row now lists this change's new `worktree_record_landing` and records that `worktree_legacy_operation` exists nowhere; the `tasks.py` row drops `closeout_door`, deleted with the door-operation-journal cut (`6982c6a7`); and the count line no longer claims 64 advertised tools. That line now records the provable relationship instead of an equality: 12 registrar modules, 60 tools registered by decorator, 60 names in `PUBLIC_TOOLS`, with `worktree_record_landing` registered but absent from `PUBLIC_TOOLS` and `task_doc` in `PUBLIC_TOOLS` but helper-registered — which is what `public_surface.py` compares. Content change, not a range repoint.
- 2026-09-11T23:05:00+00:00: The route no longer owns `worktree_enclosure_adopt_payload` or a `worktree_status_wait` registration: `registration/worktrees.py:17-22` imports only the start, attach, status and sync payload builders and registers `worktree_start`, `worktree_attach`, `worktree_status` (139-166) and `worktree_sync`, while enclosure adoption survives only as the lifecycle-owned `preview_lifecycle_enclosure_adoption`/`apply_lifecycle_enclosure_adoption` service with no public payload builder or registered tool. Both evidence rows and the Status-Change Wait section were rewritten to that current state, and the `worktrees.py` Layout row now lists the four registered tools.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_tool_payload` repointed to mcp/src/agents_remember/mcp/tools/base.py:75-77. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `register_worktree_tools` repointed to mcp/src/agents_remember/mcp/registration/worktrees.py:25-29. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-10T02:27:58+02:00 — CCR-L42 parity curation: No route impact: curator preparation and closeout now run the shared sidecar and route body/history validators independently; this route's ownership and source semantics remain unchanged. No acceptance claim is made.

- 2026-09-09T02:35:47+02:00 — CCR-L38 inherited route reconciliation: re-read this route's purpose, member inventory, route summary, and invariants against frozen candidate code tree `4c6b7bc2362bc03d50fc7a0643f34b591b805d45`; the candidate's changed paths are outside source route `mcp/src/agents_remember/mcp/registration`, so no route/member/prose/invariant change is required. route-member-count=13; source inspection only; verification metadata remains unchanged pending producer-owned realization. No acceptance or certification claim.

- 2026-09-05T07:22+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Updated the public inventory to 64 tools, preserved approved nested schema exceptions, and reviewed the read-only status-wait declaration. Verification records source review, not execution or acceptance.
- 2026-09-05T06:21+00:00 — Re-read the affected source declarations and repaired citation ranges shifted by CCR additions. Preserved the route contract and existing history; literal anchors identify the exact current construct where shared identifiers were ambiguous.

- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec: route coverage refreshes the `worktree_status_wait` server-tool registration; route index regenerated.

- 2026-08-31T20:30+02:00 — No route impact: the direct-landing MCP description now advertises
  only the explicit leaf-without-enclosure path and excludes ordinary series/master closeout and
  integration. Registered tools and route ownership are unchanged.

- 2026-08-30T15:15:36+02:00 — 260821-ARSPAWN-L4 route impact: documented the 63-tool exact-order
  public surface, the permanent cross-authority validator, and the narrow transport-owned refusal
  of undeclared dispatch inputs. No fallback or duplicate registrar was introduced; verification
  remains closeout-owned.

- 2026-08-29T21:46+02:00 — MCAR-L03: advertised exact contract-bound candidate start/poll
  semantics. Verification remains closeout-owned.

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

