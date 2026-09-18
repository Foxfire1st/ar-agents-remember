# mcp/src/agents_remember/models/ - Response Contract Models Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/models/`          |
| doc_type               | `route-local-overview`                     |
| lastUpdated | 2026-09-16T20:42+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l7-ar` uncommitted source; base `23cc7a7218b96da5147146f9796557bedfcf1d11` |
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
identities. The request exposes one closed `status|prepare|publish|validate` action vocabulary;
publication fields are forbidden on read-only actions, while publish requires every expected
source identity, predecessor digest, and declared caller. Record validation requires unique exact
coverage of the structured source-candidate set rather than accepting partial or extra judgments.

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

## 260915-CAPS-L2 Role-Capsule Contract And Compiler

`mcp/src/agents_remember/models/role_capsules/` is a **new sub-route** on this route: the master's
frozen role-capsule DTO surface plus the pure logic that compiles it. It is the first thing on this
route whose entire contract is about *what an agent seat is given*, so its reading order is worth
stating once.

The package reads in six steps, and each step is one module: `vocabulary.py` declares the frozen
ten roles/nine operations and the four composition roots; `manifest.py` parses the canonical
authored `composition-manifest.json` into typed entries **without touching the filesystem**;
`selection.py` turns an admitted binding into a scope by exact membership (no scoring, no
nearest-match, no fallback operation); `source_set.py` proves the admitted files agree with the
locked plan **in both directions**; `resolution.py` reduces each identity to exactly one block,
collapsing byte-identical duplicates and stopping on an equal-authority contradiction;
`tools.py` narrows requested tool identities against the admitted policy snapshot; and
`compiler.py` seals the result with the semantic digest and the diagnostic manifest.

`models/memory_content_excludes.py` is the route's second 260915-CAPS-L13 addition and is a
different kind of module: not a capsule DTO but the **shared memory-content exclusion policy** —
`memory.md` (the computed ledger cache) and `bootstrap/` (transient scaffolding) declared once for
all four seams that create a memory-content commit. It lives in `models` because that is the lowest
layer every producing seam can read.

Three separations are load-bearing and easy to collapse by accident:

1. **admitted input / content output / diagnostic output** — the DTOs in `types.py` keep these
   structurally apart, which is why `types.py` was split at 704 lines and the diagnostic
   projection extracted into `diagnostics.py` (541 + 217 after the A3 repairs). **Nothing in `diagnostics.py` may ever
   feed `semantic_digest`**; timestamps, unselected sources, conflict rows and refusal text are
   deliberately outside the capsule's identity.
2. **a request is not a grant** — tool requests are narrowed against `CapsuleToolPolicy`; nothing in
   this package can add a capability the policy did not already permit. **The skill channel is a
   different shape and must not be described with this one:** `compiler.skill_references` builds one
   content-addressed `CapsuleSkillReference` per declared skill (`identity`/`origin`/`uri`/`revision`)
   and consults **no** policy — a skill reference is a pointer to separately delivered content, so it
   is *carried*, and the only thing that can invalidate it is a skill root file that was not admitted.
3. **declared vocabulary over the manifest** — the role/operation registry is declared in code and
   handed to the parser, so a manifest edit fails compilation instead of minting a new role.

The semantic digest is a `\t`-separated canonical document over the seat, operation, repository,
work branch, task reference and document digest, requirement identities, the specializations
**actually composed**, one line per composed block with its revision, one line per requested tool id
in sorted order, one `skill` line per carried reference, and the task context when supplied. Order is
part of identity, not presentation over it. Ten shipped roles compile from disk twice to one digest
each and to ten different digests, so the digest is neither a constant nor order-insensitive.

`layers.toml` places this package in `models` (rank 2) precisely because it holds only
dependency-free value types, canonical source parsing, and selection logic. The contract's declared
target is not yet met tree-wide — the tree reports 16 pre-existing violations, **none** naming a
role-capsule module — so do not present the layer contract as currently satisfied.

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
| The registry maps every modeled builder and the advertised public subset to response models. | `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:243-247 |
| Contract tests prove public tool coverage and schema generation. | `PublicToolResponseModelTests`; `test_every_public_tool_has_a_response_model`; `test_every_public_tool_response_model_generates_json_schema` | mcp/tests/test_models.py:16-26 |
| The record-landing envelope is declared on this route. | "class WorktreeRecordLandingResponse(WorktreeCommandResponse):" | mcp/src/agents_remember/models/worktree.py:478-478 |
| The checkpoint-landing envelope is declared on this route. | "class WorktreeCheckpointLandingResponse(WorktreeCommandResponse):" | mcp/src/agents_remember/models/worktree.py:459-459 |
| The checkpoint registry row sits between the integrate and record-landing rows; the record-landing row follows it. | "\"worktree_checkpoint_landing\": WorktreeCheckpointLandingResponse,"; "\"worktree_record_landing\": WorktreeRecordLandingResponse," | mcp/src/agents_remember/models/tools/tool_registry.py:191-191; mcp/src/agents_remember/models/tools/tool_registry.py:192-192; mcp/src/agents_remember/models/tools/tool_registry.py:198-198; mcp/src/agents_remember/models/tools/tool_registry.py:199-199 |
| Curator coherence keeps semantic revision, attempt, immutable record, stable authority, snapshot, and action request identities separate and exact. | `CuratorCoherenceRecord`; `CuratorCoherenceAuthority`; `CuratorCoherenceSnapshot`; `CuratorCoherenceRequest` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:189-233; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:236-247; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:250-256; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:259-315 |
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
| Public message transport names only code and memory. | n/a | [mcp/src/agents_remember/models/closeout/input.py](mcp/src/agents_remember/models/closeout/input.py) |

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
| Public response registration no longer carries the dedicated wait response: `worktree_status_wait` is absent from `TOOL_RESPONSE_MODELS`, so `WorktreeStatusWaitResponse` stays defined in `models/worktree.py` with no registered tool. | "\"worktree_sync\": WorktreeSyncResponse," | mcp/src/agents_remember/models/tools/tool_registry.py:193-193 |


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
`PUBLIC_TOOLS` literal
cit:([`PUBLIC_TOOLS`], mcp/src/agents_remember/models/tools/public_roster.py:22-90) — **62 names at this
leaf, 63 from 260831-LOCR-L37, and 66 since 260915-CAPS-L4**. It is the tuple's **single definition**; `mcp/tools/base.py`
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

