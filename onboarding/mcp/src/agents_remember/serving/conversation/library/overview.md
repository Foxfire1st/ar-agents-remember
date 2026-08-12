# Native Conversation Library Route Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/library/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/library/overview.md` |
| parentOverview | [`conversation/overview.md`](../overview.md) |
| lastUpdated | 2026-08-12T04:15+02:00 |
| lastVerifiedCommitHash |  `65cb81f7de4db13c0627264fec1eb46f444e0ee3`|
| lastVerifiedCommitDate |  2026-08-12T04:57:26+02:00|

## What This Area Is

This route is the implemented dormant native conversation library.
It exposes each normalized harness's (Codex, Claude, Pi) native conversation catalog and history
through an authorized read-only library, and opens a selected native identity as a new
idempotently tracked AR control session only after exact catalog proof. Every list/read/open
call re-authorizes: the server-resolved caller binding is checked against the token-bound scope,
the canonical project scope is re-derived narrow-only, the identity digest is recomputed from
native identity, and the harness's live production-path gate must report the feature
`supported` before any native store is touched.

This is deliberately a read-and-open route. It keeps no durable conversation index, projects no
active vendor events, never mutates a running process identity (`switch_session`), and never
touches browser or Toad state. Codex reads are direct app-server connections; Claude and Pi
reads run through the repository-owned locked helpers under
`mcp/native_helpers/conversation_library/`. Each Codex connection accepts only the current
`Codex Desktop/<version>` initialize product whose diagnostics end in the exact client name and
version sent by the library; that primary Desktop version remains the thread/runtime identity.

## Hot Path Summary

Start with `api.py` for the five routes and the exact typed-error→HTTP mapping. `service.py`
re-authorizes every list/read, `open_service.py` owns the idempotent exact open plus bounded
operation ledger, `cursor.py` mints/verifies every signed token, `scope.py` derives the
narrow-only canonical scope, `gates.py` runs the live capability gates, and `factories.py`
holds the per-app shared bundle. `codex.py`/`claude.py`/`pi.py` are the three dormant resolver
ports; `helper_host.py` runs the locked Node helpers; `errors.py` is the leaf-local typed
family.

## What Belongs Here

| Path | Role |
| --- | --- |
| `api.py` | The five library routes (list/read/open/open-status/open-reconcile) plus the reviewer-O4 error-status ladder. |
| `service.py` | Per-call list/read re-authorization and capability orchestration. |
| `open_service.py` | One stable requestId + fingerprint open ledger, launch, exact catalog proof, honest retirement. |
| `cursor.py` | The one mint/verify boundary for list/read cursors, conversation keys, and server-private resume targets. |
| `scope.py` | Narrow-only canonical project scope, query digest, and bounded page sizes. |
| `gates.py` | Live production-path capability gates cached per installed-executable fingerprint. |
| `factories.py` | Per-app weak-key `LibraryShared` bundle and per-request caller-bound port/service builders. |
| `helper_host.py` | Python host for the locked repository helpers: spawn, handshake, one operation, exit. |
| `codex.py` | Direct Codex app-server list/read/resolve port plus the gate probe; also the probe-proven `subAgent*` source-kind agent listing grouped under each parent row with an honest `agents_note`. |
| `codex_normalize.py` | Codex thread-item → normalized `ConversationItem` parser. |
| `claude.py` | Locked-helper Claude list/read/resolve port; also the meta-bound `subagents/*.jsonl` sub-agent rows and reads. |
| `pi.py` | Locked-helper Pi list/read/resolve port. |
| `normalize_common.py` | Shared text-capping, provenance, required-field, and content-extraction primitives. |
| `errors.py` | Leaf-local typed error family mapped by the routes. |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Strict wire grammar, cursor brands, and operation products | `mcp/src/agents_remember/serving/conversation/models.py` (the parent contract route). |
| Runtime composition, authorization ruling, and request dependencies | `mcp/src/agents_remember/serving/conversation/` (consumed, never edited). |
| Locked Claude/Pi helper implementations and protocol | `mcp/native_helpers/conversation_library/`. |
| Tracked opener, retirement mechanics, and catalog/readiness authorities | Existing serving modules (`terminal_opener.py`, `retire.py`, `hosted_readiness.py`). |
| Any durable conversation index, browser projection, or in-place identity mutation | Nowhere; these are explicitly forbidden. |

