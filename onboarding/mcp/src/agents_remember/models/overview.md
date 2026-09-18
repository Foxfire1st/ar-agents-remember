# mcp/src/agents_remember/models/ - Response Contract Models Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/models/`          |
| doc_type               | `route-local-overview`                     |
| lastUpdated | 2026-09-18T06:50+02:00 |
| lastVerifiedCommitHash | `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be` |
| lastVerifiedCommitDate | 2026-09-18T08:36:40+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l19` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## IAS Contract-Scoped Activation And Sync Vocabulary

The activation vocabulary lives under `models/structural/atomic_series_activation.py` and is keyed by
the canonical series contract, not by a protected source pair. It separates selectable state
(`reconciling|active`) from observed state (`vacant|unreadable|reconciling|active`) and binds the
selected master plus canonical contract path to `contractFingerprint` — the SHA-256 of the canonical
resolved contract path. Each activation record is `schemaVersion "2.0"`; the former
`AtomicSeriesSourceRef` / `AtomicSeriesSourcePair` models and the `sourcePairFingerprint` field they
fed are gone, because two atomic masters commanded by one sprint derive the same protected source pair
and must nonetheless hold independent selection. This is disposable selection, not task truth, queue
membership, or lifecycle evidence.

Sync models project the stable enclosure-root journal without requiring task-document parsing.
Public status distinguishes a retained resolution, automatic resume, cancellation, terminal
completion, malformed/identity-invalid evidence, and bounded quarantine. Exact Git refs, admitted
heads, and per-side progress remain strict durable state; the response exposes only what an agent
needs to continue, cancel, or repair. Exact field membership is reconciled to the frozen candidate;
verification metadata remains closeout-owned until the new code commit exists.

CCR-R25 extends the public worktree wire vocabulary with optional
`AtomicSeriesActivationFact` and `AtomicSeriesAdmission` fields; the contract-scoped re-key makes them
per-contract. Status carries the addressed contract's activation address, `contractFingerprint`,
observed state, and record/error evidence. Admission responses explain the addressed contract's own
corrective state, the nested activation snapshot, expected/observed evidence, retry precondition, and
a contract-bound read-only status action. They no longer carry a `classification`, a `sourcePair*`
field or a `blocking` blocker — with them went the `AtomicSeriesAdmissionBlocking` model — because a
foreign live master is never this contract's wait, blocker, or retry precondition. These models
validate the projection shape only; selector mutation and recovery remain owned by the activation and
lifecycle domains.

## Current Structural Wire Vocabulary

MCAR-L02 adds the strict curator-coherence lifecycle family under
`models/lifecycles/curator_coherence.py`. It keeps the semantic requirement revision, worker
delivery attempt, exact source candidates, agent-owned judgments, immutable record generation,
stable live authority, optional attempt snapshot, and public request/response as separate typed
identities. The request exposes one closed `status|prepare|publish|validate` action vocabulary.
What `publish` requires is now **one declaration**: the nine publication members live in
`PUBLICATION_MEMBERS` beside the request model, and the validator, the `publish` refusal and the
`prepare` text all read it, so a member appended there is checked, named and stated with no second
edit. A `publish` refusal names every missing member by its request field name, a
`status`/`prepare`/`validate` refusal names the publication-only field it received, and the
`prepare` response states the complete input set — including the two members it does not derive
(`semantic_requirement_revision`, `delivery_attempt`), which stay the caller's own delivery
identities. Record validation requires unique exact coverage of the structured source-candidate set
rather than accepting partial or extra judgments.

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

## Shared Serving-Build Wire Identity

ARSPAWN-L4 owns `ServingBuildPayload` in `models/core.py` so dashboard served state and MCP
`server_info` cannot maintain parallel candidate-identity shapes. Co-location avoids adding a 26th
flat model module while keeping one strict wire authority. Required version and boot time
are supplemented by optional content digest, interpreter, package root, checkout commit, dashboard
fingerprint, and proven-dirty evidence. Absence stays honest unknown; package version alone is not
treated as exact candidate identity.

## Shared Certification Wire Ownership

[The certification wire route](certification/overview.md) owns shared frozen primitives, canonical corrective dispositions and exact stored-object references. Domain certification and lifecycle models import these concrete values; wire validity does not establish observed authority, execute a gate or select a journal record. Registry/plan compilers and the existing certificate store remain the semantic and storage owners. This extraction changes retrieval ownership while preserving the moved constraints.

## Purpose

`models/` owns the Pydantic response contracts for Agents Remember MCP payload
builders. It turns the public tool surface and internal builders
from loose dictionaries into named, inspectable models that can be validated at
runtime and tested by schema. Model homes follow tool domains: `TaskReopenResponse`
(cit:([`TaskReopenResponse`], mcp/src/agents_remember/models/task_doc.py:193-196)) lives in `task_doc.py` while keeping the `WorktreeCommandResponse` shape, since
the task_reopen payload carries the enclosure contract state.

## Hot Path Summary

Closeout and landing models expose code/memory outputs; `DirectLandingResponse.ledgerCache` is an informational cache-refresh result. The lifecycle models distinguish actual Git heads from filtered memory content and retain no ledger commit alias.

## Detailed Route Context

The model layer now carries closed lifecycle generation, legal-control, enclosure, door, successor, termination, direct-landing, and bounded legacy vocabularies while keeping scheduling projection separate.

The closeout input, source, and projection vocabulary now lives under `models/closeout/`. This is a
one-to-one package move of the existing typed contracts, not a compatibility namespace: input owns
accepted plan shape, source owns exact candidate provenance, and projection owns disposable
scheduling facts while journal models retain lifecycle evidence.

`models/closeout/input.py` no longer owns the rendering of the memory-content commit message.
Since 260913-LCA-L4 the one writer is `kernel.memory_attribution.render_memory_content_message`
(kernel/memory_attribution.py:72-97), and `EffectiveCloseoutInput.memory_content_message(code_commit)`
(input.py:148-166) is the closeout-shaped way in to it: the closeout's own message verbatim plus
exactly one final-paragraph `Code-Commit: <sha>` trailer naming the code commit that same closeout
landed. Both closeout routes still render through that wrapper — worktree closeout and the
branch-addressed direct landing — while the prepared memory-content leg, carryover, baseline adoption
and backfill call the kernel renderer directly, so the attribution has a single definition in kernel.
There is no current ledger-only producer: the cache is rebuilt without a commit. Historical commits without attribution contribute no computed mapping.

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

Start with `tools/tool_registry.py`: `TOOL_RESPONSE_MODELS` maps every modeled builder
to one response model, while `PUBLIC_TOOL_RESPONSE_MODELS` filters out retained
compatibility builders so it matches `mcp.tools.PUBLIC_TOOLS`. Both are typed
`dict[str, type[ResponseEnvelope]]` (260731-EFA-L4), not `type[BaseModel]`.
`tools/public_roster.py` (260831-LOCR-L32) is the route's zero-import leaf holding the single
definition of the advertised tuple `PUBLIC_TOOLS` (63 ordered names since 260831-LOCR-L37 added
`worktree_pause`; L22-L86); `mcp/tools/base.py`
re-exports the identical object. It lives here because a `models` response model now reads it —
`models/worktree.py` enforces the worktree surface's next-move vocabulary against it — and
`models → mcp` would be a `layers.toml` violation.
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
spend env keys; since 260821-ARSPAWN-L1 also the caller-kind provenance `spawnedByKind`
(`plane|ambient|unattributed`) mirroring the catalog row — the provenance the public `dispatch_agent`
sets by caller kind), and
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
- **The advertised tuple, the live FastMCP registration, and this registry are three separately
  declared artifacts** (260831-LOCR-L29). `finalize_tool_response` indexes
  `TOOL_RESPONSE_MODELS` by tool name, so an advertised name with no registry row raises instead of
  returning a payload. Compare all three from a live probe server —
  `mcp/tests/test_tools.py::PublicSurfaceInventoryTests` is that executor. Do not treat the
  `server_info` payload as surface authority: it reports `mcp.tools.PUBLIC_TOOLS` itself, so
  comparing it to the tuple is self-referential.
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
  The historical wire-vocabulary suite measured produced-vs-declared in both
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
| Public MCP payload builders validate through the response model registry. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:22-24 |
| The advertised public roster's single definition, in this route's zero-import `tools/` leaf; the adapter re-exports the identical object. | "PUBLIC_TOOLS = ("; "__all__ = [\"PUBLIC_TOOLS\", \"RESERVED_TOOLS\", \"TRANSPORT\"]" | mcp/src/agents_remember/models/tools/public_roster.py:22-22; mcp/src/agents_remember/mcp/tools/base.py:19-19 |
| The response model that reads the roster to enforce the worktree surface's next move against `PUBLIC_TOOLS`. | "# The next-move triple, declared here so the worktree surface's guidance is part of"; "def _require_registered_public_next_tool" | mcp/src/agents_remember/models/worktree.py:322-328; mcp/src/agents_remember/models/worktree.py:355-364 |
| The registry maps every modeled builder and the advertised public subset to response models. | `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:233-237 |
| Contract tests prove public tool coverage and schema generation. | `PublicToolResponseModelTests`; `test_every_public_tool_has_a_response_model`; `test_every_public_tool_response_model_generates_json_schema` | mcp/tests/test_models.py:16-26 |
| The record-landing envelope is declared on this route. | "class WorktreeRecordLandingResponse(WorktreeCommandResponse):" | mcp/src/agents_remember/models/worktree.py:478-478 |
| The checkpoint-landing envelope is declared on this route. | "class WorktreeCheckpointLandingResponse(WorktreeCommandResponse):" | mcp/src/agents_remember/models/worktree.py:459-459 |
| The checkpoint registry row sits between the integrate and record-landing rows; the record-landing row follows it. | "\"worktree_checkpoint_landing\": WorktreeCheckpointLandingResponse,"; "\"worktree_record_landing\": WorktreeRecordLandingResponse," | mcp/src/agents_remember/models/tools/tool_registry.py:191-191; mcp/src/agents_remember/models/tools/tool_registry.py:192-192 |
| Curator coherence keeps semantic revision, attempt, immutable record, stable authority, snapshot, and action request identities separate and exact. | `CuratorCoherenceRecord`; `CuratorCoherenceAuthority`; `CuratorCoherenceSnapshot`; `CuratorCoherenceRequest` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:190-434 |
| Operator inbox response models cover post, poll, consume, and hosted-delivery metadata. | `OperatorInboxPostResponse`; `OperatorInboxPollResponse`; `OperatorInboxConsumeResponse` | mcp/src/agents_remember/models/operator_inbox.py:54-79; mcp/src/agents_remember/models/operator_inbox.py:82-89; mcp/src/agents_remember/models/operator_inbox.py:92-98 |
| Orchestration response models cover the public manager-nudge helper. | `OrchestrationNudgeManagerResponse` | mcp/src/agents_remember/models/orchestration.py:14-24 |
| Lifecycle finalizer response model covers the terminal task finalization payload. | `LifecycleFinalizeTaskResponse` | mcp/src/agents_remember/models/lifecycles/finalize.py:14-39 |
| Terminal response models cover trusted task-seat assignment and internal hosted-session spawn. | `AttachTerminalSessionToTaskResponse`; `SpawnAgentSessionResponse` | mcp/src/agents_remember/models/terminal.py:35-48; mcp/src/agents_remember/models/terminal.py:91-137 |
| The next-step engine that fills `nextStep` from the active lifecycle. | `nextStep` | mcp/src/agents_remember/application/next_step.py:260-270 |
| The wire-test module documents the 165-of-213 `context_packet` baseline. | "165 of the 213" | mcp/tests/test_wire_vocabulary_exhaustiveness.py:7-7 |
| The worktree model declares the contract-cell vocabulary aliases (moved from worktrees by 260731-EFA-L9) with `MemoryMode` imported from kernel. | "from agents_remember.kernel.coordination_context.models import MemoryMode"; "WorkflowKind = Literal["; "HumanReviewStatus = Literal["; "LifecycleStatus = CloseoutStatus"; "CleanupStatus = Literal[" | mcp/src/agents_remember/models/worktree.py:9-9; mcp/src/agents_remember/models/worktree.py:29-40 |
| The worktree model declares the phase/next-operation/next-tool vocabulary (moved from guidance by L9). | "WorktreePhase = Literal["; "NextOperation = Literal["; "NextTool = Literal[" | mcp/src/agents_remember/models/worktree.py:40-40; mcp/src/agents_remember/models/worktree.py:50-50; mcp/src/agents_remember/models/worktree.py:59-59 |
| Guidance consumes the phase/next-operation/next-tool aliases declared by the wire model through one grouped import. | "from agents_remember.models.worktree import (" | mcp/src/agents_remember/worktrees/modules/guidance.py:9-9 |
| The drift-status vocabulary and `DriftSummaryPacket` that `drift.py` and `memory.py` import. | `DriftSummaryPacket` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:11-20 |

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| Direct landing returns cache observations separately from commits. | `DirectLandingResponse` | mcp/src/agents_remember/models/direct_landing.py:20-54 |
| Public message transport names only code and memory. | `CloseoutMessageInput` | mcp/src/agents_remember/models/closeout/input.py:46-52 |

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
builders that write them, and the module says why: `mcp.tools.base` → `models.tools.tool_registry` →
`models.terminal` is an existing import edge, so a `models.terminal` → `mcp.tools.terminal`
import would close a cycle. The invariant is one declaration, not a particular owner —
`mcp.tools.terminal` imports these aliases and annotates its status seams with them.
`VALID_SPAWN_AGENT_SESSION_STATUSES`, `VALID_SESSION_RETIRE_STATUSES` and
`VALID_SESSION_RENAME_STATUSES` are `frozenset(get_args(...))` of their aliases — the runtime
half derived from the type rather than typed beside it.

**`tools/tool_registry.py` — the loose type that made the token count wrong.** Both registries are
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

## 260821-CLIVE-L1 Closeout Vocabulary

`closeout_input.py` adds the raw-message, resolved-plan, enabled/not-applicable leg, structured-refusal, and effective-input vocabulary shared by both closeout routes. Public worktree and direct-landing responses expose that vocabulary. Lifecycle operation records use only the normalized form; no generated subject, blank sentinel, or fallback input remains below validation.

## 260821-CLIVE-L2 Historical Intermediate Architecture

Models validate immutable identity and contradictory evidence but perform no I/O or recovery.
`models.lifecycles` owns the canonical root-journal vocabulary. The transitional L2
selected/in-flight/certified queue schema was removed by L3; `models.queue` now exposes only the
disposable waiting-door projection request/response contract, while
`models.closeout_projection` owns its strict projection vocabulary.

Registered tool request/response contracts now live under `models/tools/`; the move removes the former flat paths without changing the registry's ownership or creating compatibility exports.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Strict lifecycle operation record/projection. | "class LifecycleOperationRecord(BaseModel):"; "class LifecycleOperationProjection(StrictResponseModel):" | mcp/src/agents_remember/models/lifecycles/operation.py:340-340; mcp/src/agents_remember/models/lifecycles/operation_projection.py:340-340 |
| Queue candidate projection. | `CloseoutQueueRequest`; `CloseoutQueueResponse` | mcp/src/agents_remember/models/queue/closeout_queue.py:32-37; mcp/src/agents_remember/models/queue/closeout_queue.py:40-59 |

