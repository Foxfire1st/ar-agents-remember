# mcp/src/agents_remember/mcp/registration

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`mcp/registration/` composes the advertised MCP tool families and the skill resource/protocol surface. Public Python signatures and registered descriptions live here; application behavior and response completion belong to their delegates. The server constructs its transport and application wiring, then invokes the ordered `TOOL_REGISTRARS` tuple.

## Hot Path Summary

MIK-R109: core registration removes `resolve_context`; `context_packet` advertises roots/task/actions/build/pair, not the full resolver blocks. `read_ar_files` accepts up to twenty string paths and returns knowledge locations, not document text; `refresh` is absent from the advertised schema but any supplied value reaches `argument-removed`, as do object-form entries. Knowledge registration names paged records and whole comparison reports. `create_server` applies every tool’s annotation from `mcp/read_only.py` after the registrars, refusing unlisted names. `read_ar_files`/`knowledge_read` are marked true; the freshness-capable context and report/capture-capable diff are false.

`create_server` calls nine registrars in order: core, sessions, memory, worktrees, closeout, tasks, capsule/skill resources, native role agents, and knowledge. Eight declare tools; the capsule registrar publishes resources and installs skill protocol support without declaring tools. The current `PUBLIC_TOOLS` literal contains 41 names, adding native `retire_child` and `role_start_set` to the old 39-name tuple.

A tool handler normally constructs its request value and forwards it to a payload builder. Memory quality dispatches its typed request by mode; native role calls use `asyncio.to_thread` around their payload builders. The shared `_tool_payload` adapter delegates the whole result and an optional compact answer to the application boundary; the boundary validates and logs the whole result and guards the delivered answer. Registration does not independently grant approval, retry, publication, or actor authority.

## Construction

The closeout/direct-landing registrar adds the launch-bound architect direct_execution_grant function; the task registrar retains its document/reopen/finalizer/coherence/queue groups. Direct landing selects exact leaf/grant, either existing-code verification or previewed exact-pair creation with code_commit_message/memory_commit_message and same-generation recovery. Ordinary closeout/integration retains its separate no-test/review execution contract.

### Family composition

| Module | Current surface |
| --- | --- |
| `__init__.py` | Ordered `TOOL_REGISTRARS` tuple and `ToolRegistrar` callable type. |
| `core.py` | `server_info`, `context_packet`, `read_ar_files`, `runtime_install`; public `resolve_context` is removed by MIK-R109. |
| `sessions.py` | `dispatch_agent` and native receipt-tracked `retire_child`. |
| `memory.py` | `memory_quality_check`, `citation_fix`, `route_index_refresh`, `memory_init`, baseline status/adoption, and carryover planning/apply. |
| `worktrees.py` | Start, enclosure adoption, attach, status, sync, and pause. |
| `closeout.py` | Direct landing, closeout preview/apply, integration, checkpoint publication, landing recording, operation control, cleanup, and abandonment. |
| `tasks.py` | Reopen, lifecycle finalization, task-document authoring, curator coherence, and closeout projection inspection/rebuild. |
| `capsule_serving.py` | Skill index/file resources, extension declaration, and protocol-method installation; no tools. |
| `role_agents.py` | `role_start`, Manager-owned `role_start_set`, and `role_message`, in that order. |
| `knowledge.py` | `knowledge_read`, `knowledge_diff`, and `knowledge_integrity_check`. |
| `skills_extension.py` | Skill request/result types, dispatcher support, and `skills/list` / `skills/get` handlers; no tool declarations. |

The roster is defined in the zero-import models leaf `models/tools/public_roster.py` and re-exported by `mcp/tools/base.py`. `public_surface.py` compares observed names with that roster in exact order and checks inventory/response-model and dispatch-advertisement contracts. This describes source checks, not a newly executed verification result.

### Published schemas and delegates

The standing schema contract is that FastMCP derives tool inputs from Python signatures: replacing flat parameters with one model parameter changes the published shape. Flatness remains the default; memory-quality, closeout-queue, and curator-coherence request parameters are deliberate model-shaped contracts. Preserve the registration-scoped argument-count exemption's intent rather than using it to shelter implementation logic. The root per-file ignore at pyproject.toml:38 exempts only registration modules from PLR0913; adjacent comments state the schema rationale. This source declaration is not test execution.

`dispatch_agent` takes a canonical task-document reference, role, brief, and optional label. Its description distinguishes a plane-hosted caller from an ambient launcher: hosted authority comes from injected identity, while ambient dispatch has no parent seat but retains role-altitude validation. A present invalid hosted identity is described as a refusal, not an ambient retry. The server closes the advertised dispatch schema and rejects undeclared dispatch fields before invoking the handler. Native `retire_child` separately accepts the receipt-tracked `agent_id` and `interrupt_turn`; its adapter calls the original-starter retirement owner rather than the former hosted-seat path. `role_start_set` constructs per-seat choices and delegates to the owning-Manager scope checks; shared launch selection rejects caller-supplied permission-bearing features.

