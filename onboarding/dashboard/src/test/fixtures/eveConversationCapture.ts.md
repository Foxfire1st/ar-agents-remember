# dashboard/src/test/fixtures/eveConversationCapture.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/test/fixtures/eveConversationCapture.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

The mounted eve case's input **decoder**: it reads `eveConversationCapture.json` — a wire body the
production server path serialized from the real eve projector — and rebuilds it as a typed
`ConversationItem[]` plus `ConversationStatus` by checking every field against the wire mirror's own
unions.

It exists because the capture is an **untrusted-from-TypeScript's-point-of-view JSON import**, and the
dashboard's wire-fixture guard (`test/wireFixtureGuard.test.ts`) forbids both easy answers:
`as ConversationItem[]` is a fixture *asserting* the server's shape instead of checking it, and a bare
JSON import reaching a wire-typed slot is an unchecked value in a checked slot. Every field is
therefore read through a membership predicate that **throws on a token the mirror does not declare**,
so a capture that drifts from the mirror fails the mounted case with the offending field named instead
of rendering something the server could never send.

Every token list here is the mirror's own union **spelled out**, and that duplication is deliberate:
it is the runtime check, and keeping it in a file whose whole job is this boundary makes a new union
member a one-line change in one place.

## Code Commentary

### Logic

The module exports two values and nothing else — `eveConversationItems` (line 376) and
`eveConversationStatus` (line 379) — each produced by a decoder over the imported JSON.

The primitive layer is small and total: `record()` refuses a non-object, array or null;
`text()` refuses a non-string; `number()` refuses a non-finite number; `nullableNumber()` and
`optionalText()` reconcile the two places where the wire and the mirror genuinely disagree (below).
**`oneOf()` is the load-bearing one**: it throws
`` `${field}: ${JSON.stringify(value)} is not one of ${allowed.join(", ")}` `` — the message names the
field *and* lists the accepted tokens, which is what makes a drifted capture diagnosable rather than
merely red.

`decodeBlocks()` (154) rebuilds each block as its own mirror member through a `switch` on the checked
`type`, and its `default` branch throws with a sentence explaining that the capture carries no block of
that kind and the decoder has no member to build for it. `decodeProvenance()` (225), `decodeItem()`
(240), `decodeIdentity()` (278), `decodeStatus()` (290) and `decodeItems()` (370) follow the same
shape: check, name the field, rebuild.

The token tables are the mirror's unions restated — `ITEM_KINDS`, `ITEM_PHASES`, `LANES`, `SOURCES`,
`ROLES`, `STRENGTHS`, `BLOCK_TYPES`, `PROCESS_STATES`, `PROCESS_OUTCOMES`, `TURN_STATES`,
`TURN_OUTCOMES`, `FRESHNESS_STATES`, `HARNESS_IDS` — plus `PRODUCERS`, which is declared inline in
`ProvenanceEvidence` and so has no exported name to import.

Two reconciliations are explicit rather than silent, and both are commented in place:

- **`status.turn.turnId` / `stateSince`** — the wire drops nulls (`exclude_none`), so an absent id
  means "no turn", while the mirror declares the field required-and-nullable. `optionalText(...) ?? null`
  is where the two are stated to agree.
- **`process.terminalOutcome`, `turn.waiting`, `turn.terminalOutcome`, `correlation`, `producer`** —
  optional on the wire, so the decoders pass `undefined` through instead of inventing an object.

### Conventions

- Every decoder takes the value plus the **field path** it is validating, and every thrown message
  begins with that path (`items[2].lane`, `status.freshness.state`). A failure therefore reports where
  to look without a debugger.
- Token lists are annotated `readonly <MirrorType>[]` (or `as const` where the mirror exports no name),
  so TypeScript itself flags a list that drifts from the union it mirrors.
- The decoder never mutates the input and never fills a missing field with a plausible value.

### Invariants And Boundaries

- **No cast may reach a wire-typed slot in this tree.** This module exists to satisfy that guard; a
  reintroduced `as` here would restore exactly the defect it replaced.
- **A new mirror union member is a one-line change here**, and forgetting it fails at *runtime* with
  the field named. The reviewer measured both directions: a mirror **gain** is caught at runtime when a
  capture carries the new token, and a mirror **loss** is caught one layer up by `tsc -b`, which names
  this file (measured: `eveConversationCapture.ts(40,3) TS2322` when `ConversationItemKind` lost
  `"interaction"`). The brief's expectation that narrowing a mirror union makes the *decoder* throw at
  runtime is not reproducible, because TypeScript types are erased and these lists are deliberate
  duplicates — the compiler is the layer that catches that direction.
