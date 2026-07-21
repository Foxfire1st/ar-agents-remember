# Locked Native Conversation Library Helper Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/native_helpers/conversation_library/` |
| onboardingRoute | `mcp/native_helpers/conversation_library/overview.md` |
| parentOverview | [`mcp/overview.md`](../../overview.md) |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |  2026-07-21T11:31:07+02:00|

## What This Area Is

This route is the repository-owned, exactly locked process boundary for Claude and Pi native
conversation-library access. It supplies the strict JSON-lines protocol, exact dependency/lock
ownership, request framing/schema validation, version handshake, raw-error privacy boundary, and
— since 260718-CHATS-L2 — the two locked helper entries that execute handshake, list, read, and
resolve-resume-target over the pinned SDK/`SessionManager` APIs on one correlated
request/response loop.

## Hot Path Summary

Read `src/protocol.ts` for the `ar-conversation-library-helper/v1` request/handshake boundary,
the correlated serve loop, version probing, store signing, and paging primitives;
`src/claude.ts` and `src/pi.ts` are the locked per-harness operation entries;
`src/protocol.test.ts` holds the exact-key, exact-version, byte-bound, and fixed-error privacy
proofs. `package.json` and `package-lock.json` are the only allowed runtime dependency
resolution source.

## What Belongs Here

| Path | Role |
| --- | --- |
| `package.json` | Private helper identity, scripts, engine, and exact direct dependency pins. |
| `package-lock.json` | Deterministic repository-owned transitive resolution. |
| `tsconfig.json` | Strict no-emit TypeScript contract checks. |
| `src/protocol.ts` | Versioned JSONL contract, serve loop, version probing, signing, and paging primitives. |
| `src/claude.ts` | Locked Claude SDK 0.3.207 list/read/resolve entry. |
| `src/pi.ts` | Locked Pi SessionManager 0.80.7 list/read/resolve entry. |
| `src/protocol.test.ts` | Helper handshake, shape, and privacy regressions. |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Normalized Python conversation/page/control DTOs | `mcp/src/agents_remember/serving/conversation/`. |
| Active-session projector behavior | `mcp/src/agents_remember/serving/conversation/active/` and focused vendor services. |
| Python-side port normalization, gates, and open orchestration | `mcp/src/agents_remember/serving/conversation/library/`. |
| npm cache, OpenSrc, global module, `NODE_PATH`, or `npx` resolution | Nowhere; these are explicitly forbidden. |

## Structures Found Here

- A private ESM package requiring Node 20 or newer.
- Exact `@anthropic-ai/claude-agent-sdk@0.3.207` and
  `@earendil-works/pi-coding-agent@0.80.7` direct pins plus deterministic transitive lock data.
- Discriminated handshake/list/read/resolve-resume-target request shapes.
- Exact-key validation per operation, 1 MiB request bound, non-empty fields, positive safe page
  limits, and a fixed allow-listed public helper-failure detail.
- One correlated JSON-lines serve loop per helper entry: every input line gets exactly one
  response, parse failures answer `invalid-request`, and handler failures map onto the four
  typed errors with allow-listed detail.
- Runtime version probing (`--version`, first semver token) and own-dependency version
  observation through the standard ESM resolver from inside this package only.
- Deterministic SHA-256 native-store signatures, offset list paging, and ordinal newest-window
  read paging shared by both entries.
- Strict no-emit compilation with exact optional-property and unchecked-index safety enabled.

## Operating Model

1. The Python host starts this repository-owned helper using installed dependencies from this
   package only, one short-lived process per operation.
2. A handshake carries protocol, harness, expected runtime, and expected helper versions.
3. Readiness requires the exact requested/observed/pinned version tuple.
4. Each request is byte-bounded, parsed as one JSON object, checked against the protocol version,
   and reconstructed from the exact allowed key set for its operation.
5. Raw process error detail never crosses the public boundary; callers receive fixed safe copy
   or allow-listed operation detail.