## 260821-DAGQC-L2 Closed Quality And Landing Models

The route adds strict discriminated memory-quality request DTOs and the shared
`QualityGateResult`/memory-policy models. Closeout and integration no longer expose open quality
mappings, and stable versus immutable result paths remain distinct. Direct landing keeps exactly
three top-level outcomes; journal lifecycle evidence is nested.

## 260824-PDLS — Python Test Evidence Model

`test_evidence.py` adds a closed diagnostic/certifying altitude and consumer vocabulary.
Diagnostic evidence carries exact nodes, exit code, and a structural candidate binding;
certifying evidence has no public constructor and is minted only from a verified immutable Dagger
generation. Coverage, quality, retry, route review, lifecycle, closeout, and integration require
the certifying type, keeping acceptance impossible to express as a generic payload flag.

## 260824-PDLS Final Model Reconciliation

The evidence models close authority, lifetime, cadence, and result vocabularies for diagnostic and
certifying lanes, while lifecycle models retain strict journal-owned mutation proof. Projection
invalidation removes the impossible `not-created` outcome, and validator decomposition preserves
one typed public contract instead of distributing failure-family knowledge across callers.

## 260821-ARSPAWN-L2 Stable Structural Evidence

`TerminalCatalogEntry.dispatch_brief_entry_id` is private durable reconciliation evidence, not a
structural address. It may be serialized for control-plane recovery and dashboard diagnostics.
The receipt survives promotion of a staged heir into the same document-and-role seat, but clears
when document or role changes. Promotion also clears the replacement reference so one row cannot
remain in both seat generations.

`StructuralOutcome` projects operation, status, canonical task document, role, detail, and
delivery state while deliberately excluding runtime occupant identity.

## MCAR-L03 Pair Identity Models

`memory_candidate.py` owns the frozen exact-pair schema. Memory-quality, curator-coherence, and
closeout response models reference that schema rather than copying its fields. Semantic
requirement versions, delivery attempts, candidate trees, and pair identity remain separate
contracts.

## Status-Change Wait Response

`models/worktree.py` still owns `WorktreeStatusWaitResponse`, but `models/tools/tool_registry.py`
no longer registers it: the `worktree_status_wait` tool was removed from the public surface, so the
response class is currently unregistered and unreferenced anywhere in the tree. It carries a typed
outcome, optional successor generation and meaningful revision, elapsed/timeout observations, and
the coherent lifecycle projection. It introduces no public worker PID or private operation key.

| Finding | Anchor | Source |
| --- | --- | --- |
| The read-only wait response exposes outcomes and cursors without private worker authority. | "class WorktreeStatusWaitResponse(WorktreeCommandResponse):" | mcp/src/agents_remember/models/worktree.py:393-393 |
| Public response registration no longer carries the dedicated wait response: `worktree_status_wait` is absent from `TOOL_RESPONSE_MODELS`, so `WorktreeStatusWaitResponse` stays defined in `models/worktree.py` with no registered tool. | "\"worktree_sync\": WorktreeSyncResponse," | mcp/src/agents_remember/models/tools/tool_registry.py:186-186 |


## Integrated IAS Recovery Contract

The changed lifecycle preparation model retains original command ownership and append-only terminal observations through focused validation helpers. Runtime composition and physical Git proof remain outside models. The retained `test_wire_vocabulary_exhaustiveness.py` is now support code without collected test functions; its historical census and deleted cases must not be read as current exhaustive protection.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.


## 260831-LOCR-L30 Checkpoint-Landing Wire Model

`models/worktree.py` gains `WorktreeCheckpointLandingResponse` (operation literal
`worktree_checkpoint_landing`, carrying `integrationStrategy`, `integratedCodeCommit`,
`integratedMemoryContentCommit`), `IntegrationStatus` gains the
`checkpointed` member, and `models/tools/tool_registry.py` registers the new envelope between
`worktree_integrate` and `worktree_record_landing`.

This is the same invariant the L29 section below states, satisfied a second time — and the second
landing envelope is why the registry cannot be checked as a set alone. The two tools sit adjacent in
the registry and their payloads differ only in the operation literal, so a swap between them would
still validate as a set. `mcp/tests/test_tools.py::PublicSurfaceInventoryTests` drives one
`finalize_tool_response` call per name for that reason.

**260831-LOCR-L34** adds `worktree_checkpoint_landing` to the `NextTool` vocabulary
cit:([`NextTool`], mcp/src/agents_remember/models/worktree.py:59-74) — the checkpoint's preview and its
`integration-ref-race` refusal both emit it, and it is a registered public tool — while deliberately
leaving `NextOperation` unchanged, because pausing a master is the existing
`request_integration_decision` intent rather than a lifecycle phase. The reasoning and the
reviewed-and-not-changed row live on the `models/worktree.py` card; the preview/apply parity invariant
that produced the repair is inventoried on the `worktrees/overview.md` route.

## 260831-LOCR-L29 Public-Surface Repair

`models/worktree.py` gains `WorktreeRecordLandingResponse` (operation literal
`worktree_record_landing`, carrying `integrationStrategy`, `landedCodeCommit`, and
`landingTargets`), and `models/tools/tool_registry.py` registers it immediately after
`worktree_integrate`. This route overview also governs `models/tools/`, which has no nested
overview of its own.

The route already stated the invariant — every advertised MCP tool has exactly one declared
response model — and this is the route where it can be violated invisibly. `finalize_tool_response`
indexes `TOOL_RESPONSE_MODELS` by tool name, so a tool that `mcp/registration/closeout.py` registers
is published by FastMCP while the missing row makes its own response lookup raise. The tool was
advertised and unable to return a payload, and the suite stayed green: `server_info` reports
`PUBLIC_TOOLS` itself, so the only comparison available was self-referential.

The matching census row landed in `mcp/tools/base.py` (61 advertised names at that leaf — 62 since
260831-LOCR-L30 — with `worktree_record_landing` immediately after `worktree_integrate`), and the
invariant now has an executor in
`mcp/tests/test_tools.py::PublicSurfaceInventoryTests`, which compares the live registration order
to that tuple and drives one `finalize_tool_response` call for the repaired name.

## 260831-LOCR-L32 The Public Roster Joins This Route, And The Worktree Next Move Is Enforced

This route's `tools/` leaf gained `public_roster.py` — a zero-import module whose whole body is the
62-name literal `PUBLIC_TOOLS`
cit:([`PUBLIC_TOOLS`], mcp/src/agents_remember/models/tools/public_roster.py:22-86). It is the tuple's **single definition**; `mcp/tools/base.py`
now re-exports that identical object instead of declaring its own, so
`agents_remember.mcp.tools.PUBLIC_TOOLS`, `PUBLIC_TOOL_RESPONSE_MODELS`, the live registration order,
and the `public_surface` pin all still name the same tuple with no consumer change.

The roster lives here because a model needs to read it. `models/worktree.py::WorktreeCommandResponse`
now declares `nextAction` / `nextTool` / `nextArgs`
cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:322-328) and refuses a `nextTool` outside
`PUBLIC_TOOLS` through `_require_registered_public_next_tool`
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:354-365). Before this leaf the
envelope inherited `extra="allow"` and declared none of those keys, so
`application/worktree_status.py::_project_terminal_contract_status`'s write crossed the wire verbatim
and unchecked — `worktree_abandon` reached the wire as a `nextTool` without ever being a `NextTool`
member. `models → mcp` would be a `layers.toml` violation (models = 2, mcp = 22), a function-local
import trips `ruff PLC0415`, and module-level imports in either direction are circular — so the tuple's
move into this route is the precondition of the fix, not a companion cleanup. The layering checker
returned to its exact baseline of 16 violations with no `models → mcp` edge and no new cycle.

**The invariant is per surface.** The worktree surface's next move must name a registered *public*
tool; the `task_doc` surface may name the registered-but-non-public `session_retire`
(`TaskDocResponse` is not a `WorktreeCommandResponse`). Do not widen `PUBLIC_TOOLS` to cover it.

## 260831-LOCR-L36 The Activation Vocabulary Becomes Contract-Scoped

The atomic-series activation record was re-keyed from the protected source pair to the canonical
series contract, and this route's wire models moved with it. Two atomic masters commanded by one
sprint derive the *same* protected pair (same code repository/branch and memory repository/branch;
only the work branches differ), so a one-record-per-pair store made the second master's selection
replace the first. `models/structural/atomic_series_activation.py` is now 45 lines and declares only
`AtomicSeriesActivationRecord` (16) and `AtomicSeriesActivationArchiveEvidence` (30), both
`schemaVersion "2.0"` with `contractFingerprint`.

On the worktree wire vocabulary (`models/worktree.py`, 514 lines):

- `AtomicSeriesActivationFact.contractFingerprint` replaces `sourcePairFingerprint`, so status
  evidence names the contract whose record was read.
- `AtomicSeriesAdmissionActivation.contractFingerprint` replaces `sourcePairFingerprint`.
- `AtomicSeriesAdmission` lost `classification`, `sourcePair`, `sourcePairFingerprint` and `blocking`,
  and gained `contractFingerprint`. The `AtomicSeriesAdmissionBlocking` model was deleted, so a
  foreign live master is no longer expressible as this contract's blocker or retry precondition.
- No model on this route declares `AtomicSeriesSourceRef` / `AtomicSeriesSourcePair`.

The wait vocabulary narrowed with it: the activation domain now returns only
`atomic-series-reconciling`, so a vacant record and another master's active selection are never
waiting reasons. Real wave dependencies still gate through the sprint execution graph's own
`predecessor-incomplete:` reasons, and everything under `worktrees/integration/**` is untouched by
this change.

## 260915-KS-L1 Knowledge Vocabulary

This route gained one sub-route of nine modules, `models/knowledge/`, and no authority. It is the shared
vocabulary of the experimental knowledge substrate: repository namespace identity, invariant identity and the
immutable revision aggregate, the sealed-payload digest, the provenance envelope, the source identity and locator
union, the typed operation/refusal/result contract, and the schema identity.

Three ownership rules are the reason it lives here rather than in the store that writes it:

- **Literal vocabularies are defined where they decide.** `KnowledgeState` (`proposed`/`accepted`),
  `KnowledgeOperation`, `KnowledgeRefusalCode`, `REVISION_PAYLOAD_VERSION` and `KNOWLEDGE_SCHEMA_NAME` are declared
  in their owning model and imported by the decider — never declared by the decider and re-exported downward.
- **Values, not rows.** `KnowledgeModel` is frozen with `extra="forbid"`, which makes the process-local value
  immutable; refusing an update to a stored revision is a storage rule enforced by schema triggers and the
  operation's preconditions, not by model immutability.
- **Identity is not a label.** Display version and display label are separated from immutable identity, so two
  successors of one revision may both display `v2` and both stay addressable. `RevisionDraft` deliberately has no
  `payload_digest` field: the store recomputes the seal rather than accepting it.

`Authorship` and the `SourceLocator` union are declared **shared**: they are the vocabulary the selective
read/diff contributor (KS-R07/KS-R08) is expected to consume, and the locator union is discriminated on `kind` so
that consumer needs no second locator vocabulary. That consumer does not exist yet; nothing here claims it does.
The blob identity is a Git object identity, not a copy of the bytes — there is no second content store.

Validation vocabulary matters as much as shape: `normalized_uuid` refuses a non-canonical identifier spelling
instead of rewriting it, `Authorship` requires a normalized-UTC `recorded_at`, and `SourceAnchor` refuses an
absolute, backslash, UNC or parent-escaping path so a stored record never carries one.

| Finding | Anchor | Source |
| --- | --- | --- |
| The served knowledge vocabulary as an explicit re-export list — re-cited against the working tree, which the graph half extended. | `__all__` | mcp/src/agents_remember/models/knowledge/__init__.py:160-288 |
| The frozen base and the refusal to rewrite a non-canonical identifier. | `KnowledgeModel`; `normalized_uuid` | mcp/src/agents_remember/models/knowledge/base.py:34-37; mcp/src/agents_remember/models/knowledge/base.py:95-109 |
| The invariant identity and revision aggregate, including the display-label-versus-identity separation. | `InvariantIdentity`; `InvariantRevision` | mcp/src/agents_remember/models/knowledge/invariant.py:33-55; mcp/src/agents_remember/models/knowledge/invariant.py:56-115 |
| The sealed payload, with the predecessor set inside the digest and the digest field excluded. | `canonical_revision_payload` | mcp/src/agents_remember/models/knowledge/digest.py:30-52 |
| The provenance envelope and its normalized-UTC requirement. | `Authorship` | mcp/src/agents_remember/models/knowledge/authorship.py:32-88 |
| The shared source identity, locator union and the relative-POSIX-path rule — now split into the draft and the stored anchor, with a real `UUID` identity. | `SourceLocator`; `SourceAnchorDraft`; `SourceAnchor` | mcp/src/agents_remember/models/knowledge/source.py:80-82; mcp/src/agents_remember/models/knowledge/source.py:82-129; mcp/src/agents_remember/models/knowledge/source.py:130-133 |
| The typed operation, refusal-code and result contract — re-cited against the working tree, which the graph, candidate-change, snapshot, merge, authored-judgment and detection halves have each extended since. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:101-171 |
| The invariant-creation result whose `operation` field names the operation that produced it. | `CreateRevisionResult` | mcp/src/agents_remember/models/knowledge/result.py:404-421 |
|  The storage owner that writes this vocabulary. | "class OpenedKnowledgeStore" | mcp/src/agents_remember/memory/knowledge/store.py:92-510  |
| The later requirement packets the shared envelope and locator are declared for: requirement packets `KS-R07` and `KS-R08`, which live in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address them. | — | — |

## 260915-KS-L2 The Graph Vocabulary, And The Repaired Anchor Identity

This route's knowledge sub-route grew from nine modules to eleven and the vocabulary it serves now covers the
**graph**: `family.py` carries family identity and the immutable family revision, and `graph.py` carries the two
relations and the read models both directions answer with. Four of the nine L1 modules changed, three of them
substantively.

The three graph-vocabulary rules, each the model-level half of a storage contract:

- **A guarantee is the family's own text.** `FamilyRevisionDraft` carries the joint guarantee and never composes
  it from its members, and its `payload_digest` seals the whole aggregate including the sorted predecessor set, so
  a changed guarantee is a separately identified successor.
- **A draft carries no seal, and the anchor draft carries no provenance.** `FamilyMemberDraft`,
  `RealizationClaimDraft` and `FamilyRevisionDraft` have no row digest, and `SourceAnchorDraft` has no
  `provenance` field; the store computes the first and the admitted application attaches the second.
- **A role is an authored claim.** `RealizationRole` is a closed vocabulary with an explicit `unclassified`
  member, so a missing role is representable as "not classified" rather than silently defaulted to a real one,
  and no reader infers a role or a rationale from the source.