- **The token lists are duplicates by design, not by accident.** De-duplicating them against the
  mirror would remove the only runtime check at this boundary.
- **The capture is the server's output, not a hand-written object.** `eveConversationCapture.json` is
  produced by the production serializer, and the Python side asserts the file equals what the
  projector produces today, so this decoder cannot drift away from the projection it feeds.
- Test-only: nothing in `src/` outside the test tree may import this module.

### Todos

None known. `BLOCK_TYPES` lists all twelve block kinds while the current capture exercises only a
subset; the unused members are deliberate so that a capture gaining a block kind fails on the decoder's
`default` sentence rather than on a missing list entry.

## Docs References

No `Domain Documentation` category is configured for this repository, so no live domain-documentation
pass was available for this file. The shape it validates is the repository's own wire mirror, which is
repo-internal evidence rather than external documentation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source exists in `system/sources.md`; the contract validated here is the repository's own wire mirror. | — | — |

## Repo-Internal References

The decoder is consumed by one mounted case, mirrors one type module, and validates a JSON body the
Python side produces.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two exported values the mounted case imports. | `eveConversationItems`; `eveConversationStatus` | dashboard/src/test/fixtures/eveConversationCapture.ts:376-376; dashboard/src/test/fixtures/eveConversationCapture.ts:379-379 |
| The throwing membership check that makes a drifted capture name its own field. | `oneOf` | dashboard/src/test/fixtures/eveConversationCapture.ts:146-151 |
| The per-block rebuild and its explanatory `default` refusal. | `decodeBlocks`; `BLOCK_TYPES` | dashboard/src/test/fixtures/eveConversationCapture.ts:102-115; dashboard/src/test/fixtures/eveConversationCapture.ts:154-223 |
| The item, provenance, identity and status decoders. | `decodeItem`; `decodeProvenance`; `decodeIdentity`; `decodeStatus`; `decodeItems` | dashboard/src/test/fixtures/eveConversationCapture.ts:225-238; dashboard/src/test/fixtures/eveConversationCapture.ts:240-276; dashboard/src/test/fixtures/eveConversationCapture.ts:278-288; dashboard/src/test/fixtures/eveConversationCapture.ts:290-368; dashboard/src/test/fixtures/eveConversationCapture.ts:370-373 |
| The mirror whose unions every token list restates. | `HarnessId`; `NativeConversationRef`; `ConversationLane`; `ConversationSource`; `ConversationItemKind` | dashboard/src/data/conversation/types.ts:13-13; dashboard/src/data/conversation/types.ts:16-16; dashboard/src/data/conversation/types.ts:32-32; dashboard/src/data/conversation/types.ts:50-50; dashboard/src/data/conversation/types.ts:110-110; dashboard/src/data/conversation/types.ts:15-20; dashboard/src/data/conversation/types.ts:41-49 |
| The guard this decoder exists to satisfy: a bare JSON import reaching a wire-typed slot is an unchecked value in a checked slot. | `wireFixtureGuard` | dashboard/src/test/wireFixtureGuard.ts:1-1; dashboard/src/test/wireFixtureGuard.test.ts:1-1 |
| The mounted case that consumes the decoder and asserts rendered text from the live React tree. | "rendered text from the live React tree" | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.eve.test.tsx:12-12 |
| The Python side pins the same JSON against what the projector produces today, so the decoder cannot drift from the projection it feeds. | `test_the_projection_matches_the_capture_the_mounted_ui_renders` | mcp/tests/test_eve_product_integration.py:1706-1713 |

## Cross-Repo References

No cross-repo boundary is involved: the fixture validates a body produced by this repository's own
Python server and renders it through this repository's own React surface.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_the_projection_matches_the_capture_the_mounted_ui_renders` repointed to mcp/tests/test_eve_product_integration.py:1706-1713. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: created this card for a file added by the eve
  product-integration change set. Records why a decoder replaces the four removed `as unknown as`
  casts, the throwing membership predicate that names its field, the two explicit wire/mirror
  reconciliations, and the measured asymmetry of the two drift directions (a mirror gain is caught at
  runtime, a mirror loss by `tsc -b`, because the token lists are deliberate duplicates). Verification
  metadata is pinned to the leaf's synced base commit `ff97072c` because the candidate is deliberately
  uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was
  invented here.