## Structures Found Here

- Five FastAPI routes on the prefix `/api/harnesses/{harness_id}/conversations`, with strict
  extra-forbid request bodies and one camel-case serialization point.
- A leaf-local typed error family subclassing the shared `agents_remember.errors` types, mapped
  subclass-before-base to one precise HTTP status each (no raw 500 for routine refusals).
- Purpose-branded, HMAC-SHA256-signed opaque tokens whose signing key is per-app and never
  persisted; a restart invalidates outstanding tokens honestly.
- A content-derived catalog generation (no server-side counter or index) that resets cursors
  when the native store observably changes.
- Live capability gates (contract-only): Codex proves `thread/list` over
  a real app-server connection (the observed CLI version rides the evidence as informational metadata
  only — never compared to a locked constant); Claude/Pi prove the helper handshake plus a real native
  `list` call, where the OPERATION result is the gate and the handshake reports observed versions
  informationally. Results are cached per installed-executable fingerprint, bounded by the three
  normalized harnesses.
- A bounded (256) in-memory open-operation ledger keyed by caller principal + requestId with
  LRU terminal eviction and a hard refusal when full of live work.
- An explicit `launched` authority plus an `absorbed_existing` spawn-ownership discriminator on
  every open record, so pre-launch polls never settle and foreign pre-existing sessions are
  never retired.
- First-class sub-agent rows: codex lists the probe-proven `subAgent*`
  source kinds (`subAgent`, `subAgentReview`, `subAgentCompact`, `subAgentThreadSpawn`,
  `subAgentOther`) and groups agent rows under their parent row client-side; claude enumerates
  meta-bound `subagents/*.jsonl` transcripts keyed by `toolUseId`. Missing enumeration proof
  surfaces as an exact `agents_note` — never a silent absence — truncation and nested (depth>1)
  agents are named in the note, and sub-agent identities fail closed (no native resume target,
  no fabricated names: the honest `agent <short-id>` fallback).

## Operating Model

1. Each handler resolves the runtime and authorization through the same two request
   dependencies, narrows the raw harness id, and builds caller-bound services from the per-app
   shared bundle.
2. List/read re-derive the canonical scope, re-check the live gate, verify cursor/key purpose,
   signature, scope binding, and catalog generation, then delegate to the dormant port.
3. Open resolves the conversation key, checks the expected identity digest and optional cwd
   narrowing, accepts only the canonical task-document reference plus role as optional launch
   context, and records one immutable fingerprint per (principal, requestId); identical
   replays return the retained operation, changed fingerprints conflict without launching.
4. The drive gates resume support, resolves and verifies the server-private resume target,
   launches a NEW tracked session through the existing shared opener (argv `--resume`/
   `--session` for Claude/Pi, `resume_thread_id` for Codex through the landed opener channel), and
   waits bounded for exact catalog proof (session id + harness + vendor identity + bridge
   epoch).
5. Status/reconcile re-authorize and re-observe; timeout stays `timeout-unknown` and
   reconcilable; failed or mismatched record-spawned sessions are retired idempotently with an
   honest rollback state.

## Main Flows

### Authorized native list

1. `canonical_library_scope` narrows the requested cwd inside the caller's workspace root;
   traversal, symlink escape, and malformed paths fail closed as `LibraryScopeError`.
2. The live gate must report `list` supported, else `LibraryCapabilityError` → 422 with the
   exact contract-probe-failure reason (never a version-comparison reason).
3. The port verifies the signed list cursor (purpose, scope, generation) and pages the native
   store, minting rows whose conversation keys bind scope, vendor identity, identity digest,
   and generation.

### Authorized historical read

1. `resolve_key` re-authorizes the opaque conversation key and recomputes the identity digest;
   a changed native identity fails as `stale-identity`.
2. The gate must report `read` supported; the port verifies the read cursor and returns a
   newest-window page with stable 1-based global ordinals, an honest `totalItems`, and an
   older-page cursor.

### Idempotent exact open

1. `open()` re-authorizes the key, compares the caller's expected digest, fingerprints the
   immutable request, and dedupes under the ledger lock.
2. `_prepare` resolves and verifies the resume target (kind `argv` or codex-only
   `codex-thread-resume`, both validated); `_launch` records spawn ownership before calling the
   tracked opener with the deterministic `ar-open-<digest>` session id.
