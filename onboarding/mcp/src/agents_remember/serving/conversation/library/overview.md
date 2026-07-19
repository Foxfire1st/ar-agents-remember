# Native Conversation Library Route Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/library/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/library/overview.md` |
| parentOverview | [`conversation/overview.md`](../overview.md) |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|

## What This Area Is

This route is the implemented dormant native conversation library landed by 260718-CHATS-L2.
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
`mcp/native_helpers/conversation_library/`.

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
| `codex.py` | Direct Codex app-server list/read/resolve port plus the gate probe. |
| `codex_normalize.py` | Codex thread-item → normalized `ConversationItem` parser. |
| `claude.py` | Locked-helper Claude list/read/resolve port. |
| `pi.py` | Locked-helper Pi list/read/resolve port. |
| `normalize_common.py` | Shared text-capping, provenance, required-field, and content-extraction primitives. |
| `errors.py` | Leaf-local typed error family mapped by the routes. |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Strict wire grammar, cursor brands, and operation products | `mcp/src/agents_remember/serving/conversation/models.py` (the parent contract route). |
| Runtime composition, authorization ruling, and request dependencies | `mcp/src/agents_remember/serving/conversation/` (L0; consumed, never edited). |
| Locked Claude/Pi helper implementations and protocol | `mcp/native_helpers/conversation_library/`. |
| Tracked opener, retirement mechanics, and catalog/readiness authorities | Existing serving modules (`terminal_opener.py`, `retire.py`, `hosted_readiness.py`). |
| Any durable conversation index, browser projection, or in-place identity mutation | Nowhere; these are explicitly forbidden (leaf R6). |

## Structures Found Here

- Five FastAPI routes on the L9 prefix `/api/harnesses/{harness_id}/conversations`, with strict
  extra-forbid request bodies and one camel-case serialization point.
- A leaf-local typed error family subclassing the shared `agents_remember.errors` types, mapped
  subclass-before-base to one precise HTTP status each (no raw 500 for routine refusals).
- Purpose-branded, HMAC-SHA256-signed opaque tokens whose signing key is per-app and never
  persisted; a restart invalidates outstanding tokens honestly.
- A content-derived catalog generation (no server-side counter or index) that resets cursors
  when the native store observably changes.
- Live capability gates: Codex proves `thread/list` over a real app-server connection reporting
  the exact locked CLI version; Claude/Pi prove the locked helper handshake plus a real native
  list call. Results are cached per installed-executable fingerprint, bounded by the three
  normalized harnesses.
- A bounded (256) in-memory open-operation ledger keyed by caller principal + requestId with
  LRU terminal eviction and a hard refusal when full of live work.
- An explicit `launched` authority plus an `absorbed_existing` spawn-ownership discriminator on
  every open record, so pre-launch polls never settle and foreign pre-existing sessions are
  never retired.

## Operating Model

1. Each handler resolves the L0 runtime and authorization through the same two request
   dependencies, narrows the raw harness id, and builds caller-bound services from the per-app
   shared bundle.
2. List/read re-derive the canonical scope, re-check the live gate, verify cursor/key purpose,
   signature, scope binding, and catalog generation, then delegate to the dormant port.
3. Open resolves the conversation key, checks the expected identity digest and optional cwd
   narrowing, and records one immutable fingerprint per (principal, requestId); identical
   replays return the retained operation, changed fingerprints conflict without launching.
