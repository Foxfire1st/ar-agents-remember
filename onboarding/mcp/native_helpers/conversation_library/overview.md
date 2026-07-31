# Locked Native Conversation Library Helper Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/native_helpers/conversation_library/` |
| onboardingRoute | `mcp/native_helpers/conversation_library/overview.md` |
| parentOverview | [`mcp/overview.md`](../../overview.md) |
| lastUpdated | 2026-07-26T15:45+02:00 |
| lastVerifiedCommitHash |  `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f`|
| lastVerifiedCommitDate |  2026-07-26T18:40:37+02:00|

## What This Area Is

This route is the repository-owned, exactly locked process boundary for Claude and Pi native
conversation-library access. It supplies the strict JSON-lines protocol, exact dependency/lock
ownership, request framing/schema validation, version handshake, raw-error privacy boundary, and
— the two locked helper entries that execute handshake, list, read, and
resolve-resume-target over the pinned SDK/`SessionManager` APIs on one correlated
request/response loop. The helper also exposes the Claude sub-agent surface: per-session
`subagents/` enumeration folded into the list response (with the `agentsEnumerated` marker) and
`agentId`-routed agent transcript reads over the native on-disk layout the SDK does not expose.

## Hot Path Summary

Read `src/protocol.ts` for the `ar-conversation-library-helper/v1` request/handshake boundary,
the correlated serve loop, version probing, store signing, and paging primitives;
`src/claude.ts` and `src/pi.ts` are the locked per-harness operation entries — the Claude entry
also owns the sub-agent surface (`subagents/` enumeration, the `agentsEnumerated` marker, and
`agentId`-routed transcript reads with the SDK-replicated project-slug rule);
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
| `src/claude.ts` | Locked Claude SDK 0.3.207 list/read/resolve entry plus the sub-agent enumeration and agent transcript reads over the native `subagents/` layout. |
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
- The Claude sub-agent surface: a `subagents/agent-<id>.jsonl` + `.meta.json` on-disk
  authority under `<configDir>/projects/<slug>/<sessionId>/` with the SDK-replicated slug rule
  (non-alphanumerics to `-`; over-200-char slugs truncate with a base36 Java-hash suffix of the
  original path; symlinked scopes resolve through a realpath candidate), per-row `agents`
  children folded into the list signature, the response-level `agentsEnumerated` marker, and an
  additive optional `agentId` on the `read` operation routing to the agent transcript.
- Strict no-emit compilation with exact optional-property and unchecked-index safety enabled.

## Operating Model

1. The Python host starts this repository-owned helper using installed dependencies from this
   package only, one short-lived process per operation.
2. A handshake carries protocol, harness, expected runtime, and expected helper versions.
3. Readiness is ready-by-contract: the handshake returns `ready` once the
   wire protocol version matches and reports observed runtime/helper versions as informational
   evidence; the live list/read/resolve operation is the real gate.
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
2. Match the wire protocol version; report requested/observed runtime/helper versions as
   informational evidence (ready-by-contract — no version comparison
   refuses).
3. Return `ready`; the subsequent list/read/resolve operation against the installed runtime is
   the real gate and fails closed with the exact contract reason when it cannot serve.

### Request admission

1. Reject inputs over 1 MiB or non-object/wrong-version payloads.
2. Validate the operation discriminator and harness.
3. Require the exact operation-specific key set and field types.
4. Return a reconstructed typed request so unknown/inapplicable fields cannot cross the helper seam.

### Native list and read

1. List the native sessions inside the exact canonical scope (Claude excludes worktrees), sort by
   recency, offset-page, and sign the observed store. The Claude list additionally sweeps each
   session's `subagents/` directory: page rows carry their `agents` children, the signature
   covers agent ids/mtimes, and the response carries the `agentsEnumerated` marker so an empty
   catalog stays distinguishable from a pre-enumeration helper.
2. Read one conversation read-only, window by stable 1-based ordinal, map records to typed
   payloads, and return an honest total with a SHA-256 signature. A read carrying `agentId`
   opens the Claude `agent-<agentId>.jsonl` transcript under the candidate project dirs instead
   of the SDK session messages.