3. `_prove` waits bounded for readiness and settles: exact vendor identity → `opened` (201);
   proven mismatch → `identity-mismatch` plus real retirement of the record-spawned session;
   absorbed foreign sessions fail honest `launch-failed` and are never retired; otherwise
   `timeout-unknown` (202), reconcilable by status/reconcile.

## Load-Bearing Files

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

## Local Invariants And Traps

- Possession of a cursor/key is never authorization: every call re-resolves the caller binding
  and re-checks scope, purpose, and catalog generation.
- Capability `supported` requires the live production-path CONTRACT probe to pass; a failed probe
  demotes the whole harness history surface with the exact probe-failure reason. NO version-string
  comparison gates or demotes any capability — the observed version is informational evidence.
- The deterministic open session id is replay keying, never launch evidence; only `launched`
  authorizes proof observation and retirement, and `absorbed_existing` sessions are never
  retired whatever they prove.
- `ready` without a published vendor identity can neither prove nor disprove an open; the
  record stays reconcilable and the session is not retired.
- Range-absurd but type-valid native timestamps and shape-skewed native payloads fail as typed
  `LibraryStoreError` (503), never raw 500s (review F2/F3/F4 fixes).
- Resume targets are server-private; they must never appear on any wire model, log, or
  diagnostic (review O1 hardening note: the token purpose prefix is not MAC-covered).
- The helper response byte bound is checked after `communicate()` returns (review O3); the
  helper is repository-owned and locked, so the practical risk is accepted for this leaf.
- Library cursors/keys are non-interchangeable with the active cursor family, and the
  `library-list`/`library-read` purposes are non-interchangeable with each other.
- **`_OPEN_STATUS_BY_OUTCOME` must stay TOTAL over `OpenConversationOperation.outcome`.** Since
  260731-EFA-L4 `_open_call` indexes it directly (`_OPEN_STATUS_BY_OUTCOME[operation.outcome]`)
  instead of the old `.get(operation.outcome, 500)`. A ninth outcome added without a status is now
  a loud `KeyError` at the one place that can fix it; before, it answered **500 carrying a full
  operation body** — a shape no `responses` table declares, on a status no test could ever drive,
  silently. `test_serving_response_conformance.py::DeclaredSurfaceCoverageTests
  ::test_the_open_status_map_is_total_over_the_declared_outcomes` asserts set equality between the
  map's keys and the `Literal`'s eight members, which is what makes the direct index safe.

## Repo-Internal References

The parent contract route supplies the wire grammar and the two-port split this slice
implements; the composition supplies the runtime, authorization, and dependency seams; the
tracked opener/readiness/retire authorities execute the open. Six new test suites plus the
foundation pin prove the contract on doubled boundaries, and the installed-runtime suite proves
the live gates and both real open E2Es.

