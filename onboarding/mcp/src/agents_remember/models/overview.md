# mcp/src/agents_remember/models/ - Response Contract Models Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/models/`          |
| doc_type               | `route-local-overview`                     |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Current Structural Wire Vocabulary

`TaskDocumentRef` is the shared repository-qualified work identity. `models/structural/agent.py` and
`models/structural/gates.py` define the agent-facing request/response families without runtime
address fields; internal gate correlation models are isolated behind that public boundary. The
former flat gate model has moved, with its semantic history preserved in the successor card.
`TaskDocumentRef` is a frozen value object whose explicit hash uses repository plus path; task
altitude remains topology-owned rather than becoming a third identity field.

`models/task_document.py` also owns the closed `MasterExecutionNature` wire vocabulary:
`organizational|atomic`. Persisted task-document schema, observer projection, generated dashboard
schema, and TypeScript all import or derive from that one enum rather than maintaining parallel
strings.

`lifecycles/operation.py` adds strict closeout/integration input snapshots, an internal durable
record, and a deliberately smaller public projection. The record carries private fingerprint,
candidate tree, PID, approval claim, and recovery details; the projection exposes only the task,
kind, state, phase, heartbeat, current command, result/failure, and guidance required by agents
and the dashboard. `models/worktree.py` embeds that projection without publishing operation IDs.

## Purpose

`models/` owns the Pydantic response contracts for Agents Remember MCP payload
builders. It turns the public tool surface and internal builders
from loose dictionaries into named, inspectable models that can be validated at
runtime and tested by schema. Model homes follow tool domains: `TaskReopenResponse`
(cit:([`TaskReopenResponse`], mcp/src/agents_remember/models/task_doc.py:88-91)) lives in `task_doc.py` while keeping the `WorktreeCommandResponse` shape, since
the task_reopen payload carries the enclosure contract state.

## Hot Path Summary

ACPUI-L2 adds `launch-selection-invalid` to the strict terminal spawn response for an incomplete
role-configured native selection. Existing `resolvedModel`/`resolvedEffort` fields continue to
carry settings provenance, while `sessionCommands` is now explicitly user-authored launch
configuration rather than a normalized model/effort vehicle. Dynamic catalog and process failures
remain hosted control evidence and do not inflate the pre-spawn status enum.

HFX2-L17 adds binding identity to terminal responses: attach can return `role-required` and carries
`seatRole`/`previousSeatRole`; spawn carries `seatRole`. The legacy `role` field still means
transport (`chat` or `terminal`) and is not orchestration identity.

HFX2-L15 extends the terminal spawn response with `replacementForLeaf`, resolved model/effort, and
bound session-log entry/path provenance. Delivery booleans are evidence-specific: context is true
only for the id-bearing user record, and commands require command plus non-error stdout evidence.

Start with `tool_registry.py`: `TOOL_RESPONSE_MODELS` maps every modeled builder
to one response model, while `PUBLIC_TOOL_RESPONSE_MODELS` filters out retained
compatibility builders so it matches `mcp.tools.PUBLIC_TOOLS`. Both are typed
`dict[str, type[ResponseEnvelope]]` (260731-EFA-L4), not `type[BaseModel]`.
`base.py` defines strict response envelopes, intentionally
flexible detail envelopes, token metadata fields, and the strict `NextStep`
lifecycle-hint model carried by an optional `nextStep` field on BOTH envelope
bases (`ResponseModel` and `FlexibleResponseEnvelope`), so every modeled tool
response can surface the computed next move; 260731-EFA-L4 declares the
`supervisorBanner: str | None` stale-supervisor field beside it on both bases and
names their union `ResponseEnvelope`. Domain modules then own
contract slices: `context_packet.py` for compact `ContextPacketV2`,
`providers.py` for provider summaries and diagnostics, `worktree.py` for
worktree context/status responses including `enclosurePath`, `leafId`, and `kind`, `memory.py` for memory/onboarding tools,
`runtime.py` for runtime and resolver tools, `benchmarks.py` for Codex
benchmark tools, `lifecycles/responses.py` for the `lifecycle_*` signal responses
(with `LifecycleStartResponse` also carrying an optional `frontHalfRundown`
front-half roadmap, and the task-28 `LifecycleTurnEndNotificationResponse`
adding a `summary` for the public NOTIFY-AND-CONTINUE turn-end tool),
`task_doc.py` for the `task_doc` authoring response including the optional Task 21 `masterSync`
leaf-to-master result, `gates.py` for
`LifecycleGateResponse`, the public gate decide/list responses, and retained
compatibility gate responses (L4 adds delegated-decision `decidingRole` and
`evidenceRefs` to the decide response), `operator_inbox.py` for the
three `operator_inbox_*` external-chat response contracts (task 10),
`orchestration.py` for the strict `orchestration_nudge_manager` response,
`lifecycles/finalize.py` for the strict terminal task-finalizer response, `terminal.py` for the strict
`attach_terminal_session_to_leaf` hosted-chat/terminal reassignment response AND the L2
`spawn_agent_session` dispatch response (`SpawnAgentSessionResponse` — spawned-by provenance +
context-delivery outcome (since 260707-HFX-L3 incl. the failure-evidence `deliveryCapture` field) + the server-arbitrated `leaf-taken`/pre-spawn refusal statuses; since HFX-L4 the attach/spawn models also accept
`leaf-ref-not-found` / `leaf-ref-ambiguous` refusals with the original `leafKey` and optional detail; since
260703-L16 also the `effort-invalid`/`model-invalid`/`level-invalid` refusals, the free-form spawn
provenance `launchArgs`/`promptKeywords`/`sessionCommands` + `sessionCommandsDelivered`, and the
level provenance `spawnLevel`/`spawnLevelSource`; HFX2-L10 adds the
`spend-override-unsupported` refusal for legacy caller spend fields and maintained harness-native
spend env keys), and
`tokens.py` for response token accounting. **260707-HFX-L8** adds two more strict models to
`terminal.py`: `SessionRetireResponse` (`retired`/`already-retired`/`unknown-session`/
`unknown-actor`/`retire-refused` statuses, retirement provenance fields, `detail` naming the exact
authority-policy clause on refusal) and `SessionRenameResponse` (`renamed`/`unknown-session`,
`label`/`spawnedLabel` — identity text only, no `spawn_role` field on this response since a rename
never changes it). `lifecycles/finalize.py`'s `LifecycleFinalizeTaskResponse` carries additive
`autoLandedSeats: list[str]` field for the master→super finalize edge's landed archive hook.

