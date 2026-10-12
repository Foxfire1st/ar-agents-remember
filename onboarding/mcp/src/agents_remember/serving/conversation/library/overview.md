# Native Conversation Library Route Overview

## Purpose

This area implements the dormant native conversation library for Codex, Claude, and Pi: authorized catalog listing, historical reading, and reopening a selected native conversation through a tracked AR control session. Native stores remain the history authority. The library maintains no durable conversation index and does not own active vendor-event projection, browser or Toad state, or in-place process identity switching.

Reopening exists to resume and prove one exact native identity. A launch request or deterministic session identifier is insufficient proof. The operation becomes `opened` only after readiness supplies the requested vendor identity and the service reads a bridge epoch through the runtime control-plane port. Unknown identity remains reconcilable; a proven mismatch triggers ownership-aware retirement.

Authorization belongs to the server-resolved caller binding, not possession of a signed key or cursor. The inherited policy is narrow-only project access and capability-gated native operations. Present enforcement is distributed: list derives a filesystem-canonical scope; key resolution checks the signed authorization and harness and recomputes the identity digest from signed identity fields; ports validate paging scope and observed generation; read and a newly driven open check their respective capability features. This is narrower than saying every operation repeats every filesystem, generation, and capability check.

## Hot Path Summary

The five routes share `/api/harnesses/{harness_id}/conversations`: list, historical read, open, open-status, and open-reconcile. Each handler resolves runtime and authorization, narrows the harness to Codex/Claude/Pi, and builds a caller-bound service over shared app-runtime authorities. List and read default to 50 items and cap requests at 100.

List derives the canonical scope, checks `capabilities.list`, and delegates to a harness port. The port validates an optional list cursor, obtains native catalog evidence, checks the cursor generation against its observed signature, and mints rows and continuation tokens.

Read resolves the conversation key before checking `capabilities.read`. Key resolution validates token shape/signature, exact caller authorization, harness, and the identity digest derived from harness/vendor/signed project scope. It constructs a native reference from those fields; it does not itself inspect the live native store or compare the key's catalog generation against a freshly listed catalog. The port reads native history and validates an optional read cursor against scope and its read-generation signature. Pages contain chronological newest windows, 1-based ordinals within the observed native sequence, a total count for that sequence, and an older-page cursor when available.

Open requires `expectedIdentityDigest`. It resolves the key, compares the expected digest, and, when cwd is supplied, canonicalizes that cwd against the runtime workspace and requires equality with the key's project scope. A fingerprint binds operation kind, caller authorization, harness, exact conversation key, digest, canonical project scope, and launch context. Under the ledger lock, a retained identical request returns its operation; a changed fingerprint conflicts. Raw cwd spelling is not fingerprinted: equivalent supplied paths can resolve to the same canonical scope.

A newly admitted operation checks resume capability, asks the port for a server-private target, verifies its token and vendor identity, and validates supported launch material. Claude uses `--resume`; Pi uses `--session` with the resolved session file; Codex uses the tracked opener's `resume_thread_id` channel. The service records whether a live deterministic session lane already exists, calls the tracked opener, and sets `launched` only after the opener returns an opened catalog entry. Readiness is bounded, with a default proof wait of 45 seconds.

Status and reconcile re-authorize the conversation key and require a retained operation matching the harness and exact key. They observe launched unresolved work without launching another operation. Reconcile additionally retries eligible retirement. `timeout-unknown` remains nonterminal and reconcilable. Pre-launch polls do not interpret an absent catalog row as failure.

## Construction And Ownership

`api.py` owns route declarations, request parsing, camel-case serialization, and the typed refusal-to-HTTP mapping. Request bodies forbid extra fields; optional launch context contains a canonical `TaskDocumentRef` and `seatRole`. All handlers construct `JSONResponse` objects. Their response-model declarations describe the OpenAPI surface; they do not themselves validate those already-constructed response bodies.

