# Structured Conversation Contract And Composition Overview

## Purpose

This route composes the production structured Chats surface over native conversation and control authorities. Its governing responsibility is to keep active conversation reads, dormant native history, human control operations, authorization, and declared HTTP responses coherent without making the composition layer a second native store or lifecycle authority.

The normalized wire grammar now belongs to `mcp/src/agents_remember/models/conversations/`. This route consumes that grammar and retains the app-scoped runtime, request dependencies, authorization ruling, response declarations, and root router composition. The former local `models.py` and split model files were moved without a forwarding shim. `conversation/ports.py` re-exports the canonical `serving/ports.py` definitions: there are two conversation read protocols, alongside separate control-plane and terminal-catalog seams.

Three implemented child routers own behavior. `active/` serves active pages, resumable events, and selected sub-agent history hydration. `library/` serves dormant native list/read and exact open/status/reconcile. `control/` serves exact-turn interrupt, source-aware queue and withdrawal recovery, typed attachment lifecycle and submit, read-only effective policy, and telemetry. Their route-local overviews govern those implementations; `projectors/overview.md` governs the harness-specific mapping grammar. The root composition itself neither projects vendor events nor reads native history, implements control actions, or renders the browser UI.

## Hot Path Summary

Start with `models/conversations/` for identities, purpose-branded cursors, normalized content and provenance, status, capabilities, operations, attachments, recovery, structured questions, and sub-agent participants. Read `serving/ports.py` for the active and dormant read protocols and their separate control dependencies.

At application construction, `serving/app.py` creates a frozen `ConversationRuntime` from workspace/coordination scope, catalog, control-plane client, terminal host, effective harness registry, liveness clock/configuration, capability catalog, and local-operator authorization resolver. `register_harness_control_routes` passes that same bundle to `register_conversation_routes`; the latter installs the runtime and mounts the root router. Children retrieve it through `get_conversation_runtime` and resolve request authorization through `resolve_conversation_authorization`.

For active reads, the service resolves the running catalog entry and actual bridge epoch, rejects an expected-epoch mismatch, reads the live snapshot, and builds the native identity and harness mapper before obtaining a session projector. Page and event cursors have distinct purposes and bind to caller and exact conversation identity. Events require a resume cursor; conflicting `after` and `Last-Event-ID` values are refused. Established-stream gaps are explicit mutations followed by closure, requiring a new page rather than silent reset. Selected-child history acquisition uses the same authorization and parent epoch seam; typed child failures are local outcomes inside HTTP 200, while parent authority/composition/epoch failures use the refusal ladder.

For dormant history, the library resolves authorization and canonical project scope, applies its live capability gate, and uses distinct list/read cursors and conversation keys. Exact resume targets remain server-private; possessing a token is not an authorization grant. Open requests bind caller, requested identity digest, working directory and launch context into an idempotent request product. Open status and reconciliation preserve uncertainty and rollback rather than treating an attempted launch as proof of an exact opened conversation.

For human control, request scope carries the service, caller, session and expected epoch together. Resolved scope uses the verified epoch for reference minting and decoding. Interrupt acknowledgement and settlement are separate products. Queue projections expose source/kind/phase/order and restricted identification data, not prompt bodies. Only queued cockpit rows carry a withdrawal reference, redacted preview and digest. Successful withdrawal may recover exact text and attachment references through a bounded lease; failed withdrawals and pending-recovery lists remain raw-free. Staging/rebind/submit, policy and telemetry stay inside their respective control owners.

## Construction And Ownership

`runtime.py` defines frozen `ConversationScope` and `ConversationRuntime`. The bundle binds existing authorities and adds no conversation store, index, opener, lifecycle authority or child service. Construction rejects `None` authority members. Installation rejects an already occupied runtime binding; retrieval rejects a missing binding or a value of the wrong runtime type. These are distinct checks, not a claim that every malformed binding is validated at every step.