## Route Model

- Owned compact contracts should inherit from `StrictResponseModel` or
  `ToolResponse` so unknown fields are rejected.
- Native/detail surfaces that intentionally pass through provider or service
  payloads should inherit from `FlexibleResponseModel` or `FlexibleToolResponse`.
- The strict `NextStep` model (task 27) mirrors the worktree guidance dict shape
  (`summary` plus optional `nextOperation`/`nextTool`/`nextArgs`/`nextRequiredArgs`),
  so an operational hint and a gate-raise share one vocabulary (a gate junction
  is just `nextTool="lifecycle_gate"`). Both envelope bases
  ([base.py](agents-remember/mcp/src/agents_remember/models/base.py)) declare an
  optional `nextStep: NextStep | None` field, populated for in-lifecycle calls at
  the [mcp/tools/base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py)`::_tool_payload`
  choke point and excluded when None, so lifecycle-less calls stay unchanged.
- Both envelope bases also declare `supervisorBanner: str | None` (260731-EFA-L4), set at
  the same choke point. It had been written by the choke point since 260707-HFX2-L2 R5 but
  declared on no model, which is the specific hole: `ResponseModel` is `extra="forbid"`, so
  a response carrying a stale-supervisor banner failed its OWN `model_validate`, and
  `FlexibleResponseEnvelope`'s `extra="allow"` accepted it undeclared — tolerated drift is
  for the PROVIDER's fields, not this package's. `ResponseEnvelope` is the
  `ResponseModel | FlexibleResponseEnvelope` alias naming the two families; the split between
  them is about `extra`, not about the header, and both carry the same
  `ok`/`tokens`/`nextStep`/`supervisorBanner` fields.
- `ContextPacketV2` keeps startup context compact and points detailed provider
  troubleshooting to `provider_diagnostics`.
- Token metadata fields exist on every modeled response; the final S6 wiring
  fills them from the serialized JSON payload.

## Invariants And Boundaries

- Every public MCP tool must have exactly one declared response model in
  `PUBLIC_TOOL_RESPONSE_MODELS`; every retained compatibility builder that still
  returns through `_tool_payload` must have one in `TOOL_RESPONSE_MODELS`.
- Do not rely on Pydantic to silently coerce nested raw dictionaries for owned
  contract objects. Construct nested models explicitly, or call
  `NestedModel.model_validate(...)` only at a narrow raw-adapter boundary.
- Keep `context_packet` free of `rawStatus` and duplicate top-level
  `pathRules`; detailed provider state belongs in `provider_diagnostics`.
- Nullable response fields that can be omitted after `exclude_none=True` must
  declare optional defaults (`= None`); otherwise a later public payload
  validation pass treats the missing key as a required-field error.
- Flexible models are for intentionally raw/detail payloads, not a shortcut for
  avoiding a stable public contract.
- **A wire vocabulary is IMPORTED from whoever produces it; it is never retyped on this
  route** (260731-EFA-L4). A hand-copied `Literal` beside a producer's own is a set that can
  only be compared against the producer when a real payload carries the new member — which
  happens as a `ValidationError` raised inside an `@server.tool()` handler that has no
  `except` for one. Nested `Literal` aliases flatten under PEP 586, so folding a producer's
  alias into a longer list (`Literal["attached", ..., LeafRefStatus]`) publishes exactly the
  same enum it did when the members were spelled out. Where the producing module cannot be
  imported without a cycle, the vocabulary is declared HERE and the producer imports it (see
  `terminal.py` below) — one declaration is the invariant; a particular module owning it is
  not.
- **Nothing on this route declares a status a producer cannot emit, or omits one it can.**
  `mcp/tests/test_wire_vocabulary_exhaustiveness.py` measures produced-vs-declared in both
  directions and is the suite to extend when a new status appears.
- **Nothing on this route may reach the network while the package is importing.**
  `tokens.py` builds `DEFAULT_TOKEN_COUNTER = TiktokenTokenCounter()` at module
  scope, and `mcp/tools/base.py` imports `finalize_payload_tokens` from it — so
  that construction runs on the server's startup path, and anything it touches
  runs there too. Adding a second `tiktoken` encoding therefore means
  vendoring its vocabulary too — `vendored_vocabulary_cache` raises
  `TokenizerVocabularyError` (`errors.py`) for any name other than
  `VENDORED_ENCODING_NAME` rather than letting `tiktoken` download it.
- **A vendored vocabulary is verified by this route before `tiktoken` is pointed at
  it, never afterwards.** `_verify_vendored_vocabulary` hashes the file against
  `VENDORED_VOCABULARY_SHA256` and raises for absent, unshipped, *or byte-wrong*;
  only then does `vendored_vocabulary_cache` set `TIKTOKEN_CACHE_DIR`, and only to
  the verified file's own parent directory. Delegating the check to `tiktoken` is not
  equivalent and must not be "simplified" back: `tiktoken.load.read_file_cached`
  checks the same digest but answers a mismatch by deleting the file and downloading
  a replacement over it — inside an installed package that is a startup fetch plus a
  rewrite of the installed tree, or a `PermissionError` on a read-only install.
- Tools whose bulk moved to `temp/tool-reports/` (2.5.1: runtime install,
  provider diagnostics/watchers; 2.5.2: carryover plan/apply) document the
  compact wire fields as optional declared fields on their flexible models —
  `reportPath` everywhere, plus the per-tool digests (rebind `phases`,
  carryover `decisions`/`carriedPaths`) — so the compact shape is discoverable
  from the model even though the envelope stays flexible.

