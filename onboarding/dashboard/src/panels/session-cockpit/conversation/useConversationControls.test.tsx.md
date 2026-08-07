# dashboard/src/panels/session-cockpit/conversation/useConversationControls.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/useConversationControls.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T11:20+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The interrupt-hook suite (design §9.5; findings F1/F5/F24/F26; register L4.R1). It pins the turn-id
correlation from item evidence, the enable/honest-disabled reason matrix, and the turn-scoped typed
refusal path — the exact behaviors the review caught as falsely claimed in round 1.

## Code Commentary

### Logic

- **Fixtures (260731-EFA-L4)** cit:([`capabilitiesWithInterrupt`], dashboard/src/test/fixtures/conversationWire.ts:149-153): the local `capabilities()` helper is gone. It built
  `{ controls: { interrupt: … } } as unknown as ConversationCapabilities` — a tree with ONE leaf and
  twenty-two missing, on a model the server fills completely — and is replaced by
  `capabilitiesWithInterrupt`, imported under the same local name `capabilities`, from
  `test/fixtures/conversationWire.ts`. The interrupt leaf keeps its exact old shape, including the
  `reason: \`interrupt ${state}\`` string the reason assertions compare against. `IDENTITY`,
  `streamingItem` and `status` likewise build on `conversationIdentity` / `conversationItem` /
  `conversationStatus`.
- **`resolveWorkingTurnId` (F1)** cit:([`resolveWorkingTurnId`], dashboard/src/panels/session-cockpit/conversation/useConversationControls.ts:90-97): prefers the canonical status turn id; correlates from the
  newest streaming item's `turnId` when status omits it on the hosted-codex topology (L4.R1); is null
  when the turn is not `working` even if items carry a `turnId`; is null when a working turn's id is
  genuinely unresolvable.
- **`useConversationInterrupt` — enable / honest reasons** cit:([`useConversationInterrupt`], dashboard/src/panels/session-cockpit/conversation/useConversationControls.ts:88-170):
  - ENABLES the stop when working + the id resolves from item evidence, with a stale L1 `unverified`
    capability present, and asserts `keyshortcut === "Control+Shift+."` AND `reason === undefined` —
    the F24 guard that the known-stale L1 text never leaks onto the enabled control.
  - a genuinely unresolvable working turn renders disabled with the HONEST reason
    `turn identity unavailable on this wire` (never the stale capability text).
  - a not-working turn offers no stop; a hard-`unavailable` capability disables with its exact reason.
  - **the F26/F5a refusal path** cit:([`useConversationInterrupt`], dashboard/src/panels/session-cockpit/conversation/useConversationControls.ts:88-170): a mocked typed 422 envelope (no `acknowledgement`) goes
    through the REAL client parse — never guessed into an accepted interrupt — so a dispatch disables
    the control for THAT turn with the server's exact `detail`, `onStop === undefined`; a later working
    turn (new id) clears the turn-scoped refusal and re-enables the stop with `reason === undefined`.

### Invariants And Boundaries

- The suite exercises the real `activeConversationStore` (seeded projections) and the real client
  parse, so the refusal test is non-vacuous (a 422 is parsed, not stubbed into success).
- It is the regression guard for L4.R1 (item-evidence correlation) and F24 (no stale-reason leak on
  the enabled control) — both were live-observed failures the review required closed.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The hook + `resolveWorkingTurnId` under test (imported at L17). | `resolveWorkingTurnId` | dashboard/src/panels/session-cockpit/conversation/useConversationControls.ts:90-97 |
| The store seeded with projections (`activeConversationStore`, imported at L5). | `activeConversationStore` | dashboard/src/data/conversation/store.ts:207-215 |
| The reducer `emptyProjection`/projection type (imported at L4). | `emptyProjection` | dashboard/src/data/conversation/reducer.ts:68-81 |
| The status/capability/item wire types the fixtures build (imported at L6-L10). | `ConversationStatus`, `ConversationCapabilities`, `ConversationItem` | dashboard/src/data/conversation/types.ts:158-176; dashboard/src/data/conversation/types.ts:197-229; dashboard/src/data/conversation/types.ts:253-283 |
| `capabilitiesWithInterrupt` (aliased to `capabilities` here) and the full `conversationCapabilities` tree it overrides one leaf of. | `capabilitiesWithInterrupt` | dashboard/src/test/fixtures/conversationWire.ts:149-153 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-03T02:32:19+02:00 — Curator W3-B02: anchored 2 Repo-Internal citation rows and converted
  4 prose citations to the explicit `cit:` grammar, using exact current TypeScript identifiers and
  repository-relative paths; verification metadata remains unchanged.

- 2026-08-01T11:20+02:00 — 260731-EFA-L4 curator: the Logic section did not mention the fixtures at
  all, and the local `capabilities()` helper it would have described no longer exists, so a Fixtures
  bullet was added. The removed helper returned a ONE-leaf tree
  (`{ controls: { interrupt: … } } as unknown as ConversationCapabilities`) against a model the server
  fills with twenty-three leaves; `capabilitiesWithInterrupt` is imported under the same local name and
  produces the full tree with that one leaf overridden. Before attesting that the described matrix is
  unchanged I checked the two claims that depend on capability CONTENT: the F24 guard asserts
  `reason === undefined` on the enabled control while a stale `unverified` capability is present, and
  the hard-`unavailable` case asserts the exact reason — both still hold because
  `capabilitiesWithInterrupt` keeps the identical `reason: \`interrupt ${state}\`` string the old helper
  built. The twenty-two newly-present leaves (`steer`, `followUp`, `attachments`, `policyRead`,
  telemetry, history, live) are unread by `useConversationInterrupt`. Suite re-run: all cases pass.
  Citation repairs, re-anchored on their describes: `resolveWorkingTurnId` L67-L94 → L56-L84;
  `useConversationInterrupt` L96-L180 → L85-L170 (the old upper bound exceeded the 170-line file);
  the F26/F5a refusal `it` L141-L180 → L130-L169; the four import-line citations re-checked against the
  reshuffled import block (`useConversationControls` L12 → L17, types L6-L11 → L6-L10; the store and
  reducer lines were already correct). One row added for the builder module.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the interrupt-hook
  suite — item-evidence turn-id correlation (F1/L4.R1), the enable/honest-disabled reason matrix with
  the F24 no-stale-leak guard on the enabled control, and the F26 turn-scoped typed-refusal path
  through the real client parse. Verification is pinned to the leaf base (`0be0099`) because the new
  source file is uncommitted; closeout owns its first source stamp.
