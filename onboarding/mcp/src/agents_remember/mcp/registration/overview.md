# mcp/src/agents_remember/mcp/registration

## Governing Overview

Ordinary registration declares payload handlers lazily through registration.lazy; a valid explainer binding adds four tools to AR’s general tools, and calls to those four check the launched-seat identity. Core keeps both task_context readers and the removed-refresh refusal (hidden from `inputSchema` via `SkipJsonSchema[Any]`); central read-only marks are attached at registration in `AgentsRememberMCP.add_tool`.

[overview](../../../../../overview.md)

The explainer render registration keeps revision and run identity in the core answer and treats inventory and carried assets as optional bounded report sections.

## Purpose

`mcp/registration/` composes the advertised MCP tool families and the skill resource/protocol surface. Public Python signatures and registered descriptions live here; application behavior and response completion belong to their delegates. The server constructs its transport and application wiring, then invokes the ordered `TOOL_REGISTRARS` tuple.

## Hot Path Summary

The read_ar_files registration describes a bounded short brief for eligible paths. The read-only tool can name source, card and overview locations and carry rule text in a fuller reply. Compact rows keep each path and can give applicable existence, card status and a brief pointer with saved freshness. The description explains covering-write renewal, the refresh condition and the writer's report when refresh cannot proceed. The knowledge_read tool keeps its record naming and separate writers view.

MIK-R109: core registration removes `resolve_context`; `context_packet` advertises roots/task/actions/build/pair, not the full resolver blocks. `read_ar_files` accepts up to twenty string paths and can return knowledge locations and rule text as space permits. The document bodies stay in their files; `refresh` is annotated with `SkipJsonSchema[Any]` so it stays absent from the advertised schema while any supplied value still reaches `argument-removed`, as do object-form entries. Knowledge registration names paged records and whole comparison reports. `create_server` constructs `AgentsRememberMCP` with `enforce_read_only_marks=True` so `add_tool` attaches each tool's central annotation from `mcp/read_only.py` at registration time (refusing unlisted names before role narrowing), then enables listing-time schema compaction (`_compact_server_tool_schemas`, applied on copied `MCPTool` instances in `list_tools()` via `models/tools/tool_schema_compaction.py::compact_tool_schema` without mutating stored tools) before optional role-allowlist scoping. `read_ar_files`/`knowledge_read` are marked true; the freshness-capable context and report/capture-capable diff are false. Every ordinary registered tool description stays within the 500-character raw ceiling pinned in `test_role_tool_scope.py`.

The current ordinary source has 44 public names, including the mounted user_settings_init, explainer_control and citation_note_revision. Family registrars keep their existing request/response/application owners while using compact descriptions and docs/reference/mcp-tools.md for the longer account. Task write operations accept forwarded fields_file/section_body_file inputs; removed reads guide canonical file reading. Sync accepts the exact continue/cancel action and the `repository-default` sync source, not a knowledge_resolution input; memory content resolution remains file-authored and staged under its transaction owner. Reachable task-state refusals and role outcomes are bounded answers, not new authority from a docstring or a finished tool turn.

An ordinary `create_server` passes `build_skills_extension()` into `MCPServer(extensions=[...])` (with `preserve_handshake_extensions` middleware for pre-2026 `initialize` compatibility) and calls nine tool registrars in `TOOL_REGISTRARS` order: core, native seat retirement, memory, worktrees, closeout, tasks, native role agents, knowledge and explainer control. The explainer registrar's `render` answer carries the announce of a first browser fetch whole and adds the load's `browser` record to a publishing answer, so the seat reads the same state the review page draws. The current source `PUBLIC_TOOLS` literal contains 44 ordinary names, including native `retire_child`, `role_start_set`, the mounted `user_settings_init`, `citation_note_revision` and `explainer_control`, with `dispatch_agent` absent. This is the current source declaration, not a claim that adding those names to an old population alone computes its size or that a live server was interrogated.

## Construction