| Finding | Anchor | Source |
| --- | --- | --- |
| The dormant library read port defines scoped list, historical read, and server-private resume-target resolution. | `ConversationLibraryPort` | mcp/src/agents_remember/serving/ports.py:93-118 |
| The L0 request dependencies are the only consumption seam the handlers use. | `get_conversation_runtime`; `resolve_conversation_authorization` | mcp/src/agents_remember/serving/conversation/dependencies.py:21-23; mcp/src/agents_remember/serving/conversation/dependencies.py:26-36 |
| The tracked opener absorbs identical replays through the live catalog row and carries the codex-only `resume_thread_id`. | `open_terminal_session` | mcp/src/agents_remember/serving/terminal_opener.py:678-730 |
| The locked Claude and Pi helpers dispatch list, read, and resume operations through their request handlers. | `handleClaude`; `handlePi` | mcp/native_helpers/conversation_library/src/claude.ts:65-78; mcp/native_helpers/conversation_library/src/pi.ts:54-67 |
| The foundation pin asserts exactly the five owned library routes and the helper source set. | `test_exactly_two_conversation_ports_exist`; `test_root_composes_three_owned_child_routers`; `test_helper_package_and_lock_select_only_the_exact_repository_dependencies` | mcp/tests/test_conversation_foundation.py:22-29; mcp/tests/test_conversation_foundation.py:32-107; mcp/tests/test_conversation_foundation.py:125-136 |
| The five route declarations, the total (no-`.get`-default) `_OPEN_STATUS_BY_OUTCOME`, and the `_error_response`/`_ERROR_STATUS_TABLE` mapper the shared refusal table transcribes. | `api_library_list`; `api_library_read`; `api_library_open`; `api_library_open_status`; `api_library_open_reconcile`; `_OPEN_STATUS_BY_OUTCOME`; `_error_response`; `_ERROR_STATUS_TABLE` | mcp/src/agents_remember/serving/conversation/library/api.py:75-84; mcp/src/agents_remember/serving/conversation/library/api.py:109-130; mcp/src/agents_remember/serving/conversation/library/api.py:133-158; mcp/src/agents_remember/serving/conversation/library/api.py:169-199; mcp/src/agents_remember/serving/conversation/library/api.py:202-221; mcp/src/agents_remember/serving/conversation/library/api.py:224-243; mcp/src/agents_remember/serving/conversation/library/api.py:271-286; mcp/src/agents_remember/serving/conversation/library/api.py:291-305 |
| `LIBRARY_RESPONSES` (six statuses) and `OPEN_OUTCOME_RESPONSES` — the open trio's own outcomes as success shapes, each union-ed with the refusal model the shared table declares for the same status. | `LIBRARY_RESPONSES`; `OPEN_OUTCOME_RESPONSES` | mcp/src/agents_remember/serving/conversation/response_contract.py:125-135; mcp/src/agents_remember/serving/conversation/response_contract.py:178-198 |
| The six focused suites cover routes, cursors/scope, gates, ports, the open service, and installed-runtime production gates. | `# mcp/tests` | onboarding/mcp/tests/overview.md:4-1333 |
| The installed Codex 0.144.5 runtime fixture records disabled capabilities and the native-history/list-read-resume production-gate evidence. | "codex-0.144.5-installed-20260718"; "enablesCapabilities"; "native-history/list-read-resume"; "L2 production gate" | mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json:3-3; mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json:9-9; mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json:23-23; mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json:31-31 |

## Cross-Repo References

No cross-repository implementation participates in this route. The locked npm dependencies are
third-party libraries resolved only from this repository's package/lock, and the resolved memory
policy allows no neighboring repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant cross-repo evidence found. | — | — |

## Docs References

The resolved `Domain Documentation` registry has no entries. This route therefore uses the
repository-owned contract, production seams, fixtures, and tests as its direct evidence and does
not fabricate an external citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this library gate. | — | — |

## File-Level Onboarding Map

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

## Child Overviews

None. The fifteen modules form one coherent, bounded library slice; a deeper overview would
fragment the same authority boundary.

## How To Use This Area

Read this overview and the exact file sidecar first. Route/mapping changes require the ASGI
route suite; token/scope changes require the cursor suite; gate or port behavior changes require
the doubled suites plus the installed-runtime suite on a machine with the harnesses installed.
Never infer capability from fixture existence or a locked dependency: only the live gates decide.

## Needs Verification

- Claude library is enabled or `unverified` strictly by the live helper CONTRACT probe (a real
  `list`/`read` through the locked SDK helper against the installed runtime), no longer by an
  installed-vs-locked version comparison. An auto-updated claude that
  answers the helper `list` now enables the surface; a failed probe fails closed with the exact
  contract reason.

## Sub-Agent Listing Route Impact

The dormant library now surfaces sub-agent conversations: codex lists the probe-proven
`subAgent*` source kinds and groups agent rows under each parent row client-side; claude
enumerates meta-bound `subagents/*.jsonl` transcripts and reads them through the composite
`<sessionId>/<agentId>` vendor-id grammar. Enumeration without proof surfaces as an exact
`agents_note` — never a silent absence — and sub-agent resume-target resolution fails closed
(sub-agent transcripts have no native resume target). The five routes, cursor/key authority,
live gates, and the open/reconcile service are unchanged.

Route indexes are intentionally not regenerated during this partitioned curator pass; the manager will run the single aggregate refresh after all curator ownership is complete. Existing verification metadata remains pre-commit.

## 260731-EFA-L2 — Per-App vs Per-Caller, And Probes That Cannot Be Half-Faked

The read-and-open boundary, the re-authorization chain and the gate-before-store rule are all
unchanged. Three values now carry rules this route previously enforced only by convention.