`service.py` owns list/read orchestration and conversation-key authorization. `scope.py` owns list ordering (`last-activity-desc`), canonical project scope, query digest, and page-size bounds. Requested paths resolve through symlinks, must be existing directories within the resolved workspace root, and fail with a typed scope refusal on malformed paths or escape. This is a workspace containment predicate, not an additional repository-membership check.

`factories.py` memoizes `LibraryShared` by exact runtime in a locked weak-key map. The shared bundle contains one random cursor signing key, gate registry, helper host, and open ledger. Ports and services are built for each caller. This avoids rebuilding signing/operation state per request or sharing an authority bundle across unrelated runtimes. `LibraryBinding(runtime, shared, authorization)` makes the per-app/per-caller split explicit; `OpenRequest` keeps the caller's idempotent request inputs together.

`cursor.py` owns list/read cursors, conversation keys, resume targets, identity digests, and signature-derived catalog generations. Tokens contain canonical JSON protected by HMAC-SHA256 under a per-runtime-bundle key that is not persisted. Restarting with a new key invalidates outstanding tokens and requires native re-listing. List/read cursor payloads include signed purpose bindings. The external token prefix is checked separately and is not included in the MAC input; conversation keys and resume targets use key bindings without a signed purpose field. Keep the inherited server-private resume-target boundary explicit rather than treating prefix branding alone as cryptographic separation.

`gates.py` discovers installed harnesses and caches one result per normalized harness and executable fingerprint. The fingerprint uses resolved executable path, size, and modification time. Unknown or absent harnesses return unavailable capabilities; typed production-probe failures return unverified capabilities with their reason. Codex proves connection, initialization, and `thread/list(limit=1)`; Claude/Pi prove helper preflight, correlated handshake, and a native helper `list(limit=1)`. Those successes select capability products advertising list/read/resume support. They are not separate read or resume probes on every call. Cached gates likewise do not constitute a fresh operation probe for every request.

Observed runtime/helper versions are informational, following the named `260718-CHATS-L5F R4` contract-only decision. Locked version constants and version-bearing success text remain provenance or explanatory strings, not observed-versus-locked capability predicates. Codex and Claude advertise partial history/tool completeness; Pi advertises supported completeness. Pi's actual read implementation uses `SessionManager.getBranch()`, so its page is the current branch sequence, not demonstrated coverage of every append-only entry on every branch.

`codex.py` opens short-lived direct app-server connections. Its default resolver uses the native-PATH seam; the probe also supplies a native-path environment. Native executable resolution rejects incompatible Windows interop paths on POSIX. Resolver `RuntimeError` within `_AppServer.__aenter__` and path-resolution failures become `LibraryStoreError`; this is not a claim that every surrounding environment-construction failure is converted at that same point. The connection sends the Agents Remember client name/version and requires the shared initialize validator's exact client suffix. The validator accepts a parsed server-product name as diagnostics, extracts its reported version, and requires codexHome/platform fields; it does not require `Codex Desktop` as the product name.

`AppServerSeams` now includes environment, transport factory, and executable resolver. Its frozen default represents production behavior. `GateProbes` groups Codex probing, executable lookup, and environment access. The inherited intent is to substitute a coherent machine/process seam, avoiding mixed fake/live environments; the dataclasses are dependency bundles, not runtime enforcement that every member must be replaced together.

`claude.py` and `pi.py` use `helper_host.py` and repository-owned Node helpers under `mcp/native_helpers/conversation_library/`. Each call performs spawn, handshake, one operation, and exit using `node --import tsx` from the helper package. No cache/global-module discovery is delegated to these ports. The host validates protocol, correlation, response shape, and required observed version fields; the operation result decides success. A version mismatch alone does not reject the surface. Missing runtime/helper prerequisites, malformed responses, timeout, process failure, and unsupported operations produce typed failures. Raw process stderr is withheld.