Both registered role-start handlers hand blocking work to the shared request-thread runner. Cancellation drains that work inside the still-active tool call. The outer request owns memo cleanup and the trim attempt. Role messages and the settings initializer use the detached request-thread runner instead: a cancellation ends the request at once, and an error the worker raises later is still written to the tool log.

The closeout/direct-landing registrar adds the launch-bound architect direct_execution_grant function; the task registrar retains its document/reopen/finalizer/coherence/queue groups. Direct landing selects exact leaf/grant, either existing-code verification or previewed exact-pair creation with code_commit_message/memory_commit_message and same-generation recovery. Ordinary closeout/integration retains its separate no-test/review execution contract.

### Family composition

| Module | Current surface |
| --- | --- |
| `__init__.py` | Ordered `TOOL_REGISTRARS` tuple and `ToolRegistrar` callable type. |
| `core.py` | `server_info`, `context_packet`, `read_ar_files`, `runtime_install`; public `resolve_context` is removed by MIK-R109. |
| `seat_retirement.py` | Native receipt-tracked `retire_child`; sessions.py and dispatch_agent are removed. |
| `memory.py` | `memory_quality_check`, `citation_fix`, `citation_note_revision`, `route_index_refresh`, `memory_init`, baseline status/adoption, and carryover planning/apply. |
| `worktrees.py` | Start, enclosure adoption, attach, status, sync, and pause. |
| `closeout.py` | Direct landing, `direct_execution_grant`, closeout preview/apply, integration, checkpoint publication, landing recording, operation control, cleanup, and abandonment. |
| `tasks.py` | Reopen, lifecycle finalization, task-document authoring, curator coherence, and closeout projection inspection/rebuild. |
| `capsule_serving.py` | Builds the SEP-2640 `SkillsExtension` (`build_skills_extension`) carrying `skill://` resources and extension declaration before `MCPServer` construction; no tools. |
| `role_agents.py` | `role_start` (with injected `Context`), Manager-owned `role_start_set`, `user_settings_init`, and `role_message`, in that order. |
| `knowledge.py` | `knowledge_read`, `knowledge_diff`, `knowledge_integrity_check`, and `knowledge_write`. |
| `explainer.py` | Architect-only `explainer_control`. |
| `skills_extension.py` | `SkillsExtension` (SEP-2133 `Extension`), `preserve_handshake_extensions` initialize middleware, request/result types, and `skills/list` / `skills/get` handlers; no tool declarations. |

The roster is defined in the zero-import models leaf `models/tools/public_roster.py` and re-exported by `mcp/tools/base.py`. `public_surface.py` compares observed names with that roster in exact order and checks inventory/response-model and dispatch-advertisement contracts. This describes source checks, not a newly executed verification result.

### Published schemas and delegates

The standing schema contract is that `MCPServer` derives tool inputs from Python signatures (omitting injected `Context` parameters): replacing flat parameters with one model parameter changes the published shape. Flatness remains the default; memory-quality, closeout-queue, and curator-coherence request parameters are deliberate model-shaped contracts. Preserve the registration-scoped argument-count exemption's intent rather than using it to shelter implementation logic. The root per-file ignore at pyproject.toml:38 exempts only registration modules from PLR0913; adjacent comments state the schema rationale. This source declaration is not test execution.

Native `retire_child` accepts the receipt-tracked agent_id and interrupt_turn through seat_retirement.py and delegates to the original-starter retirement owner. It is not a hosted-seat dispatch adapter. role_start/role_start_set/role_message keep their actual native selection, starter, held-message and permission-feature refusal boundaries; no undeclared-dispatch schema hook remains.

The core readers accept a task-scoped reader context where applicable. Their descriptions require the task-document reference and contract path together for canonical leaf reads (`read_ar_files` names `(task_document_ref, contract_path)` matching `TaskScopedReaderContext.model_fields`); configured Projects scope applies when it is omitted. Retained attach/status resolution uses the shared `TaskRef` locator vocabulary; it does not restore public `resolve_context`.

