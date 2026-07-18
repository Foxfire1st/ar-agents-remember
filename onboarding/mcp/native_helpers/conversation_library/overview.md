# Locked Native Conversation Library Helper Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/native_helpers/conversation_library/` |
| onboardingRoute | `mcp/native_helpers/conversation_library/overview.md` |
| parentOverview | [`mcp/overview.md`](../../overview.md) |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|

## What This Area Is

This route is the repository-owned, exactly locked process boundary for future Claude and Pi native
conversation-library access. It currently supplies a strict JSON-lines protocol shell, exact
dependency/lock ownership, request framing/schema validation, version handshake, and raw-error
privacy boundary. It intentionally implements no list, read, or resume operation behavior.

## Hot Path Summary

Read `src/protocol.ts` for the `ar-conversation-library-helper/v1` request/handshake boundary and
`src/protocol.test.ts` for exact-key, exact-version, byte-bound, and fixed-error privacy proofs.
`package.json` and `package-lock.json` are the only allowed runtime dependency resolution source.

## What Belongs Here

| Path | Role |
| --- | --- |
| `package.json` | Private helper identity, scripts, engine, and exact direct dependency pins. |
| `package-lock.json` | Deterministic repository-owned transitive resolution. |
| `tsconfig.json` | Strict no-emit TypeScript contract checks. |
| `src/protocol.ts` | Versioned JSONL request/response and validation shell. |
| `src/protocol.test.ts` | Helper handshake, shape, and privacy regressions. |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Normalized Python conversation/page/control DTOs | `mcp/src/agents_remember/serving/conversation/`. |
| Active-session projector behavior | `mcp/src/agents_remember/serving/conversation/active/` and focused vendor services. |
| Helper behavior that actually lists/reads/resumes native history | A later native-library implementation after installed-runtime proof. |
| npm cache, OpenSrc, global module, `NODE_PATH`, or `npx` resolution | Nowhere; these are explicitly forbidden. |

## Structures Found Here

- A private ESM package requiring Node 20 or newer.
- Exact `@anthropic-ai/claude-agent-sdk@0.3.207` and
  `@earendil-works/pi-coding-agent@0.80.7` direct pins plus deterministic transitive lock data.
- Discriminated handshake/list/read/resolve-resume-target request shapes.
- Exact-key validation per operation, 1 MiB request bound, non-empty fields, positive safe page
  limits, and a fixed allow-listed public helper-failure detail.
- Strict no-emit compilation with exact optional-property and unchecked-index safety enabled.

## Operating Model

1. The Python host will start this repository-owned helper using installed dependencies from this
   package only.
2. A handshake carries protocol, harness, expected runtime, and expected helper versions.
3. Readiness requires the exact requested/observed/pinned version tuple.
4. Each request is byte-bounded, parsed as one JSON object, checked against the protocol version,
   and reconstructed from the exact allowed key set for its operation.
5. Raw process error detail never crosses the public boundary; callers receive fixed safe copy.
6. Operation execution remains absent until later leaves prove installed Claude/Pi interoperability.

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

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `src/protocol.ts` | protocol/privacy boundary | Establishes exact framing, versions, shape, and raw-error containment before behavior exists. | covered |
| `package.json` | dependency authority | Names the only allowed direct helper versions and verification commands. | covered |
| `package-lock.json` | resolution authority | Prevents ambient runtime dependency selection. | covered |
| `src/protocol.test.ts` | regression proof | Exercises exact versions, operation key sets, and hostile secret/path error examples. | covered |
| `tsconfig.json` | static contract | Makes strict no-emit checking part of the package gate. | covered |

## Local Invariants And Traps

- Repository package and lock data are the only dependency authority; never search cache, OpenSrc,
  global modules, `NODE_PATH`, or run `npx` as a fallback.
- Locked dependency presence is not proof that native history works and must not promote a
  capability.
- Exact-key validation rejects both unknown fields and known fields belonging to another operation.
- Raw helper stderr/detail is not a public authority. Fixed allow-listed copy prevents newly shaped
  secrets or local paths from bypassing a regex vocabulary.
- The package is behavior-empty beyond handshake/parsing. Do not document list/read/resume as
  implemented until the actual process seam and installed versions pass.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The helper protocol fixes exact versions, a 1 MiB bound, exact operation keys, and fixed safe error detail. | L3-L10; L84-L139; L141-L259 | [protocol.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.ts) |
| The helper suite probes exact version tuples, malformed/wrong-version frames, cross-operation fields, and a hostile secret/path corpus. | L14-L210 | [protocol.test.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.test.ts) |
| The Python foundation suite forbids incidental resolution and verifies package/lock pins. | L63-L99 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

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
| `src/protocol.ts` | [`src/protocol.ts.md`](src/protocol.ts.md) | covered | Versioned request/privacy boundary. |
| `src/protocol.test.ts` | [`src/protocol.test.ts.md`](src/protocol.test.ts.md) | covered | Exact helper regression matrix. |

## Child Overviews

None. The five-file helper is one coherent, bounded package; a separate `src/` overview would
fragment the same protocol boundary.

## How To Use This Area

Read this overview, the exact package/lock cards, and the protocol card before changing helper
selection or framing. Run both `npm run typecheck` and `npm test`; also run the Python foundation
suite because it guards repository topology and forbidden resolution strings.

## Needs Verification

- Installed Claude 2.1.211 plus SDK 0.3.207 list/read/resume interoperability remains unexercised.
- Installed Pi 0.80.7 list/read/resume/session-file resolution remains unexercised.

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the governing helper overview for
  exact repository resolution, strict JSONL admission/handshake, and fixed raw-error privacy.
  Verification is blank because the new source route is uncommitted; closeout owns its first stamp.