The Claude helper lists scope-exact SDK sessions with `includeWorktrees: false`, sweeps their sub-agent directories, and carries enumeration evidence even for an empty catalog. Sub-agent identity is the composite `<sessionId>/<agentId>`; optional native metadata supplies description, type, model, `toolUseId`, and spawn depth. Missing metadata retains an honest `agent <short-id>` title rather than inventing a name or requiring a join key. Malformed metadata fails closed. Main history uses SDK messages; sub-agent history reads native JSONL. Both return ordinal windows over the sequence they actually obtained. Claude explicitly refuses resume-target resolution for composite sub-agent identities.

Codex requests top-level kinds `cli`, `vscode`, `exec`, and `appServer`, plus a separate bounded page of `subAgent`, `subAgentReview`, `subAgentCompact`, `subAgentThreadSpawn`, and `subAgentOther`. It groups children by native `parentThreadId` without experimental parent-list filters. Native RPC refusal of agent enumeration becomes an exact `agents_note`; transport failure remains a store error. The agent fetch cap is 100, with a truncation note on continuation. Detected nested agents whose parents are agents are not shown and are named in the note. Claude instead shows detected depth>1 agents flat under the top-level session and explains that limitation. Missing Claude enumeration evidence produces an unavailable note, including on an empty catalog.

`codex_normalize.py`, the Claude/Pi parsers, and `normalize_common.py` normalize native history into shared conversation models. Native provenance stays `native-only`, with producers named only where justified. Unknown vendor kinds/content remain explicit `unknown-vendor` evidence. Shared text capping uses 8192 characters plus a visible truncation marker. Codex flattens native turns/items; Claude uses native UUID/message records; Pi retains native entry identifiers and branch ordinals. This area does not infer missing vendor history or promote native evidence into AR-authored provenance.

Wire grammar and operation products now live in `models/conversations/`, including history, cursors, identity, and opening. The canonical library port lives in `serving/ports.py`; runtime and authorization dependencies remain in the parent conversation area. The tracked opener, readiness, control-plane authority, and retirement modules retain lifecycle ownership. File sidecars and the parent overview provide the preserved route map; this proposal does not replace their coverage metadata.

## Invariants And Boundaries

A token is never authorization. Preserve the caller-binding, harness, scope, purpose, signature, and observed paging-generation predicates at their actual owners. List re-derives filesystem scope; read/key resolution uses the signed scope; an explicitly supplied open cwd must match that scope. The key's identity digest is an HMAC over identity fields, not a live-native-store freshness probe. Native presence/readability is subsequently established by the port operation.

Generation means a digest of selected observable signature fields, not a durable counter, full-store index, or proof that every possible native edit is detected. Codex list generation samples the first 100 top-level IDs, continuation presence, fetched agent IDs, and enumeration note. Codex read generation includes vendor ID, item count, and updatedAt. Claude/Pi helpers similarly sign selected IDs, modification values, lengths, and tail identities. Paging resets when these signatures differ; edits outside those observables need not change the generation.

The in-memory open ledger defaults to 256 records. Access updates LRU order; admission evicts terminal records and refuses when every retained record is live or unresolved. Idempotence is guaranteed by retained request state within this app lifetime, not an eternal durable one-launch receipt. Restart or terminal eviction removes the retained operation. `pending` and `timeout-unknown` are nonterminal; successful and failed terminal outcomes are eviction candidates.

The deterministic `ar-open-<digest>` identifier is replay keying, never evidence of launch. `launched` authorizes proof observation and retirement. `absorbed_existing` protects a pre-existing live session from retirement regardless of proof outcome. A matching absorbed session may settle opened; a mismatching one fails `launch-failed` and remains untouched. Failed or mismatching record-owned launched sessions use the retirement authority. Retirement is idempotent after completion; an absent row does not falsely mark retirement complete, and published identity can carry `retire-pending` or `retire-failed` for reconcile. Pre-identity launch failure can keep wire rollback `not-needed` while server-side retirement is attempted, as required by the landed operation product.

Readiness rereads catalog identity after observing the bridge, comparing session ID, tmux name, and creation time. Locally, the library settlement compares the observed vendor ID with the requested vendor ID and then reads the bridge epoch. It constructs the active reference with the requested harness and scope. Preserve the inherited exact session/harness/vendor/epoch intent, but this local construction is not itself an independent comparison of every requested identity component; downstream authority validation remains a separate boundary.