**`LibraryBinding(runtime, shared, authorization)` (`open_service.py`) makes the scope split
explicit.** The runtime and the shared library state are *per-app*; the authorization is
*per-caller*. Every operation fingerprint, ledger key and minted session id is derived from that
pairing — binding them once is what stops one caller's request from being keyed under another's
identity. A function in this route that takes `runtime` and `shared` without an authorization is
operating outside a caller's scope and should be suspected.

**`OpenRequest(request_id, expected_identity_digest, cwd=, launch_context=)` is one idempotent open
in the caller's own words.** The request id keys the ledger, the identity digest is the exact row
the caller believes it is opening, and cwd/launch context narrow where and how. **Replaying the id
with any of the others changed is a conflict, not a second open** — and that is only checkable
because the four form one fingerprinted value. Splitting them back into separate parameters would
silently re-permit the replay.

**`AppServerSeams` (`codex.py`) and `GateProbes` (`gates.py`) are all-or-nothing substitution
seams.** `AppServerSeams(env, transport_factory)`: the environment selects the binary and its
credentials, the transport factory decides how the process is spoken to — a fake transport against
the real environment (or the reverse) talks to a process nobody meant to start. `GateProbes(
codex_probe, which, environment)`: a gate answers "can this harness serve a library here?" only by
probing the machine, via the codex app-server probe, PATH lookup, and the process environment —
**faking one while leaving the others live probes two different machines.** Each has a frozen
module-level default (`DEFAULT_APP_SERVER_SEAMS`, `DEFAULT_GATE_PROBES`) standing for "the real
machine". Tests substitute the whole seam or none of it.

`ToolPhase` in `codex_normalize.py` dropped its `# noqa: UP040` — the Ruff target version now
matches the package's declared 3.11 floor, so the directive had nothing to suppress.

## 260731-EFA-L4 — The Five Routes Declare Their Shapes, And One Silent 500 Was Deleted

The read-and-open boundary, the re-authorization chain, the gate-before-store rule, the cursor/key
authority and the open ledger are all unchanged. Two things changed in `api.py`.

**1. Every route declares what it answers with.**

| Route | `response_model` | `responses` |
| --- | --- | --- |
| `GET ""` | `ConversationLibraryPage` | `LIBRARY_RESPONSES` |
| `GET /{conversation_key}` | `HistoricalConversationPage` | `LIBRARY_RESPONSES` |
| `POST /{conversation_key}/open` | `OpenConversationOperation` (`status_code=201`) | `{**LIBRARY_RESPONSES, **OPEN_OUTCOME_RESPONSES}` |
| `POST /{conversation_key}/open-status` | `OpenConversationOperation` (`status_code=201`) | same |
| `POST /{conversation_key}/open-reconcile` | `OpenConversationOperation` (`status_code=201`) | same |

`LIBRARY_RESPONSES` is `_ERROR_STATUS_TABLE` + `_error_response` transcribed: every typed library
error lands on one of 400/403/404/409/422/503, so one table is the complete refusal surface of all
five routes. The open trio need a second table because **they answer with two families on the same
statuses**: `_OPEN_STATUS_BY_OUTCOME` picks 201/202/409/422/503 from the operation's own `outcome`
and the body there is the operation (a `pending` open is an ANSWER, not an error), while
`_error_response` still maps typed library errors onto the same 409/422/503 with refusal bodies.
Because `{**a, **b}` is a dict merge and not a union, `OPEN_OUTCOME_RESPONSES` unions the refusal
member into each overlapping status itself — a bare operation-only entry would overwrite
`LIBRARY_RESPONSES`' entry and declare, on nine (route, status) pairs, a model the route cannot
produce.

**2. `_open_call` lost its `.get(..., 500)` default — a real behaviour change.** It now indexes
`_OPEN_STATUS_BY_OUTCOME[operation.outcome]` directly. Before, an outcome nobody had mapped was
answered as **HTTP 500 carrying a full operation body**: a shape no `responses` table names, on a
status no test could drive, with no signal anywhere. Now it raises at the one place that can fix it,
and `test_serving_response_conformance.py::DeclaredSurfaceCoverageTests
::test_the_open_status_map_is_total_over_the_declared_outcomes` asserts set equality between the
map's eight keys and `OpenConversationOperation.outcome`'s `Literal` members, so a ninth outcome
fails in CI before it can reach the index.