`authorization.py` owns the local single-user ruling. `LocalOperatorAuthorizationResolver.for_workspace` binds a server-resolved operator principal to the resolved workspace path. Request resolution accepts only literal loopback IP peers; absent, unresolved or non-loopback peers fail closed. `require` compares an external binding against that exact operator/workspace identity. The resolver is explicitly not a general authenticated identity system. Remote or multi-user requirements invalidate this ruling and require a separate authentication design. Browser principal/tenant claims have no input channel in the conversation request dependency, which consults the ASGI peer address. The principal implementation uses `os.getuid()` where available and `getpass.getuser()` otherwise; the latter is not grounds for an unconditional claim that environment-derived identity is impossible on every platform.

`dependencies.py` owns the two narrow request seams. `router.py` composes active, library and control children and performs runtime installation before mounting. Children own service construction and behavior inside their seams rather than rebinding the shared composition.

The present API modules declare 25 routes: three active, five library and seventeen control. Active contains page, events and selected-child history hydration. Library contains list, read, open, open-status and open-reconcile. Control contains interrupt request/status/reconcile; queue read and withdrawal request/status/reconcile; pending recovery list, recovery fetch and acknowledgement; attachment stage/rebind/status/reconcile; submit; policy; and telemetry. The active and control prefixes share the terminal namespace but own different endpoint paths; library owns the dormant-library namespace. None is an empty shell.

`response_contract.py` owns the three route-assembled wrappers `StagedAttachments`, `ConversationSubmitted` and `AgentHistoryHydrated`, plus the withdrawal answer union and six shared response tables. Refusal tables describe child error mapping; outcome tables also describe operation-shaped answers on non-200 statuses. A pending open, an acknowledged-but-unsettled interrupt, and a failed withdrawal are operation outcomes rather than automatically refusal-shaped bodies. Because API declarations merge dictionaries, an outcome entry must retain the refusal members possible at that same status. Submit similarly declares its own body on 200/202/422, with typed refusal included where applicable.

Keep this module distinct from app-level `serving/response_contract.py`. The source records the package/import-cycle reason for the split; after the model migration its imports use the independent `models/conversations/` package. That historical rationale does not establish that the former exact import cycle is still unavoidable today.

Vendor transport, executable/process lifecycle and harness-specific probing belong to serving adapters. Durable inbox and queue authority belong to the control plane and its serving adapters. The locked Claude/Pi history helper belongs to `mcp/native_helpers/conversation_library/`. Browser rendering and composer state belong to `dashboard/src/`.

Internal child bundles preserve facts that are correct only together: `ControlRequest` and verified `ControlScope`; `RefBinding` and `RefTarget`; evidence-strength-bearing `TurnTransition`; `ProjectedSession`; `LibraryBinding` and fingerprinted `OpenRequest`; and projector placement/collaboration/task identity values. These are internal call shapes, not public wire vocabulary. The active projector is now a package: its shared `SessionProjectionSpine` and `BridgeReaders` keep component identity, epoch, mapping, mutation stream and reader substitutions together. Native ingestion, echo ingestion, interaction projection, child history and rebuild coordination remain child-owned.

Blocking resolution is offloaded at the active and control service choke points. Active offloads catalog resolution, epoch and snapshot reads; control's asynchronous `resolve_entry` and `verify_epoch` offload their blocking reads. This preserves the availability intent of the historical repair without claiming all possible blocking work throughout serving has been audited.

## Invariants And Boundaries

The canonical `WireModel` forbids extra fields, freezes model attributes, and uses camel-case aliases while allowing population by field name. Purpose-branded opaque values enforce their prefixes; signing, caller checks and persistence belong to the concrete token authorities. Active page/event tokens and library list/read/key/resume tokens are not interchangeable. The active authority checks signature, schema, purpose, caller, session, epoch and native identity; library tokens carry scoped bindings and generations and are rechecked by their owning services. Token possession alone must not replace request authorization.

