# dashboard/src/panels/session-cockpit/conversation/ConversationSurface.eve.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationSurface.eve.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

**Mounted UI evidence for an eve conversation** — packet behaviour 3, "display live and replayed
transcript, tools, questions/approvals, interruption and failure states through existing conversation
projections and UI components".

It mounts the **shipped** `ConversationSurface` — the same component the cockpit renders — over the
projection an eve session really produces, and asserts what a reader sees. Every expectation reads
rendered text from the live React tree through the surface's own test ids; this is a DOM mount in the
repository's component-test harness (jsdom via vitest), not a projector assertion.

No dashboard file was added for eve to make this possible: the case exercises the existing
harness-agnostic surface, which is the leaf's own claim in test form.

## Code Commentary

### Logic

Six cases over one shared `describe`, all seeding the real store the way hydration does:

`seed()` builds an `ActiveConversationProjection` from `emptyProjection(STATUS.identity)` plus the
decoded items, setting `stream: "live"` and `lastAppliedDelivery: "live"`, and writes it into
`activeConversationStore` under `STATUS.identity.arSessionId`. The surface is then rendered with that
session id, `visible: true`, and no-op retry/diagnostics callbacks.

The six assertions, and the packet behaviour each one evidences:

| Case | What it reads from the DOM |
| --- | --- |
| renders the surface for an eve session identity | `conversation-surface` exists, and the status identity's harness is `"eve"` |
| shows the operator message, the tool round-trip and the finalized answer | the operator's own words, the tool name `ar_workspace_write`, and its output `note.txt written` |
| shows a cancelled turn as an interrupted turn boundary, not as a clean completion | `conversation-turn-result` rows include both an `interrupted` label and a `turn complete` label — the disambiguation, rendered |
| shows the failure state and the parked-session notice as their own rows | `MODEL_CALL_FAILED` and `eve session parked and ready for` |
| shows the input request and the authorization challenge as answerable rows | exactly two `conversation-interaction` rows: `question: Proceed with the write?` with its `Approve`/`Deny` options, and `write note.txt`; every `interaction-phase` reads `waiting for answer` |
| renders nothing as an unknown-vendor row for a pinned-release frame | the body does **not** contain `unknown vendor event` |

The last case is the negative half of the projector's silence set: frames the pinned release emits
routinely are consumed by name, so a mounted surface must not show them as preserved vendor evidence.
The fifth case is the packet's "an input request" and behaviour 3's "questions/approvals" read as
rendered rows rather than as items in a list.

`beforeEach` pins jsdom geometry (`offsetHeight`/`offsetWidth`/`scrollHeight`/`clientHeight`/`clientWidth`)
because jsdom has no layout and the virtualized timeline would otherwise render no rows.
`afterEach` cleans up, waits 200 ms and resets the store, so one case cannot leak into the next.

`AmbientTelemetry` is mocked to `null` — the one substitution — because it is unrelated to the
conversation being asserted and would otherwise mount a live telemetry surface.

### Conventions

- **No `as` assertion appears in this file.** The capture is decoded by
  `test/fixtures/eveConversationCapture.ts`, which reads the production-serialized JSON through the
  wire mirror's own unions and throws on a token the mirror does not declare, so the wire-fixture
  guard stays satisfied. The two `const` declarations at the top are typed annotations over
  already-checked values, not casts.
- Assertions read rendered text (`textContent`) and test ids, never component internals.
- The file is named `<Component>.<harness>.test.tsx` to mark it as the harness-specific mount beside
  the harness-agnostic `ConversationSurface.test.tsx`.

### Invariants And Boundaries

- **The input is the server's real output.** `eveConversationCapture.json` is production-serialized,
  and the Python side asserts the file equals what the projector produces today — so this case cannot
  silently test a stale projection, and a hand edit to the fixture breaks the Python side first.
- **A reintroduced cast here re-opens the defect the decoder closed.** The guard
  (`test/wireFixtureGuard.test.ts`) is enforced tree-wide, and the reviewer verified it green at 23/23
  with this file in place.
- **The mounted class is jsdom over a production-serialized body, not a real browser against a real
  model.** There is no hosted credential in this environment and the dev bench mounts no conversation
  surface; this limit is declared rather than papered over.
- **Only the transport seam is doubled.** Everything below it — adapter, mapper, cursor, transcript,
  projections — is production code, and the frames this surface renders were produced by that code.
- A perturbation of the capture (a bad lane token, a narrowed decoder list) must fail this file or the
  decoder, naming the field. The reviewer ran both and both fired.

### Todos

None known.

## Docs References

No `Domain Documentation` category is configured for this repository, so no live domain-documentation
pass was available for this file. It asserts the repository's own rendered surface.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source exists in `system/sources.md`; the subject is this repository's own React surface and wire body. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shipped surface this case mounts, and the store it seeds. | `ConversationSurface`; `activeConversationStore`; `emptyProjection` | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:269-269; dashboard/src/data/conversation/store.ts:207-207; dashboard/src/data/conversation/reducer.ts:68-68 |
| The decoder that supplies the items and status with no cast. | `eveConversationItems`; `eveConversationStatus` | dashboard/src/test/fixtures/eveConversationCapture.ts:376-376; dashboard/src/test/fixtures/eveConversationCapture.ts:379-379 |
| The guard the no-cast discipline satisfies. | `wireFixtureGuard` | dashboard/src/test/wireFixtureGuard.ts:1-1; dashboard/src/test/wireFixtureGuard.test.ts:1-1 |
| The Python cases that pin the same capture against the live projector and assert the states it must show. | `test_the_projection_matches_the_capture_the_mounted_ui_renders`; `test_the_capture_shows_the_states_the_packet_names`; `test_live_frames_and_replayed_frames_project_identically`; `test_a_reconnect_replays_evidence_without_duplicating_items` | mcp/tests/test_eve_product_integration.py:1445-1452; mcp/tests/test_eve_product_integration.py:1454-1485; mcp/tests/test_eve_product_integration.py:1496-1514; mcp/tests/test_eve_product_integration.py:1516-1532; mcp/tests/test_eve_product_integration.py:1706-1713; mcp/tests/test_eve_product_integration.py:1715-1746; mcp/tests/test_eve_product_integration.py:1757-1775; mcp/tests/test_eve_product_integration.py:1777-1793 |
| The turn-boundary rendering the cancelled case reads (the amber interrupted line and the notice row). | `TurnResultItem` | dashboard/src/panels/session-cockpit/conversation/TurnResultItem.tsx:46-82 |
| The interaction row the question and authorization cases read. | `InteractionItem` | dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx:73-101 |
| The harness-agnostic sibling mount this file sits beside. | `ConversationSurface.test.tsx` | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.test.tsx:1-1 |

## Cross-Repo References

No cross-repo boundary is involved: the surface, the store and the wire body are all this
repository's own.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-16T11:43:03+00:00: Generated citation repair: `TurnResultItem` repointed to dashboard/src/panels/session-cockpit/conversation/TurnResultItem.tsx:46-82. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:03+00:00: Generated citation repair: `InteractionItem` repointed to dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx:73-101. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: created this card for a file added by the eve
  product-integration change set. Records the six mounted assertions and the packet behaviour each
  evidences, the no-cast decoding discipline it satisfies, the store-seeding and jsdom-geometry
  requirements, and the declared limit that this is jsdom over a production-serialized body rather
  than a real browser against a real model. Verification metadata is pinned to the leaf's synced base
  commit `ff97072c` because the candidate is deliberately uncommitted — the governed closeout stamps
  the real code commit, and no hash or fingerprint was invented here.