A ready bridge without a published vendor identity proves neither match nor mismatch. The operation stays `timeout-unknown` and reconcilable without retirement. Failed control or terminated/unknown launched sessions take ownership-aware failure handling.

The open route deliberately supplies `legacy_launch_capsule` with `LIBRARY_REOPEN_LEGACY_REASON`, preserving the named `260915-CAPS-L15` decision. A capsule delivered to a Codex thread this session did not open has unknown applied revision; the current refresh plan selects `FRESH_THREAD`, and request construction drops `threadId`. That would destroy the exact-reopen proof this route exists to obtain. This is a reasoned route-specific exception, not an unspecified missing capsule. The inherited owner of a future capsule-carrying reopen is the final-verification leaf with the harness delivery leaves that own thread lifecycle.

The inherited policy that sub-agent histories have no native resume target is explicit in Claude's resolver. Codex's local resolver instead calls `thread/read(includeTurns=False)` and mints a `codex-thread-resume` target without a source-kind-specific refusal there. Preserve the cross-harness no-resume statement as inherited intent with this implementation difference; do not infer that every downstream Codex launch path permits or refuses sub-agent resume from this function alone.

Routine typed refusals map subclass-before-base to 400/403/404/409/422/503; unexpected exceptions remain loud. Range-absurd Codex/Claude timestamps and selected malformed native shapes have typed store-error conversions, rather than a blanket guarantee for every possible exception. The open outcome map directly indexes all eight declared outcomes: opened→201; pending/timeout-unknown→202; unsupported→422; stale-identity/request-conflict/identity-mismatch→409; launch-failed→503. Keep that map total when changing the outcome model. The open response declarations union operation and refusal shapes on overlapping statuses so dict merging does not erase the refusal family. Null identity/cursor fields remain meaningful on the wire.

Resume targets remain server-private and must not be placed on public wire models, logs, or diagnostics. The helper timeout is 30 seconds; its 64 MiB stdout limit is checked after `communicate()` has collected the response. This is a post-collection rejection, not a streaming memory bound. Retain the named O3 acceptance and O1 token-prefix hardening limit rather than silently strengthening the implementation claim.

## Historical And Verification Limits

This is a source-only adjudication at the stated code head. No tests, harnesses, helpers, app-server connections, or delivery gates were executed. Source predicates and capability reason strings are not fresh acceptance evidence.

The inherited card records six focused suites, a foundation pin, installed-runtime production gates, and two real open E2Es. It also names artifacts retired in the `d3610903` suite reduction: the installed Codex 0.144.5 runtime fixture and native-history/list-read-resume evidence. Those removed witnesses are not present execution receipts and cannot establish current installation support or capability enablement. Preserve the named historical evidence and its retirement limit without claiming it still proves the route today.

The `260731-EFA-L2` history explains the per-app/per-caller binding, grouped open request, coherent substitution seams, and removal of an obsolete `ToolPhase` Ruff suppression when the target matched Python 3.11. `260731-EFA-L4` explains response-shape declarations and deletion of the silent unmapped-outcome 500 fallback. Its named `test_serving_response_conformance.py::DeclaredSurfaceCoverageTests::test_the_open_status_map_is_total_over_the_declared_outcomes` and `ConversationSuccessConformanceTests` are inherited verification references, not results from this pass. The inherited harness-specific failure legs remain declared-and-undriven with recorded reasons; this proposal does not recreate unavailable reasons or upgrade those legs to exercised evidence.

The `260731-EFA-L9` history moved wire contracts and the canonical port out of the former monolith; current imports determine their present locations. `260731-EFA-L23` made native executable resolution a Codex seam and server-product diagnostics non-authoritative, superseding the contradictory Desktop-only prose while retaining the exact client-suffix requirement.