`runtime_install` constructs `RuntimeInstallRequest`, including the optional `experiment` input, and forwards it unchanged. Its compact description summarizes preserving user data, replacing scaffolds, provisioning the pinned Paseo host/plugin (reconciling daemon settings and leaving host restart to the developer), reporting leftover removed stores without deleting them and server currentness, and refreshing a running dashboard, pointing to `docs/tool-details.md` for details. There is no host-selection parameter. Detailed experiment-selection and absent-block application semantics remain in the application owner and are not established by this registrar description.

### Memory and knowledge contracts

`citation_fix` retains flat arguments — `document`/`documents`, an optional `contract_path`, `dry_run`, `mode` (`sync`/`start`/`poll`), and `run_id` — and no caller glob argument: the `exclude` list and the `CitationOperationScope` packing it fed were removed with the legacy citation router. What survives is internal: the fixer skips authoring-refused sidecars, which is not a caller interface. Mutually exclusive `document` and finite `documents` selectors address one card or several; empty and oversized lists are refused by the scope owner. Its compact description states that it repairs moved citation anchors and authors sidecar references in a leaf memory worktree (with `dry_run` preview or async `mode=start`+`dry_run=true` then `mode=poll`), leaves renames/deletions/ambiguous anchors to the curator, refuses legacy-format memory, and points to `docs/tool-details.md`.

Memory quality receives one mode-discriminated request and dispatches sync/start/poll to their corresponding builders. Its compact description states that it checks memory before closeout (findings, counts, checklist location, not semantic certification), accepts `mode` sync/start/poll with `contract_path` for candidate runs, includes `knowledgeWorklist` and `knowledgeGate` in full leaf logs, requires validated `curator_coherence` for ready memory, and points to `docs/tool-details.md`. Official vs candidate diagnostics, deterministic same-input publication, and attestation semantics remain owned by the controller and application owners rather than established by this overview.

The knowledge family selects converted memory roots rather than exposing database-path or caller-namespace inputs. Read receives the workspace default repository and coordination-root cache location separately; the caller's `repositoryRoot` is forwarded as supplied. Diff receives `coordination_root` for writing the full comparison report; integrity takes the server alone. The registered family contains no change or project tool. The family mounts four operations: read, diff, integrity and write. `knowledge_write` carries the command's leaf, crossing and wave target selection, takes server settings for a raise, plans by default and writes only with the explicit file-write flag, then returns the report or a refusal — the same plan, write, refusal and report behaviour as the command route, with its admission boundary and no Git commit.

The read description advertises `Read memory. Views:` naming eleven views — `source_context`, `invariant`, `family`, `record`, `records`, `impact`, `search`, `weakness`, `dependent`, `writers`, and `consolidation_proposal` (`masterId`) — notes automatic code-tree pairing via `repo_id`/`contractPath`/`memoryRoot` with `repositoryRoot`/`codeTreeId` override, notes `recordId`/`recordIds` accept text IDs (`INV-`/`WKN-`/`DPD-`), names the CLI write commands (`agents-remember knowledge-ingest` and `agents-remember knowledge-bootstrap`), and points to `docs/reference/mcp-tools.md`. Stable ordering, paging, continuations, route-chain rows, and family-complete internal selection remain owned by the knowledge reader application layer.

Integrity now accepts `memoryRoot`, `codeRoot`, `contractPath`, and `baseCommits`, constructing `IntegrityCheckRequest`. Its description names validator output and the leaf's latest change-to-knowledge worklist. The former `databasePath`/`repositoryId` and `runId`/`inputDigest` registration accounts no longer describe this wire signature.

The knowledge family mounts four operations — read, diff, integrity and write — and `knowledge_write` is curator authoring through the same plan, write, refusal and report behaviour as the command route, with server settings for a raise, a default plan, an explicit file-write flag and no Git commit. That statement must not be read as a promise of zero storage writes: the diff description explicitly says a working-tree comparison creates loose unreferenced Git objects while changing no ref, branch, index, or working file. The read description and delegate also distinguish the derived index/cache from authored knowledge.