Native identity, unknown evidence and input provenance must remain distinguishable. Unknown-input items stay native-history evidence with `native-only` or `unknown` strength and no claimed producer. Terminal-controlled input has its own operator/controlled-terminal authority and may have exact or correlated provenance; it must not be relabeled as exact native input. Cockpit, durable inbox, interaction-response and control-authority items likewise retain their own lane/producer/strength products.

Status separates process and turn state and carries freshness and evidence. Unknown-strength evidence cannot establish `ready`. Waiting requires a reason without an interaction id; needs-input requires an exact interaction id. Interrupted/failed and other turn states must carry compatible terminal-outcome products. Canonical status and transition ownership remain with the active status service, including the intent that weaker observations cannot displace stronger justified state.

Capabilities are evidence products, not fixture-existence or version-equality claims. `supported` and `partial` require the runtime-fixture tier and a fixture identifier; other non-none tiers require evidence, and the none tier is unavailable only. Attachment support additionally requires actionable MIME/count/byte limits. These validators check the declared evidence product, not the historical capture itself or a fresh running harness.

The inherited policy is contract-based verification rather than runtime/helper version comparison. Present active/control builders use harness-keyed declarations, and control builders discard the supplied snapshot rather than dynamically probing it. Active interrupt capability delegates to the control owner so it has no independent hardcoded verdict. Library capability gates do perform a production-path probe: successful Codex connect/list returns supported history products; successful locked Claude/Pi helper list does likewise, with failures returning unverified products. Version strings remain evidence metadata in these examined owners. This is bounded source evidence, not a whole-call-path assertion that no other version predicate exists anywhere.

Harness vocabulary includes Codex, Claude, Pi and Eve. Active mapping/capability ownership includes Eve; the dormant library factories and gate normalization remain Codex/Claude/Pi. Active dispatch is keyed and does not let a new harness inherit Pi evidence by fall-through. Eve live text, thinking, tools and interactions are declared supported, completeness partial; its missing native history page is explicitly unavailable, while historical completeness remains unverified. Eve control declares supported interrupt and policy-read, unavailable attachments, and unavailable telemetry. The control owner's broader prose saying every control other than interrupt is unavailable is inconsistent with its explicit supported policy-read construction; the field construction decides this description.

Claude live features and historical completeness in the active capability view retain never-probed reasons; active native-page read is unavailable because that surface is stream/replay-only. Claude interrupt is now declared supported from the named 2.1.217 interrupt probe and is shared into the active view. Claude attachment image support, policy and telemetry remain unverified; file/resource kinds are unavailable. Claude dormant-library support is conditional on its live helper gate and cannot be summarized as permanently unverified.

Codex control telemetry declares supported cumulative token usage, unavailable context-window and cost metrics, and unverified rate-limit/compaction metrics. Pi telemetry retains unverified session/context/token/cost/compaction claims and unavailable rate-limit evidence. Active capability views are separate products and should not be silently equated with the control telemetry declaration. No declaration here is fresh acceptance of a runtime.

Open operations validate phase/outcome, complete and matching spawned identity, catalog-generation association and rollback products. Unsupported and stale-identity no-launch outcomes carry no spawned identity. Opened requires identity, catalog proof and no rollback; identity-mismatch requires catalog generation and matching failure rollback. The inherited broader requirement that identity-bearing failures be catalog-proven remains intent: these local validators do not impose that exact predicate on every launch-failed product. That observation does not establish absence of proof in the open service or tracked opener.

Interrupt acknowledgement does not establish settlement. Requested acknowledgement permits pending settlement only; rejected requires failed settlement; accepted and unknown allow the declared pending or terminal products. `settled_at` must agree with whether settlement is terminal.