The core readers accept a task-scoped reader context where applicable. Their descriptions require the task-document reference and contract path together for canonical leaf reads; configured Projects scope applies when it is omitted. Retained attach/status resolution uses the shared `TaskRef` locator vocabulary; it does not restore public `resolve_context`.

`runtime_install` constructs `RuntimeInstallRequest`, including the optional `experiment` input, and forwards it unchanged. Its current description covers preservation of user data, scaffold replacement, pruning legacy binaries, reporting unused provider keys, and provisioning the build-pinned host/plugin from the shared `paseoRuntime` block without writing shared settings. There is no host-selection parameter. The older experiment-selection and absent-block result promises are not stated by this registrar's current description; their application semantics remain an explicit verification gap.

### Memory and knowledge contracts

`citation_fix` retains flat arguments and an optional keyword-only `exclude` list. Its description says caller globs narrow one call beyond configured onboarding exclusions and `.gitignore`; the handler packs them into `CitationOperationScope`. Mutually exclusive `document` and finite `documents` selectors address one card or several; empty and oversized lists are refused by the scope owner. Converted-memory authoring records citation rows into sidecar references and re-records moved anchors; selected cards need no `expected_snapshot` in that mode. The description distinguishes a count-bearing status answer from the whole result in the log detail file. The description also distinguishes leaf-contract admission from pre-baseline bootstrap admission. Validation of individual exclude patterns belongs to the scope/application owner and is not independently established here.

Memory quality receives one mode-discriminated request and dispatches sync/start/poll to their corresponding builders. Its registered description distinguishes official repository diagnostics from exact contract-scoped candidate runs, raw checklist status from coherence readiness, and structured report-digest-bound attestation from semantic certification. It describes deterministic same-input publication and contract-scoped census/report output; these are advertised owner contracts, not evidence of a run performed for this overview.

The knowledge family selects converted memory roots rather than exposing database-path or caller-namespace inputs. Read receives the workspace default repository and coordination-root cache location separately; the caller's `repositoryRoot` is forwarded as supplied. Diff and integrity have separate delegates and do not receive that configuration pair. The registered family contains no change or project tool. Its description directs curator authoring to knowledge-ingest or knowledge-bootstrap rather than a mounted knowledge writer.

The read description names three views, `source_context`, `invariant`, and `family`; stable ordering is effective when `orderingInput` is omitted. Pages and continuations share the bounded knowledge-read contract, including supported tokens from retained internal published-intent computation. Mounted `read_ar_files` now names files without a published-intent body or continuation. The following full-selection account describes internal computation; the mounted knowledge reader projects record names and locations. `currentness` is described at the walk's code tree, including the continuation's tree on resumed pages; without one, invariants are unverifiable. A source-path read includes the path's invariants, containing-family headers and remaining members, advertised families, then compact route-chain family rows. A family ID without a source path selects the full family, and invariant views name their families.

Integrity now accepts `memoryRoot`, `codeRoot`, `contractPath`, and `baseCommits`, constructing `IntegrityCheckRequest`. Its description names validator output and the leaf's latest change-to-knowledge worklist. The former `databasePath`/`repositoryId` and `runId`/`inputDigest` registration accounts no longer describe this wire signature.

The knowledge family says that knowledge authoring is outside the mounted surface. That statement must not be read as a promise of zero storage writes: the diff description explicitly says a working-tree comparison creates loose unreferenced Git objects while changing no ref, branch, index, or working file. The read description and delegate also distinguish the derived index/cache from authored knowledge.

`context_packet` describes optional drift as reference-anchor and tree-validity measurement, with invariant currentness assigned to knowledge read/integrity and no repair performed there. The current memory registrar has no `drift_check` tool. The inherited baseline-adoption description account requires application-owner verification before it can be treated as an operative promise.

### Worktree, task, and publication descriptions

Worktree registration advertises contract-addressed reconciliation with memory-sync choice and continue/cancel actions. Status constructs a `TaskRef` and delegates read-only observation; it has no registered wait counterpart. Enclosure adoption is present in both the current registrar and roster, contrary to the inherited removal account.

The pause/checkpoint distinction remains explicit in the registered descriptions. Pause releases atomic-series activation and hands control to the developer without publication, ref movement, commit, landing, or ledger row; it retains the master's branches, worktrees, enclosure, and unstarted leaves. Checkpoint landing publishes an unfinished master's accumulated committed pair to its source branch under explicitly requested developer approval, keeps the master open, and does not retire or clean it up. These are distinct verbs in separate families.

Closeout wiring is divided into direct-landing, closeout-command, integration-command, and reclamation helpers. The public message vocabulary is code and memory only; the canonical input model forbids extras. Enabled commit legs require explicit nonblank messages according to the descriptions; direct landing verifies existing code rather than accepting a code-message input. Operation control is task-addressed and publishes a generation, while keeping private operation keys and process IDs off the wire. Registration forwards corrective dispositions rather than deciding them.

The standing transaction-only account says closeout/integration delegate publication and do not automatically acquire certification, strict quality, coherence, or independent-review authority. The older automatic altitude-gate account conflicts with that standing account and is not retained as a current promise. The lower application owners were not completely examined here, so neither account is promoted to fresh lifecycle acceptance.