`context_packet` describes optional drift as reference-anchor and tree-validity measurement, with invariant currentness assigned to knowledge read/integrity and no repair performed there. The current memory registrar has no `drift_check` tool. The memory registrar mounts `citation_note_revision` with the leaf contract, card/reference identity, note, base digest and dry-run flag; it advertises in-place note replacement and named refusal without changing targets or anchors. Baseline adoption's current short description distinguishes lifting the actionable drift gate from the paired-anchor validator: a stale code/test reference still refuses as `R198.1-reference-anchor`. These descriptions advertise owner contracts rather than proving a write or an adoption.

### Worktree, task, and publication descriptions

Worktree registration advertises contract-addressed reconciliation with memory-sync choice, continue/cancel actions, the `repository-default` sync source, and the warning that memory merges only through `worktree_sync` and raw `git merge` is an unsupported hand edit. Status constructs a `TaskRef` and delegates read-only observation; it has no registered wait counterpart. Enclosure adoption is present in both the current registrar and roster.

The pause/checkpoint distinction remains explicit in the registered descriptions. Pause releases atomic-series activation and hands control to the developer without publication, ref movement, commit, landing, or ledger row; it retains the master's branches, worktrees, enclosure, and unstarted leaves. Checkpoint landing publishes an unfinished master's accumulated committed pair to its source branch under explicitly requested developer approval, keeps the master open, and does not retire or clean it up. These are distinct verbs in separate families.

> **Retained historical source account — superseded by the current route account:**
> Closeout wiring is divided into direct-landing, closeout-command, integration-command, and reclamation helpers. The public message vocabulary is code and memory only; the canonical input model forbids extras. Enabled commit legs require explicit nonblank messages according to the descriptions; direct landing verifies existing code rather than accepting a code-message input. Operation control is task-addressed and publishes a generation, while keeping private operation keys and process IDs off the wire. Registration forwards corrective dispositions rather than deciding them.

> **Retained historical source account — superseded by the current route account:**
> The standing transaction-only account says closeout/integration delegate publication and do not automatically acquire certification, strict quality, coherence, or independent-review authority. The older automatic altitude-gate account conflicts with that standing account and is not retained as a current promise. The lower application owners were not completely examined here, so neither account is promoted to fresh lifecycle acceptance.

> **Retained historical source account — superseded by the current route account:**
> Task-document authoring remains separate from activation/publication. Its operation is a plain string; the published description carries the operation vocabulary. The step plane distinguishes update, create, reasoned removal, and focused read, addresses a unit by `step={id,parent?}`, and describes reasoned removal of a done unit or on a Completed document. Execution-graph authoring describes a validated mutation batch, graph-less bootstrap, judgment-bearing changes, and structural constraints; registration forwards the typed target/edit/call values.

> **Retained historical source account — superseded by the current route account:**
> The task description identifies retirement as the operation that archives a master, distinguishes sprint-commanded and standalone retirement, and states readiness refusals, explicit edge removal for unfinished successors, preview, and same-request recovery. It also says an abandoned row does not block a master and that a sprint-commanded master stays in place when finalized. These facts belong to the task description, not the native-role source attached to inherited reference 24.

> **Retained historical source account — superseded by the current route account:**
> Lifecycle finalization's current description derives the exact leaf row from an existing immediate parent or a folder `task.json` master listing it; a sub-task with neither is refused. Optional parent assertions must match the derived edge. It refuses unresolved declared steps, does not auto-check steps or complete recursive ancestors, and requires landed-state/carryover checks before cleanup.