Queue privacy is structural: only source cockpit plus phase queued is withdrawable and carries cockpit identification. Terminal and durable rows remain body-free. Withdrawal recovery belongs only to successful withdrawal/recovery responses, not failures or pending projections. The successful product includes exact text, digest, submitted draft revision and attachment recovery references. Recovery-unacknowledged requires expiry; no-recovery products cannot carry expiry. Control stores are bounded; recovery and staged-asset leases are 900 seconds. Acknowledgement, invoked expiry sweeps and pressure reclamation end fetchable recovery according to their local predicates; the control owner distinguishes this from immediate erasure of every journal or stored-answer copy. Post-disposal replay must not restore fetchable content, as the inherited recovery intent requires. These leases and retained ledgers are not a permanent recovery guarantee.

Structured per-question interactions preserve question text, header, options and multi-select alongside the existing flattened prompt/choices. Session-direct interaction response is owned by `harness_control_api.py`, outside the 25 conversation child routes. Its purpose is to answer a pending vendor interaction for seats without a lifecycle; the source states that expected epoch and exact interaction identity remain authority guards. This distinct response path does not turn conversation composition into lifecycle ownership.

Six optional wire fields retain defaults of `None`: freshness `last_evidence_at`/`age_ms`, turn `turn_id`/`state_since`, event `previous_cursor`, and page-window `older_cursor`. Historical serializers omit none-valued fields, so nullable-but-required declarations could reject their own emitted body. Keep omission compatibility distinct from a claim that an entire present response conformance suite has passed.

## Historical And Verification Limits

The original card records contract-matrix, foundation-topology, composition, authorization and response-conformance suites as historical witnesses. Those claims are retained as historical evidence, not renewed execution verdicts. This proposal inspected source text and route declarations only; it ran no product code, tests, runtime probes or certification checks.

260718-CHATS-L0 records the repair of authorities previously trapped in harness-control composition and the single immutable runtime/request seam. L2/L3 record the implemented native library/control ownership; L5F records the developer ruling that contract verification, rather than version drift, decides capability support. The prior seven-site grep claim is historical and was not repeated as exhaustive present evidence.

The older Claude 2.1.216 fixture-capture follow-on and blanket unverified statement are historical limits, not the present interrupt verdict. Named present exceptions are the Claude 2.1.217 interrupt declaration and conditional library helper promotion; other Claude live/control/telemetry limits remain explicit. Codex cumulative token usage remains the supported control telemetry metric in the examined declarations. Captured fixture identifiers and source strings describing an installed probe do not establish a fresh installed-runtime result on this checkout.

260727-CHATS-IM-L2 records active projector decomposition, selected-child acquisition behind authorization/epoch proof and typed child-local failure without claiming parent or sibling failure. It also records the intended import-compatible projector facade and adapter-owned probing; that history is not a new compatibility implementation request.

260731-EFA-L2 records deletion of five lint suppressions under the then Python 3.11 floor and later migration to Python 3.13. Those runtime statements are historical: present package metadata requires Python >=3.14,<3.15, while Ruff still targets py313 and Pyright configuration states 3.14. Do not infer a runtime version from the Ruff target.

260731-EFA-L4 records response declaration and omission/default repair, the former import-cycle rationale, and conformance failures involving dictionary overwrite of refusal models. The behavior rationale survives; its old emitted-byte equivalence and suite outcomes were not freshly established. L9 records relocation of wire grammar and canonical ports without a model forwarding shim. L16 records the blocking-resolution availability repair. L23 records native Codex executable resolution and product-agnostic initialize diagnostics; the present library request uses client name `agents_remember`, title `Agents Remember`, version `3.0.0`, and validates against the same requested name/version. The earlier Desktop host-first description is not the current request identity.