**The repaired anchor identity is a correction to the L1 vocabulary, not a new feature.** `SourceAnchor.anchor_id`
was declared `anchor_id: UUID = Field(pattern=UUID_PATTERN)`, and Pydantic refuses to apply a string `pattern`
constraint to its UUID schema, so **every** anchor construction raised
`TypeError: Unable to apply constraint 'pattern' … for schema of type 'uuid'` — the class was unconstructible, and
it stayed latent because no L1 test constructed one. The field is now a plain `UUID` and the canonical stored text
is derived at the storage boundary (`records.anchor_row` writes `str(anchor.anchor_id)`), exactly as it is for an
authorship operation identity. The same change split `SourceAnchor` into the draft (what the author decided) and
the stored record (the draft plus the provenance envelope), which is what keeps provenance out of a caller's hands.
The lesson a future reader should take is narrow and reusable: on an identifier field, a `pattern`-constrained
string and a parsed `UUID` are not interchangeable spellings — one of them is unconstructible.

The `models/` route's own statement that `REVISION_PAYLOAD_VERSION` is the payload version is now one of two:
`FAMILY_REVISION_PAYLOAD_VERSION` exists because the family payload seals a different field set, so a digest can
never be mistaken for the other object's identity.

| Finding | Anchor | Source |
| --- | --- | --- |
| The family identity, the immutable revision aggregate and its self-consistency rules. | `FamilyIdentity`; `FamilyRevisionDraft`; `FamilyRevision` | mcp/src/agents_remember/models/knowledge/family.py:51-55; mcp/src/agents_remember/models/knowledge/family.py:58-102; mcp/src/agents_remember/models/knowledge/family.py:105-109 |
| The two relation shapes, the closed authored role vocabulary and the four read models. | `FamilyMemberDraft`; `RealizationClaimDraft`; `RealizationRole`; `UNCLASSIFIED_ROLE`; `AnchorRealizations` | mcp/src/agents_remember/models/knowledge/graph.py:49-56; mcp/src/agents_remember/models/knowledge/graph.py:65-85; mcp/src/agents_remember/models/knowledge/graph.py:36-44; mcp/src/agents_remember/models/knowledge/graph.py:46-46; mcp/src/agents_remember/models/knowledge/graph.py:120-129 |
| The draft/stored split and the repaired `UUID` identifier field. | `SourceAnchorDraft`; `SourceAnchor` | mcp/src/agents_remember/models/knowledge/source.py:82-129; mcp/src/agents_remember/models/knowledge/source.py:130-133 |
| The two payload versions and the family payload's sealed field set. | `FAMILY_REVISION_PAYLOAD_VERSION`; `canonical_family_revision_payload` | mcp/src/agents_remember/models/knowledge/digest.py:26-27; mcp/src/agents_remember/models/knowledge/digest.py:71-90 |
| The shared accepted/proposed rule both revision aggregates apply at construction. | `require_consistent_acceptance` | mcp/src/agents_remember/models/knowledge/base.py:40-56 |
| The extended served surface, including the graph names. | `__all__` | mcp/src/agents_remember/models/knowledge/__init__.py:123-202 |
| The eight graph operations and the anchor-endpoint union the request vocabulary gained. | `AnchorEndpoint`; `NewAnchor`; `AnchorReference`; `CreateRealizationClaimResult` | mcp/src/agents_remember/models/knowledge/result.py:343-343; mcp/src/agents_remember/models/knowledge/result.py:325-325; mcp/src/agents_remember/models/knowledge/result.py:508-508; mcp/src/agents_remember/models/knowledge/result.py:332-332; |
| The storage owners that write this vocabulary: the graph modules, plus the store for the invariant half. | `create_family_revision`; `class OpenedKnowledgeStore` | mcp/src/agents_remember/memory/knowledge/families.py:133-162; mcp/src/agents_remember/memory/knowledge/store.py:92-510 |
| The requirement this graph vocabulary belongs to: requirement packet `KS-R02@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it. | — | — |

## 260915-KS-L3 The Candidate-Change Vocabulary

This route's knowledge sub-route grew from eleven modules to twelve, and the vocabulary it serves now covers the
**write boundary** rather than only the stored shapes. `candidate.py` is the whole vocabulary of the one
candidate-change operation: the resolved context, the expected-record model, the closed command union, the batch
and its factual receipt. Three of its rules are the model-level half of a storage contract:

- **A resolved context is compared, never trusted.** `KnowledgeContext` carries what the admitted runtime
  resolved, and `context_digest` seals every field but itself; `CandidateResolution` deliberately has **no**
  dataset-identity field, so an application cannot pass a remembered digest — it can only read one. The model
  validator refuses an unsealed context at construction, and the operation re-derives the digest inside its
  transaction, which is the only defence against a `model_copy`-built batch that bypasses the validator.
- **The union is the reach.** `ProposedCommand` is eighteen frozen members discriminated on `kind` with
  `extra="forbid"`: there is no promotion member, no approval member, no arbitrary-SQL member and no free-form
  field, so "this operation never accepts knowledge" and "a payload cannot confer authority" are properties of
  the vocabulary rather than rules the operation remembers to apply. Command payloads carry **no** `Authorship`:
  the admitted envelope is attached by the store, and a draft that arrived with its own is re-stamped.
- **Expected state, never assumed state.** `ExpectedRecord` is `present` with a digest or `absent` without one,
  and there is deliberately no third mode — "I did not say" is not an expectation. `ChangeBatch` refuses two
  expectations for one record.

The receipt is part of the contract too: `RecordIdentity.state` is exactly `written | removed`, a removal carries
the digest the row had, a command whose effect was already stored contributes no entry, and
`MutationResult._require_consistent_receipt` refuses a refusal that changed anything, a non-refused result with a
refusal, a `no_change` result with entries, a `changed` result with an empty entry list, or a `changed` result
whose two identities are equal.

`models/knowledge/result.py` grew the two label-edit request/result pairs and the two candidate-boundary codes
(`target_not_candidate`, `promotion_not_supported`), while the `task-candidate` lane deliberately reuses
`unauthorized_scope`. **The refusal code `no_change` remains declared with no producer** — the reachable
vocabulary is the *result state*, and a consumer must not branch on the code.

| Finding | Anchor | Source |
| --- | --- | --- |
| The lane vocabulary, including the read-only `baseline` member that exists so it can be refused by name. | `KnowledgeLane`; `CANDIDATE_LANES` | mcp/src/agents_remember/models/knowledge/candidate.py:107-107; mcp/src/agents_remember/models/knowledge/candidate.py:109-109 |
| The resolved context and its two consistency validators. | `KnowledgeContext` | mcp/src/agents_remember/models/knowledge/candidate.py:182-223 |
|  The module-level digest the validator calls and the operation re-derives. | "def context_digest" | mcp/src/agents_remember/models/knowledge/candidate.py:226-226  |
| The expectation model and its present-with-digest / absent-without-digest rule. | `ExpectedRecord` | mcp/src/agents_remember/models/knowledge/candidate.py:244-266 |
| **The closed union with no promotion, approval or SQL member — twenty-two members after this leaf's four composition command kinds joined the eighteen**, and the members are the operation's entire reach. | `ProposedCommand` | mcp/src/agents_remember/models/knowledge/candidate.py:469-493 |
| The alias a batch's commands travel under, and the construct that makes the union's membership checkable in one place. | `ChangeCommand` | mcp/src/agents_remember/models/knowledge/candidate.py:495-589 |
| The resolution shape that deliberately omits the dataset identity. | `CandidateResolution` | mcp/src/agents_remember/models/knowledge/candidate.py:498-515 |
| The batch and the receipt consistency validator the operation's results must satisfy. | `ChangeBatch`; `MutationResult`; `RecordIdentity` | mcp/src/agents_remember/models/knowledge/candidate.py:239-260; mcp/src/agents_remember/models/knowledge/candidate.py:518-543; mcp/src/agents_remember/models/knowledge/candidate.py:546-589 |
| The two candidate-boundary codes and the three operations that leaf added to the served vocabulary. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:101-171 |
| The served operation union the candidate-boundary leaf joined. | `KnowledgeOperation` | mcp/src/agents_remember/models/knowledge/result.py:36-96 |
| The invariant-label result that leaf added to the served vocabulary. | `SetInvariantLabelResult` | mcp/src/agents_remember/models/knowledge/result.py:570-590 |
| The operation that consumes this vocabulary. | `change_candidate` | mcp/src/agents_remember/memory/knowledge/candidate.py:61-80 |
| The composition seam that resolves a context from a live candidate and seals it. | `resolve_candidate_context`; `build_candidate_context` | mcp/src/agents_remember/application/knowledge.py:252-273; mcp/src/agents_remember/application/knowledge.py:275-301 |
| The seam entry point that applies a batch under the admitted provenance. | `change_knowledge_candidate` | mcp/src/agents_remember/application/knowledge.py:303-315 |
| The lane rules the batch operation applies before it takes the lock. | `require_writable_lane` | mcp/src/agents_remember/memory/knowledge/candidate.py:83-102 |

## 260915-KS-L4 The Snapshot Vocabulary

The knowledge sub-route grew a thirteenth module, `models/knowledge/snapshot.py`, and the vocabulary it adds is a
**local working object's** vocabulary rather than a stored shape's: one candidate directory, its sealed receipt,
one closed snapshot stage, one publication request/result, the publication-state measurement a read gates on, and
the closed disposal union. `models/knowledge/result.py` grew six operations and seven refusal codes in the same
change, and the facade re-exports all of it.

Three model-level rules carry the contract, and each is the reason a field is missing rather than present:

- **The receipt carries no dataset digest.** `CandidateReceipt` records namespace, lane, the exact code and memory
  inputs, the schema generation and the candidate reference, and seals every one of them with `receipt_digest` —
  but the *dataset's* logical identity is deliberately absent, because a caller that could state it could hand-write
  the identity its publication would later be compared against. The identity is read from the database or it does
  not exist, and `build_candidate_receipt` derives rather than accepts.
- **Every result is closed, and `state` is the only branch.** `CandidateResult`, `SnapshotPublicationResult`,
  `PublicationState` and `CandidateDisposalResult` each refuse an inconsistent combination at construction: a
  refusal carries its refusal and reports nothing it did not establish, a non-refusal names what it reached, and a
  refused publication reports **no** destination identity at all. `PreparedKnowledgeSnapshot` carries both the
  logical identity and the physical `file_digest` because publication decides two different questions — "is this
  the same knowledge?" and "is this the file I froze?".
- **The disposal union has exactly two members, and its authorization is carried, not examined.**
  `CandidateDisposition` is `DiscardCandidate | PublishedCandidate` discriminated on `kind`; there is no "it looked
  disposable" mode. `DiscardCandidate.authorization_ref` is stored because the caller owns the approval chain,
  while this layer decides only permissibility (whether the named identity is the one the candidate holds now, and
  therefore whether discarding abandons work no retained publication covers).

The refusal vocabulary's own rule is unchanged by the addition and worth restating where the codes are declared:
`no_change` remains a **result state** in two vocabularies (the batch's `MutationResult` and the publication's
`SnapshotPublicationResult`) and a refusal code with no producer, and `snapshot_incomplete` /
`publication_durability_unconfirmed` exist because "the private stage did not complete" and "the replacement
completed but cannot be confirmed" need different remedies.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The snapshot vocabulary's own module: layout, receipt, stage, publication and disposal.** | `CANDIDATE_DATABASE_NAME`; `CandidateReceipt`; `PreparedKnowledgeSnapshot`; `SnapshotPublicationResult`; `CandidateDisposition` | mcp/src/agents_remember/models/knowledge/snapshot.py:52-54; mcp/src/agents_remember/models/knowledge/snapshot.py:109-141; mcp/src/agents_remember/models/knowledge/snapshot.py:224-236; mcp/src/agents_remember/models/knowledge/snapshot.py:259-293; mcp/src/agents_remember/models/knowledge/snapshot.py:351-354 |
| The two derived paths that keep write and publication on one file. | `candidate_database_path`; `candidate_receipt_path` | mcp/src/agents_remember/models/knowledge/snapshot.py:58-62; mcp/src/agents_remember/models/knowledge/snapshot.py:64-67 |
| The typed admitted handle that confers no authority by itself. | `AdmittedCandidateDestination` | mcp/src/agents_remember/models/knowledge/snapshot.py:70-93 |
| The baseline that requires the identity the caller admitted for it. | `CandidateBaseline` | mcp/src/agents_remember/models/knowledge/snapshot.py:96-106 |
| The receipt's sealing helper and the one derived constructor. | `receipt_digest`; `build_candidate_receipt` | mcp/src/agents_remember/models/knowledge/snapshot.py:144-148; mcp/src/agents_remember/models/knowledge/snapshot.py:151-185 |
| The destination request whose "expected absent" mode is the only way to overwrite. | `SnapshotDestinationRequest`; `PublishSnapshotRequest` | mcp/src/agents_remember/models/knowledge/snapshot.py:239-249; mcp/src/agents_remember/models/knowledge/snapshot.py:252-256 |
| The measurement that reports two identities and guesses nothing. | `PublicationState` | mcp/src/agents_remember/models/knowledge/snapshot.py:296-321 |
| The carried-not-examined authorization reference and the verdict. | `DiscardCandidate`; `PublishedCandidate`; `CandidateDisposalResult` | mcp/src/agents_remember/models/knowledge/snapshot.py:324-337; mcp/src/agents_remember/models/knowledge/snapshot.py:340-345; mcp/src/agents_remember/models/knowledge/snapshot.py:357-375 |
| **The operation and refusal vocabulary this leaf extended.** | `KnowledgeOperation`; `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:36-78; mcp/src/agents_remember/models/knowledge/result.py:82-147 |
| The facade that re-exports the whole snapshot surface as the served vocabulary. | `__all__` | mcp/src/agents_remember/models/knowledge/__init__.py:160-288 |
| The lifecycle and publication operations that produce these values. | `create_candidate`; `publish_candidate_snapshot`; `publication_state` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:85-98; mcp/src/agents_remember/memory/knowledge/publication.py:66-111; mcp/src/agents_remember/memory/knowledge/materialization.py:34-99 |
| The second composition seam that admits these values and returns them unchanged. | `admitted_candidate_destination`; `publish_knowledge_snapshot` | mcp/src/agents_remember/application/knowledge_snapshot.py:67-82; mcp/src/agents_remember/application/knowledge_snapshot.py:134-139 |
| The node that proves the publication outcome is a measurement rather than a claim. | "test_a_logical_no_op_retains_the_published_bytes" | mcp/tests/test_knowledge_snapshot_publication.py:239-239 |

## 260915-KS-L5 The Merge Vocabulary

The knowledge sub-route grew a fourteenth module, `models/knowledge/merge.py`, and it declares the **structural**
half of the substrate's vocabulary: three datasets that already exist, two base claims, the coverage facts of a
delta, one conflict record and one outcome. The absence the whole module is built around is stated in its own
docstring rather than left to a consumer's inference: **nothing here can carry a judgement about whether the
merged knowledge is correct** — there is no compatibility, acceptance, approval or "harmless" field, and the one
non-refusal state is named `structurally_merged` because that is the entire claim.

Three splits are load-bearing, and each is a place a weaker model would have permitted a guess:

- **An explicit input versus a resolved one.** `MergeInput` names a dataset *and* the exact logical identity the
  caller admitted for it. A caller cannot hand over a path and let the operation decide which dataset it meant;
  the identity is re-read and compared before any byte is copied. The `reference` field is the caller's own
  durable anchor and is carried as a fact — this layer does not read Git objects to decide what a dataset is.