4. The drive gates resume support, resolves and verifies the server-private resume target,
   launches a NEW tracked session through the existing shared opener (argv `--resume`/
   `--session` for Claude/Pi, `resume_thread_id` for Codex through the landed L0E channel), and
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
   exact observed-versus-locked reason.
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
| `gates.py` | capability authority | Capability honesty: supported only with live production-path evidence at the locked versions. | covered |
| `factories.py` | composition | Per-app shared bundle without `app.state` edits or import-time singletons. | covered |
| `helper_host.py` | helper boundary | Locked spawn/handshake/exit discipline; raw helper stderr never disclosed. | covered |
| `codex.py` | codex port | Direct read-only app-server list/read/resolve with honest partial completeness. | covered |
| `codex_normalize.py` | codex parser | Exact provenance normalization; unknown vendor kinds become explicit evidence, never guesses. | covered |
| `claude.py` | claude port | Helper-backed list/read/resolve with the version re-proof on every spawn. | covered |
| `pi.py` | pi port | Helper-backed list/read/resolve; reading never calls `switch_session` on any process. | covered |
| `normalize_common.py` | shared primitives | One home so the three resolvers cannot drift apart. | covered |
| `errors.py` | typed family | Leaf-local errors the route table maps exactly; parallel leaves stay collision-free. | covered |

## Local Invariants And Traps

- Possession of a cursor/key is never authorization: every call re-resolves the caller binding
  and re-checks scope, purpose, and catalog generation.
- Capability `supported` requires live runtime-fixture evidence at the exact locked versions;
  any mismatch demotes the whole harness history surface with the exact reason.
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

## Repo-Internal References

The parent contract route supplies the wire grammar and the two-port split this slice
implements; the L0 composition supplies the runtime, authorization, and dependency seams; the
tracked opener/readiness/retire authorities execute the open. Six new test suites plus the
foundation pin prove the contract on doubled boundaries, and the installed-runtime suite proves
the live gates and both real open E2Es.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The dormant library read port defines scoped list, historical read, and server-private resume-target resolution. | L59-L84 | [ports.py](agents-remember/mcp/src/agents_remember/serving/conversation/ports.py) |
| The L0 request dependencies are the only consumption seam the handlers use. | L21-L36 | [dependencies.py](agents-remember/mcp/src/agents_remember/serving/conversation/dependencies.py) |
| The tracked opener absorbs identical replays through the live catalog row and carries the codex-only `resume_thread_id`. | L170-L257 | [terminal_opener.py](agents-remember/mcp/src/agents_remember/serving/terminal_opener.py) |
| Locked helper entries and the JSONL protocol serve the Claude/Pi ports and host. | L50-L63; L54-L67 | [claude.ts](agents-remember/mcp/native_helpers/conversation_library/src/claude.ts), [pi.ts](agents-remember/mcp/native_helpers/conversation_library/src/pi.ts) |
| The foundation pin asserts exactly the five owned library routes and the helper source set. | L32-L56; L113-L120 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The six focused suites cover routes, cursors/scope, gates, ports, the open service, and installed-runtime production gates. | L1-L8 | [mcp/tests overview](../../../../../tests/overview.md) |
| Runtime fixtures record the observed (never enabling) gate/open evidence rows per harness. | L21-L34 | [codex-0.144.5.json](agents-remember/mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json) |

## Cross-Repo References

No cross-repository implementation participates in this route. The locked npm dependencies are
third-party libraries resolved only from this repository's package/lock, and the resolved memory
policy allows no neighboring repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant cross-repo evidence found. | — | — |

## Docs References

The resolved `Domain Documentation` registry has no entries. This route therefore uses the
repository-owned contract, production seams, fixtures, and tests as its direct evidence and does
not fabricate an external citation.

| Finding | Citations | Source Path |
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

- Claude library stays `unverified` on this machine (installed 2.1.214 ≠ locked 2.1.211) until a
  real installed 2.1.211 user/assistant/tool/permission history passes the locked SDK 0.3.207
  list/read/exact resume replay gate.

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the governing overview for the
  implemented dormant native library — authorized list/read, live capability gates, signed
  cursor/key authority, narrow-only scope, locked-helper and direct app-server ports, and the
  idempotent exact open/status/reconcile service with honest retirement — after same-reviewer
  PASS closed findings F1–F5 across four fix rounds. Verification is blank because the new
  source route is uncommitted; closeout owns its first source stamp.