The original card's browser-rendering gate, pre-commit verification metadata, aggregate-refresh instructions, no-cross-repository evidence and empty Domain Documentation registry describe the inherited curation context. They are not current source-derived delivery or registry receipts. Prior test counts, successful delivery claims and old witnesses not examined here remain historical only. Original reference identities/targets and route/status/coverage metadata are preserved by the parent curator; this proposal creates no new lifecycle status or publication receipt.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/overview.md` |
| parentOverview | [`serving/overview.md`](../overview.md) |

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `models.py` | contract/policy | Prevents identity, provenance, capability, status, and operation contradictions at the public boundary. | covered |
| `ports.py` | boundary | Keeps active and dormant history reads distinct and prevents control authority from becoming a read-store port. | covered |
| `runtime.py` | composition authority | Binds the existing server authorities into one immutable app-scoped value; broken or duplicate composition fails closed at startup or request entry. | covered |
| `authorization.py` | authorization ruling | Resolves the one local operator on the server, keeps browser identity claims out of resolution, and fails closed off loopback. | covered |
| `dependencies.py` | consumption seam | Keeps child leaves off `app.state` and the composition; the only request fact used is the TCP peer. | covered |
| `router.py` | composition | Owns the single registration seam (runtime install plus root mount) and isolates later leaf ownership. | covered |
| `active/api.py` | implemented routes | Owns the two active production routes (page + resumable events) and the O4 typed-error ladder inside its seam. | covered |
| `library/api.py` | implemented routes | Owns the five native-library routes and the O4 error-status ladder inside its seam. | covered |
| `control/api.py` | implemented routes | Owns the seventeen control routes (interrupt, queue/withdrawal recovery, attachments, policy, telemetry) and the O4 error ladder inside its seam. | covered |

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Public route-registration facade. |
| `models.py` | [`models.py.md`](models.py.md) | covered | Stable normalized grammar and authority guards. |
| `response_contract.py` | [`response_contract.py.md`](response_contract.py.md) | covered | Declared HTTP response contract for the conversation surface. |
| `ports.py` | [`ports.py.md`](ports.py.md) | covered | Exact two-port read boundary. |
| `runtime.py` | [`runtime.py.md`](runtime.py.md) | covered | Immutable app-scoped composition authority. |
| `authorization.py` | [`authorization.py.md`](authorization.py.md) | covered | Server-resolved local-operator ruling. |
| `dependencies.py` | [`dependencies.py.md`](dependencies.py.md) | covered | Child-facing request dependency seam. |
| `router.py` | [`router.py.md`](router.py.md) | covered | Root child-router composition plus runtime install. |
| `active/__init__.py` | [`active/__init__.py.md`](active/__init__.py.md) | covered | Active route package marker. |
| `active/api.py` | [`active/api.py.md`](active/api.py.md) | covered | The two active production routes plus the O4 mapping authority. |
| `active/service.py` | [`active/service.py.md`](active/service.py.md) | covered | Per-app serving authority. |
| `active/projector.py` | [`active/projector.py.md`](active/projector.py.md) | covered | Per-session projection engine. |
| `active/store.py` | [`active/store.py.md`](active/store.py.md) | covered | Idempotent projection store. |
| `active/cursor.py` | [`active/cursor.py.md`](active/cursor.py.md) | covered | Signed page/event cursor authority. |
| `active/status.py` | [`active/status.py.md`](active/status.py.md) | covered | Canonical status service. |
| `active/capabilities.py` | [`active/capabilities.py.md`](active/capabilities.py.md) | covered | Exact-session capability evidence. |
| `active/factories.py` | [`active/factories.py.md`](active/factories.py.md) | covered | Running-session factory. |
| `projectors/__init__.py` | [`projectors/__init__.py.md`](projectors/__init__.py.md) | covered | Mapper protocol, channel bindings, registry. |
| `projectors/common.py` | [`projectors/common.py.md`](projectors/common.py.md) | covered | Strict parsing, output types, provenance builders. |
| `projectors/codex.py` | [`projectors/codex.py.md`](projectors/codex.py.md) | covered | Codex frame grammar. |
| `projectors/claude.py` | [`projectors/claude.py.md`](projectors/claude.py.md) | covered | Claude frame grammar + submission echo. |
| `projectors/pi.py` | [`projectors/pi.py.md`](projectors/pi.py.md) | covered | Pi entry/event grammar. |
| `library/__init__.py` | [`library/__init__.py.md`](library/__init__.py.md) | covered | Library route package marker. |
| `library/api.py` | [`library/api.py.md`](library/api.py.md) | covered | Five native-library routes plus the O4 mapping authority. |
| `library/service.py` | [`library/service.py.md`](library/service.py.md) | covered | List/read re-authorization orchestration. |
| `library/open_service.py` | [`library/open_service.py.md`](library/open_service.py.md) | covered | Idempotent exact open ledger/service. |
| `library/cursor.py` | [`library/cursor.py.md`](library/cursor.py.md) | covered | Signed cursor/key/resume-target authority. |
| `library/scope.py` | [`library/scope.py.md`](library/scope.py.md) | covered | Narrow-only canonical scope authority. |
| `library/gates.py` | [`library/gates.py.md`](library/gates.py.md) | covered | Live production-path capability gates. |
| `library/factories.py` | [`library/factories.py.md`](library/factories.py.md) | covered | Per-app shared bundle and caller-bound builders. |
| `library/helper_host.py` | [`library/helper_host.py.md`](library/helper_host.py.md) | covered | Locked helper process host. |
| `library/codex.py` | [`library/codex.py.md`](library/codex.py.md) | covered | Direct Codex app-server port. |
| `library/codex_normalize.py` | [`library/codex_normalize.py.md`](library/codex_normalize.py.md) | covered | Codex thread-item normalization. |
| `library/claude.py` | [`library/claude.py.md`](library/claude.py.md) | covered | Helper-backed Claude port. |
| `library/pi.py` | [`library/pi.py.md`](library/pi.py.md) | covered | Helper-backed Pi port. |
| `library/normalize_common.py` | [`library/normalize_common.py.md`](library/normalize_common.py.md) | covered | Shared normalization primitives. |
| `library/errors.py` | [`library/errors.py.md`](library/errors.py.md) | covered | Leaf-local typed error family. |
| `control/__init__.py` | [`control/__init__.py.md`](control/__init__.py.md) | covered | Control route package marker. |
| `control/api.py` | [`control/api.py.md`](control/api.py.md) | covered | The seventeen control routes plus the O4 mapping authority. |
| `control/service.py` | [`control/service.py.md`](control/service.py.md) | covered | Per-app control service authority. |
| `control/refs.py` | [`control/refs.py.md`](control/refs.py.md) | covered | Opaque signed control-reference authority. |
| `control/capabilities.py` | [`control/capabilities.py.md`](control/capabilities.py.md) | covered | Control-domain capability gate. |
| `control/operations.py` | [`control/operations.py.md`](control/operations.py.md) | covered | Exact-turn interrupt ledger. |
| `control/queue_projection.py` | [`control/queue_projection.py.md`](control/queue_projection.py.md) | covered | Source-aware queue projection. |
| `control/previews.py` | [`control/previews.py.md`](control/previews.py.md) | covered | Preview/digest transforms. |
| `control/withdrawals.py` | [`control/withdrawals.py.md`](control/withdrawals.py.md) | covered | Cockpit-only withdrawal + bounded recovery. |
| `control/recovery_assembly.py` | [`control/recovery_assembly.py.md`](control/recovery_assembly.py.md) | covered | Recovery content/digest/ref assembly. |
| `control/attachments.py` | [`control/attachments.py.md`](control/attachments.py.md) | covered | Typed attachment lifecycle. |
| `control/asset_spool.py` | [`control/asset_spool.py.md`](control/asset_spool.py.md) | covered | Confined staged-bytes filesystem boundary. |
| `control/policy.py` | [`control/policy.py.md`](control/policy.py.md) | covered | Read-only effective-policy projection. |
| `control/telemetry.py` | [`control/telemetry.py.md`](control/telemetry.py.md) | covered | Evidence-bound telemetry. |