Curator coherence's compact description names its four actions (`prepare`, `publish`, `inspect`, `validate`), all nine required publication identity/caller fields, inline or file-backed judgments (`judgments` or `judgments_file`), and points to `docs/tool-details.md` for the longer explanation. Structured-manifest authority, action-specific validation, candidate-set file/rendering, exact evidence namespaces, duplicate-input refusal and publication/readiness semantics belong to the request/application owners; shortening the docstring does not make those detailed clauses current registration promises or confer acceptance. Closeout queue's compact description names inspecting or rebuilding a sprint's waiting-only closeout queue and its states (`valid-built`, `invalid-empty`, `blocked`), pointing to `docs/reference/mcp-tools.md`; it does not declare, select, defer, withdraw, or mutate closeout intent.

### Skill transport

After proving the catalog servable, `capsule_serving.build_skills_extension` constructs a `SkillsExtension` (SEP-2133 `Extension`) carrying the `io.modelcontextprotocol/skills` capability, `skills/list` and `skills/get` `MethodBinding` entries, and `ResourceBinding` entries for `skill://index.json` and each served skill file, passed to `MCPServer(extensions=[...])` at server construction with `preserve_handshake_extensions` middleware restoring `capabilities.extensions` and `capabilities.experimental={}` on pre-2026 `initialize` responses. Both method handlers use the catalog registry. The index resource retains this server's own well-known-discovery shape; extension enumeration is `skills/list`, not that index. The optional directory-read method/capability is deliberately absent.

Resource construction delegates reads to the served-file owner; registration does not activate skills or confer local-file trust. Resource and skill counts depend on the actual catalog and are not fixed here at the inherited 85-resource/14-skill values. The formerly advertised capsule/catalog tools are absent from the current registrar and roster.

Closeout and landing compact descriptions name each route's states and knowledge-gate / durable-generation boundaries (with `docs/reference/mcp-tools.md` carrying the longer account), rather than promising broad quality, certification, or review gates. Direct landing exposes optional `leaf_id` and recovers via `worktree_operation_control`; closeout preview/apply name the knowledge-gate check and `knowledge-gate-refused` findings; integration, checkpoint landing, and recorded landing keep their exact transaction checks in their application owners.

> **Retained historical source account — superseded by the current route account:**
> The existing role_message registration adds file-only body, attachments and filed-message/reply/hash/limit/successor response fields through its strict models. Registered tool identity remains the same while input/result shape extends; no message index/search/public dashboard tool is introduced. Whole payloads are not copied into wake text.

## Invariants And Boundaries

- Preserve approved public schema shapes and registration order. A new advertised tool requires coordinated registrar, roster, response-model, and reference-document changes; a new family requires a tuple entry.
- Keep ordinary tool bodies focused on request construction and delegation. This is standing intent, not a claim that every function in this directory is a decorated tool: resource constructors, extension wiring, registrars, and helpers are present.
- Keep semantic decisions and validation with their deciding owners. The narrow dispatch-input check closes the transport schema without moving application authority into registration.
- Keep runtime actor identity and private operation capabilities out of caller-invented identifiers. Native role registration constructs typed calls and delegates to the Paseo role adapter; registration alone does not prove exact replay, model/effort/tier validation, or real native bindings.
- Do not add arbitrary-shell or arbitrary-command tools.
- Published descriptions must identify operation intent and refusal vocabulary accurately, including publication versus pause and preview versus mutation.

## Verification And Authority Limits

Lifecycle status and acceptance are outside these operative descriptions. No tests, quality tools, native-host exchanges, installations, commits, or acceptance operations were executed for this proposal. Missing lifecycle authority is an uncertainty, not a new current status.

Historical assertions about signature-exemption tests, fixture pinning, seeded mutation outcomes, SDK measurement, historical offender counts, import-migration effects, refresh-validator parity, automatic integration gates, and application-only experiment/baseline behavior were not established by the bounded source review. They remain named verification gaps rather than executable promises. The standing schema and delegation intent survives above; discrepancies in current implementation are disclosed rather than silently repaired.