- **A base claim versus a base fact.** The claim is a closed union of `SuppliedGitBase` (the caller resolved it)
  and `ResolvedGitBase` (the caller claims one commit is the *unique* common base and asks for the evidence).
  There is no third member, so "the operation may pick one" is not expressible. `MergeBaseResolution` records
  which of the two applied, so a reader can tell "the history had one common base" from "the caller said which
  commit it was" without re-deriving it from the claim.
- **A measurement versus a verdict.** `MergeCoverage` reports which tables the changeset touched, which the
  replay proved covered, and how many operations of each kind were materialised; `MergeOutcome` reports the
  identities it observed. Neither can express an opinion about the data.

Two model-level rules a consumer must not flatten, because each is enforced at construction:

- **A table that changed but carried no operation is representable, and it is not silent.** `TableCoverage`
  separates `table_changed` (read from the two datasets) from `operations` (counted from the changeset) — the
  exact pair whose disagreement *is* the silent-omission class — and `MergeCoverage` covers every canonical
  table, so "examined and had nothing to carry" cannot be confused with "never attached".
- **A conflict record states only what the engine supplied.** `MergeConflict` has two shapes:
  `engine_attributed`, where the callback held the operation and the record carries its table, kind and the exact
  row key (read from the operation's **old** values, because a changeset omits a key column an `UPDATE` did not
  change), and `engine_reported_without_row`, where a foreign-key conflict gave the callback no change at all, so
  the row fields are absent and `detail` says so. No violation count is reported for that shape: the pinned
  binding raises `ConstraintError` with no count, so a number there would be the operation's own inference.