## Evidence
- Retained reference account (no fresh execution or acceptance inferred): Cursor brands, identity bindings, strict wire configuration, provenance authority, and the sub-agent participant grammar are centralized in the contract module. [1]
- Retained reference account (no fresh execution or acceptance inferred): Canonical status, capability evidence, library agent rows, open rollback, withdrawal recovery, and fixture non-promotion are fail-closed products. [2]
- Retained reference account (no fresh execution or acceptance inferred): Exactly two read ports separate active exact-session reads from dormant native library reads. [3]
- Retained reference account (no fresh execution or acceptance inferred): Three owned child routers — all implemented, none behavior-empty — compose through one stable root that also installs the one runtime. [4]
- Retained reference account (no fresh execution or acceptance inferred): The immutable runtime/scope types, install-once binding, and fail-closed retrieval define the app-scoped composition authority. [5]
- Retained reference account (no fresh execution or acceptance inferred): The server-resolved local-operator resolver, loopback-only classification, and cross-principal rejection define the authorization ruling. [6]
- Retained reference account (no fresh execution or acceptance inferred): The two request dependencies are the only child-facing consumption seam and consult only the TCP peer. [7]
- Retained reference account (no fresh execution or acceptance inferred): `create_app` CONSTRUCTS the one runtime from existing authorities and hands it to the harness-control registration, which INSTALLS it exactly once through its single `register_conversation_routes(app, runtime)` call. [8]
- Retained reference account (no fresh execution or acceptance inferred): The strict response contract for the 25 conversation routes: the three shapes assembled at a route that had no model at all, plus the six `responses=` tables the child APIs spread. [9]