## 260915-CAPS-L4 The Capsule And Skill-Resource Wire Contracts

This route gained two modules that own the AR MCP surface's wire vocabulary for the capsule operation
and the SEP-2640 skills transport. Both are value modules: dataclasses or strict response models plus
their rendering, with no behavior that decides a selection, a permission or a trust level.

- `role_capsule_resources.py` — the three strict response envelopes (`role_capsule_compile`,
  `skill_catalog_list`, `skill_catalog_read`) and their nested payloads, plus the bridge-name and
  `server-supplied-data` trust constants. The capsule envelope carries **both** shapes: `ok` false plus
  a typed `refusalStatus` is a refusal, not an error type, and the identity/provenance fields are
  optional precisely because a refusal legitimately carries only what was established before it
  refused.
- `skill_resources.py` — the discovery registry (`SkillResourceEntry`, `SkillResourceFile`,
  `SkillResourceCatalog`, `UnreadableSkill`), the **SEP-2640 entry shape**
  (`{uri, frontmatter, resources:[{uri,digest,size}]}`), this server's own Agent Skills discovery index,
  and the `_meta` provenance block. Identity is `origin` + name, which is what keeps two servers serving
  a same-named skill distinct. `entry_documents()` is the **enumeration surface** the `skills/list`
  method returns; `discovery_metadata()` is what this server's own listing tools hand out; neither can
  reach a file body.

Two vocabulary facts that belong at route level, because they are the route's own
"defined here, imported by whoever decides it" rule applied to a security property:

