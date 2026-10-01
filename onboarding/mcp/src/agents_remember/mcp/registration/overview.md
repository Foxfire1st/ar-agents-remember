# mcp/src/agents_remember/mcp/registration

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/mcp/registration`       |

## Governing Overview

[overview.md](../../../../../overview.md)

## 260928-MIK-L37 The `citation_fix` Description Names Its Converted-Memory Mode

[`memory.py`](memory.py.md)'s registered `citation_fix` keeps its flat signature. Its description gains one sentence
(L37 fix round P1b): on converted memory the tool authors the cards' citation rows into sidecar references and
re-records moved anchors, and `document` then needs no `expected_snapshot` and scopes the run to that one card. The
behaviour is the application's (`memory_tools.citation_fix_tool`). No tool was added or removed.

- The registered citation_fix tool and its description. [23]


## 260928-MIK-L38 The `lifecycle_finalize_task` Description Names The Folder Master

`lifecycle_finalize_task`'s description in [`tasks.py`](tasks.py.md) now says the finalizer derives and reconciles
the leaf's exact row when the leaf declares an existing immediate parent "or names none and its folder's task.json
master lists it" (MIK-R38; ruling 2026-09-30T12:33:07 Q3), and that "a sub-task naming none whose folder task.json is
not a master is refused" (review R1 note 5, ruling 13:11:32; "sub-task", not "leaf", by ruling 14:12:52). No tool,
argument or schema changed; the same clauses are in `docs/reference/mcp-tools.md` and the c-09 skill.

- The description's two new clauses. [1]

## 260928-MIK-L05 The Read Description Names The Route-Chain Rows And The Family Seed

`knowledge_read`'s description in [`knowledge.py`](knowledge.py.md) continues the leaf-read sentence (MIK-R05):
after the advertised families come one compact `chain_family` row per family routed at the path's directory or
an ancestor, with `payload.routeChain` stating the chain (`no_governing_family` when none); and
`source_context` with a family ID in `familyRevisionId` and no `sourcePath` returns that family's full content
(ruling Q1, 2026-09-30 03:32:18). No input schema changed: the family seed reuses the existing
`familyRevisionId` argument.

- The description sentences on the chain rows and the family seed. [2]

## 260928-MIK-L01 The Read Description Names The Family-Complete Leaf Read

`knowledge_read`'s description in [`knowledge.py`](knowledge.py.md) gained two sentences: on a converted tree,
`source_context` with `sourcePath` is the family-complete leaf read (the path's own invariants, each containing
family's header and remaining members with their entries, then the advertised families), the same selection and
`manifestDigest` `read_ar_files` returns; and the `invariant` view names its invariant's families in `families`
(MIK-R01 rules 6 and 7). No input schema changed; a non-default `orderingInput` on a fresh leaf read is refused
by the tree read (ruling Q7, 2026-09-29 23:21:57).

- The description sentences on the leaf read. [3]

## 260928-MIK-L02 The Read Description Names The Page, The Threshold And The Continuation

`knowledge_read`'s description in [`knowledge.py`](knowledge.py.md) now states, for a converted memory tree,
that every response is a page within one token threshold, that `continuation` accepts the token any page
minted (including the published-intent block of `read_ar_files`), and that `currentness` is taken at the
walk's code tree (MIK-R02). The one schema change is `orderingInput`'s default, now `None` ("not supplied"),
with `stable_ordering` still the effective default (architect rulings Q5 of 2026-09-29 19:56:40 and F1 of
20:40:40).

- The route's read description of a bounded, cross-surface continuation. [4]

## 260928-MIK-L03 The Read Description Names `currentness`

`knowledge_read`'s description in [`knowledge.py`](knowledge.py.md) gained one sentence: for a converted
memory tree, `currentness` gives each returned invariant's state at the code tree named by `codeTreeId`, and
without it they are unverifiable (MIK-R03; architect ruling 2, 2026-09-29T18:42:37). No input schema
changed.

- The description sentence, at the walk's code tree since MIK-R02. [5]

## 260928-MIK-L08 The Integrity Check Registrar Takes A Leaf's Contract

The `knowledge_integrity_check` registrar in [`knowledge.py`](knowledge.py.md) makes `databasePath` and
`repositoryId` optional and adds the keyword-only `contractPath` (MIK-R08 rule 7); it passes all six inputs
into one `IntegrityCheckRequest`, and its published docstring says a leaf may be named without a dataset to
get its latest change-to-knowledge worklist. No registered name, response model or registration order
changed.

- The registrar's optional pair, `contractPath` and docstring. [6]

## 260928-MIK-L12 The `knowledge_change` Description Names The File Route

One sentence, and nothing else on this route moves: the `knowledge_change` registrar's published docstring now
says that on a converted memory tree (it holds `knowledge/layout.json`) both CLI entry points write knowledge
files through the curator file writer (MIK-R12) instead of the database. The tool stays registered and refusing
by architect ruling; removing it from the registered roster is MIK-R26's (leaf L26). No registered name, wire
argument, response model or registration order changed.

- The registrar's docstring sentence. [7]

## 260921-ICR-L32 The Mounted Refusal Names Both Shipped Entry Points, And Nothing Else On This Route Moves

One route-level fact, and it is the completion of the L20 section above rather than a new surface. The
`knowledge_change` registrar's published docstring now names **both** shipped CLI entry points that reach the
one writer — `agents-remember knowledge-ingest` for a leaf enclosure's ordinary route and
`agents-remember knowledge-bootstrap` for a repository with no enclosure in scope. No registered name, wire
argument, response model or registration order changed, and the refusal itself is untouched: every record kind
is still refused with `registration_absent` and nothing is written.
**Why it was one name and is now two:** when `ICR-R20@v1` landed the sentence, `knowledge-ingest` **was** the
only reachable entry point, so the singular form was true; `ICR-R29@v1` then shipped the second and left the
sentence incomplete in the one place a model reads at the moment it decides. The correction is dated and
attributed here because the earlier sentence was not false when it was written — it stopped being complete.
No staleness marker for it was ever recorded in memory, so this section *is* the record.

## 260915-KS-L41 The Knowledge Family Hands Over A Default Repository, Not Half A Resolution Pair

The knowledge registrar was already the one family in this route that consumes the runtime config at all,
and this leaf changed *what* it hands over. `_register_knowledge_read` now forwards
`repository_root=repositoryRoot` exactly as the caller supplied it — `None` stays `None` — and passes
`workspace_root=str(config.workspace_root)` as a **separate** argument into `knowledge_read_payload`. The
read builder is therefore the one place that decides whether a source-resolution pair can be named at
all. The previous spelling defaulted the root to the configured workspace and left `code_tree_id` as the
caller supplied it, and a context carrying `repository_root` without `code_tree_id` is refused by its own
model ("source resolution needs both repository_root and code_tree_id; supplying one without the other is
an incomplete resolution request") — so a minimal schema-conformant `knowledge_read` raised a raw
validation error out of the mounted tool instead of returning a view. The workspace root is now a
*default repository*: used only when the caller names no repository of its own, and then only when a tree
can actually be resolved from it.

The same family publishes one new pair of wire arguments. `knowledge_integrity_check` gained
keyword-only `runId` and `inputDigest`, forwarded unchanged to the payload builder, and its published
docstring now states the split the operation's own contract depends on: **the scope selects the recorded
run, while `runId` or `inputDigest` binds one exact run among several in that scope**, and the response
names the selected run and its input identities so the conditions cannot be read as belonging to a run
they were not measured over. Registration neither validates nor defaults either argument and assembles
none of the five run fields the response carries — that is the builder's answer. The four other
registrars still take the server alone, which remains this route's structural statement that nothing else
in the family is configured.

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

## Evidence

### Repo-Internal References

- `create_server` loops over `TOOL_REGISTRARS` and owns nothing else about the tool surface. [8]
- The payload builders every declaration forwards to. [9]
- `PUBLIC_TOOLS` — the advertised name list this package must match (63 names), defined in `models` and re-exported by the adapter. [10]
- The `PLR0913` per-file-ignore and the reasoning recorded beside it. [11]
- `TaskRef` — the shared task locator three read-side tools pack. [12]

Current working-candidate evidence for this route:

- Canonical closeout input rejects a ledger message field. [13]

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

- Worktree registration composition, re-read and re-cited by the L37 curator at the current declaration. [14]
- Public payload builders — the enclosure-adoption payload builder was removed; this route now consumes the start, attach, status and sync builders. [15]

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

## 260918-TSIP-L3 The Published Description Names Its Nine Fields (`T50`)

`curator_coherence`'s registered description is the load-bearing contract for `publish`, because the
request schema cannot express the requirement: `CuratorCoherenceRequest.model_json_schema()
["required"]` is `["action","contract_path"]`, the nine publication fields are conditional on
`action == "publish"`, and a model-level validator reports `loc: ()`. The description previously named
the identity classes `prepare` returns without marking `semantic_requirement_revision`,
`delivery_attempt` or `caller` required, so a caller could supply every field the published text named
and still be refused with *"publish requires every identity, predecessor, and caller field"*. The
registered text now names all nine — `semantic_requirement_revision`, `delivery_attempt`,
`expected_predecessor_digest`, `expected_code_candidate_tree`, `expected_memory_candidate_tree`,
`expected_task_topology_fingerprint`, `expected_task_intent`, `expected_attestation_sha256`, `caller` —
and states that `status`/`prepare`/`validate` forbid them, while
`models/lifecycles/curator_coherence.py`'s refusal appends `missing: <every absent field>`. **The two
halves are separate surfaces and can regress alone**, so both are pinned in
`mcp/tests/test_tools.py::CuratorCoherencePublishContractTests`: one `publish` request per omitted
field, each asserted against `errors()[0]["msg"]` rather than the rendered error (which echoes
`input_value` and would report "named" for a message that names nothing), with the complete request
accepted first as the positive control.

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

- The removed wait registration has no public replacement; the observation registration now declares read-only addressing, refusal behavior and typed request construction for `worktree_status`. [16]

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

## 260915-KS-L20 The Knowledge Operation Family, Appended As The Fourteenth Registrar

`mcp/registration/knowledge.py` is the family module `registration/__init__.py`'s docstring describes: one
`register_knowledge_tools(server, config)` declaring its family against the server it is handed and
delegating to the payload builders on `mcp/tools/knowledge.py`. It is **appended** to `TOOL_REGISTRARS` —
the fourteenth entry, after the capsule-and-skill registrar — and never inserted, because FastMCP publishes
tools in registration order and every existing name therefore keeps the position it was advertised at. The
five operation families are spelled as `Doc13:181-187` spells them: `knowledge_read`, `knowledge_change`,
`knowledge_diff`, `knowledge_integrity_check`, `knowledge_project`; the same five names were appended to
`PUBLIC_TOOLS`' tail and given strict response models in the same change, so the roster, the registrar and
the registry never disagreed.

**The surface performs no domain reasoning, and that is the whole contract.** Each handler validates its
wire request, delegates, and returns the typed shape the response model declares. `knowledge_read` returns
recorded claims and assessments as attributed records; `knowledge_change` records a caller-authored
proposal through an admitted operation **another leaf owns** and authors nothing; `knowledge_diff` carries
only effect labels an identified agent or assessment supplied; `knowledge_integrity_check` reports
conditions and their limits and produces no verdict; `knowledge_project` renders through the projection
writer and writes no file itself. The runtime configuration supplies exactly one thing to this family — the
workspace root a read resolves recorded source anchors against when the caller names none — because
everything else a handler needs (the dataset path, the namespace, the destination) is caller-supplied: the
substrate decides nothing about which dataset or which vault is meant.

**Nothing is mounted for the reviewer, and the refusal of that is recorded rather than implied.**
`KS-R22@v1` owns the Intent Reviewer, the cockpit route and the browser client. What this module publishes
is the interface that leaf mounts — the five operations, the review-matrix view and the typed models behind
them — and it adds no panel, no route and no client. The one honest partial in the leaf is here: a
`knowledge_change` call for a record kind outside the two admitted kinds returns the shipped
`registration_absent` refusal naming the absent admitted operation, rather than inventing a second write
path, because constructing an admitted destination from a thin tool call needs candidate-resolution facts
another owner supplies.

## 260915-KS-L32 Route Impact — The Read Request Publishes A Source-Path Seed

This leaf changed exactly one file this route governs, `mcp/src/agents_remember/mcp/registration/knowledge.py`,
and the change is a **published parameter**, not an internal one: `_register_knowledge_read` declares
`sourcePath: str | None = None` on the registered `knowledge_read` signature (line 74) and forwards it as
`source_path=sourcePath` into the request it builds (line 94). The signature IS the published schema on this
route, so a caller can now name one source path and reach `path → invariant → family` through the public tool
instead of having to discover a database path and a repository UUID first — the front-door gap CYCLE-03 named.

What did **not** change: every other registered parameter and its forwarding, the response models, the error
shapes, and the five-name roster this route publishes. The new parameter is optional and defaults to `None`,
so a caller that does not name it gets exactly the previous behaviour.

The read side of that parameter — the seed it constructs and what the view does with it — belongs to the
`mcp/src/agents_remember/application` and `models/knowledge` routes and is recorded there.

## 260921-ICR-L20 The Mounted Refusal Names The Ordinary Publication, And Nothing Else On This Route Moves

One route-level fact, and it is deliberately the smallest one this route has ever carried: the
knowledge family's *refusal* gained a sentence, and no registered name, no wire argument, no response
model and no registration order changed.

`knowledge_change` refuses every record kind with `registration_absent` and writes nothing — that is
its whole body, and it is unchanged. What changed is what its published docstring tells a caller who
reached it: the write plane's reachable entry point, `agents-remember knowledge-ingest`, no longer only
"commits a whole curator hand-off list through the admitted batch" but, **on the curator's ordinary
route, publishes that candidate to the repository's one declared published dataset location and reads
the published identity back**. A caller that reads the refusal to learn where writing *does* happen now
learns the whole route rather than half of it, which is `ICR-R20@v1`'s point: a mounted tool that can
only name a writer would leave the publication half of the ordinary route undiscoverable from the
surface a caller most likely consults.

**`260921-ICR-L32` completed that sentence's other half, which `ICR-R20@v1` could not have known about.**
When L20 landed it, `knowledge-ingest` **was** the only reachable entry point, so naming it alone was
true; `ICR-R29@v1` then shipped a second (`agents-remember knowledge-bootstrap`, the taskless
repository-foundation route) and left the docstring singular, which made the sentence incomplete about
the store in the one place a model reads at the moment it decides. L32 corrected **three** homes to name
the one writer and **both** shipped CLI entry points that reach it — this registrar's docstring
(`knowledge.md:125-127`), the module comment in `mcp/tools/knowledge.py` (`:90-93`) and the mounted
refusal detail (`:425-426`), plus the two further homes `cli/knowledge_ingest.py` (`:112-115`) and
`application/knowledge_ingest.py` (`:1-9`) that the hand sweep found. Every one was **completed, not
deleted**, and a case (`test_the_write_plane_is_named_by_both_its_shipped_entry_points`) now pins it.
**No staleness marker was ever written** for the old singular sentence: the curation that was told to
record one as "what the surface said at its bytes" did not in fact record it, so a later seat reading
the durable bytes (not the report) found the singular sentences standing unmarked and corrected them
here — dated and attributed, so a reader can tell which revision each sentence was true at.

Three things this section deliberately does **not** claim: the family is still the fourteenth and last
`TOOL_REGISTRARS` entry (five registrars, read → change → diff → integrity → projection); no handler
computes anything new; and the publication itself is not reachable from this route at all — it lives in
`application/knowledge_publication_route.py` and the CLI, and this module only names it.

- **The refusal whose docstring now names the ordinary publication and its read-back, and the registrar that declares it.** [17]
- The operation family entry point this leaf leaves exactly as it was: five registrars, declared order, appended at the tail. [18]
- **The writer the refusal names for the write half, and the module that now owns the publication half the refusal also names.** [19]
- The subcommand spelling the docstring carries, and the parser that registers it. [20]

## 260928-MIK-L23 The Knowledge Family Hands Over The Coordination Root

**Route impact (MIK-R23@v1).** In [`knowledge.py`](knowledge.py.md) the read, diff and project registrars now
also pass `coordination_root=str(config.coordination_root)` to their builders: it is where a converted memory
tree's derived index is cached when a caller's `databasePath` names such a tree. `_register_knowledge_diff`
and `_register_knowledge_project` take `config` for this. The published input schemas are unchanged, the
family's position in `TOOL_REGISTRARS` is unchanged, and no other family module moved.

- The entry point, now handing `config` to the diff and project registrars. [21]
- The three registrars that forward the coordination root. [22]