3. Native absence or unreadability answers typed `stale-identity`, never a synthetic empty page;
   malformed native sub-agent content (meta or transcript JSON) fails closed as typed
   `helper-failed`, never skipped.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `src/protocol.ts` | protocol/privacy/execution boundary | Establishes exact framing, versions, shape, raw-error containment, and the shared serve/probe/sign/page primitives. | covered |
| `src/claude.ts` | claude operations | Scope-exact SDK list/read/resolve with typed stale-identity posture, plus sub-agent enumeration and agent transcript reads over the native `subagents/` layout. | covered |
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
- Sub-agent identity is evidence-bound: missing/invalid `.meta.json` degrades
  to the honest agent-id fallback, malformed native meta/transcript JSON fails closed as typed
  `helper-failed`, and only the `agentsEnumerated` response marker distinguishes "no agents" from
  "helper predates enumeration" over an empty catalog.
- `agentId` is the one sanctioned additive optional request key (read only): invisible to pre-existing
  callers, never a required-key change.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The helper protocol fixes exact versions, a 1 MiB bound, exact operation keys, fixed safe error detail, and the serve/probe/sign/page primitives. | L3-L10; L84-L139; L141-L259 | [protocol.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.ts) |
| The helper suite probes exact version tuples, malformed/wrong-version frames, cross-operation fields, and a hostile secret/path corpus. | L14-L210 | [protocol.test.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.test.ts) |
| The Python foundation suite forbids incidental resolution and verifies package/lock pins plus the exact helper source set. | L63-L120 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The Python host and Claude/Pi ports drive these entries on the production seam. | L100-L148 | [helper_host.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/helper_host.py) |
| The installed-runtime suite proves the Pi gate/round-trip and the real Pi open through these helpers, and pins the Claude gate on the live list CONTRACT — asserting the reason is never a version-mismatch demotion. | L217-L263; L284-L413; L554-L586 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |

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
| `src/protocol.ts` | [`src/protocol.ts.md`](src/protocol.ts.md) | covered | Versioned request/privacy boundary plus execution primitives. |
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
  comparison: `buildHandshake` is always `ready`
  once the wire protocol version matches and reports the observed runtime/helper versions as
  informational evidence — it never handshakes `incompatible` on a version drift. The real gate is
  whether the subsequent `list`/`read` operation succeeds against the installed runtime; a failing
  operation fails closed with the exact contract reason, and an auto-updated claude that answers
  `list` enables the surface.
- Installed Pi 0.80.7 list/read/resolve passed through the production helper seam (the
  installed-runtime gate).

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the installed-runtime suite citation and
  rewrote the claim that carried it. `test_conversation_library_installed.py` is now 590 lines: the Pi
  gate + list/read/resolve round-trip are L217-L263, `PiOpenEndToEndTests` is L284-L413, and
  `ClaudeGateHonestyTests` is L554-L586 (was `L215-L262; L360-L568`). The old claim asserted a "Claude
  version-mismatch fail-closed posture", which the suite now explicitly disproves —
  `test_installed_claude_library_gates_on_contract_not_version` asserts the reason contains neither
  "differs from the locked" nor a version mismatch — so the claim was rewritten to state the
  contract-only gate the test actually pins, matching this file's Needs Verification note.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: recorded the Claude sub-agent surface — the
  `subagents/` on-disk authority with the SDK-replicated project-slug rule, per-row `agents`
  enumeration folded into the list signature, the `agentsEnumerated` response marker, and the
  additive optional `agentId` routing reads to agent transcripts with fail-closed
  malformed-content posture. Also corrected the PRE-EXISTING stale version-tuple handshake
  claims in Operating Model step 3 and Main Flows > Exact handshake (they still described the
  pre-L5F R4 gate; ready-by-contract is the doctrine since 2026-07-21 — surfaced as a
  contradiction the L5F pass left behind). Verification stays pinned until L7 closeout stamps
  the candidate commit.
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