`models/knowledge/result.py` grew the two operations (`resolve_merge_base`, `merge_knowledge_datasets`) and
twelve refusal codes in the same change — one per observable failure point, so the twelve different next actions
stay distinguishable. `duplicate_identity` and `delete_reference_conflict` are the two whose meaning a reader must
read from the merge's cards rather than from the code name: the first fires even on byte-identical payloads, and
the second names no row.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The merge vocabulary's own module: the explicit input, the closed base claim, coverage, conflict and outcome.** | `MergeInput`; `SuppliedGitBase`; `ResolvedGitBase` | mcp/src/agents_remember/models/knowledge/merge.py:110-121; mcp/src/agents_remember/models/knowledge/merge.py:81-86; mcp/src/agents_remember/models/knowledge/merge.py:89-101; mcp/src/agents_remember/models/knowledge/merge.py:243-284; mcp/src/agents_remember/models/knowledge/merge.py:293-346; mcp/src/agents_remember/models/knowledge/merge.py:349-391 |
| The one non-refusal state name, which is the entire claim the operation makes. | `MERGE_STATES` | mcp/src/agents_remember/models/knowledge/merge.py:78-78 |
| The request that carries the proven resolution, the paths it deliberately keeps out of the resolution, and the optional destination. | `MergeRequest` | mcp/src/agents_remember/models/knowledge/merge.py:189-215 |
| The base-resolution request and the resolution that records which claim applied. | `MergeBaseRequest`; `MergeBaseResolution` | mcp/src/agents_remember/models/knowledge/merge.py:124-154; mcp/src/agents_remember/models/knowledge/merge.py:157-186 |
| The per-table coverage fact that separates "changed" from "carried an operation". | `TableCoverage` | mcp/src/agents_remember/models/knowledge/merge.py:218-240 |
| **The operation and refusal vocabulary this leaf extended.** | `KnowledgeOperation`; `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:36-78; mcp/src/agents_remember/models/knowledge/result.py:82-147 |
| The merge operation that consumes this vocabulary. | `merge_knowledge_datasets` | mcp/src/agents_remember/memory/knowledge/merge.py:131-163 |
| The base resolution that produces the value this vocabulary consumes. | `resolve_merge_base` | mcp/src/agents_remember/memory/knowledge/merge_base.py:75-105 |
| The third composition seam that takes these values and returns them unchanged. | `merge_resolved_knowledge_datasets` | mcp/src/agents_remember/application/knowledge_merge.py:55-64 |
| The node that asserts the published outcome carries no verdict field and reports the coverage record. | "def test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate(" | mcp/tests/test_knowledge_guarded_merge.py:307-376 |
| The boundary node that holds the conflict record to the engine's own row identity. | "test_the_conflict_record_prefers_the_old_side_and_reports_a_missing_key_as_such" | mcp/tests/test_knowledge_guarded_merge_boundaries.py:165-184 |

## 260915-KS-L6 The Portable Vocabulary, And The Boundary It Draws Around External Input

The knowledge sub-route gained its **fifteenth module**, `models/knowledge/portable.py`, and
`models/knowledge/result.py` gained two operation names and one refusal code. The portable vocabulary is the
wire shape of the artifact contract, and three splits carry it — each exists because collapsing it would make a
statement the code cannot support:

- **A request versus an admitted identity.** `ExportRequest.expected_identity` is **required**, because an export
  is addressed at a dataset rather than at whatever a path currently holds; storage re-reads it before encoding.
- **A validated artifact versus a published dataset.** `PortableValidation` reports what was *checked* — with
  `row_counts` over every canonical table **including the empty ones**, because "present and empty" is the fact
  that separates a complete export from one that dropped a collection — while `ImportResult` reports what now
  *exists*. Neither can carry a verdict and neither can grant acceptance: a row whose `state_at_origin` says
  `accepted` crosses as that stored value and nothing more.
- **A staging fact versus a destination fact.** An import can validate perfectly and still not publish, so
  `ImportResult.verified_identity` is carried **independently of `state`**, and the model refuses to construct
  unless the verified identity and the destination's identity agree on the logical digest.

`ImportRequest.expected_destination` is a **closed two-mode choice** in effect — the exact identity the caller
observed, or `None` for "expected to be absent" — and there is no third mode: an occupied destination nobody
admitted is `destination_occupied` rather than replaced, and a named-but-absent destination is `destination_stale`
rather than a silent fresh install. `expected_repository_id` is optional and only narrows.

**The one vocabulary addition is the narrowest member of the whole refusal union.** `invalid_export` exists
because the portable artifact is the only input on any of these paths that can be **malformed as a document** —
an unknown envelope field, a missing manifest key, a repeated JSON key, a row whose fields are not the declared
columns in declared order, a value the declared type cannot hold, or a text that is not the canonical rendering of
the document it holds — which is this route's own recorded rule ("a code is a vocabulary decision, not a
raise-site convenience") at its sharpest. `unsupported_schema`, `duplicate_identity`, `invalid_reference` and
`destination_occupied` are shared with the paths where the failure is the same fact. The two operations are
separate for the same reason the merge pair is: an export answers "what is this dataset, logically" and an import
answers "may this artifact become a dataset here".

**One convention is worth stating here because it is a deliberate non-change:** `models/knowledge/__init__.py`
does **not** re-export the portable (or merge) vocabulary, so a consumer reaches it as
`agents_remember.models.knowledge.portable` — the shape the merge vocabulary already follows.

| Finding | Anchor | Source |
| --- | --- | --- |
| The portable sub-route module, its three splits and its deliberately absent verdict. | `ExportRequest`; `ImportRequest`; `PortableValidation`; `ExportResult`; `ImportResult` | mcp/src/agents_remember/models/knowledge/portable.py:36-44; mcp/src/agents_remember/models/knowledge/portable.py:47-63; mcp/src/agents_remember/models/knowledge/portable.py:66-98; mcp/src/agents_remember/models/knowledge/portable.py:101-133; mcp/src/agents_remember/models/knowledge/portable.py:136-176 |
| The one code and the two operations this leaf added to the shared vocabulary. | `KnowledgeRefusalCode`; `KnowledgeOperation` | mcp/src/agents_remember/models/knowledge/result.py:36-78; mcp/src/agents_remember/models/knowledge/result.py:82-147 |
| The five factories that produce the portable boundary's codes. | `invalid_export_refusal`; `non_canonical_export_refusal`; `unsupported_schema_refusal`; `destination_occupied_refusal`; `destination_absent_refusal`; `import_validation_failed_refusal` | mcp/src/agents_remember/memory/knowledge/export_refusals.py:26-50; mcp/src/agents_remember/memory/knowledge/export_refusals.py:53-75; mcp/src/agents_remember/memory/knowledge/export_refusals.py:78-102; mcp/src/agents_remember/memory/knowledge/export_refusals.py:105-126; mcp/src/agents_remember/memory/knowledge/export_refusals.py:129-148; mcp/src/agents_remember/memory/knowledge/export_refusals.py:151-172 |
| The encoder and reader this vocabulary describes. | `parse_export`; `validate_export`; `encode_export` | mcp/src/agents_remember/memory/knowledge/export_portable.py:490-543; mcp/src/agents_remember/memory/knowledge/export_portable.py:667-712; mcp/src/agents_remember/memory/knowledge/export_portable.py:276-301 |
| The nodes that hold the round trip and the no-promotion rule to this vocabulary. | "test_a_populated_dataset_round_trips_to_an_equal_logical_dataset"; "test_accepted_origin_state_crosses_as_data_and_is_not_promoted" | mcp/tests/test_knowledge_portable_roundtrip.py:401-470; mcp/tests/test_knowledge_portable_roundtrip.py:473-486 |

## 260915-KS-L7 The Recorded-Scope Read Vocabulary

The knowledge sub-route gained its **sixteenth module**, `models/knowledge/read.py`, and three existing modules
changed: `result.py` gained one operation and six refusal codes, `base.py` gained the shared path rule
`require_plain_git_path`, and `source.py`'s anchor validator now delegates its Git-pathspec half to it. The
selective read's vocabulary holds no SQL, no Git call and no authority decision — it declares what a caller may
ask for and what a caller is told.

**Four splits are load-bearing, and each is a place a future edit could silently undo a guarantee:**

- **Seed versus selection.** The seed is a **closed discriminated union** of five kinds — `path`, `invariant`,
  `invariant_revision`, `family`, `family_revision`, one per row of the requirement's table — and it carries **no
  filter, no sort, no revision preference and no display version**, because none of those may select a record.
  The only thing that narrows a selection is an exact identity the caller named.
- **Selection versus page.** The three `primary_items_*` fields describe **one walk**: the declared selection
  total, the cumulative returned, what remains. All three travel on every page, so a one-item page cannot be read
  as a one-item scope **at any position** — not only at its first page — and `KnowledgeReadCounts` refuses its own
  arithmetic contradiction at construction.
- **Provenance versus verdict.** Every statement, role, rationale and lifecycle crosses as the authored text it
  is stored as, and **the response has no field that could hold a current-truth marker, a severity or a
  ranking**. That absence is how the requirement's *Forbidden Overreach* is enforced structurally rather than by
  discipline, and it is the property this route's "a wire vocabulary is imported from its producer" rule protects.
- **Continuing versus re-binding.** `KnowledgeReadCursor` names the exact snapshot, context, selector, policy,
  manifest and position it continues, so a cursor presentable against another dataset is refused rather than
  serving a page assembled from two revisions.

**Three model-level invariants a consumer may rely on**, each refused at construction: `KnowledgeReadPage`
refuses `has_more == enumeration_complete` or a `has_more` that disagrees with the presence of a continuation
(**a truncated page cannot be presentable as complete**); `KnowledgeReadCounts` refuses
`returned + remaining != total`; and `KnowledgeReadResult` refuses to be both a page and a refusal, or neither.

**The read context is the whole admission one read has,** and it enforces two rules at construction: the selected
snapshot must belong to the named repository namespace, and source resolution needs **both** `repository_root` and
`code_tree_id`. A half-specified resolution is refused rather than answered with `not_requested`, because that
would report a caller's mistake as a fact about a recorded anchor. **`task_ref=None` is a supported state and not
a degraded one** — a baseline read during planning needs no leaf, an enclosure or a fabricated task.

**The vocabulary additions are the ones only a bounded, continuable selection can reach:** the operation
`read_knowledge_scope` (one rather than two, because a seed and a continuation are two ways of asking one
question and a caller branches on the refusal code, not on which of the two it passed) and six codes —
`selector_absent`, `registration_absent` (the two **absences**, separated by which question the caller got wrong,
and neither a verdict of "no semantic impact"), `page_budget_too_small` (the selection is valid and one
indivisible item does not fit; the position is unchanged), `continuation_binding_mismatch` (**no partial page**),
`snapshot_unavailable` (which is also what a schema generation this build cannot read surfaces as, so the read
does **not** use `unsupported_schema`) and `selection_incomplete` (no total, no partial manifest). Measured, the
unions are **twenty-five operations and forty-four refusal codes**.

**One deliberate difference from the two preceding leaves is worth recording here.**
`models/knowledge/__init__.py` does **not** re-export the portable or merge vocabularies, but it **does**
re-export the read vocabulary and lists every one of its names in `__all__` — so a consumer may reach the read
shapes from either `agents_remember.models.knowledge` or `agents_remember.models.knowledge.read`.

**The path rule is shared, and that is the reason `base.py` is in this change set.** `require_plain_git_path`
refuses Git pathspec **magic** — the leading-`:` family — while **admitting `*`, `?` and `[`**, which `ls-tree`
addresses as literal characters (measured on `git 2.54.0`). Both typed path boundaries call it, so a spelling the
write path refuses cannot be presented as a seed that is answered with an absence. The card for
`models/knowledge/base.py` carries the measured table.

| Finding | Anchor | Source |
| --- | --- | --- |
| The read sub-route module: the closed seed union, the context, the page and the cursor. | `KnowledgeReadSeed`; `PathSeed`; `KnowledgeReadContext`; `KnowledgeReadPage`; `KnowledgeReadCursor` | mcp/src/agents_remember/models/knowledge/read.py:204-213; mcp/src/agents_remember/models/knowledge/read.py:144-171; mcp/src/agents_remember/models/knowledge/read.py:216-263; mcp/src/agents_remember/models/knowledge/read.py:451-482; mcp/src/agents_remember/models/knowledge/read.py:514-531 |
| **The corrected count model and the truncated page that cannot claim completeness.** | `KnowledgeReadCounts`; `KnowledgeReadPage` | mcp/src/agents_remember/models/knowledge/read.py:404-448; mcp/src/agents_remember/models/knowledge/read.py:451-482 |
| The one operation and six codes this leaf added to the shared vocabulary. | `KnowledgeOperation`; `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:36-78; mcp/src/agents_remember/models/knowledge/result.py:82-147 |
| **The shared Git-pathspec rule, with `*`, `?` and `[` admitted as literal characters.** | `require_plain_git_path` | mcp/src/agents_remember/models/knowledge/base.py:59-92 |
| The write path's delegation of its pathspec half to that one rule. | `SourceAnchorDraft` | mcp/src/agents_remember/models/knowledge/source.py:82-127 |
| **The facade's ninth source, which this leaf did add to `__all__`.** | `KNOWLEDGE_READ_POLICY_VERSION` | mcp/src/agents_remember/models/knowledge/__init__.py:71-71 |
| The cursor decoder the read re-exports through the facade. | `continue_from_cursor` | mcp/src/agents_remember/models/knowledge/read.py:582-588 |
| The cursor encoder the read re-exports through the facade. | `cursor_for` | mcp/src/agents_remember/models/knowledge/read.py:561-579 |
| The nodes that hold these models to their own invariants. | "test_a_truncated_page_states_that_items_remain_rather_than_claiming_completeness"; "test_a_page_budget_of_one_item_still_advertises_the_second_location" | mcp/tests/test_knowledge_read_scope.py:838-871; mcp/tests/test_knowledge_read_scope.py:547-657 |

## 260915-KS-L8 The Comparison Vocabulary

The knowledge sub-route gained its **seventeenth module**, `models/knowledge/diff.py`, and `result.py` gained
**one** operation — `diff_knowledge_scope` — and **no refusal code at all**, so the measured unions are
**twenty-six operations and forty-four codes** (L8 is the first knowledge leaf whose boundary needed no new
refusal vocabulary, and that is recorded as a fact rather than a silence: the comparison's whole failure
surface is R07's own six codes plus `selected_input_unavailable`, and a one-sided absence travels as a value
beside the page rather than as a seventh code). The module declares what a comparison may ask and what a
caller is told; it holds no SQL, no Git resolution and no authority decision.

**Four split lines are the contract, and each is a place a future edit could silently undo a guarantee:**

- **Two snapshots, one selector policy, and no field that could carry a second one.** `KnowledgeDiffSide`
  carries the exact snapshot and an *optional* selector that **replaces** the request's seed for that side
  only — the packet's *"an explicit revision selector may address different before/after revision IDs"* as a
  value. The request has **no field** that could express a computed relevance, a ranking or an inferred
  impact, so the forbidden second relevance rule is not representable here. The one production path this
  reaches is `SelectionQuery.seed_override`, documented on the memory route's overview and in the
  sub-route's own modules — a parameterisation of R07's single rule, **not** a second rule.
- **Provenance versus verdict.** `KnowledgeDiffSourceChange` carries the two sides' observations and four
  booleans about which object moved, and **nothing that could hold a severity, a "strengthens", a "harmless"
  or a neutrality finding**. The record's own field changes are a separate collection on the item, so a
  source-only change cannot read as a changed obligation — the packet's second non-conforming example made
  structurally impossible rather than merely avoided.
- **Absence versus selection.** `DiffCoverage` keeps `present_outside_selection` apart from
  `absent_from_snapshot`, and `SideAbsence` carries one side's own typed absence **beside** the page rather
  than replacing it, because a comparison can legitimately find that one side holds nothing for the selector
  while the other holds records.
- **A comparison's cursor is not a read's cursor.** `continue_diff_from_cursor` is a separate decoder for a
  separate document: a read cursor positions a page in one selection and a comparison cursor positions one in
  a union of two, so presenting either to the other operation is a caller's mistake and both refuse it by
  name.

**Three model-level invariants a consumer may rely on**, each refused at construction: `KnowledgeDiffPage`
refuses `has_more == enumeration_complete` or a `has_more` disagreeing with the presence of a continuation
(**a truncated comparison cannot be presentable as complete**); `KnowledgeDiffCounts` refuses its own
arithmetic contradiction **and** a display/suppression total larger than the comparison; and
`KnowledgeDiffResult` refuses to be both a page and a refusal or neither, and **refuses a declared limitation
that disagrees with its omissions in either direction** — while `no_semantic_assessment_performed` is
unconditional.

**The closed vocabularies and the one member that was removed.** `DiffItemKind` (five), `DiffCoverage`
(five), `DiffRecordTransition` (six, whose `superseding`/`superseded` pair is recognised **only** from the
authored predecessor edge — never a label, a display version or an insertion order), `DiffOmissionReason`
(three) and `DiffLimitation` (four) are literals rather than free text. `assessment_beyond_this_increment`
was declared and then **removed** in fix round 1 because nothing in the package constructed it and no
limitation advertised it: a reason with no producer is dead vocabulary in a table the validator checks in
both directions. `KNOWLEDGE_DIFF_FIELD_NAMES` is the nine compared record fields in declared order, with
`selection_reasons` deliberately absent — which route of a selection reached a record is a fact about a
traversal, not about the record.

**One deliberate non-change to the facade.** `models/knowledge/__init__.py` does **not** re-export the
comparison vocabulary, exactly as it does not re-export the portable or merge vocabularies — a consumer names
`agents_remember.models.knowledge.diff`, and the module is not in the facade change set.

| Finding | Anchor | Source |
| --- | --- | --- |
| The comparison sub-route module: the two sides, the request, the item, the page and the result. | `KnowledgeDiffSide`; `KnowledgeDiffRequest`; `KnowledgeDiffItem`; `KnowledgeDiffPage`; `KnowledgeDiffResult` | mcp/src/agents_remember/models/knowledge/diff.py:182-205; mcp/src/agents_remember/models/knowledge/diff.py:245-253; mcp/src/agents_remember/models/knowledge/diff.py:318-354; mcp/src/agents_remember/models/knowledge/diff.py:475-498; mcp/src/agents_remember/models/knowledge/diff.py:501-570 |
| **The record half and the source half, with no field that could hold a verdict and `missing_side` as a reason rather than a third change statement.** | `KnowledgeDiffSourceChange` | mcp/src/agents_remember/models/knowledge/diff.py:288-315 |
| **The binding and the digest derived from it, which is how a candidate change invalidates a continuation by construction.** | `KnowledgeDiffBinding`; `diff_binding_digest` | mcp/src/agents_remember/models/knowledge/diff.py:256-274; mcp/src/agents_remember/models/knowledge/diff.py:277-285 |
| **The counts that keep the comparison total and the display total apart, and the two closed vocabularies.** | `KnowledgeDiffCounts`; `DiffCoverage`; `DiffRecordTransition` | mcp/src/agents_remember/models/knowledge/diff.py:432-460; mcp/src/agents_remember/models/knowledge/diff.py:118-131; mcp/src/agents_remember/models/knowledge/diff.py:133-140 |
| The expansion as a value, with the attributed and unattributed changed paths kept apart. | `KnowledgeDiffExpansion` | mcp/src/agents_remember/models/knowledge/diff.py:406-429 |
| **The comparison's own cursor and its two functions, deliberately not the read's decoder.** | `KnowledgeDiffCursor`; `diff_cursor_for`; `continue_diff_from_cursor` | mcp/src/agents_remember/models/knowledge/diff.py:573-586; mcp/src/agents_remember/models/knowledge/diff.py:589-605; mcp/src/agents_remember/models/knowledge/diff.py:608-621 |
| **The one operation this leaf added, and the unchanged code union.** | `KnowledgeOperation`; `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:36-78; mcp/src/agents_remember/models/knowledge/result.py:82-147 |
| **The node that measures the absent verdict over the serialized response, and the node that holds the two change statements apart.** | "test_no_field_of_a_comparison_can_carry_a_strengthening_or_harmlessness_verdict"; "test_the_two_change_statements_are_separate_fields_and_neither_implies_the_other" | mcp/tests/test_knowledge_diff_boundaries.py:481-507; mcp/tests/test_knowledge_diff_boundaries.py:510-540 |
| The nodes that hold the page and result invariants: the truncated comparison and the unestablished limitation. | "test_a_truncated_comparison_cannot_be_presented_as_a_complete_one"; "test_a_comparison_that_declares_a_limit_it_did_not_establish_fails_construction" | mcp/tests/test_knowledge_diff_scope.py:678-739; mcp/tests/test_knowledge_diff_scope.py:603-675 |


## 260915-KS-L10 The Route Operations, And The Envelope's Refusal

This leaf added vocabulary, not a new sub-route, and the additions are exactly the two an operable `Route`
needs. `models/knowledge/result.py`'s `KnowledgeOperation` literal gained **`author_route`** and
**`set_governing_route`** — `routes.py` had been borrowing `create_invariant_revision` as the operation its
refusals named, so a caller acting on a route refusal was told an invariant-revision operation failed. The
refusal vocabulary itself did **not** grow: inadmissible record payloads are refused with the already-shipped
**`invalid_payload`** code, because "the payload you supplied is not this kind's shape" is the same fact the
envelope seam needs and no narrower code could say it better. The route rules reuse the shipped
`invalid_reference`, `missing_expected_row` and `lineage_cycle` codes for a non-confined path, an unauthored
route or parent, and a cycle respectively, and `relationship_constraint` for a second governing route on an
already-governed row.

The deliberately absent vocabulary is as load-bearing as the additions: there is **no** `Route` model in this
sub-route and no `route_schema`-style declaration, because the three generation-2 tables
(`route`, `knowledge_record`, `record_revision`) are declared by `memory/knowledge/schema_v2.py` as pinned DDL
and the route operations take frozen request dataclasses (`RouteDraft`, `GoverningRouteDraft`) rather than
pydantic models. Nothing here became a second identity authority: no field on any model in this sub-route
carries a route's identity as a fingerprint.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two operations the route write layer added, so a route refusal names a route operation. | `author_route`; `set_governing_route` | mcp/src/agents_remember/models/knowledge/result.py:36-96 |
| The shipped code an inadmissible record payload is refused with — reused rather than widened, and re-cited by hand against the current tree. | `invalid_payload` | mcp/src/agents_remember/models/knowledge/result.py:134-134; mcp/src/agents_remember/models/knowledge/result.py:117-117 |
| The route rules' refusal shapes and the frozen request objects they report on. | `normalize_route_path`; `set_governing_route` | mcp/src/agents_remember/memory/knowledge/routes.py:76-90; mcp/src/agents_remember/memory/knowledge/routes.py:398-480 |

## 260915-KS-L11 The Authored-Judgment Vocabulary

The knowledge sub-route gained its **eighteenth and nineteenth modules** — `models/knowledge/facet.py`
and `models/knowledge/facet_read.py` — and the widening of the operation's own vocabulary in
`models/knowledge/candidate.py` and `models/knowledge/result.py`: **eighteen command kinds** (the shipped
twelve plus six facet commands), **six new operations** and **no new refusal code**:
`facet.py` added no code of its own, and every failure the write path reports reuses a shipped one
(`invalid_payload`, `invalid_reference`, `missing_expected_row`, `stale_precondition`,
`promotion_not_supported`, `lineage_cycle`, `unsupported_schema`) — all seven **reused unchanged**, and the
four factories the leaf added were mechanisms under codes the vocabulary already declared. The six
facet acts joined `KnowledgeOperation`, so the operation union stands at **thirty-five members** while the
refusal-code union stays at **forty-four**.

**One closed list is the whole vocabulary, and everything else is derived from it.** `FACET_KINDS` is the
eight subtypes; `FacetKind` is the same eight spellings; one frozen payload model per subtype carries that
subtype's minimum meanings; `FacetPayload` is the discriminated union whose member set is exactly the eight;
and `FACET_RECORD_SCHEMAS` derives `facet-<kind>/v1` from the kind. A ninth subtype has **no member to
resolve to**, so it cannot be stored as a generic facet — it becomes the typed `invalid_payload` refusal at
the envelope seam, which is also why `AddFacet` carries its payload as a mapping: validating it in the
command would turn that refusal into a parse error.

**Three splits are load-bearing, and each is a place a future edit could undo a guarantee:**

- **Authored content versus provenance.** No payload field can be read as, or substituted for, the record's
  authorship: a decision's `decider` is content *about who decided*, there is no field for `actor_ref`,
  `authorization_ref`, `operation_id` or `recorded_at`, and `extra="forbid"` is what refuses a payload that
  arrives carrying one.
- **Guidance versus verdict.** `DiagnosticGuidancePayload` requires an interpretation **and** the limit of
  that interpretation, and carries no field that could hold an assessment, a compatibility verdict, a
  severity or an endorsement — for any of the eight subtypes.
- **Recorded designation versus derived currency.** `ExplanationRecord.current_revision_id` is the
  designation the record *stores*; `None` is the fact "no designation recorded" rather than a fallback to
  the newest revision, and no field of the read vocabulary could be read as "latest".

**The two closed sets this module declares are deliberately separate declarations.** The four attachment
endpoint kinds and the two explanation subject kinds spell two names identically because both name the same
canonical table, but they are separate constants and separate typed unions: an attachment's endpoint set and
an explanation's subject set are two closed sets that could diverge, and sharing a literal would hide it.
The **route is deliberately absent from the endpoint set** — the route association is the envelope's own
`governing_route_id`, and a second route mechanism here would be the competing one the design forbids.

**One precision the union does not carry, stated so it is not inferred:** `AddFacet.facet_kind` is a
length-bounded `str` rather than the `FacetKind` literal, so the *command* accepts any nonempty kind name
and the closure is enforced one seam later. That is the deliberate trade above, not an oversight — but a
reader should not conclude the ninth subtype is unconstructible at the command.

**One deliberate non-change to the facade.** `models/knowledge/__init__.py` does **not** re-export this
vocabulary, exactly as it does not re-export the portable, merge or comparison vocabularies — a consumer
names `agents_remember.models.knowledge.facet` or `...facet_read`, and neither module is in the facade
change set.

| Finding | Anchor | Source |
| --- | --- | --- |
| The one closed list and the declarations derived from it. | `FACET_KINDS`; `FacetPayload`; `FACET_RECORD_SCHEMAS` | mcp/src/agents_remember/models/knowledge/facet.py:68-77; mcp/src/agents_remember/models/knowledge/facet.py:183-193; mcp/src/agents_remember/models/knowledge/facet.py:209-211 |
| **The six authored commands and the union they join, which is the operation's widened reach.** | `FacetCommand`; "ProposedCommand = Annotated[" | mcp/src/agents_remember/models/knowledge/candidate.py:469-493; mcp/src/agents_remember/models/knowledge/facet.py:492-500 |
| **The standalone request and the receipt that carries no approval, endorsement or judgement field.** | `FacetWriteRequest`; `FacetWriteResult` | mcp/src/agents_remember/models/knowledge/facet.py:512-529; mcp/src/agents_remember/models/knowledge/facet.py:560-585 |
| **The facet selection's own policy, the complete-or-refused bound and the page whose completeness is not a settable flag.** | `FACET_SELECTION_POLICY_VERSION`; `FACET_SELECTION_ITEM_LIMIT`; `FacetReadPage` | mcp/src/agents_remember/models/knowledge/facet_read.py:56-56; mcp/src/agents_remember/models/knowledge/facet_read.py:61-61; mcp/src/agents_remember/models/knowledge/facet_read.py:332-354 |
| The two seed kinds and the six item kinds as closed unions. | `FacetReadSeed`; `FacetReadItem` | mcp/src/agents_remember/models/knowledge/facet_read.py:182-185; mcp/src/agents_remember/models/knowledge/facet_read.py:241-249 |
| The eight subtypes' payload models and the two nonempty-tuple meanings. | `ScenarioPayload`; `LimitationPayload` | mcp/src/agents_remember/models/knowledge/facet.py:132-143; mcp/src/agents_remember/models/knowledge/facet.py:146-152 |
| **The nodes that hold the closure, the per-subtype refusals and the receipt's absent verdict fields.** | "test_the_seam_registry_is_exactly_the_eight_declared_subtypes"; "test_a_facets_authorship_lifecycle_and_receipt_are_stored_data_with_no_verdict" | mcp/tests/test_knowledge_facets.py:181-227; mcp/tests/test_knowledge_facets.py:306-343 |
| **The six operations this leaf added to the shared vocabulary, and the unchanged code union.** | `KnowledgeOperation`; `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:36-90; mcp/src/agents_remember/models/knowledge/result.py:82-147 |

## 260915-KS-L14 The Detection Vocabulary, And The Two Operations It Adds

The knowledge sub-route gained its **twentieth module** — `models/knowledge/detection.py` — and the
shared served vocabulary grew by **two operations and one refusal code**: `record_detection_run` and
`read_detection_run` join `KnowledgeOperation`, and `detection_self_reference` joins
`KnowledgeRefusalCode`. The operation union therefore stands at **thirty-seven members** and the code
union at **forty-five**. Two members rather than one, for the reason the read pair and the diff pair are
one each: recording a run and reading one back are different acts, and the read is the one that must
answer with the recorded order rather than with whatever order rows come back in.

**No field of either record can hold a conclusion, and the absence is declared rather than inferred.**
The module's whole vocabulary is built so that a severity, an assessed priority, a conflict or
compatibility verdict, a causal explanation, a harmlessness label and an authored finding are
**unrepresentable**: `CONCLUSION_BEARING_FIELD_NAMES` is one closed list of those concepts and
`conclusion_bearing_fields` is a total, mechanical **review of a model's declared field set** — it reads
`model_fields`, not an instance, so a field is reported whether or not any payload populates it. The
shipped base's `extra="forbid"` refuses a payload that supplies one; `observed_basis_detail` refuses a
verdict written into the prose field by requiring `detail` to *equal* the rendering of the record's own
recorded basis. Both records also carry the unconditional `no_semantic_assessment_performed` limitation,
so the absence is a stated fact rather than something a reader infers from a missing field.

**The closed vocabularies are declared as a `Literal` and as a tuple, and a case asserts they agree.**
`DetectionCondition` / `DETECTION_CONDITIONS` (the five declared conditions), `DeclaredInputSet` /
`DECLARED_INPUT_SETS` (the three readings), `DetectionChangeGranularity`, `DetectionScopeStatus`,
`DetectionLimitation` / `DETECTION_LIMITATIONS` and `MANIFEST_DESTINATION_KINDS`. Three published
identities travel with them: `DETECTION_POLICY_VERSION` (the detection contract's name, in the shipped
constant idiom), `CONDITION_VOCABULARY_VERSION` (the vocabulary versioned with the policy, so a condition
the policy does not declare is refused *with the version it was refused against*), and
`DETECTION_EXTRACTOR_VERSION` — **authored rather than imported**, because the shipped anchor resolver has
no symbol extractor and returns `unsupported_locator`, so there was no existing constant to cite.

**The declared input set is checked against the member's own recorded discriminator, never by counting
sides.** `DetectionRecordedInputSet` enforces that `both_sides_declared` records both declared sides each
under its own selector and context and **no** counterpart-probe outcome, that `union_of_both_sides` records
both sides *and* the probe's recorded outcome per reported item, and that `trigger_side_only` records
exactly one side and no probe at all. Each refusal names the member and what was recorded instead, because
a two-sided condition reported from a one-sided read is the silent-widening shape the requirement exists
to prevent — and a `trigger_side_only` signal that *asserts* something about the unread side gets its own
refusal, since the absence of a counterpart is a scope limitation rather than a finding of equality.

**Two shapes carry what the record cannot say.** `DetectionScopeManifest.resolve` reports a reference as
`retained` only for a resolved durable-publication destination with a recorded identity, and otherwise
`unresolved` **with what would resolve it** — never as an empty manifest, and never as an error;
`DetectionManifestResolution`'s validator refuses either half without its required field.
`DetectionRunCurrentness` carries the recorded and current versions beside the state and **no signal at
all**: its `signals_unchanged` field is the literal `True`, which is the type saying that this operation
cannot rewrite what it read. `DetectionRunReproduction` carries both run identities, both ordered
sequences, every differing input and one verdict that must follow from those facts.

**The record's own field set is all-required.** `DetectionSignalPayload` carries every field requirement
1.1 lists — signal id, repository, governing route, condition, vocabulary version, declared input set,
observed changes, relationship paths, the two published versions, the scope manifest, the registered scope
status, the unmapped paths and the limitations — with the four collection fields required even though
three are frequently empty, so a signal that observed nothing *states* that rather than defaulting.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The three published identities, including the extractor version authored because no shipped constant exists to cite.** | `DETECTION_POLICY_VERSION`; `DETECTION_EXTRACTOR_VERSION`; `CONDITION_VOCABULARY_VERSION` | mcp/src/agents_remember/models/knowledge/detection.py:96-134 |
| The five declared conditions and the three declared input sets, each as the validated type beside the tuple a caller enumerates. | `DETECTION_CONDITIONS`; `DECLARED_INPUT_SETS` | mcp/src/agents_remember/models/knowledge/detection.py:124-149 |
| **The closed conclusion-name list and the declared-field-set review that makes "no conclusion is representable" checkable rather than asserted.** | `CONCLUSION_BEARING_FIELD_NAMES`; `conclusion_bearing_fields` | mcp/src/agents_remember/models/knowledge/detection.py:217-283 |
| The observed-change granularities, the declared scope status and every declareable limitation. | `DetectionChangeGranularity`; `DetectionScopeStatus`; `DETECTION_LIMITATIONS` | mcp/src/agents_remember/models/knowledge/detection.py:156-209 |
| **The declared-input-set discriminator contract: two sides and no probe, both sides and the probe, or one side and no probe.** | `DetectionRecordedInputSet` | mcp/src/agents_remember/models/knowledge/detection.py:546-632 |
| **The manifest reference and its two-state resolution, which reports an unresolvable reference with what would resolve it rather than as an empty manifest.** | `DetectionScopeManifest`; `DetectionManifestResolution` | mcp/src/agents_remember/models/knowledge/detection.py:417-543 |
| **The all-required signal field set, and the `detail`-equals-rendering rule that refuses a verdict in prose as it refuses a verdict field.** | `DetectionSignalPayload`; `observed_basis_detail` | mcp/src/agents_remember/models/knowledge/detection.py:635-753; mcp/src/agents_remember/models/knowledge/detection.py:1017-1033 |
| **The run payload: the per-signal declarations not collapsed into a run default, and the declared total order over signal identity.** | `DetectionRunPayload` | mcp/src/agents_remember/models/knowledge/detection.py:756-827 |
| **The currentness answer that carries the recorded versions beside the current ones and cannot hold a re-interpreted signal.** | `DetectionRunCurrentness` | mcp/src/agents_remember/models/knowledge/detection.py:942-987 |
| The one typed outcome per detection operation, serving its signals in the run's recorded order. | `DetectionRunResult` | mcp/src/agents_remember/models/knowledge/detection.py:990-1014 |
| **The two operations and the one refusal code this leaf added to the shared vocabulary.** | `KnowledgeOperation`; `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:36-96; mcp/src/agents_remember/models/knowledge/result.py:101-171 |
| The envelope registry every typed payload pair is registered under — four families now — and the two-kind set derived from the detection entries. | `PAYLOAD_MODELS`; `DETECTION_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:103-103; mcp/src/agents_remember/memory/knowledge/record_envelope.py:143-143; mcp/src/agents_remember/memory/knowledge/record_envelope.py:142-142 |
| **The requirement-revision family this route gained: its frozen payload vocabulary, the pair it declares in the envelope's kind vocabulary, and the kind set derived from it.** | `RequirementRevisionPayload` | mcp/src/agents_remember/models/knowledge/requirement.py:172-213 |
| The pair that family declares in the envelope's typed kind vocabulary. | `REQUIREMENT_REVISION_KIND`; `REQUIREMENT_REVISION_SCHEMA` | mcp/src/agents_remember/models/knowledge/requirement.py:80-84 |
| The kind set derived from the registry entries that pair is built from. | `REQUIREMENT_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:148-150 |
| **The recorded quotation-degree ruling, and the absence it turns on: no payload field is the operative obligation.** | "test_a_payload_carrying_an_operative_obligation_field_is_refused" | mcp/tests/test_knowledge_requirement_reference_contract.py:294-310 |
| The two operation members the requirement record group added, and the fact that no refusal code was added with them. | `record_requirement_revision`; `read_requirement_revisions` | mcp/src/agents_remember/models/knowledge/result.py:114-114; mcp/src/agents_remember/models/knowledge/result.py:113-113 |
| **The cases that hold the field-set review, the three declared input sets and the retention answer.** | "test_the_signal_field_set_is_required_and_carries_no_conclusion_bearing_field"; "test_the_declared_input_set_vocabulary_is_exactly_three_members_each_with_its_own_discriminator"; "test_a_manifest_may_not_be_reported_retained_at_a_destination_that_cannot_retain_it" | mcp/tests/test_knowledge_detection_signals.py:185-222; mcp/tests/test_knowledge_detection_signals.py:346-360; mcp/tests/test_knowledge_detection_signals.py:527-569 |
| The eight graph operations and the anchor-endpoint union the request vocabulary gained, each cited at its own declaration. | `AnchorReference`; `AnchorEndpoint`; `NewAnchor`; `CreateRealizationClaimResult` | mcp/src/agents_remember/models/knowledge/result.py:300-316; mcp/src/agents_remember/models/knowledge/result.py:307-315; mcp/src/agents_remember/models/knowledge/result.py:483-498; mcp/src/agents_remember/models/knowledge/result.py:327-327; mcp/src/agents_remember/models/knowledge/result.py:316-316; mcp/src/agents_remember/models/knowledge/result.py:326-326; mcp/src/agents_remember/models/knowledge/result.py:343-343; mcp/src/agents_remember/models/knowledge/result.py:325-325; mcp/src/agents_remember/models/knowledge/result.py:332-332; mcp/src/agents_remember/models/knowledge/result.py:508-508 |
| The envelope registry key pair each detection payload is registered under, and the two-kind set derived from it. | `PAYLOAD_MODELS`; `DETECTION_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:86-127; mcp/src/agents_remember/memory/knowledge/record_envelope.py:144-144; mcp/src/agents_remember/memory/knowledge/record_envelope.py:143-143; mcp/src/agents_remember/memory/knowledge/record_envelope.py:142-142 |

## Update History
- 2026-09-18T06:09:03+00:00: Generated citation repair: `REQUIREMENT_RECORD_KINDS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:148-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 014df62463362d92ea768ade7d81f0ca0b615347d5c6feed94e130d80244a24d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:06:32+00:00: Generated citation repair: `CreateRevisionResult` repointed to mcp/src/agents_remember/models/knowledge/result.py:404-421. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:06:32+00:00: Generated citation repair: `SetInvariantLabelResult` repointed to mcp/src/agents_remember/models/knowledge/result.py:570-590. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: `invalid_payload` repointed to mcp/src/agents_remember/models/knowledge/result.py:117-117. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: `REQUIREMENT_RECORD_KINDS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:149-151. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:50+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **recorded the requirement-revision payload vocabulary this route gained, corrected the registry row it made stale, and retired the card's generated projection bullets by hand.** The route's registry row described the envelope registry as the place *detection* payloads are registered and paired it with a derived set at a range the module's growth had moved; it now states the registry as the four-family seam it is (`:93-113`), keeps the detection set at its own declaration (`:124`), and three rows are added: the requirement family's frozen payload vocabulary with the pair it declares and the kind set derived from it, the **recorded quotation-degree ruling with the absence it turns on** (no payload field is the operative obligation, asserted falsifiably at the payload plane), and the two `KnowledgeOperation` members this leaf added together with the fact that **no refusal code was added with them** — recorded as a fact rather than left to a diff, because 'this leaf needed no new vocabulary' and 'this leaf's vocabulary was never reviewed' must not read alike. Three generated projection bullets were retired after their claims were re-read: `AnchorEndpoint`/`NewAnchor`/`AnchorReference`/`CreateRealizationClaimResult` (whose ranges were a projection of the graph request and result models), `invalid_payload` (re-cited at the refusal literal), and the detection registry pair above. Verification metadata advances to the leaf's base commit `e963a01c` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T06:50+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): **re-read the `__all__` claim against the declaration as it now stands, re-cited it by hand to `mcp/src/agents_remember/models/knowledge/__init__.py:160-288` (the declaration's own extent), and removed the generated projection bullet that had rewritten its range mechanically.** The claim was retained rather than softened: the re-export list is still the served knowledge vocabulary, and this leaf is what extended it with the composition vocabulary, so the range that evidences the claim is the declaration itself. A mechanically projected range is unverified evidence, and an agent has now read the declaration it points at.
- 2026-09-18T06:35+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 2 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: ``AnchorEndpoint`; `NewAnchor`; `AnchorReference`; `CreateRealizationClaimResult`` → `mcp/src/agents_remember/models/knowledge/result.py:319-322; mcp/src/agents_remember/models/knowledge/result.py:308-316; mcp/src/agents_remember/models/knowledge/result.py:301-305; mcp/src/agents_remember/models/knowledge/result.py:484-498`; ``invalid_payload`` → `mcp/src/agents_remember/models/knowledge/result.py:110-110`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): added the **citation-binding vocabulary and projection rule** section — the route's twenty-first and twenty-second knowledge modules and the two operations they contribute — and **moved the two counts this route states as facts**: the operation union is **thirty-nine** rather than thirty-seven (the L14 section said thirty-seven and is corrected in place, not superseded by a later paragraph that would leave a stale number above it), while the code union stays at **forty-five**, and the new section says so explicitly for this leaf rather than leaving a reader to derive it. The section records the two decisions a reader must not get wrong. First, **the binding carries no content address, digest or fingerprint**: its four authored facts are the owner revision (referenced, not minted — the recorded Git blob identity the memory side already supplies), the key as written, the typed target reference and the shipped locator, and ambiguity is therefore decided by equality over the **recorded key text** rather than by a computed digest. Second, **the vocabulary extends the shipped one in one direction only**: four of the nine states are literally `ANCHOR_RESOLUTIONS` members and `AnchorResolutionState` gains no member, so an anchor resolution can never acquire a citation fact. It also records the declared key-form coverage (an unread form is a counted state, not a gap), the counts validator that refuses a report whose per-state counts do not partition the declared set, the absent semantic-completeness field, and the projection rule's three enforced consequences — including that an unassessed claim is `None` rather than an empty instance. Every citation range in this overview was re-read against the current source; the ones this leaf moved were corrected by hand in the same pass and no generated bullet is left enforcing a claim on this document's account.