- **`contentTrust` is a stated constant, not an inferred or settable field**, and
  **`declaredAllowedTools` is an observation, never a grant** — a host MUST NOT honor mechanisms
  declared in skill content, and no field on these models is a channel through which it could. The
  leaf's mutation probe removes the related guarantee on the admitted-policy side (`M2`) and its named
  case fails.
- **`requestedTools` and `grantedTools` are separate fields on the capsule envelope.** The compiler
  narrows every request against the admitted policy snapshot; keeping both on the wire is what makes
  that narrowing auditable rather than invisible.

A third fact, added by the post-rejection repairs and worth carrying here because it is a wire-shape
decision rather than a reader's choice: **the entry's `frontmatter` is the verbatim `SKILL.md`
frontmatter, not a two-field summary.** SEP-2640 §Enumeration requires *"every field the author wrote,
not a curated subset"*, so `SkillResourceEntry.frontmatter` carries the whole YAML map the reader
produced, and `license`, `metadata` and future specification fields pass through unchanged. A nested
skill is published flat: an ordinary entry whose `uri` merely shares a path prefix with its parent's.

Both modules import nothing from `mcp` — the same `models` rank constraint this route's
`tools/public_roster.py` records. The protocol methods that consume these values live on the `mcp`
route (`registration/skills_extension.py`), which is the correct direction for this rank.

| Finding | Anchor | Source |
| --- | --- | --- |
| The capsule envelope keeps one shape for success and refusal, with the seat facts it established. | `RoleCapsuleResponse` | mcp/src/agents_remember/models/role_capsule_resources.py:86-115 |
| The requested-versus-granted split that makes the compiler's narrowing auditable. | `CapsuleRequestedToolPayload`; `RoleCapsuleResponse.grantedTools` | mcp/src/agents_remember/models/role_capsule_resources.py:56-60; mcp/src/agents_remember/models/role_capsule_resources.py:112-112 |
| Identity is origin plus name, and a listing cannot reach a body. | `SkillResourceEntry.identity`; `discovery_metadata` | mcp/src/agents_remember/models/skill_resources.py:83-87; mcp/src/agents_remember/models/skill_resources.py:149-170; mcp/src/agents_remember/models/skill_resources.py:200-221 |
| The trust statement is a constant and a declared tool set is observed, never applied. | `SERVER_SUPPLIED_CONTENT_TRUST`; `declared_allowed_tools` | mcp/src/agents_remember/models/role_capsule_resources.py:31-32; mcp/src/agents_remember/models/skill_resources.py:219-234; mcp/src/agents_remember/models/skill_resources.py:270-285 |
| The three registry rows that make the new names returnable. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:155-238 |

## 260915-CAPS-L7 The Eve Capsule Carrier Format

This route gained `eve_capsule_carrier.py`, which owns the **format** of the one value AR hands a pinned
eve runtime before it executes. The launch environment can carry a reference and a digest but not the
compiled instructions, so the content travels as a file whose bytes that digest addresses.

It owns the format and nothing else — it parses bytes it is handed and computes digests over them, with
**no filesystem import by design**. Reading the file, writing it and deciding whether a launch may
proceed belong to the tiers that own those surfaces, and that separation is what lets one shape serve
the compiler side (`application`) and the launch side (`serving`) with neither importing the other.

Four properties are enforced here rather than trusted, all at parse time:

- **Self-describing identity** — `EveCapsuleIdentity` names the seat it belongs to, so a carrier left
  over from another seat is refused by `require_identity` instead of applied.
- **The digest is over the exact bytes on disk**, so a carrier edited after it was written is refused.
- **Every consumer-needed field is required**, so a truncated or hand-written carrier fails naming the
  missing field rather than contributing an empty instruction block; the three parallel instruction
  lists must correspond one to one.
- **The workspace scope and the workspace root are forced equal** (`_require_workspace_confinement`),
  so the runtime cannot read and execute in one directory while its write rule admits another.