L14: the task-doc node model exposes the optional `orchestrates` list and the sessions wire model carries the optional `spawnRole` — both additive, absent on old payloads.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public MCP payload builders validate through the response model registry. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:73-75 |
| The registry maps every modeled builder and the advertised public subset to response models. | `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:223-227 |
| Contract tests prove public tool coverage and schema generation. | `PublicToolResponseModelTests`; `test_every_public_tool_has_a_response_model`; `test_every_public_tool_response_model_generates_json_schema` | mcp/tests/test_models.py:16-26 |
| Operator inbox response models cover post, poll, consume, and hosted-delivery metadata. | `OperatorInboxPostResponse`; `OperatorInboxPollResponse`; `OperatorInboxConsumeResponse` | mcp/src/agents_remember/models/operator_inbox.py:54-79; mcp/src/agents_remember/models/operator_inbox.py:82-89; mcp/src/agents_remember/models/operator_inbox.py:92-98 |
| Orchestration response models cover the public manager-nudge helper. | `OrchestrationNudgeManagerResponse` | mcp/src/agents_remember/models/orchestration.py:12-22 |
| Lifecycle finalizer response model covers the terminal task finalization payload. | `LifecycleFinalizeTaskResponse` | mcp/src/agents_remember/models/lifecycles/finalize.py:13-33 |
| Terminal response models cover trusted task-seat assignment and internal hosted-session spawn. | `AttachTerminalSessionToTaskResponse`; `SpawnAgentSessionResponse` | mcp/src/agents_remember/models/terminal.py:32-44; mcp/src/agents_remember/models/terminal.py:85-127 |
| The next-step engine that fills `nextStep` from the active lifecycle. | `nextStep` | mcp/src/agents_remember/application/next_step.py:260-270 |
| The wire-test module documents the 165-of-213 `context_packet` baseline. | "165 of the 213" | mcp/tests/test_wire_vocabulary_exhaustiveness.py:7-7 |
| Produced-vs-declared vocabulary measurement runs in both directions. | `test_every_contract_literal_validates_at_its_wire_field`; `test_every_repo_state_the_git_facts_reader_writes_validates`; `test_every_next_guidance_literal_validates_at_its_wire_field` | mcp/tests/test_wire_vocabulary_exhaustiveness.py:635-645; mcp/tests/test_wire_vocabulary_exhaustiveness.py:691-706; mcp/tests/test_wire_vocabulary_exhaustiveness.py:741-751 |
| The worktree model declares the contract-cell vocabulary aliases (moved from worktrees by 260731-EFA-L9) with `MemoryMode` imported from kernel. | "from agents_remember.kernel.coordination_context.models import MemoryMode"; "WorkflowKind = Literal["; "HumanReviewStatus = Literal["; "LifecycleStatus = CloseoutStatus"; "CleanupStatus = Literal[" | mcp/src/agents_remember/models/worktree.py:9-9; mcp/src/agents_remember/models/worktree.py:14-15; mcp/src/agents_remember/models/worktree.py:17-17; mcp/src/agents_remember/models/worktree.py:19-19 |
| The worktree model declares the phase/next-operation/next-tool vocabulary (moved from guidance by L9). | "WorktreePhase = Literal["; "NextOperation = Literal["; "NextTool = Literal[" | mcp/src/agents_remember/models/worktree.py:20-20; mcp/src/agents_remember/models/worktree.py:30-30; mcp/src/agents_remember/models/worktree.py:39-39 |
| Guidance consumes the phase/next-operation/next-tool aliases declared by the wire model through one grouped import. | "from agents_remember.models.worktree import (" | mcp/src/agents_remember/worktrees/modules/guidance.py:10-14 |
| The drift-status vocabulary and `DriftSummaryPacket` that `drift.py` and `memory.py` import. | `DriftSummaryPacket` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:11-19 |

## 260712-TRH-L4 Route Impact

Models now distinguish spawned-unbriefed, harness-ready, and briefed and carry the readiness/dispatch statuses, exact-session proof fields, dispatch kind, and separated supervisor state surface.


### 260713-PHA-L5 Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

## 260731-EFA-L3 Route Impact — `tokens.py` Counts Offline

The token counter no longer downloads its vocabulary. `TiktokenTokenCounter.__post_init__` used to
call `tiktoken.get_encoding("o200k_base")` bare, which on a cold cache fetched
`o200k_base.tiktoken` from `openaipublic.blob.core.windows.net` — and because
`DEFAULT_TOKEN_COUNTER = TiktokenTokenCounter()` is built at module scope on the import path of
every MCP tool, that HTTPS round trip happened *while the server was starting*. A fresh container,
an offline machine or a hermetic CI job could not start the server at all.

The vocabulary now ships inside the package at
`agents_remember/package_data/tiktoken/fb374d419588a4632f3f557e76b4b70aebbca790`. That file name is
not decoration: `tiktoken.load.read_file_cached` keys its cache on `sha1(url)`, so it is the only
name a cache hit can have, and `vendored_vocabulary_path()` recomputes it from
`VENDORED_VOCABULARY_URL` rather than hard-coding the digest — the shipped file and the download it
replaces stay provably the same thing. `__post_init__` now loads inside
`vendored_vocabulary_cache(self.encodingName)`, which points `TIKTOKEN_CACHE_DIR` at the vendored
directory for the duration of that one load, under `_CACHE_DIR_LOCK`, and restores
the operator's previous value afterwards. Scoped rather than exported, because the vendored
directory sits inside an installed (usually read-only) package and any *other* encoding loaded later
in the process would try to write its download there. The operator's own `TIKTOKEN_CACHE_DIR` is
deliberately overridden rather than honoured — theirs may be cold, and honouring a cold one is
exactly the download this exists to remove.

**The route verifies the vocabulary itself, before tiktoken is told where to look.**
`vendored_vocabulary_cache` calls the private `_verify_vendored_vocabulary(encoding_name)` as its
first statement — ahead of the lock and ahead of any environment mutation — and that helper raises
`TokenizerVocabularyError` in three cases: an encoding this package does not ship, an absent file,
and a file whose SHA-256 does not equal `VENDORED_VOCABULARY_SHA256`. It then hands back the
verified path, and only *that file's own parent directory* is ever exported, so tiktoken cannot be
pointed at a directory whose contents were not checked.

Leaving the digest to tiktoken is not the same thing, and the difference is the whole point.
tiktoken checks the same SHA-256, but it does **not** fail closed on a mismatch:
`tiktoken.load.read_file_cached` deletes the offending cached file and downloads a replacement over
it. Pointed at this package's directory, that turns a corrupt vendored copy into a silent network
fetch on the server's startup path *and* a rewrite of the installed tree — or, on the read-only
install this module is written for, into a `PermissionError` from the write-back instead of the
designed refusal. Checking first is what makes corruption behave like absence. `VENDORED_VOCABULARY_SHA256`
is restated here rather than imported, and that is not a second source of truth:
`mcp/tests/test_cold_start.py` re-derives it from the installed tiktoken, so a release that changes
what tiktoken asks for fails there. Hashing costs one full read of 3.6 MB per counter construction,
which in the server is once per process.

`_CACHE_DIR_LOCK` is a `threading.RLock`, not a `Lock`, because the guarded region spans the `yield`
in an exported context manager. The obvious use of one —
`with vendored_vocabulary_cache(name): TiktokenTokenCounter()` — has the counter's own load re-enter
the manager on the same thread, which on a non-reentrant lock is a permanent hang with no timeout
and no traceback rather than a wrong answer. The lock's honest scope is "the counters this package
builds": `TIKTOKEN_CACHE_DIR` is process-global and belongs to tiktoken, so a thread that reads or
writes it without coming through here can still observe or clobber the override, and nothing at this
layer can prevent that.

Nothing about the response contract changed: the shipped bytes are the download's bytes, so counts
are the same numbers and `name` still reports
`tiktoken:o200k_base`. There is deliberately no approximate fallback — a fallback would make a
reported count depend on whether the machine that produced it had egress, silently mixing exact and
estimated values inside one dashboard aggregate. A vendored file that is missing **or present with
the wrong bytes** raises `TokenizerVocabularyError` instead, naming both the expected and the found
digest, so a build that failed to ship it — or a `core.autocrlf=true` checkout that rewrote its line
endings — says so at startup rather than working only where the network happens to be reachable.

## 260731-EFA-L4 Route Impact — Vocabularies Come From Their Producers

Every change here has the same shape: a `Literal` this route had typed out by hand, standing
beside the module that actually produces those values, replaced by an import of the producer's
own alias. The failure mode being removed is a **set difference**, and it lands as a
`ValidationError` raised inside an MCP tool handler with no `except` for one.

**`worktree.py` — six copies, six drifts, 165 of 213 contracts.** `WorktreeSummary`'s
vocabularies were all local `Literal`s. They now come from
`worktrees.worktree_contract` (`WorkflowKind`, `MemoryMode`, `HumanReviewStatus`,
`IntegrationStatus`, `CleanupStatus`, and `CloseoutStatus` aliased to the published wire name
`LifecycleStatus`) and `worktrees.modules.guidance` (`WorktreePhase`, `NextOperation`,
`NextTool`). Only `WorktreeState` stays local — it is produced entirely inside
`application.worktree_status`, which constructs the model directly, so the checker already sees a single
writer. What the copies had missed is checkable against the producers: the local
`WorkflowKind` was `Literal["chat", "light", "light-task"]` while the contract's is
`Literal["chat-task", "light-task"]` — the copy did not contain the kind `worktree_start`'s own
docstring advertises and had two members the contract cannot write; local `CleanupStatus` lacked
`reopened`; local `WorktreePhase` lacked `carryover-pending` and `abandoned`; local
`NextOperation` lacked `request_carryover_decision`; local `NextTool` lacked
`memory_carryover_apply`. Measured effect, recorded in
`test_wire_vocabulary_exhaustiveness.py`'s docstring: 165 of the 213 `series-contract.md` files
on disk (77.5%) made `context_packet` raise, across seven independent gaps. Two additive
optional fields join the summary: `nextRequiredArgs` gains a documented absent-means-nothing-
required reading (the producer writes the key only when there is a required argument, and the
projection reports what the producer said rather than substituting `[]`), and
`unknownContractCells: list[str] | None` reports `"<field>=<raw token> read as <fallback>"` for
any contract cell outside its declared vocabulary — the file still projects as `active` with
substituted values, and heals the next time a lifecycle tool writes it.

**`context_packet.py` — three retyped vocabularies.** `RepoSummary.state` takes
`kernel.git_facts.RepoState` and `BranchFreshness.state` takes
`kernel.git_freshness.FreshnessState`, both of which are assembled here through
`model_validate` of an untyped dict, so a copy would be measured against the producer only
when a real degrade path fired. `MemorySummary.mode` moves from `Literal["internal",
"external"]` to `worktrees.worktree_contract.MemoryMode`, which has always included
`disabled` — `WorktreeSummary` in the SAME response already declared it, so one packet could
pass `memoryMode="disabled"` and fail `memory.mode` on the same value.

**`drift.py` / `memory.py` — one vocabulary, three declarations, two of them short.**
`DriftStatus` now lives once, in
`memory_quality/integrity/onboarding_drift_check/models.py` beside `run_drift_summary` which
produces it, and both wire models import it. `models.drift.DriftStatus` had been
`Literal["notChecked", "checked"]` and `DriftSummary` declared no `error` field, while
`run_drift_summary` returns `{"status": "error", "error": ...}` whenever the onboarding root is
missing — so `include_drift=true` against a repo without onboarding raised out of the tool on
the status *and* the key, i.e. the diagnostic crashed on exactly the call meant to explain the
problem. `DriftSummary` gains `error: str | None`. `models.memory.DriftCheckStatus` was the
third copy (correct, but a third place for the next member not to arrive) and is gone.

**`read_files.py` — the alias moved to the decider.** `FileReadStatus` is declared in
`application/read_files.py`, where `_resolve_onboarding` decides it and now returns it as its
annotated type, and this model imports it. Note the direction: this is a `models/` →
`application/` import, the reverse of the usual layering, chosen because the deciding function
is the single writer and it puts the value into an untyped payload dict. It creates no cycle —
`application/read_files.py` does not import `models.read_files`.

**`terminal.py` — folded members and runtime halves.** `LeafAssignmentStatus` and
`SpawnAgentSessionStatus` fold in `worktrees.leaf_refs.LeafRefStatus` (the pair
`leaf-ref-not-found`/`leaf-ref-ambiguous`) instead of respelling it; `Literal` flattening means
the published enums are unchanged (`get_args(LeafAssignmentStatus)` is still the same six
members). The three terminal vocabularies stay declared HERE rather than beside the payload
builders that write them, and the module says why: `mcp.tools.base` → `models.tool_registry` →
`models.terminal` is an existing import edge, so a `models.terminal` → `mcp.tools.terminal`
import would close a cycle. The invariant is one declaration, not a particular owner —
`mcp.tools.terminal` imports these aliases and annotates its status seams with them.
`VALID_SPAWN_AGENT_SESSION_STATUSES`, `VALID_SESSION_RETIRE_STATUSES` and
`VALID_SESSION_RENAME_STATUSES` are `frozenset(get_args(...))` of their aliases — the runtime
half derived from the type rather than typed beside it.

**`tool_registry.py` — the loose type that made the token count wrong.** Both registries are
`dict[str, type[ResponseEnvelope]]`. Under the previous `dict[str, type[BaseModel]]`,
`TOOL_RESPONSE_MODELS[tool].model_validate(payload)` was typed as a bare `BaseModel`, on which
`nextStep` and `supervisorBanner` are not attributes a checker knows — so the choke point had
no type-clean way to set them on the validated response, and wrote them into the dict AFTER
`model_dump` and AFTER `finalize_payload_tokens`. Two consequences, both silent: the served
response carried bytes the advertised `tokens` did not count, and `supervisorBanner` was a key
on an object whose model did not declare it. Naming the union is what let the choke point be
reordered (see the `mcp/tools/` overview). Verified: all 62 registered models are
`ResponseModel` or `FlexibleResponseEnvelope` subclasses and all 62 declare both fields, so the
narrower type is true of the whole registry today.

## 260731-EFA-L9 Route Impact — Conversation Wire Models Join This Route

The route now owns more than MCP response contracts. 260731-EFA-L9 moved the stable
conversation/evidence/control-wire grammar out of `serving/` into the new
`models/conversations/` child route (16 responsibility-owned modules + curated `__init__.py`
export surface), moved the terminal-catalog row vocabulary into `models/terminal_catalog.py`,
and added the task-document wire vocabulary in `models/task_document.py`. The route model is
unchanged in kind — strict owned contracts, curated exports — but the wire surface it governs is
now shared by serving projectors/control and the response-model registry. `models/__init__.py`
re-exports the curated conversation surface (R6); no forwarding shims exist at the old serving
paths.

## L23 Source-Lineage Contract

The model layer now owns closed lineage relation, side, edge-state, aggregate
state, recovery, and terminal refusal vocabularies. Worktree, terminal, observer,
and dashboard consumers import or mirror this strict shape instead of accepting
free strings or agent-supplied identity.

## 260815-DAG-L3 Queue Models

`models/closeout_queue.py` adds the strict action-specific request, categorical scheduling grade,
exact evidence facts, candidate state machine, atomic blocker, bounded canonical queue state, and
ready/waiting/blocked/in-flight response projection. Every persisted/public text and collection is
bounded, impossible state/owner/commit combinations fail validation, external memory requires exact
evidence while internal/disabled use a typed not-applicable state, and only a one-way lifecycle
owner fingerprint reaches durable state. Since 260815-DAG-L13 `LANE_OCCUPYING_STATES` narrows the
landing lane to selected/closeout-in-flight/integration-in-flight candidates (a certified candidate
no longer occupies it), and the response carries the scheduling readout fields (`mode`,
`registers`, `laneOwner`, `legalNextOperations`, `acquisitionFacts`). Shared `TaskDocumentRef` values enforce their repository
and path bounds after canonical normalization, avoiding JSON Schema constraints that the generated
TypeScript projection could not express truthfully.

## 260815-DAG-L4 L4 Durable Authority Models

Worktree, closeout-queue, and task projections now distinguish organizational direct-super lineage from atomic series lineage and carry exact configured repository, ref, candidate, recovery, and conflict-transaction facts required by the mutation plane.

## 260815-DAG-L15 Route Impact

`MemoryQualityCheckResponse` gained the optional async `status`/`runId` run envelope (L15-R7); the synchronous response shape is unchanged.

## 260815-DAG Master Full-Gate Repair Route Impact

`models/closeout_queue.py` moved to the new `models/queue/` sub-route; `models/task_doc.py` `TaskDocResponse` gained the special-op wire fields (the strict-envelope rejection fix).

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: `closeout_queue` moved to the new `models/queue` sub-route; `task_doc.py` gained the special-op wire fields. Verified at code commit e5cb139f.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: MemoryQualityCheckResponse async status/runId envelope (L15-R7). Verified at code commit de3a0fd9.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16 route impact: new `models/declared_caller.py` (the shared
  request-carried ambient identity) and `models/direct_landing.py` (`DirectLandingResponse`);
  `CloseoutQueueRequest.caller` and the structural gate requests carry an optional declared caller;
  `tool_registry.py` registers `direct_landing`. Verified at code commit a9d50e08.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: `models/closeout_queue.py` gained
  `LANE_OCCUPYING_STATES` and the queue response readout fields (`mode`, `registers`, `laneOwner`,
  `legalNextOperations`, `acquisitionFacts`); the models-route purpose is unchanged. Verification
  remains closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — No route impact: 260815-DAG-L5 added three lifecycle-operation wire models; the models route purpose is unchanged.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-15T09:36+02:00 — L3 fast-hook repair: clarified the validator-owned task-reference
  bounds and why they do not become an unrenderable projection-schema keyword.
- 2026-08-15T09:10+02:00 — 260815-DAG-L3 route impact: added the strict bounded queue request,
  candidate/state, evidence, blocker, and projection vocabulary. Verification remains closeout-owned.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1 route impact: the shared task-document model vocabulary
  owns the closed organizational/atomic nature used by both persisted tasks and projection DTOs.
- 2026-08-14T06:25+02:00 — No route impact: L23 extends the existing lifecycle-operation model
  family with exact candidate/recovery evidence; strict-model ownership and public/private identity
  boundaries remain in the lifecycles child route. Verification remains closeout-owned.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: routed lifecycle response, finalizer, and asynchronous-operation models through the cohesive `models/lifecycles/` child overview while preserving one vocabulary owner per wire set. Verification metadata remains closeout-owned.

- 2026-08-12T20:20+02:00 — L23 curator: documented strict source-lineage model ownership; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: documented strict durable lifecycle records and the private-identity-free public projection; verification provenance remains closeout-owned.

- 2026-08-11T20:28+02:00 — 260731-EFA-L19 closeout-gate repair: recorded the explicit immutable
  `TaskDocumentRef` value/hash contract; verification metadata remains commit-owned.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: reconciled the model route with canonical
  `TaskDocumentRef` structural requests, document-projected gates, and agent-visible responses that
  omit private occupant coordinates.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 route impact: recorded the models/conversations child
  route, terminal-catalog/task-document vocabulary moves, and the curated export additions.
  Verification metadata pinned until closeout stamps the L9 code commit.
- 2026-08-04T08:45:26+02:00 — 260731-EFA-L6 S18-B07 curator correction: split the measurement and vocabulary-import claims and rebound them to frozen module bodies/imports; same-reviewer delta pending.
- 2026-08-03T02:57:31+02:00 — W3-B05 curator: resolved 10 Tier-2 table findings and 1 Tier-2 prose finding with exact source paths; fixer generated all final ranges.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No route impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:26+02:00 — 260731-EFA-L4 curator: **body corrected.** Every changed file on this
  route replaced a hand-copied `Literal` with an import of the producing module's alias, so the
  route gained a rule it did not state — added it as an invariant ("a wire vocabulary is imported
  from whoever produces it, never retyped here"), with the cycle-driven exception `terminal.py`
  documents, and the note that PEP 586 flattening means folding a producer's alias into a longer
  `Literal` republishes the identical enum (verified: `get_args(LeafAssignmentStatus)` still
  returns the same six members). Added the route-impact section above with the specific set
  differences each copy carried, checked against the producers rather than taken from the leaf's
  summary: local `WorkflowKind` was `["chat", "light", "light-task"]` against the contract's
  `["chat-task", "light-task"]`, local `CleanupStatus` lacked `reopened`, local `WorktreePhase`
  lacked `carryover-pending`/`abandoned`, local `NextOperation` lacked
  `request_carryover_decision`, local `NextTool` lacked `memory_carryover_apply`, and
  `MemorySummary.mode` lacked `disabled` while `WorktreeSummary` in the same response declared it.
  The 165-of-213 figure is quoted from `test_wire_vocabulary_exhaustiveness.py`'s module docstring,
  which is where it is measured. Recorded `DriftSummary.error` and the `DriftStatus`
  three-copies-to-one consolidation, `models/read_files.py`'s deliberate models→application import
  (no cycle — confirmed by importing the module standalone), the two new `WorktreeSummary` fields,
  and `supervisorBanner`/`ResponseEnvelope` on `base.py`. Corrected the `tool_registry.py` entry in
  the Hot Path Summary and explained the mechanism precisely: `type[BaseModel]` made the two
  envelope fields unreachable by type, which is why they were written into the already-dumped,
  already-token-counted dict — verified that all 62 registered models satisfy the narrower type.
  Added five reference rows to the 2-column table. Verification metadata pinned until closeout
  stamps the L4 commit.
- 2026-07-31T22:38+02:00 — 260731-EFA-L3 curator (re-verification pass after the fix workers).
  **Corrected the parenthetical "(tiktoken verifies its SHA-256 on load)", which credited tiktoken
  with an integrity guarantee it does not provide.** `tokens.py` now verifies the digest itself:
  `_verify_vendored_vocabulary` hashes the file against the new `VENDORED_VOCABULARY_SHA256` and
  raises `TokenizerVocabularyError` for absent, unshipped, or byte-wrong — and
  `vendored_vocabulary_cache` calls it as its *first* statement, ahead of the lock and ahead of
  touching `TIKTOKEN_CACHE_DIR`. Recorded why: `tiktoken.load.read_file_cached` checks the same hash
  but answers a mismatch by deleting the file and downloading a replacement over it, which inside an
  installed package is a startup fetch plus a rewrite of the installed tree (or a `PermissionError`
  on a read-only install). Also corrected the cache-override sentence — the directory handed to
  tiktoken is the *verified file's own parent*, not `VENDORED_VOCABULARY_DIR` reached independently
  — and recorded that `_CACHE_DIR_LOCK` is now a `threading.RLock` because the guarded region spans
  the `yield` and the documented `with vendored_vocabulary_cache(...): TiktokenTokenCounter()` use
  re-enters it on the same thread, where a plain `Lock` hangs forever with no diagnostic. Changed
  "a missing vendored file raises" to missing **or byte-wrong**, and added a second import-path
  invariant covering the verify-before-delegate rule. Response models, field names, the strict/
  flexible split and the reported `tiktoken:o200k_base` counter name are all unchanged.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-31T20:58+02:00 — 260731-EFA-L3 curator: recorded that `tokens.py` no longer fetches the
  `o200k_base` vocabulary at import. Added the route-impact section above (vendored
  `package_data/tiktoken/<sha1(url)>` file, `vendored_vocabulary_path()`/`vendored_vocabulary_cache`,
  the scoped-and-locked `TIKTOKEN_CACHE_DIR` override, no approximate fallback) and one new
  invariant: nothing on this route may touch the network during import, so a second `tiktoken`
  encoding must be vendored or `TokenizerVocabularyError` refuses it. Response contracts, field
  names and reported counter name are unchanged. Verification metadata pinned until closeout stamps
  the L3 commit.
- 2026-07-31T16:55+02:00 — No route impact: re-verified the attestation below in the exact form the
  closeout gate reads. Both changed files in this route (`context_packet.py`, `memory.py`) were
  parsed at the L2 base commit and at the current revision and their syntax trees are identical, so
  the reflow of the `BranchFreshness.state` `Literal` member list and of the parenthesized
  `description=` string on `MemoryCarryoverApplyResponse.reportPath` changed no model, field name,
  alias, default, validation rule or serialization behaviour this overview describes. The route's
  shape — which modules own which contracts — is untouched.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation, no route impact. Two files in this route
  (`context_packet.py`, `memory.py`) were touched by the whole-tree `ruff format` pass (commit
  `00e8379`) and by nothing else: a `Literal` member list and one parenthesized `description=`
  string were reflowed. No model, field, alias, serialization rule or contract in this route
  changed, so this overview was re-read against the current source and deliberately **not**
  rewritten — every claim below still holds. Note for readers arriving from other routes: the
  parameter objects introduced across the package in L2 are *local* to the modules that use them
  and were deliberately not added here — this route stays the home of wire and response contracts,
  not of internal call-shape bundles. Verification metadata pinned until closeout stamps the L2
  commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: added the strict incomplete-selection status
  and clarified resolved selection, user-authored session commands, and runner-owned dynamic
  failure evidence. Verification metadata remains pinned until closeout stamps the L2 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17 models route impact: added pair-binding response fields
  and the role-required attach status without changing the strict response-module layout.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 models route impact: added replacement, resolved-knob,
  and bound-log response fields and corrected delivery semantics. Verification metadata remains
  pinned until closeout stamps the eventual L15 code commit.

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 route impact: `models/lifecycle_finalize.py` now
  exposes `autoLandedSeats` for completion-edge archive landing; the former `autoRetiredSeats`
  contract is no longer the current finalizer response field. Verification metadata pinned until
  closeout stamps the HFX2-L11 commit.

- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 route impact: `models/terminal.py` adds the
  `spend-override-unsupported` status to `SpawnAgentSessionStatus`, covering legacy caller spend
  fields and maintained harness-native spend/env keys. Additive strict-model status update; no
  module-layout or strict/flexible taxonomy change. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L10 commit.

- 2026-07-08T14:45+02:00 — No route impact: 260707-HFX2-L1 adds `ownerRole`/`ownerAgentId`/`ownerLifecycleId` to `OperatorInboxPostResponse` (`models/operator_inbox.py.md` documents the field addition); the response-contract pattern and module layout are unchanged.
- 2026-07-08T02:43+02:00 — 260707-HFX-L8 route impact (seat lifecycle: retirement + live identity +
  turn-state, issues #12/#4): `models/terminal.py` adds `SessionRetireResponse`/`SessionRenameResponse`
  (strict `ToolResponse`), `tool_registry.py` registers `session_retire`/`session_rename` → those
  models; `models/lifecycle_finalize.py`'s `LifecycleFinalizeTaskResponse` gains additive
  `autoRetiredSeats: list[str]`. Follows the existing STRICT `ToolResponse` pattern, so the
  strict/flexible split this overview describes is unchanged. Verification metadata pinned until
  closeout stamps the HFX-L8 commit.
- 2026-07-07T23:30+02:00 — 260707-HFX-L4 route impact: `models/terminal.py` accepts
  `leaf-ref-not-found` / `leaf-ref-ambiguous` statuses on terminal attach and spawn responses, with
  optional detail for attach refusals. Verification metadata pinned until closeout stamps the
  260707-HFX-L4 commit.
- 2026-07-07T23:20+02:00 — 260707-HFX-L3 route impact (additive field): `terminal.py`'s
  `SpawnAgentSessionResponse` gained `deliveryCapture` — the pane-capture evidence attached whenever
  context delivery or submit fails (never a bare false-success boolean); the response model shape is
  otherwise unchanged.
- 2026-07-07T18:40+02:00 — No route impact: 260703-L18 finding 1 declares the additive optional
  `removedSubtask`/`deletedFiles`/`wouldDeleteFiles` fields on `TaskDocResponse` so a `remove_subtask`
  success validates against `extra="forbid"`; it stays a STRICT `ToolResponse`, so the strict/flexible
  split this overview describes is unchanged (detail in the file sidecar).
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application) route impact: `terminal.py`'s
  `SpawnAgentSessionResponse` gained three refusal statuses (`effort-invalid`/`model-invalid`/
  `level-invalid`) and the free-form + level provenance fields (all additive, `None`-omitted). No
  other model changed. Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-06T23:59:58+02:00 — L14 route impact (body): optional orchestrates + spawnRole on the response models. Verification metadata pinned until closeout stamps the L14 commit.

- 2026-07-06T23:59:42+02:00 — 260703-L14 (visual hierarchy + chat grouping) route impact: `terminal.py`'s `SpawnAgentSessionResponse` gained the optional `spawnRole` field mirroring the new catalog column (additive, `None`-omitted). Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-04T12:32+02:00 — 260703-L4 route impact: `models/gates.py` extends
  `GateDecideResponse` with delegated-decision attribution and evidence refs.
  It remains a strict `ToolResponse`, so the strict/flexible route model is
  unchanged. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-04T12:31+02:00 - L3 route impact: added the strict orchestration
  nudge response model and expanded inbox response fields for delivery metadata.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2 route impact: `models/terminal.py` adds the strict
  `SpawnAgentSessionResponse` (+ `SpawnAgentSessionStatus`) for the agent-facing `spawn_agent_session`
  dispatch tool, and `tool_registry.py` registers `spawn_agent_session` → that model in the strict public
  response-contract path. It follows the existing STRICT `ToolResponse` pattern, so the strict/flexible
  split this overview describes is unchanged. Verification metadata pinned until closeout stamps the L2
  commit.
- 2026-07-03T00:35+02:00 — L11 route impact: TaskReopenResponse added in task_doc.py; tool_registry maps task_reopen to it.
- 2026-07-02T17:04+02:00 — L9 route impact: added `models/terminal.py` with the strict
  `AttachTerminalSessionToLeafResponse` and registered it in `tool_registry.py` for the new public
  reassignment tool. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-27T22:00+02:00 — Task 28 route impact: `models/lifecycle.py` adds `LifecycleTurnEndNotificationResponse(LifecycleResponse)` (adds a required `summary`) and `tool_registry.py` registers `lifecycle_turn_end_notification` → that strict response as a real public tool (not in `INTERNAL_COMPAT_TOOL_NAMES`; `TOOL_RESPONSE_MODELS` → 55, `PUBLIC_TOOL_RESPONSE_MODELS` → 51, still matching `PUBLIC_TOOLS`). It follows the existing STRICT `ToolResponse` pattern, so the strict/flexible split this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T18:43+02:00 — Task 27 route impact: `base.py` adds the strict `NextStep`
  lifecycle-hint model (`summary` + optional `nextOperation`/`nextTool`/`nextArgs`/`nextRequiredArgs`,
  mirroring the worktree guidance dict so a gate-raise is `nextTool="lifecycle_gate"`) and an optional
  `nextStep: NextStep | None` field on both envelope bases (`ResponseModel`, `FlexibleResponseEnvelope`),
  populated at `mcp/tools/base.py::_tool_payload` and excluded when None; `lifecycle.py::LifecycleStartResponse`
  gains an optional `frontHalfRundown: list[str] | None`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 route impact: `models/task_doc.py` adds the optional
  `TaskDocMasterSync` nested response so `task_doc` leaf writes can report same-root master-row changes.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T14:16+02:00 — Task 25: response-model route now distinguishes all modeled builders (`TOOL_RESPONSE_MODELS`) from the advertised public subset and includes `LifecycleGateResponse` for the unified gate junction.
- 2026-06-25T07:26+02:00 — Task 19: `models/gates.py` now models gate wait decision metadata and the
  strict `GateResponseWaitResponse`, with `tool_registry.py` mapping `gate_response_wait` into the public
  response-contract surface. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: worktree response models now declare leaf enclosure identity (`enclosurePath`, `leafId`, `kind`) and finalizer responses declare `taskArchive` for completed root-task archival. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: added `models/lifecycle_finalize.py`, a strict `ToolResponse` for `lifecycle_finalize_task`. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: added `models/operator_inbox.py` and its three strict `ToolResponse` registry rows. The strict/flexible route model is unchanged. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-19T07:23 — No route impact: slice 3c R5 adds the additive optional `dryRun`/`rendered`/`diff`/`wouldLose` fields to `TaskDocResponse` (set only on a dry-run preview); it stays a STRICT `ToolResponse`, so the strict/flexible split this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: added `models/gates.py` (the four `gate_*` strict `ToolResponse` subclasses) to the route and their `tool_registry` rows; they follow the existing STRICT pattern, so the strict/flexible split this overview describes is unchanged. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-13T22:34 — Slice 3c commit 1: added `models/task_doc.py` (`TaskDocResponse`, a STRICT `ToolResponse`) to the route and its `tool_registry` row; it follows the existing STRICT pattern, so the strict/flexible split this overview describes is unchanged. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T18:45+02:00 — No route impact: slice 2c declares one optional `lifecycleId` field on the flexible `WorktreeCommandResponse`; the strict/flexible response-contract route model this overview describes is unchanged (detail in the file sidecar).
- 2026-06-13T16:41+02:00 — Slice 2b: added `models/lifecycle.py` (the six `lifecycle_*` STRICT response models) to the route; they follow the existing STRICT `ToolResponse` pattern, so the strict/flexible split this overview describes is unchanged. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T06:47+02:00 — No route impact: issue #62 removed `DirectCloseoutPreviewResponse`/`DirectCloseoutApplyResponse`, their registry rows, and their package exports; the strict/flexible route model this overview describes is unchanged (detail in the file sidecars).
- 2026-06-10T09:56+02:00 — No route impact: sub-task D adds `WorktreeSyncResponse` (one more flexible `WorktreeCommandResponse` subclass) and its registry row (GitHub #54); the strict/flexible route model this overview describes is unchanged (detail in the file sidecars).
- 2026-06-10T07:40+02:00 — No route impact: `models/worktree.py` only documented the existing flexible `providers` field's async setup states (GitHub #53).
- 2026-06-10T05:30+02:00 — Route body caught up with the 2.5.1/2.5.2 compact-response field documentation pattern (`reportPath` + per-tool digests declared on flexible models); previous closeouts had only stamped the verification header. Developer-flagged gap.
- 2026-06-08T09:57+02:00: Re-verified response model guidance after compact provider `ok` fields became optional-null defaults for skipped-provider payload re-validation.
- 2026-06-06T12:15: Re-verified against the current response model package; corrected the payload-builder reference from the deleted `mcp/tools.py` file to the `mcp/tools/` package.
- 2026-05-28T19:52+02:00: Created for the Pydantic public response-contract model package while S2/S4 source changes are still uncommitted in the checkout.