- 2026-09-18T05:15+02:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): added the **detection vocabulary** section — the route's twentieth knowledge module and the two operations plus one refusal code it contributed to the shared served vocabulary — and re-read three stale rows by hand rather than letting a machine projection re-point them. The section records that neither record can hold a conclusion because the vocabulary makes the concept names unreviewable-by-construction: `conclusion_bearing_fields` reviews a model's **declared** field set, `extra="forbid"` refuses an extra field and `observed_basis_detail` refuses a verdict written into the prose field by requiring equality with the rendering of the record's own recorded basis; the three published identities, including the extractor version that is **authored because the shipped resolver has no symbol extractor to cite**; the declared-input-set discriminator contract checked against the member's own recorded facts rather than by counting sides; the manifest resolution that reports an unresolvable reference with what would resolve it and never as an empty manifest; and the currentness answer whose `signals_unchanged` literal is the type saying it cannot rewrite what it read. **Three rows were corrected against the current source**: the shared typed-contract row carried three ranges that no longer held `CreateRevisionResult` or `SetInvariantLabelResult` and is split into one anchor per row, and the `invalid_payload` row moved with the growing unions (`:96` → `:102`). Two further rows had their anchor sets split for the same reason — a cell naming several anchors across several ranges cannot resolve to one extent, which is why the repair tool declines it. Verification metadata advances to this leaf's base commit `4264dcc9` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T04:55+02:00 — 260915-KS-L11 owning seat (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read this route's union claim against the source and re-cited it by hand, replacing a generated projection.** The row and the section above it said *twelve* members; `ProposedCommand` admits **eighteen** after this leaf, which this route's own L11 section already states. Row and prose now agree with `models/knowledge/candidate.py:372-392`, so the citation is an agent's read of the declaration rather than a projected range.
- 2026-09-18T03:05+02:00 — 260915-KS-L24 curator (uncommitted change set on `ar/260915-ks-l24`, base `9c12e8b1`): **re-read the curator-coherence paragraph and the row this candidate falsified, and recorded what the tool now says.** The "publication fields are forbidden on read-only actions, while publish requires every expected source identity, predecessor digest, and declared caller" sentence described the rule the defect was made of: it names three prose categories while the two members that actually caused the refusal belong to none of them, and the shipped refusal said exactly the same thing. The paragraph now states the single `PUBLICATION_MEMBERS` declaration beside the request model, the named-missing-member refusal, the named-supplied-member sibling refusal, and the `prepare` statement that includes the two delivery identities `prepare` does not derive. The reference row's four `:189-233; :236-247; :250-256; :259-315` ranges no longer held `CuratorCoherenceRequest` (it moved to `:370-434` when the declaration was inserted above it); the row now cites **one** range over the whole coherence identity family it names, because this card's own `citation_fix` declines a multi-range cell for it (`projection_no_resolved_extent`). No other row of this 1 600-line route was re-read in this pass. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-18T01:18+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read the older union row in this route against the source and recorded a contradiction instead of softening it.** The row at `:811` reading "The closed eighteen-member union ... the eighteen kinds are the operation's entire reach" is **no longer true**, and this leaf's own section below says so: `ProposedCommand` now admits **eighteen** members (the shipped twelve plus the six facet commands) and the union row's citation was re-pointed to `372-392` accordingly. The row's *counts* were not rewritten, because a claim's meaning belongs to the owning seat rather than to the citation curator; the correction owed is `twelve` → `eighteen` in both places in that row. This entry also records where the leaf's own route-review entry lives: it was written one section too high (under `## Invariants And Boundaries`) and this round moved it into this section, where the review rail can see it. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `KnowledgeLane`; `CANDIDATE_LANES` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:99-99; mcp/src/agents_remember/models/knowledge/candidate.py:101-101. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "def context_digest" repointed to mcp/src/agents_remember/models/knowledge/candidate.py:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `ExpectedRecord` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:244-266. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `CandidateResolution` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:397-414. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `invalid_payload` repointed to mcp/src/agents_remember/models/knowledge/result.py:96-96. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T00:25+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): recorded the knowledge sub-route's **authored-judgment vocabulary** — `models/knowledge/facet.py` (the closed eight-subtype list and its derived declarations, the four closed attachment endpoints, the two closed explanation subjects, six authored commands, the standalone request and the factual receipt) and `models/knowledge/facet_read.py` (the separate selection's seeds, stored values, items, counts, page and result). The section states the measured unions (**eighteen command kinds**, the shipped twelve plus six) and the unchanged refusal code set — every failure reuses a shipped code — and the **three load-bearing splits**: authored content versus provenance (no payload field can be read as the record's authorship, and `extra="forbid"` refuses one that tries), guidance versus verdict (`DiagnosticGuidancePayload` requires an interpretation and its limit and has nowhere to put an assessment), and recorded designation versus derived currency (`current_revision_id` is stored, `None` is a fact, and no field could be read as "latest"). It records that the two closed sets are **separate declarations** so they can diverge visibly, that the route is **deliberately absent** from the endpoint set because the association is the envelope's own, the precision that `AddFacet.facet_kind` is a length-bounded string while the closure is enforced at the envelope seam, and the deliberate non-change that the facade does not re-export this vocabulary. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): **route meaning extended in one place.** This leaf added vocabulary rather than a sub-route: `KnowledgeOperation` gained `author_route` and `set_governing_route`, because `routes.py` had been borrowing `create_invariant_revision` as the operation its refusals named. The body records the refusal vocabulary's deliberate **absence** of growth — an inadmissible record payload reuses the already-shipped `invalid_payload` code, and the route rules reuse `invalid_reference`, `missing_expected_row`, `lineage_cycle` and `relationship_constraint` — and the equally deliberate absence of any `Route` model or schema declaration here, since the generation-2 tables are pinned DDL and the route operations take frozen request dataclasses. No model in this sub-route carries route identity as a fingerprint, so nothing became a second identity authority. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T07:33:51+00:00: Generated citation repair: `AnchorEndpoint`; `NewAnchor`; `AnchorReference`; `CreateRealizationClaimResult` repointed to mcp/src/agents_remember/models/knowledge/result.py:284-287; mcp/src/agents_remember/models/knowledge/result.py:273-281; mcp/src/agents_remember/models/knowledge/result.py:266-270; mcp/src/agents_remember/models/knowledge/result.py:449-463. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "class WorktreeRecordLandingResponse(WorktreeCommandResponse):" repointed to mcp/src/agents_remember/models/worktree.py:478-478. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "from agents_remember.models.worktree import (" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:9-9. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "class LifecycleOperationRecord(BaseModel):"; "class LifecycleOperationProjection(StrictResponseModel):" repointed to mcp/src/agents_remember/models/lifecycles/operation.py:340-340; mcp/src/agents_remember/models/lifecycles/operation_projection.py:340-340. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "test_a_logical_no_op_retains_the_published_bytes" repointed to mcp/tests/test_knowledge_snapshot_publication.py:239-239. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `AnchorEndpoint` in the row 769 of this card from mcp/src/agents_remember/models/knowledge/result.py:273-274 to mcp/src/agents_remember/models/knowledge/result.py:284, the extent of the construct the claim is about (the checker named line(s) [284, 295] as its live location); re-pointed `AnchorReference` in the row 769 of this card from mcp/src/agents_remember/models/knowledge/result.py:284 to mcp/src/agents_remember/models/knowledge/result.py:266, the extent of the construct the claim is about (the checker named line(s) [266, 285] as its live location); re-pointed `KnowledgeOperation` in the row 814 of this card from mcp/src/agents_remember/models/knowledge/result.py:66-115 to mcp/src/agents_remember/models/knowledge/result.py:36, the extent of the construct the claim is about (the checker named line(s) [36, 152, 349] as its live location); re-pointed `KnowledgeOperation` in the row 863 of this card from mcp/src/agents_remember/models/knowledge/result.py:66-115 to mcp/src/agents_remember/models/knowledge/result.py:36, the extent of the construct the claim is about (the checker named line(s) [36, 152, 349] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `AnchorReference` in the row 769 of this card from mcp/src/agents_remember/models/knowledge/result.py:449-450 to mcp/src/agents_remember/models/knowledge/result.py:266-267, the extent of the construct the claim is about (the checker named line(s) [266, 285] as its live location); re-pointed `NewAnchor` in the row 769 of this card from mcp/src/agents_remember/models/knowledge/result.py:266-267 to mcp/src/agents_remember/models/knowledge/result.py:273-274, the extent of the construct the claim is about (the checker named line(s) [273, 285] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `AnchorReference` in the row 769 of this card from mcp/src/agents_remember/models/knowledge/result.py:273-274 to mcp/src/agents_remember/models/knowledge/result.py:266-267, the extent of the construct the claim is about (the checker named line(s) [266, 285] as its live location); re-pointed `CreateRealizationClaimResult` in the row 769 of this card from mcp/src/agents_remember/models/knowledge/result.py:266-267 to mcp/src/agents_remember/models/knowledge/result.py:449-450, the extent of the construct the claim is about (the checker named line(s) [449, 461] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/src/agents_remember/models/knowledge/result.py:449-450 in the row 769 of this card; the repetition added no pooled evidence
- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): recorded the knowledge sub-route's **seventeenth module**, `models/knowledge/diff.py`, and the **one** operation `result.py` gained — with **no new refusal code**, which the card states as a fact rather than a silence (the comparison's failure surface is R07's six codes plus `selected_input_unavailable`, and a one-sided absence is a value beside the page, not a seventh code). The section states the **four split lines** a future edit must not undo: two snapshots with **one** selector policy and no field able to express a second relevance rule (the per-side selector as the packet's *"different before/after revision IDs"* expressed as a value); provenance versus verdict, where a source-only change cannot read as a changed obligation because the record's field changes are a separate collection; absence versus selection, with `present_outside_selection` kept apart from `absent_from_snapshot` and a side's absence carried **beside** the page; and a comparison cursor that is **not** a read cursor. It records the three construction-time invariants (the truncated comparison; the counts' arithmetic **and** display-total bounds; the limitation/omission check running in both directions with `no_semantic_assessment_performed` unconditional), the closed vocabularies with the **removal** of `assessment_beyond_this_increment` as a reason with no producer, the six-state transition union whose supersession pair is read **only** from the authored predecessor edge, and the deliberate non-change that the facade does **not** re-export this vocabulary. It also corrects the `result.py` citation range this card carried, because the operation insertion moved every anchor below it. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): recorded the knowledge sub-route's **sixteenth module**, `models/knowledge/read.py`, and the three changes to existing modules (one operation and six refusal codes in `result.py`; the shared path rule in `base.py`; `source.py` delegating its pathspec half to it). The card states the **four load-bearing splits** — a closed five-member seed union carrying no filter, sort, revision preference or display version; the three `primary_items_*` fields describing one **walk** so a one-item page cannot be read as a one-item scope at any position; provenance versus verdict, where **the response has no field that could hold a current-truth marker** (the requirement's *Forbidden Overreach* enforced structurally); and continuing versus re-binding — plus the three model-level invariants refused at construction and the two context rules (`task_ref=None` a supported baseline state; an all-or-nothing source resolution). It records the six new codes with the distinction each carries, the measured union sizes (twenty-five operations, forty-four codes), and one **deliberate difference** from the two preceding leaves: this package's `__init__.py` does **not** re-export the portable or merge vocabularies but **does** re-export the read vocabulary and lists it in `__all__`. It also records the shared pathspec rule with `*`, `?` and `[` admitted. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l07`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): recorded the knowledge sub-route's fifteenth module and the **portable wire vocabulary** it serves, plus the two operations and one code `models/knowledge/result.py` grew. The card states the three splits the module is built around — a required admitted identity on the export request, a validation report versus a published result neither of which can carry a verdict, and a staging fact versus a destination fact with the verified identity carried independently of the state — the closed two-mode destination admission with no third mode, and the `row_counts` over all ten tables that separates a complete export from one that dropped a collection. It records the one vocabulary addition as the **narrowest** member of the refusal union and why (the portable artifact is the only input that can be malformed *as a document*), and the deliberate non-change that this package's `__init__.py` does not re-export the vocabulary — a consumer names `models.knowledge.portable`, as the handoff tells the next leaves to. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l06`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): recorded the knowledge sub-route's fourteenth module and the **structural merge vocabulary** it serves — the explicit input that carries the identity a caller admitted, the closed two-member base claim, the coverage facts that separate "changed" from "carried an operation", the two-shape conflict record and the outcome. The card states the absence the module is built around (no field can carry a verdict, and `structurally_merged` is the entire claim), the two shapes a consumer must not flatten (`duplicate_identity` fires even on byte-identical payloads; `delete_reference_conflict` names no row because the engine supplies none and reports no count), and the two operations plus twelve refusal codes `models/knowledge/result.py` grew. The pre-existing citation rows in this card were re-derived after the L5 insertions moved every anchor below them. Verification metadata remains closeout-owned.
- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): recorded the knowledge sub-route's thirteenth module and the **local-working-object vocabulary** it serves — the candidate layout and its sealed receipt, the closed snapshot stage carrying both identities, the publication request/result pair, the publication-state measurement, and the two-member disposal union. Three absences are stated as the contract: the receipt carries **no dataset digest** (so a caller cannot hand-write the identity its publication will be compared against), the closed disposal union has no "looked disposable" member, and `authorization_ref` is **carried rather than examined** because permissibility is this layer's question and the approval chain is the caller's. The card also records the six operations and seven refusal codes `models/knowledge/result.py` grew, and restates the `no_change` distinction where the codes are actually declared — two result states are reachable, the refusal code still has no producer. Verification metadata remains closeout-owned.
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base
  `27242ecb`): recorded the knowledge sub-route's growth from eleven modules to twelve and the **write-boundary
  vocabulary** it now serves — the resolved-context-versus-authored-content split with the digest that seals it and
  the deliberately absent dataset-identity field on `CandidateResolution`, the expected-versus-assumed rule, the
  closed twelve-command union whose members make promotion, approval and arbitrary SQL unrepresentable, and the
  factual receipt whose consistency validator the operation's results must satisfy. Also recorded the two
  label-edit request/result pairs, the two candidate-boundary refusal codes (`target_not_candidate`,
  `promotion_not_supported`) and the deliberate reuse of `unauthorized_scope` for the unvalidatable task lane, with
  the carried limitation that the *refusal code* `no_change` still has no producer while the *result state* is the
  reachable vocabulary. Verification metadata remains closeout-owned.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base
  `60e0820e`): recorded the knowledge sub-route's growth from nine modules to eleven and the graph vocabulary it
  now serves (family identity and the immutable family revision; the two relations, the closed authored role
  vocabulary with its explicit `unclassified`, and the four read models), the three graph-vocabulary rules that
  are each the model-level half of a storage contract, the second payload version, and the **repaired anchor
  identity** — `SourceAnchor.anchor_id` was a `pattern`-constrained string on a `UUID` field, which made every
  anchor unconstructible, and is now a plain `UUID` with its canonical text derived at the storage boundary.
  Verification metadata remains closeout-owned.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base
  `67b21aeb`): recorded the new `models/knowledge/` vocabulary sub-route — nine modules carrying repository,
  invariant and revision identity, the sealed-payload digest, the shared provenance envelope and locator union,
  and the typed operation/refusal/result contract — with the three ownership rules (vocabulary defined where it
  decides, values not rows, identity not label) and the declared-but-absent read/diff consumer. Verification
  metadata remains closeout-owned.
- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Updated model routing and checkpoint result vocabulary; retained only informational cache exposure. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): corrected the change-set
  attribution in the renderer paragraph — the one-writer move is `260913-LCA-L4`, not L5, as the
  sibling cards and this repository's own overview record. Verification metadata remains
  closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the
  `mcp/src/agents_remember/models/` route changed since the recorded verification commit. Re-read
  the card against the frozen on-disk source and re-checked its claims and cited ranges: nothing
  this card asserts is falsified by the change, so no wording changed. Verification metadata remains
  closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): this master moved the one
  memory-content-message renderer out of `models/closeout/input.py` into
  `kernel/memory_attribution.py`. Corrected the route claim: the model method is now the
  closeout-shaped wrapper around the kernel renderer, which is the single definition, and the other
  memory-content producers call the kernel renderer directly. Verification metadata remains
  closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 4 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-13T23:21+02:00 — 260913-LCA-L2 (uncommitted change set on `ar/260913-lca-l2-ar`):
  correction to the entry below, which is kept as the record of what was true when L1 wrote it. This
  route renders the memory-content attribution but no longer owns its key: `CODE_COMMIT_TRAILER_KEY`
  is declared once in `kernel/memory_attribution.py` — the reader of the hashed object, one rank below
  `models` in `layers.toml` — and `models/closeout/input.py` imports it at `input.py:9`, so
  `grep -rn '"Code-Commit"' --include=*.py mcp/` has exactly one hit and the two-literal drift the L1
  entry's wording implied is gone. The layer contract fixes the direction: a kernel module importing a
  model would import upward. Content change; verification metadata remains closeout-owned and no
  acceptance claim is made.