This module is also the single home of the four environment names and of the two instruction
**channels**. The channel choice is load-bearing rather than stylistic: the trusted instructions go in
the **system** role, which eve keeps outside conversation history and includes on every model call — so
they survive turn boundaries, compaction and clear — while task facts go in the **user** role, because
they are content rather than authority and compaction may legitimately summarize them.

| Finding | Anchor | Source |
| --- | --- | --- |
| The carrier format added to this route: schema, value types and the on-disk byte contract. | `EVE_CAPSULE_CARRIER_SCHEMA`; `EveCapsuleCarrier`; `to_bytes`; `from_bytes`; `carrier_digest` | mcp/src/agents_remember/models/eve_capsule_carrier.py:32-32; mcp/src/agents_remember/models/eve_capsule_carrier.py:168-231; mcp/src/agents_remember/models/eve_capsule_carrier.py:287-296 |
| The two channels and why the distinction is load-bearing. | `ROLE_INSTRUCTION_CHANNEL`; `TASK_CONTEXT_CHANNEL` | mcp/src/agents_remember/models/eve_capsule_carrier.py:46-58 |
| The parse-time confinement invariant and the wrong-seat refusal. | `_require_workspace_confinement`; `require_identity` | mcp/src/agents_remember/models/eve_capsule_carrier.py:273-285; mcp/src/agents_remember/models/eve_capsule_carrier.py:299-320 |
| The four environment names declared beside the format so writer and reader cannot drift. | `BINDING_REF_ENV`; `CAPSULE_PATH_ENV`; `CAPSULE_DIGEST_ENV`; `WORKSPACE_ROOT_ENV` | mcp/src/agents_remember/models/eve_capsule_carrier.py:34-42 |
| The producer that builds this value and the two consumers that verify it, none of them in this route. | `build_carrier`; `verify_capsule_binding`; `loadVerifiedCapsule` | mcp/src/agents_remember/application/eve_capsule/__init__.py:282-324; mcp/src/agents_remember/serving/eve_runtime_launch.py:447-497; eve_runtime/agent/lib/capsule.ts:109-149 |

## 260915-CAPS-L11 One Refusal Shape For One Class Of Source Defect

`sources.py` on this route now refuses an **emptied** admitted source the same way it already refused
a non-UTF-8 one: a typed `CapsuleSourceError` carrying `status="source-empty"`, a detail naming the
source path, and a next action — rather than a bare `ValueError` escaping `CapsuleSource.text`.

**Why the shape matters rather than the message.** `compile_admitted_capsule` catches only
`CapsuleCompilationError`, so an untyped raise from the value layer surfaced to an operator as a
traceback instead of the named refusal the compiler's own boundary promises. One class of defect now
has one refusal shape at one boundary.

**A property a reader should not have to rediscover:** emptiness is discovered while blocks are
*composed* — after admission succeeded and a real manifest parsed — so the guard is reachable only
through a real composition. That is why the leaf's case drives a disposable copy of the shipped
corpus rather than a fixture, and it is what makes the seed failable.

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `PUBLIC_TOOL_RESPONSE_MODELS` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:243-247. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "class WorktreeRecordLandingResponse(WorktreeCommandResponse):" repointed to mcp/src/agents_remember/models/worktree.py:478-478. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "from agents_remember.models.worktree import (" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:9-9. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "class LifecycleOperationRecord(BaseModel):"; "class LifecycleOperationProjection(StrictResponseModel):" repointed to mcp/src/agents_remember/models/lifecycles/operation.py:340-340; mcp/src/agents_remember/models/lifecycles/operation_projection.py:340-340. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "\"worktree_sync\": WorktreeSyncResponse," repointed to mcp/src/agents_remember/models/tools/tool_registry.py:193-193. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T16:04+02:00 — 260915-CAPS-L11 curator (**final-verification leaf**): this route's `sources.py` changed and the route body is updated for it. The card now records the **D25 repair**: an admitted source that decodes to whitespace only is refused as a typed `CapsuleSourceError(status="source-empty")` on the same boundary as `source-not-utf8`, instead of raising a bare `ValueError` that `compile_admitted_capsule` does not catch — one refusal shape for one class of defect, with the leaf's case driving the shipped corpus because emptiness is discovered after admission succeeds. The card's identity-helper and value-type ranges were re-anchored to the candidate, and a stale `nine roles / eight operations` vocabulary on the sibling admission card was corrected to the registry's **ten / nine**. No verification stamp advanced — the candidate is uncommitted and the governed closeout owns the real commits. Earlier entries are preserved exactly as written.

- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: this route gained `eve_capsule_carrier.py`, the
  **format** of the value AR hands a pinned eve runtime before it executes, recorded in the new
  `## 260915-CAPS-L7 The Eve Capsule Carrier Format` section. The section names the module's deliberate
  narrowness (format only, no filesystem import, so the compiler side and the launch side can share one
  shape without importing each other), the four properties enforced at parse rather than trusted
  (self-describing identity, digest over the exact on-disk bytes, every consumer-needed field required
  with the three instruction lists forced one-to-one, and the workspace scope forced equal to the
  workspace root), and the two instruction channels as load-bearing rather than stylistic: system role
  for trusted instructions so they survive turn boundaries, compaction and clear, user role for task
  facts because they are content and compaction may summarize them. It also records that the producer
  and both consumers live in other routes. Verification metadata moves to the leaf's synced base
  `23cc7a72`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code
  commit and no hash or fingerprint was invented here.

- 2026-09-16T17:59+02:00 — 260915-CAPS-L13 curator: **route body corrected for the two modules this
  leaf added to this route** (`CAPS-R13@v1`). In the role-capsule sub-route the frozen vocabulary is
  now **ten roles / nine operations** (was stated as nine/eight) and the shipped determinism property
  is **ten shipped roles compiling to ten different digests** (was nine to nine); both are the
  registry extension this leaf made in `vocabulary.py`. Added `models/memory_content_excludes.py` to
  the route section as what it is — the shared memory-content exclusion policy (`memory.md`,
  `bootstrap/`) rather than another capsule DTO — with the reason it sits in `models`: that is the
  lowest layer all four producing seams can read. No other claim on this route changed.
- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass** (uncommitted change set on
  `ar/260915-caps-l4`, base `b00a4ac2`): refreshed this route section against the settled candidate.
  `skill_resources.py` now owns the **SEP-2640 entry shape** (`{uri, frontmatter, resources:[{uri,digest,size}]}`)
  and the enumeration surface (`entry_documents()`), distinct from this server's own
  `discovery_metadata()` listing and its own Agent Skills discovery index. Added the route-level fact
  the repairs introduced: an entry's `frontmatter` is the **verbatim** `SKILL.md` frontmatter — "every
  field the author wrote, not a curated subset" — with `license`, `metadata` and future specification
  fields passing through, and nested skills published flat. Recorded that the protocol methods consuming
  these values live on the `mcp` route, which is the correct direction for the `models` rank. Verification
  metadata remains closeout-owned; no acceptance claim is made.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator (uncommitted change set on `ar/260915-caps-l4`,
  base `b00a4ac2`): added the two new wire-contract modules to this route — `role_capsule_resources.py`
  (the three strict envelopes, with the capsule's shared success/refusal shape and the deliberate
  `requestedTools` versus `grantedTools` split) and `skill_resources.py` (the discovery registry, the
  index document and the `_meta` provenance block). Recorded the two security-property vocabulary facts
  at route level: the trust statement is a stated constant and a declared tool set is an observation
  never applied, with the mutation-probe entry that makes the related admitted-policy guarantee
  executable. Corrected the L32 section's roster literal from "62-name" to the measured lineage
  (**62 at that leaf, 63 from L37, 66 since this change**) and repointed its single-definition range to
  `models/tools/public_roster.py:22-90`. Verification metadata remains closeout-owned; no acceptance
  claim is made.

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