- App construction binds the shared authorities and local workspace resolver into one runtime. [10]
- Harness registration passes that runtime to the conversation root. [11]
- Root composes three children and installs before mounting. [12]
- Missing members, duplicate installation, and missing/foreign retrieval have distinct checks. [13]
- Local resolution checks literal loopback peers and exact operator/workspace bindings. [14]
- Request authorization consults only the ASGI client host. [15]
- Two canonical conversation read protocols coexist with separate control/catalog seams. [16]
- Child-history hydration is the third active route; typed child outcomes use HTTP 200. [17]
- SSE emits replay then live frames, closes on gap and detaches. [18]
- Active cursor verification checks purpose, signature, caller and exact identity. [19]
- Library cursor verification checks typed purpose and signed envelope. [20]
- Wire base forbids extras and freezes attributes; opaque brands require a prefix. [21]
- Supported/partial evidence products require runtime-fixture tier and fixture identity. [22]
- Unknown input and terminal-controlled input have different provenance predicates. [23]
- Waiting/terminal products and unknown-ready rejection are explicit model predicates. [24]
- Library promotion follows successful Codex or helper probe, retaining failure uncertainty. [25]
- Claude interrupt is supported while image and policy remain unverified. [26]
- Eve has supported interrupt and policy, unavailable assets and telemetry. [27]
- Active dispatch includes Eve and delegates its interrupt verdict. [28]
- Codex library initialize uses and validates the same Agents Remember client identity. [29]
- Open rollback validators distinguish opened, no-launch and identity-mismatch predicates. [30]
- Queue withdrawal identity is restricted to queued cockpit rows. [31]
- Successful withdrawal alone has a recovery body; pending projection has references/expiry. [32]
- Interrupt acknowledgement/settlement and terminal timestamps form validated products. [33]
- Outcome response tables explicitly retain same-status refusal members. [34]
- Session-direct question response belongs to harness control for lifecycle-free seats. [35]
- Blocking active resolution is offloaded before epoch comparison. [36]
- Control catalog and epoch resolution are offloaded. [37]
- Recovery and staged-asset leases are 900 seconds. [38]