6. The entries execute list (scope-exact, sorted, offset-paged, signed), read (read-only native
   open, ordinal-windowed, honestly totaled), and resolve (identity re-proof plus launch
   material for the Python port's server-private resume target).

## Main Flows

### Exact handshake

1. Select the repository pin for Claude or Pi.
2. Compare requested runtime/helper and observed runtime/helper against that exact pin.
3. Return `ready` only for the complete match; otherwise return `incompatible` with safe detail.

### Request admission

1. Reject inputs over 1 MiB or non-object/wrong-version payloads.
2. Validate the operation discriminator and harness.
3. Require the exact operation-specific key set and field types.
4. Return a reconstructed typed request so unknown/inapplicable fields cannot cross the helper seam.

### Native list and read

1. List the native sessions inside the exact canonical scope (Claude excludes worktrees), sort by
   recency, offset-page, and sign the observed store.
2. Read one conversation read-only, window by stable 1-based ordinal, map records to typed
   payloads, and return an honest total with a SHA-256 signature.
3. Native absence or unreadability answers typed `stale-identity`, never a synthetic empty page.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `src/protocol.ts` | protocol/privacy/execution boundary | Establishes exact framing, versions, shape, raw-error containment, and the shared serve/probe/sign/page primitives. | covered |
| `src/claude.ts` | claude operations | Scope-exact SDK list/read/resolve with typed stale-identity posture. | covered |
| `src/pi.ts` | pi operations | Read-only SessionManager list/branch-read/session-file resolution with typed stale-identity posture. | covered |
| `package.json` | dependency authority | Names the only allowed direct helper versions and verification commands. | covered |
| `package-lock.json` | resolution authority | Prevents ambient runtime dependency selection. | covered |
| `src/protocol.test.ts` | regression proof | Exercises exact versions, operation key sets, and hostile secret/path error examples. | covered |
| `tsconfig.json` | static contract | Makes strict no-emit checking part of the package gate. | covered |

## Local Invariants And Traps

- Repository package and lock data are the only dependency authority; never search cache, OpenSrc,
  global modules, `NODE_PATH`, or run `npx` as a fallback.
- Locked dependency presence is not proof that native history works and must not promote a
  capability — the Python-side live gates decide support.
- Exact-key validation rejects both unknown fields and known fields belonging to another operation.
- Raw helper stderr/detail is not a public authority. Fixed allow-listed copy prevents newly shaped
  secrets or local paths from bypassing a regex vocabulary.
- Reads are read-only: no entry is appended, branched, switched, or mutated by this package.
- Claude scope-exact listing excludes worktrees; a caller's authorized scope is never widened to
  another checkout's history.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The helper protocol fixes exact versions, a 1 MiB bound, exact operation keys, fixed safe error detail, and the L2 serve/probe/sign/page primitives. | L3-L10; L84-L139; L141-L259 | [protocol.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.ts) |
| The helper suite probes exact version tuples, malformed/wrong-version frames, cross-operation fields, and a hostile secret/path corpus. | L14-L210 | [protocol.test.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.test.ts) |
| The Python foundation suite forbids incidental resolution and verifies package/lock pins plus the exact helper source set. | L63-L120 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The Python host and Claude/Pi ports drive these entries on the production seam. | L100-L148 | [helper_host.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/helper_host.py) |
| The installed-runtime suite proves the Pi gate/round-trip/open and the Claude version-mismatch fail-closed posture through these helpers. | L215-L262; L360-L568 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |

## Cross-Repo References

The installed npm dependencies are third-party libraries, but no neighboring workspace repository
is read or updated by this route.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant cross-repo implementation evidence found. | — | — |

## Docs References

The resolved Domain Documentation registry has no entries. Exact package/lock contents and local
tests are used as direct evidence; no external behavior is claimed from package names alone.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this helper gate. | — | — |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `package.json` | [`package.json.md`](package.json.md) | covered | Direct version and script authority. |
| `package-lock.json` | [`package-lock.json.md`](package-lock.json.md) | covered | Deterministic transitive dependency authority. |
| `tsconfig.json` | [`tsconfig.json.md`](tsconfig.json.md) | covered | Strict compiler contract. |
| `src/protocol.ts` | [`src/protocol.ts.md`](src/protocol.ts.md) | covered | Versioned request/privacy boundary plus L2 execution primitives. |
| `src/claude.ts` | [`src/claude.ts.md`](src/claude.ts.md) | covered | Locked Claude SDK operation entry. |
| `src/pi.ts` | [`src/pi.ts.md`](src/pi.ts.md) | covered | Locked Pi SessionManager operation entry. |
| `src/protocol.test.ts` | [`src/protocol.test.ts.md`](src/protocol.test.ts.md) | covered | Exact helper regression matrix. |

## Child Overviews

None. The seven-file helper is one coherent, bounded package; a separate `src/` overview would
fragment the same protocol boundary.

## How To Use This Area

Read this overview, the exact package/lock cards, and the protocol card before changing helper
selection or framing. Run both `npm run typecheck` and `npm test`; also run the Python foundation
suite because it guards repository topology and forbidden resolution strings, and the
installed-runtime suite on machines with the harnesses to prove the production seam.

## Needs Verification

- Installed Claude library capability is decided by the live helper CONTRACT probe, not a version
  comparison (260718-CHATS-L5F R4, developer ruling 2026-07-21): `buildHandshake` is always `ready`
  once the wire protocol version matches and reports the observed runtime/helper versions as
  informational evidence — it never handshakes `incompatible` on a version drift. The real gate is
  whether the subsequent `list`/`read` operation succeeds against the installed runtime; a failing
  operation fails closed with the exact contract reason, and an auto-updated claude that answers
  `list` enables the surface.
- Installed Pi 0.80.7 list/read/resolve passed through the production helper seam (260718-CHATS-L2
  installed-runtime gate).

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: version-gate REMOVAL (developer ruling
  2026-07-21, R4) in `protocol.ts::buildHandshake`. Corrected the now-false Needs-Verification claim
  that the installed 2.1.214 runtime handshakes `incompatible` against a locked 2.1.211 gate: the
  handshake is ready-by-contract, reports observed runtime/helper versions as informational evidence,
  and never compares to a locked constant; the live `list`/`read` operation is the only gate. Helper
  framing, typed error vocabulary, and paging primitives unchanged. Verification stays pinned until
  L5F closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: extended the helper overview for the two
  locked operation entries (`claude.ts`, `pi.ts`) and the protocol's added serve-loop, version
  probing, signing, and paging primitives; the package is no longer behavior-empty, while the
  resolution, privacy, and scope-exactness invariants are unchanged. Verification metadata
  remains pinned until closeout stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the governing helper overview for
  exact repository resolution, strict JSONL admission/handshake, and fixed raw-error privacy.
  Verification is blank because the new source route is uncommitted; closeout owns its first stamp.