- 2026-09-13T21:42+02:00 — 260913-LCA-L1 (uncommitted change set on `ar/260913-lca-l1-ar`): recorded that
  this route now owns the one rendering of the memory-content commit message —
  `models/closeout/input.py`'s `CODE_COMMIT_TRAILER_KEY` and
  `EffectiveCloseoutInput.memory_content_message(code_commit)`, the closeout's own body plus exactly one
  final-paragraph `Code-Commit: <sha>` trailer naming the code commit the same closeout landed, used by
  both closeout routes while the `memory.md`-only ledger commit keeps `message_for("ledger")` and carries
  none. Content change; verification metadata remains closeout-owned and no acceptance claim is made.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "class WorktreeRecordLandingResponse(WorktreeCommandResponse):" repointed to mcp/src/agents_remember/models/worktree.py:479-479. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "\"worktree_sync\": WorktreeSyncResponse," repointed to mcp/src/agents_remember/models/tools/tool_registry.py:186-186. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: the advertised tuple this route defines grew by one name
  (`worktree_pause`, so `PUBLIC_TOOLS` holds 63 ordered names and its extent is L22-L86) and the route
  gained one response envelope (`WorktreePauseResponse`, whose only own field is `paused`). The rest of
  the route is unchanged. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T14:21:37+02:00 — LOCR-L36 contract-scoped activation re-key: rewrote the route's activation section (retitled `## IAS Contract-Scoped Activation And Sync Vocabulary`) and the CCR-R25 paragraph to state that the activation fact, the nested activation snapshot, and the admission envelope are keyed by the addressed contract's `contractFingerprint`; recorded that `AtomicSeriesSourceRef` / `AtomicSeriesSourcePair` and the `sourcePairFingerprint` field are gone, that `AtomicSeriesAdmission` lost `classification` / `sourcePair*` / `blocking`, and that `AtomicSeriesAdmissionBlocking` was deleted so a foreign master is never a blocker. Added the `## 260831-LOCR-L36 The Activation Vocabulary Becomes Contract-Scoped` route-impact section with the exact declared line map. Rebound the 12 citations that shifted when `models/worktree.py` shrank from 533 to 514 lines: the next-move triple 322-328, `_require_registered_public_next_tool` 355-364, `WorktreeRecordLandingResponse` 466, `WorktreeCheckpointLandingResponse` 458, `WorktreeStatusWaitResponse` 392, `WorkflowKind` 29-40, `WorktreePhase` 40, `NextOperation` 50, `NextTool` 59 and the `NextTool` literal range 59-73. No verification stamp advanced.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:15+00:00 — 260831-LOCR-L34: recorded on this route that `NextTool` gained
  `worktree_checkpoint_landing` while `NextOperation` was deliberately left unchanged (pausing a
  master is the existing `request_integration_decision` intent, not a phase), and pointed to the
  `models/worktree.py` card for the reasoning and to the `worktrees/overview.md` route for the
  preview/apply parity invariant behind the repair. Content change, not a range repoint; verification
  metadata remains closeout-owned and no acceptance claim is made.
- 2026-09-13T08:49:05+00:00: Generated citation repair: "class WorktreeRecordLandingResponse(WorktreeCommandResponse):" repointed to mcp/src/agents_remember/models/worktree.py:478-478. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T08:49:05+00:00: Generated citation repair: "class WorktreeCheckpointLandingResponse(WorktreeCommandResponse):" repointed to mcp/src/agents_remember/models/worktree.py:470-470. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T08:49:05+00:00: Generated citation repair: "class WorktreeStatusWaitResponse(WorktreeCommandResponse):" repointed to mcp/src/agents_remember/models/worktree.py:404-404. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: added this route's new `tools/public_roster.py`
  leaf (the single `PUBLIC_TOOLS` definition) to the entry-point prose and the reference table, and
  recorded the worktree next-move declarations (`models/worktree.py:331-333`) plus their `PUBLIC_TOOLS`
  membership validator (`:358-369`) as this route's enforcement of the advertised vocabulary. Recorded
  why the roster had to move here (the `models → mcp` layering violation, the unwritable `PLC0415`
  local import, and the circular module-level imports) and the per-surface rule. Verification metadata
  remains closeout-owned; no acceptance claim.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `_tool_payload` repointed to mcp/src/agents_remember/mcp/tools/base.py:22-24. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "class WorktreeRecordLandingResponse(WorktreeCommandResponse):" repointed to mcp/src/agents_remember/models/worktree.py:471-471. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "class WorktreeCheckpointLandingResponse(WorktreeCommandResponse):" repointed to mcp/src/agents_remember/models/worktree.py:463-463. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "class WorktreeStatusWaitResponse(WorktreeCommandResponse):" repointed to mcp/src/agents_remember/models/worktree.py:397-397. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: recorded `WorktreeCheckpointLandingResponse`, the
  new `checkpointed` member of `IntegrationStatus`, and the registry row between the integrate and
  record-landing rows; corrected the L29 section's 61-name census to the historical reading and
  re-derived the shifted reference ranges. Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-11T23:44:56+00:00: Generated citation repair: "\"worktree_sync\": WorktreeSyncResponse," repointed to mcp/src/agents_remember/models/tools/tool_registry.py:184-184. No content impact: mechanical anchor-range projection bound to citation source snapshot fc36bf81fd36002f552f72a34a44e9713fa47fc86ced6632de3215e5011793d3; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:41:08+02:00 — 260831-LOCR-L29 public-surface repair: recorded the new
  `WorktreeRecordLandingResponse` envelope and its `TOOL_RESPONSE_MODELS` row on this route, added
  the three-artifact invariant (advertised tuple, live registration, response registry) with the
  self-referential-`server_info` warning, and added the combined reference row. Verification
  metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T23:05:00+00:00: The claim anchored the public wait registration on the `"worktree_status_wait": WorktreeStatusWaitResponse,` row, which no longer exists anywhere in the tree: `mcp/src/agents_remember/models/tools/tool_registry.py` does not import `WorktreeStatusWaitResponse` and its `TOOL_RESPONSE_MODELS` now carries only the remaining worktree commands. The row now records that removal, anchored to the surviving `"worktree_sync": WorktreeSyncResponse,` mapping at 183, and the Status-Change Wait Response prose states that the class in `models/worktree.py` is currently unregistered and unreferenced.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_tool_payload` repointed to mcp/src/agents_remember/mcp/tools/base.py:75-77. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `PUBLIC_TOOL_RESPONSE_MODELS` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:227-231. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T02:27:58+02:00 — CCR-L42 parity curation: No route impact: curator preparation and closeout now run the shared sidecar and route body/history validators independently; this route's ownership and source semantics remain unchanged. No acceptance claim is made.
- 2026-09-08T16:24:06+02:00 — CCR-L38 preparation range refresh: repointed the worktree vocabulary and wait-response anchors after the frozen model additions. This is a mechanical source-range correction; verification metadata remains closeout-owned.
- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: recorded the optional activation fact and bounded admission vocabulary added to worktree response models. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.
- 2026-09-06T21:58:28+00:00 — Reconciled this route against the source delta from `245057ab16e19afdaabd5c188c9576b22e0c0870` to `d36109038b3f2b500c138f9dc1ea9c9f9a247489`. Updated current ownership and policy claims; prior verification commit/date and history remain unchanged. Source inspection only; no test, review or acceptance claim.
- 2026-09-06T14:48:58+00:00 — Added the nearest certification wire route from source at `c69d5171187fa1957025e393270db9f5a864ab14`; the remaining model domains are outside this bounded routing update. Prior verification stamps and all earlier history are preserved.
- 2026-09-05T06:21+00:00 — Re-read the affected source declarations and repaired citation ranges shifted by CCR additions. Preserved the route contract and existing history; literal anchors identify the exact current construct where shared identifiers were ambiguous.
- 2026-09-05T06:21+00:00 — Re-read the reopened affected citation claims against the frozen source, corrected their current wording/ranges, and replaced ambiguous symbols with exact declaration anchors. Verification records this source-backed claim review; it is not a code acceptance or final Gate-5 verdict.
- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.
- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec: route coverage refreshes `WorktreeStatusWaitResponse` (`models/worktree.py`) and the `TOOL_RESPONSE_MODELS` row (`models/tools/tool_registry.py`); route index regenerated.
- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: re-anchored the strict record/projection row after the public projection envelope moved from `operation.py` into `models/lifecycles/operation_projection.py`. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.
- 2026-08-31T20:30+02:00 — No route impact: 260831-DER changes integration authority
  classification and direct-landing documentation without adding or changing a model vocabulary.
- 2026-08-30T17:08:05+02:00 — ARSPAWN-L4 Dagger repair: moved the shared serving-build payload
  into the existing core model module and removed the transient extra module. Verification remains
  closeout-owned.
- 2026-08-30T15:15:36+02:00 — 260821-ARSPAWN-L4 route impact: added the shared strict
  `ServingBuildPayload` authority consumed by both MCP and dashboard serving surfaces. Verification
  remains closeout-owned.
- 2026-08-29T21:46+02:00 — MCAR-L03: added the canonical pair schema and shared wire bindings.
  Verification remains closeout-owned.
- 2026-08-29T09:45+02:00 — MCAR-L02 route impact: added the strict curator-coherence identity and
  action family, including exact judgment coverage and separate semantic-revision, delivery-attempt,
  immutable-generation, stable-authority, and snapshot boundaries. Verification metadata remains
  closeout-owned until the A005 code commit exists.
- 2026-08-28T14:15+02:00 — PDLS closeout: re-read `test_evidence.py` against the landed candidate;
  the existing final model reconciliation already describes the closed diagnostic/certifying,
  authority, cadence, lifetime, and result vocabulary. Stamped committed provenance.
- 2026-08-26T12:30+02:00 — Reconciled ARSPAWN-L2 private brief evidence, same-seat promotion, and
  runtime-id-free structural outcome rules onto the IAS models overview. Verification remains
  closeout-owned.
- 2026-08-26T08:55+02:00 — Finalized the activation/sync vocabulary label against the frozen
  pass-13 candidate.
- 2026-08-26T08:20+02:00 — Reconciled activation and sync field ownership to the frozen candidate;
  only commit-derived verification remains open.
- 2026-08-26T06:25+02:00 — Reconciled the structural-limit move: the activation snapshot and
  archive vocabulary now live under `models/structural/`; the former flat model path has no
  compatibility owner. Final verification remains post-Dagger owned.
- 2026-08-25T17:21+02:00 — Reconciled the final evidence, lifecycle, and projection model changes.
  Verification remains closeout-owned.
- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: reconciled the final `models/closeout/` package move and preserved its typed input/source/projection ownership at the new paths. Verified against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is not Dagger certification.
- 2026-08-24T21:23+02:00 — 260824-PDLS added the typed Python evidence firewall.
- 2026-08-24T16:00+02:00 — Final cumulative closeout audit: marked the L2
  lifecycle-shaped queue model as historical and named the final projection-only model owners.
- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: added strict quality request/result types and closed direct-landing outcome vocabulary. Verification metadata remains pinned until architect-owned closeout.
- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: recorded the `models/tools/` package layout, repaired current registry evidence paths, and verified the governed L2 route at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.
- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: route claims reconciled to accepted candidate tree `4241908c`; verification metadata remains closeout-owned.
- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 route impact: `SpawnAgentSessionResponse` gains the caller-kind provenance `spawnedByKind` (`plane|ambient|unattributed`) mirroring the catalog row; response-model route model unchanged. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.
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
- 2026-06-19T07:23+02:00 — No route impact: slice 3c R5 adds the additive optional `dryRun`/`rendered`/`diff`/`wouldLose` fields to `TaskDocResponse` (set only on a dry-run preview); it stays a STRICT `ToolResponse`, so the strict/flexible split this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: added `models/gates.py` (the four `gate_*` strict `ToolResponse` subclasses) to the route and their `tool_registry` rows; they follow the existing STRICT pattern, so the strict/flexible split this overview describes is unchanged. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-13T22:34+02:00 — Slice 3c commit 1: added `models/task_doc.py` (`TaskDocResponse`, a STRICT `ToolResponse`) to the route and its `tool_registry` row; it follows the existing STRICT pattern, so the strict/flexible split this overview describes is unchanged. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T18:45+02:00 — No route impact: slice 2c declares one optional `lifecycleId` field on the flexible `WorktreeCommandResponse`; the strict/flexible response-contract route model this overview describes is unchanged (detail in the file sidecar).
- 2026-06-13T16:41+02:00 — Slice 2b: added `models/lifecycle.py` (the six `lifecycle_*` STRICT response models) to the route; they follow the existing STRICT `ToolResponse` pattern, so the strict/flexible split this overview describes is unchanged. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T06:47+02:00 — No route impact: issue #62 removed `DirectCloseoutPreviewResponse`/`DirectCloseoutApplyResponse`, their registry rows, and their package exports; the strict/flexible route model this overview describes is unchanged (detail in the file sidecars).
- 2026-06-10T09:56+02:00 — No route impact: sub-task D adds `WorktreeSyncResponse` (one more flexible `WorktreeCommandResponse` subclass) and its registry row (GitHub #54); the strict/flexible route model this overview describes is unchanged (detail in the file sidecars).
- 2026-06-10T07:40+02:00 — No route impact: `models/worktree.py` only documented the existing flexible `providers` field's async setup states (GitHub #53).
- 2026-06-10T05:30+02:00 — Route body caught up with the 2.5.1/2.5.2 compact-response field documentation pattern (`reportPath` + per-tool digests declared on flexible models); previous closeouts had only stamped the verification header. Developer-flagged gap.
- 2026-06-08T09:57+02:00: Re-verified response model guidance after compact provider `ok` fields became optional-null defaults for skipped-provider payload re-validation.
- 2026-06-06T12:15+02:00: Re-verified against the current response model package; corrected the payload-builder reference from the deleted `mcp/tools.py` file to the `mcp/tools/` package.
- 2026-05-28T19:52+02:00: Created for the Pydantic public response-contract model package while S2/S4 source changes are still uncommitted in the checkout.
