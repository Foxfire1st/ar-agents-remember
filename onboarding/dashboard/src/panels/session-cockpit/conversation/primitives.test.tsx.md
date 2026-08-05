# dashboard/src/panels/session-cockpit/conversation/primitives.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/primitives.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T05:30+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The R11 progressive-disclosure unit pins for `CapabilityReason` (260718-CHATS-L5P). It is the
deterministic proof that a partial/unavailable capability is surfaced as a short honest CUE, not the
implementation-jargon paragraph the developer findings called an above-the-fold wall — the
composed/live screenshot of the cue over a real codex conversation is the reviewer's R13 live pass, but
the disclosure LOGIC is fully covered here.

## Code Commentary

### Logic

- cit:([`cap`], dashboard/src/panels/session-cockpit/conversation/primitives.test.tsx:10-17) builds a `FeatureCapability` with a realistic long `reason` (the exact
  developer-observed jargon string) so the test proves the paragraph is NOT rendered inline.
- cit:(["renders nothing when the capability is supported"], dashboard/src/panels/session-cockpit/conversation/primitives.test.tsx:20-23) Case 1 renders nothing for a supported capability and asserts that the capability cue is absent.
- cit:(["shows the short state word, not the full reason paragraph, and puts the reason in the tooltip"], dashboard/src/panels/session-cockpit/conversation/primitives.test.tsx:25-34) Case 2 renders the one-word partial cue, keeps the reason out of visible text, and places it in the title while echoing `data-state`.
- cit:(["prefixes the cue and the tooltip with a disambiguating label when given"], dashboard/src/panels/session-cockpit/conversation/primitives.test.tsx:36-46) Case 3 prefixes the unavailable cue and title with the history label and reason.

### Invariants And Boundaries

- The visible cue is always the one-word state (optionally `<label> <state>`); the full server reason
  is title-only. If a future change re-renders the reason inline, these pins fail — that is the guard.
- Pure render assertions over `@testing-library/react`; no store, network, or timers.

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
| The component under test (the R11 cue). | `CapabilityReason` | dashboard/src/panels/session-cockpit/conversation/primitives.tsx:140-158 |
| The capability type the fixture builds. | `FeatureCapability` | dashboard/src/data/conversation/types.ts:234-244 |
| The surface that renders the labeled `history`/`live` cues in production. | `ConversationSurface` | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:100-381 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-04T13:25:51+02:00 — 260731-EFA-L6 S18-B01 same-reviewer semantic-binding repair: rebound all three case claims to their complete test bodies under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 3 citation items; scoped citation check now passes.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: created the sidecar for the new R11
  progressive-disclosure test — three cases pinning that `CapabilityReason` shows the one-word state
  (optionally `<label> <state>`), keeps the full server reason in the `title` only, and renders nothing
  when supported. Verification pinned to the leaf base (`352d5cd`) because the new test file is
  uncommitted; closeout owns its first source stamp.
</content>
</invoke>