The following inherited metadata is retained verbatim and is not lifecycle or acceptance authority:

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/mcp/registration`       |

## Citation preview registration

The memory family extends the existing `citation_fix` declaration with flat `mode` and `run_id` fields. It preserves synchronous repair and admits background start only for preview. Mode validation and projection remain in the payload owner; registration does not create another registry.

- **Retained historical source account — superseded by the current route account:** Finalization description includes folder-master derivation and refusal.
- **Retained historical source account — superseded by the current route account:** Read description retains route-chain rows and family selection.
- **Retained historical source account — superseded by the current route account:** Current family-complete read description; former range crossed into request construction.
- **Retained historical source account — superseded by the current route account:** Bounded paging, continuation, and walk-currentness description.
- **Retained historical source account — superseded by the current route account:** Current walk-code-tree currentness description.
- **Retained historical source account — superseded by the current route account:** Current tree/contract integrity signature and delegate replace the database/run-selection account.
- **Retained historical source account — superseded by the current route account:** Three-operation knowledge composition.
- **Retained historical source account — superseded by the current route account:** Server invokes the ordered registrar tuple after application/transport wiring.
- **Retained historical source account — superseded by the current route account:** Shared response adapter delegates whole-result and optional answer completion.
- **Retained historical source account — superseded by the current route account:** Roster declaration and unchanged adapter export; current count is 41.

- Current single literal PUBLIC_TOOLS contains 44 ordinary public names (the predecessor41 plus user_settings_init, explainer_control and citation_note_revision) and excludes dispatch_agent; native role, retirement and knowledge vocabulary remains. Source census only, no live advertisement, new CODE grade or MEMORY acceptance. The retained base export is the same roster object.
- **Retained historical source account — superseded by the current route account:** Inherited argument-count exemption target retained pending location confirmation.
- **Retained historical source account — superseded by the current route account:** Shared task locator.
- **Retained historical source account — superseded by the current route account:** Canonical message input and refused-field vocabulary retain both named co-targets.
- **Retained historical source account — superseded by the current route account:** Current worktree registrar composition replaces the old import-range target.
- **Retained historical source account — superseded by the current route account:** Attach import retained; enclosure adoption is also currently imported.
- **Retained historical source account — superseded by the current route account:** Existing status-related range retained with the complete current handler as deciding witness.
- **Retained historical source account — superseded by the current route account:** Three-operation knowledge family, without mounted change/project.
- **Retained historical source account — superseded by the current route account:** Read receives runtime roots; diff and integrity keep separate delegates.
- **Retained historical source account — superseded by the current route account:** Current citation handler includes converted-memory, finite card selection, status-answer and caller-exclude descriptions.
- **Retained historical source account — superseded by the current route account:** Native role registration declares start, set start and messaging; it does not witness task retirement.
- **Retained historical source account — superseded by the current route account:** Core identity, reader-context, and install registration.
- Ordered composition uses seat retirement, not a removed sessions registrar, and retains the capsule resource position between task and role-agent registration.

- **Retained historical source account — superseded by the current route account:** Server wiring and strict dispatch boundary.
- **Retained historical source account — superseded by the current route account:** Runtime request construction and current installation description.

- Current composed PUBLIC_TOOLS declares 44 ordinary names (the predecessor 41 plus user_settings_init, citation_note_revision and explainer_control); the41-name predecessor membership is historical. This is source declaration only, not runtime advertisement or execution.

- **Retained historical source account — superseded by the current route account:** Skill resources, declaration coupling, and index/file construction.
- **Retained historical source account — superseded by the current route account:** Extension installation and catalog-backed methods.
- **Retained historical source account — superseded by the current route account:** Task descriptions, including coherence transport, retirement and current queue projection.
- **Retained historical source account — superseded by the current route account:** Pause and sync descriptions and forwarding.
- **Retained historical source account — superseded by the current route account:** Closeout descriptions, message inputs, and delegate composition.
- **Retained historical source account — superseded by the current route account:** Native-role adapters forward typed single-start, set-start and message calls to Paseo owners.

- The current ordinary source has 44 public names, including the mounted user_settings_init, citation_note_revision and explainer_control. Family registrars keep their existing request/response/application owners while using compact descriptions and docs/reference/mcp-tools.md for the longer account. Task write operations accept forwarded fields_file/section_body_file inputs; removed reads guide canonical file reading. Sync accepts the exact continue/cancel action and the `repository-default` sync source, not a knowledge_resolution input; memory content resolution remains file-authored and staged under its transaction owner. Reachable task-state refusals and role outcomes are bounded answers, not new authority from a docstring or a finished tool turn. Source declaration only; no live advertisement, execution or acceptance is inferred.

## The settings initializer's registration

`role_agents.py` mounts `user_settings_init` beside the three role tools and reads the caller's harness name from the served request's own client info, so a launch is told which harness the calling chat runs and is told nothing when the client named none.

- The transport's own client name, or no name at all.
- The registration that mounts the role tools and the settings initializer.

 pyproject.toml — lines 38-38

The mounted `knowledge_read` registration describes the `writers` view as per-writer aggregates with revision counts and a complete report path. Record rows still carry IDs, kinds, states and locations.

## Evidence

- \[7] mcp/src/agents_remember/mcp/registration/knowledge.py — symbol register_knowledge_tools

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/mcp/server.py::create_server - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

- The current composed ordinary source has 44 public names, including the mounted user_settings_init, explainer_control and citation_note_revision. Family registrars keep their existing request/response/application owners while using compact descriptions and docs/reference/mcp-tools.md for the longer account. Task write operations accept forwarded fields_file/section_body_file inputs; removed reads guide canonical file reading. Sync accepts the exact continue/cancel action and the `repository-default` sync source, not a knowledge_resolution input; memory content resolution remains file-authored and staged under its transaction owner. Reachable task-state refusals and role outcomes are bounded answers, not new authority from a docstring or a finished tool turn.
 mcp/src/agents_remember/mcp/registration/role_agents.py — symbol register_role_agent_tools; mcp/src/agents_remember/mcp/registration/role_agents.py — symbol role_start; mcp/src/agents_remember/mcp/registration/role_agents.py — symbol role_start_set; mcp/src/agents_remember/mcp/registration/role_agents.py — symbol role_message
 mcp/src/agents_remember/mcp/registration/tasks.py — symbol _register_closeout_queue_tools; mcp/src/agents_remember/mcp/registration/tasks.py — symbol _register_curator_coherence_tools; mcp/src/agents_remember/mcp/registration/tasks.py — symbol _register_task_reopen_tools; mcp/src/agents_remember/mcp/registration/tasks.py — symbol _register_task_finalizer_tools; mcp/src/agents_remember/mcp/registration/tasks.py — symbol _TASK_DOC_TOOL_DESCRIPTION; mcp/src/agents_remember/mcp/registration/tasks.py — symbol _register_task_document_tools; mcp/src/agents_remember/mcp/registration/tasks.py — symbol register_task_tools
 mcp/src/agents_remember/models/tools/public_roster.py — code file; mcp/src/agents_remember/mcp/registration/tasks.py — code file; mcp/src/agents_remember/mcp/registration/worktrees.py — code file; mcp/src/agents_remember/mcp/registration/closeout.py — code file; mcp/src/agents_remember/mcp/registration/role_agents.py — code file
 mcp/src/agents_remember/mcp/registration/role_agents.py — symbol register_role_agent_tools


- The role-agent registrar mounts `role_start`, `role_start_set`, `user_settings_init`, and `role_message`; the callables preserve their declared argument shapes and delegate to their application payload owners. [24]



- The task registrar composes closeout queue, curator coherence, task reopen and finalizer tools with task_doc registration; the shared task_doc description names write operations and alignmentSweep. [33]




- The current composed ordinary source has 44 public names, including the mounted user_settings_init, explainer_control and citation_note_revision. Family registrars keep their existing request/response/application owners while using compact descriptions and docs/reference/mcp-tools.md for the longer account. Task write operations accept forwarded fields_file/section_body_file inputs; removed reads guide canonical file reading. Sync accepts the exact continue/cancel action and the `repository-default` sync source, not a knowledge_resolution input; memory content resolution remains file-authored and staged under its transaction owner. Reachable task-state refusals and role outcomes are bounded answers, not new authority from a docstring or a finished tool turn. [38]





- register_role_agent_tools owns the mounted role-agent declarations and dispatches them to their existing application payload owners. [40]



- One registered citation operation forwards the extended signature. [42]

- Lifecycle finalization proves the landed edge, completes a task once all steps are done, and reconciles its parent row (ancestors are not completed; leaves require a master). [1]

- Current single literal PUBLIC_TOOLS contains 44 ordinary public names, including mounted `user_settings_init`, `explainer_control` and `citation_note_revision`, and excludes dispatch_agent; native role, retirement and knowledge vocabulary remains. Source census only, no live advertisement, new CODE grade or MEMORY acceptance. The retained base export is the same roster object. [10]

- Current composed PUBLIC_TOOLS declares 44 ordinary names; the 41-name predecessor membership is historical. This is source declaration only, not runtime advertisement or execution. [29]
[2] mcp/src/agents_remember/mcp/registration/knowledge.py — lines 95-97
[3] mcp/src/agents_remember/mcp/registration/knowledge.py — lines 90-99
[4] mcp/src/agents_remember/mcp/registration/knowledge.py — lines 85-98
[5] mcp/src/agents_remember/mcp/registration/knowledge.py — lines 89-91

- The integrity registrar mounts `knowledge_integrity_check` for converted-tree validation and leaf worklist reporting. [6]


- \[6] mcp/src/agents_remember/mcp/registration/knowledge.py — symbol _register_knowledge_integrity_check [7]


- The shared MCP adapter declares _tool_payload and forwards the whole tool result, optional projection and optional fitter into response completion. [9]

[10] mcp/src/agents_remember/models/tools/public_roster.py — symbol PUBLIC_TOOLS; mcp/src/agents_remember/mcp/tools/base.py — symbol __all__
[12] mcp/src/agents_remember/application/task_docs/task_ref.py — symbol TaskRef
[13] mcp/src/agents_remember/models/closeout/input.py — symbol CloseoutMessageInput; mcp/src/agents_remember/models/closeout/input.py — symbol CloseoutInvalidField

- \[13] mcp/src/agents_remember/models/closeout/input.py — symbol CloseoutMessageInput; mcp/src/agents_remember/models/closeout/input.py — symbol CloseoutInvalidField [14]

- \[16] mcp/src/agents_remember/mcp/registration/worktrees.py — lines 172-199; mcp/src/agents_remember/mcp/registration/worktrees.py — lines 177-203 [17]

- mcp/src/agents_remember/mcp/registration/core.py — code file [26]

[29] mcp/src/agents_remember/models/tools/public_roster.py — code file

- Skill resources, extension assembly, and index/file resource construction. [31]

- SEP-2133 `SkillsExtension` registration, initialize handshake middleware, and catalog-backed `skills/list` and `skills/get` handlers. [32]

- \[10] mcp/src/agents_remember/models/tools/public_roster.py — symbol PUBLIC_TOOLS; mcp/src/agents_remember/mcp/tools/base.py — symbol __all__ The root PLR0913 exception supports the flat MCP registration signatures; it is not itself the PUBLIC_TOOLS or __all__ declaration. [11]
- `citation_fix` repairs moved citation anchors and authors sidecar references in a leaf memory worktree. [23]

- The ordered ordinary registrar tuple includes explainer control, and the same server adds the bound explainer surface only for a launch that bound it as an explainer seat. [41]




- The mounted knowledge tool registrar delegates read, diff, integrity and writing to their distinct registrations. [22]