The Codex source-kind comments retain a named historical installed Codex 0.145.0 probe on 2026-07-26 and a vendor enum witness; Claude's slug comments retain SDK 0.3.207/live-directory provenance. Those old external/vendor/live witnesses were not independently examined here. Current request kinds, slug construction, and failure behavior are source-visible, but their installed-vendor compatibility remains a historical claim until separately verified.

The CAPS-L15 whole-production-launch-site enumeration claim and named `test_every_production_launch_request_site_is_wired_or_declares_its_legacy_chain` remain inherited verification context. This pass confirms this route's explicit legacy reason and the current Codex fresh-thread mechanism, not an exhaustive audit of every production launch site.

The inherited O1 limit is that the external token prefix is not MAC-covered; O3 is the helper response-size check after collection. F1/O5 distinguish session-ID presence from launch evidence; F1b refuses a false retirement tombstone on an absent row; F5 protects absorbed pre-existing sessions; F2/F3/F4 concern malformed paths, payload shapes, and timestamp ranges; O4 concerns precise routine-refusal mapping and settling an escaping open-drive fault. These named responsibilities remain visible without converting historical reviews into current execution verdicts.

The inherited resolved-memory claims of no permitted neighboring repository and an empty Domain Documentation registry were not re-resolved in this source-only pass. No cross-repository implementation or external documentation is introduced as evidence here. The old partitioned-curation refresh note is pass context, not product behavior or an instruction authority. Existing status, coverage, route metadata, excluded tables, and reference identities remain under parent preservation.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/library/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/library/overview.md` |
| parentOverview | [`conversation/overview.md`](../overview.md) |

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `api.py` | route/mapping authority | Keeps every typed refusal on its precise HTTP status; a raw 500 here violates the O4 contract. | covered |
| `service.py` | authorization orchestration | The one boundary where every list/read re-authorizes before any native store is touched. | covered |
| `open_service.py` | open authority | Guarantees one launch per stable requestId, exact catalog proof, and no wrong retirement. | covered |
| `cursor.py` | token authority | Every opaque token's mint/verify boundary; tampering or cross-purpose use fails closed. | covered |
| `scope.py` | scope authority | The narrow-only canonical scope and query digest every cursor/key binds. | covered |
| `gates.py` | capability authority | Capability honesty: supported only when the live production-path CONTRACT probe passes; no version comparison gates or demotes. | covered |
| `factories.py` | composition | Per-app shared bundle without `app.state` edits or import-time singletons. | covered |
| `helper_host.py` | helper boundary | Locked spawn/handshake/exit discipline; raw helper stderr never disclosed. | covered |
| `codex.py` | codex port | Direct read-only app-server list/read/resolve with honest partial completeness. | covered |
| `codex_normalize.py` | codex parser | Exact provenance normalization; unknown vendor kinds become explicit evidence, never guesses. | covered |
| `claude.py` | claude port | Helper-backed list/read/resolve; the per-spawn handshake reports observed versions informationally (no version gate). | covered |
| `pi.py` | pi port | Helper-backed list/read/resolve; reading never calls `switch_session` on any process. | covered |
| `normalize_common.py` | shared primitives | One home so the three resolvers cannot drift apart. | covered |
| `errors.py` | typed family | Leaf-local errors the route table maps exactly; parallel leaves stay collision-free. | covered |

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Library route package marker. |
| `api.py` | [`api.py.md`](api.py.md) | covered | Five library routes plus the O4 error-status ladder. |
| `service.py` | [`service.py.md`](service.py.md) | covered | List/read re-authorization orchestration. |
| `open_service.py` | [`open_service.py.md`](open_service.py.md) | covered | Idempotent exact open ledger/service. |
| `cursor.py` | [`cursor.py.md`](cursor.py.md) | covered | Signed cursor/key/resume-target authority. |
| `scope.py` | [`scope.py.md`](scope.py.md) | covered | Narrow-only canonical scope authority. |
| `gates.py` | [`gates.py.md`](gates.py.md) | covered | Live production-path capability gates. |
| `factories.py` | [`factories.py.md`](factories.py.md) | covered | Per-app shared bundle and caller-bound builders. |
| `helper_host.py` | [`helper_host.py.md`](helper_host.py.md) | covered | Locked helper process host. |
| `codex.py` | [`codex.py.md`](codex.py.md) | covered | Direct Codex app-server port. |
| `codex_normalize.py` | [`codex_normalize.py.md`](codex_normalize.py.md) | covered | Codex thread-item normalization. |
| `claude.py` | [`claude.py.md`](claude.py.md) | covered | Helper-backed Claude port. |
| `pi.py` | [`pi.py.md`](pi.py.md) | covered | Helper-backed Pi port. |
| `normalize_common.py` | [`normalize_common.py.md`](normalize_common.py.md) | covered | Shared normalization primitives. |
| `errors.py` | [`errors.py.md`](errors.py.md) | covered | Leaf-local typed error family. |

## Evidence
- Retained reference account (no fresh execution or acceptance inferred): The declared reason and the explicit legacy declaration on the launch. [1]
- Retained reference account (no fresh execution or acceptance inferred): The refresh plan that makes a capsule-carrying reopen a fresh thread. [2]
- Retained reference account (no fresh execution or acceptance inferred): The identity proof the reopen exists for, which the exclusion protects. [3]
- Retained reference account (no fresh execution or acceptance inferred): The cases pinning the declaration and the whole-site enumeration. [4]
- Retained reference account (no fresh execution or acceptance inferred): The dormant library read port defines scoped list, historical read, and server-private resume-target resolution. [5]
- Retained reference account (no fresh execution or acceptance inferred): The L0 request dependencies are the only consumption seam the handlers use. [6]
- Retained reference account (no fresh execution or acceptance inferred): The tracked opener absorbs identical replays through the live catalog row and carries the codex-only `resume_thread_id`. [7]
- Retained reference account (no fresh execution or acceptance inferred): The locked Claude and Pi helpers dispatch list, read, and resume operations through their request handlers. [8]

- Five routes resolve runtime/caller, declare response shapes, serialize JSONResponse, and use a total outcome map plus ordered typed refusal mapping. [9]
- List canonicalizes requested scope; key resolution checks signed caller/harness/digest; read checks its feature before delegating. [10]
- Requested cwd must resolve to a directory inside workspace root; query digest binds harness/scope/sort and page limits are bounded. [11]
- Authorities are memoized per runtime and caller-bound ports/services are constructed separately. [12]
- Cursor purposes are signed in their binding; external prefixes are checked separately from the canonical payload MAC. [13]
- Gate success comes from connect/list or helper list; normalized cache entries use executable fingerprints, and successful products advertise broader features. [14]
- Helper operation success is checked after correlated handshake; timeout and byte rejection are explicit, with byte checking after collection. [15]
- Open idempotence is retained-state fingerprinting over canonical scope and launch context; terminal records can be evicted. [16]
- Resume preparation, explicit legacy launch, launched marker, bounded proof, and ownership-aware retirement remain separate predicates. [17]
- Initialize accepts a parsed diagnostic product and exact client suffix, with required home/platform fields. [18]
- Native resolver is a third Codex seam; agent enumeration is bounded/noted and Codex local resume target resolution does not distinguish source kinds. [19]
- Codex generation signatures use sampled IDs/notes or count/update fields rather than the complete store. [20]
- Claude rejects composite-agent resume and distinguishes missing enumeration proof from known empty enumeration. [21]
- Claude helper lists exact scope without worktrees, allows absent metadata with honest fallback, and reads main versus agent history separately. [22]
- Pi history and total count come from the current branch; target resolution locates the native session file within scoped listing. [23]
- Unknown-revision resumed Codex threads become fresh when capsule delivery is present, and request construction drops threadId. [24]
- Readiness rejects catalog replacement and requires ready control plus acceptable submission state. [25]
- Overlapping open statuses declare operation/refusal unions; operation models constrain phase/outcome and complete identity products. [26]
- Normalization retains native-only provenance, visible text capping, native ordinals, and explicit unknown-vendor evidence. [27]