Task-document authoring remains separate from activation/publication. Its operation is a plain string; the published description carries the operation vocabulary. The step plane distinguishes update, create, reasoned removal, and focused read, addresses a unit by `step={id,parent?}`, and describes reasoned removal of a done unit or on a Completed document. Execution-graph authoring describes a validated mutation batch, graph-less bootstrap, judgment-bearing changes, and structural constraints; registration forwards the typed target/edit/call values.

The task description identifies retirement as the operation that archives a master, distinguishes sprint-commanded and standalone retirement, and states readiness refusals, explicit edge removal for unfinished successors, preview, and same-request recovery. It also says an abandoned row does not block a master and that a sprint-commanded master stays in place when finalized. These facts belong to the task description, not the native-role source attached to inherited reference 24.

Lifecycle finalization's current description derives the exact leaf row from an existing immediate parent or a folder `task.json` master listing it; a sub-task with neither is refused. Optional parent assertions must match the derived edge. It refuses unresolved declared steps, does not auto-check steps or complete recursive ancestors, and requires landed-state/carryover checks before cleanup.

Curator coherence's description names all nine conditional publication identity/caller fields and forbids them for status/prepare/validate. It separates structured authority from generated Markdown, requires explicit evidence namespaces and candidate judgments, and delegates validation to the shared owner. `prepare` describes a complete candidate-set file and reading rendering, with counts, digest and locations in the answer. `publish` permits inline judgments/assessments or one absolute `judgments_file`, refuses supplying a list both ways, and answers published counts and the file SHA-256 when used. These transport changes do not change publication expectations or acceptance authority. Closeout queue now advertises inspection or idempotent rebuild of a disposable projection: exact-current valid-built or non-admitting invalid-empty, with current task/door truth as inputs. It explicitly does not declare, select, defer, withdraw, or mutate closeout intent; the inherited action-specific scheduling-mutation account is obsolete.

### Skill transport

After proving the catalog servable, skill registration declares the extension and installs its mandatory methods together, then adds the server's index resource and each served skill file. The extension installer adds request-union and dispatcher support and installs handlers in the SDK request-handler map. Both method handlers use the catalog registry. The index resource retains this server's own well-known-discovery shape; extension enumeration is `skills/list`, not that index. The optional directory-read method/capability is deliberately absent.

Resource construction delegates reads to the served-file owner; registration does not activate skills or confer local-file trust. Resource and skill counts depend on the actual catalog and are not fixed here at the inherited 85-resource/14-skill values. The formerly advertised capsule/catalog tools are absent from the current registrar and roster.

Closeout and landing descriptions separate each route's exact invariant judgment from broad quality/certification/review. Direct landing exposes optional leaf_id; leaf integration rejudges its closeout pair; master final/checkpoint/recorded routes declare validator, net staleness, chain and history checks.

The existing role_message registration adds file-only body, attachments and filed-message/reply/hash/limit/successor response fields through its strict models. Registered tool identity remains the same while input/result shape extends; no message index/search/public dashboard tool is introduced. Whole payloads are not copied into wake text.

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

## Evidence


- Finalization description includes folder-master derivation and refusal. [1]
- Read description retains route-chain rows and family selection. [2]
- Current family-complete read description; former range crossed into request construction. [3]
- Bounded paging, continuation, and walk-currentness description. [4]
- Current walk-code-tree currentness description. [5]
- Current tree/contract integrity signature and delegate replace the database/run-selection account. [6]
- Three-operation knowledge composition. [7]
- Server invokes the ordered registrar tuple after application/transport wiring. [8]
- Shared response adapter delegates whole-result and optional answer completion. [9]
- Roster declaration and unchanged adapter export; current count is 41. [10]
- Inherited argument-count exemption target retained pending location confirmation. [11]
- Shared task locator. [12]
- Canonical message input and refused-field vocabulary retain both named co-targets. [13]
- Current worktree registrar composition replaces the old import-range target. [14]
- Attach import retained; enclosure adoption is also currently imported. [15]
- Existing status-related range retained with the complete current handler as deciding witness. [16]
- Three-operation knowledge family, without mounted change/project. [17]
- Read receives runtime roots; diff and integrity keep separate delegates. [22]
- Current citation handler includes converted-memory, finite card selection, status-answer and caller-exclude descriptions. [23]
- Native role registration declares start, set start and messaging; it does not witness task retirement. [24]
- Core identity, reader-context, and install registration. [25]
- Current ordered family composition. [26]
- Server wiring and strict dispatch boundary. [27]
- Runtime request construction and current installation description. [28]
- Current 41-name roster membership. [29]
- Exact-order inventory and dispatch advertisement validation. [30]
- Skill resources, declaration coupling, and index/file construction. [31]
- Extension installation and catalog-backed methods. [32]
- Task descriptions, including coherence transport, retirement and current queue projection. [33]
- Pause and sync descriptions and forwarding. [34]
- Closeout descriptions, message inputs, and delegate composition. [35]
- Ambient/hosted dispatch description and typed forwarding. [36]
- Native-role adapters forward typed single-start, set-start and message calls to Paseo owners. [37]
