# dashboard/src/panels/session-cockpit/conversation/useConversationControls.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/useConversationControls.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The interrupt-hook suite (design §9.5; findings F1/F5/F24/F26; register L4.R1). It pins the turn-id
correlation from item evidence, the enable/honest-disabled reason matrix, and the turn-scoped typed
refusal path — the exact behaviors the review caught as falsely claimed in round 1.

## Code Commentary

### Logic

- **`resolveWorkingTurnId` (F1)** (L67-L94): prefers the canonical status turn id; correlates from the
  newest streaming item's `turnId` when status omits it on the hosted-codex topology (L4.R1); is null
  when the turn is not `working` even if items carry a `turnId`; is null when a working turn's id is
  genuinely unresolvable.
- **`useConversationInterrupt` — enable / honest reasons** (L96-L180):
  - ENABLES the stop when working + the id resolves from item evidence, with a stale L1 `unverified`
    capability present, and asserts `keyshortcut === "Control+Shift+."` AND `reason === undefined` —
    the F24 guard that the known-stale L1 text never leaks onto the enabled control.
  - a genuinely unresolvable working turn renders disabled with the HONEST reason
    `turn identity unavailable on this wire` (never the stale capability text).
  - a not-working turn offers no stop; a hard-`unavailable` capability disables with its exact reason.
  - **the F26/F5a refusal path** (L141-L180): a mocked typed 422 envelope (no `acknowledgement`) goes
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The hook + `resolveWorkingTurnId` under test. | L12 | [useConversationControls.ts](useConversationControls.ts) |
| The store seeded with projections. | L5 | [../../../data/conversation/store.ts](../../../data/conversation/store.ts) |
| The reducer `emptyProjection`/projection type. | L4 | [../../../data/conversation/reducer.ts](../../../data/conversation/reducer.ts) |
| The status/capability/item wire types the fixtures build. | L6-L11 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the interrupt-hook
  suite — item-evidence turn-id correlation (F1/L4.R1), the enable/honest-disabled reason matrix with
  the F24 no-stale-leak guard on the enabled control, and the F26 turn-scoped typed-refusal path
  through the real client parse. Verification is pinned to the leaf base (`0be0099`) because the new
  source file is uncommitted; closeout owns its first source stamp.