**What enforces the declarations.** Not FastAPI: every handler here returns a `JSONResponse` it
built, so the decorator contributes an OpenAPI schema and validates nothing at runtime.
`test_serving_response_conformance.py` drives the real routes and validates the returned body
against the model declared for the status that came back; the library/open success bodies are
driven off a real bridge in `ConversationSuccessConformanceTests` (they need a conversation key this
app's own authority will sign), while the harness-specific failure legs remain declared-and-undriven
with a recorded reason.

## 260731-EFA-L9 Route Impact — Contract Imports Moved

The library child routes now import the page/history wire contracts from `models/conversations/history.py` and the canonical library port from `serving/ports.py` after the L9 monolith split. Library behavior is unchanged.

## Update History

- 2026-08-12T04:15+02:00 — 260731-EFA-L22 Codex Desktop repair: recorded current Desktop
  host-first initialize identity and exact request client-name/version validation for the native
  library connector.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: updated the exact-open operating model for
  canonical `TaskDocumentRef` launch context; no leaf or caller-visible runtime address survives as
  a second routing authority.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 route impact: L9 caller/import re-points recorded and body updated.

- 2026-08-04T13:25:51+02:00 — 260731-EFA-L6 S18-B01 same-reviewer semantic-binding repair: split helper dispatch from runtime-fixture ownership under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-08-02T18:15+02:00 — 260731-EFA-L6 curator W1-B06: anchored 9 Repo-Internal reference rows; scoped result 0 findings.

- 2026-08-01T09:10+02:00 — 260731-EFA-L4 curator: recorded the five route declarations and the one
  real behaviour change — `_open_call` dropped `_OPEN_STATUS_BY_OUTCOME.get(outcome, 500)` for a
  direct index, so an unmapped outcome is now a loud failure instead of a silent 500 carrying a full
  operation body on an undeclared status, held total by a set-equality test against the outcome
  `Literal`'s eight members. Recorded why the open trio need a second `responses` table (the same
  statuses carry either the operation or a refusal) and why every entry in it unions both models
  (`{**a, **b}` is a merge, so an operation-only entry would delete the shared refusal on nine
  (route, status) pairs). Added the totality rule to Local Invariants And Traps and two reference
  rows (`library/api.py`, `conversation/response_contract.py`); all ranges read back. Named the
  conformance suite rather than FastAPI as the enforcement, since every handler here returns a
  `JSONResponse` it built itself. Gate, cursor/key, scope and open-ledger behaviour are unchanged.
  Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: `LibraryBinding` (per-app runtime/shared bound to a
  per-caller authorization) and `OpenRequest` (the four facts whose joint fingerprint is what makes
  a replay a conflict rather than a second open) replaced the parallel parameter lists;
  `AppServerSeams` and `GateProbes` made the two substitution surfaces all-or-nothing, with frozen
  defaults standing for the real machine. No wire, gate, digest rule or read path changed.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-26T15:52 — 260718-CHATS-L7 curator: documented the sub-agent library rows (codex
  `subAgent*` source-kind grouping, claude `subagents/*.jsonl` enumeration/reads, the
  capability-honest `agents_note`, fail-closed sub-agent identity/resume) in the port rows and
  Structures list. Routes, token authority, gates, and open/reconcile are unchanged. Aggregate
  route-index generation remains manager-owned; verification metadata stays pinned
  (L7 uncommitted).
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: version-gate REMOVAL (developer ruling
  2026-07-21, R4). Corrected the now-false "supported at the exact locked versions / observed-versus-
  locked reason / version re-proof on every spawn" doctrine throughout: the live production-path
  CONTRACT probe (codex `thread/list`; claude/pi helper `list`) is the only gate, the handshake
  reports observed runtime/helper versions as informational evidence, and no version comparison gates
  or demotes. Routes, cursor/key authority, ports, and open/reconcile service unchanged. Verification
  stays pinned until L5F closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the governing overview for the
  implemented dormant native library — authorized list/read, live capability gates, signed
  cursor/key authority, narrow-only scope, locked-helper and direct app-server ports, and the
  idempotent exact open/status/reconcile service with honest retirement — after same-reviewer
  PASS closed findings F1–F5 across four fix rounds. Verification is blank because the new
  source route is uncommitted; closeout owns its first source stamp.
