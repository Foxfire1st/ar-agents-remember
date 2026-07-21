# dashboard/src/panels/session-cockpit/conversation/primitives.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/primitives.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T05:30+02:00 |
| lastVerifiedCommitHash | `1119b64ff1564c5fc76fd518f88e529535c04b34` |
| lastVerifiedCommitDate | 2026-07-21T08:14:40+02:00|
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

- `cap(overrides)` (L10) builds a `FeatureCapability` with a realistic long `reason` (the exact
  developer-observed jargon string) so the test proves the paragraph is NOT rendered inline.
- Case 1 (L20): `state === "supported"` → nothing renders (`capability-reason` absent).
- Case 2 (L25): a `partial` capability renders visible text EXACTLY `"partial"` (the one-word state),
  the visible text does NOT contain the reason paragraph, and the exact reason IS in the `title`;
  `data-state` echoes the state.
- Case 3 (L36): an optional `label` disambiguates — visible cue becomes `history unavailable` and the
  `title` is prefixed `history: <reason>`.

### Invariants And Boundaries

- The visible cue is always the one-word state (optionally `<label> <state>`); the full server reason
  is title-only. If a future change re-renders the reason inline, these pins fail — that is the guard.
- Pure render assertions over `@testing-library/react`; no store, network, or timers.

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
| The component under test (the R11 cue). | L5 | [primitives.tsx](primitives.tsx) |
| The capability type the fixture builds. | L4 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The surface that renders the labeled `history`/`live` cues in production. | — | [ConversationSurface.tsx](ConversationSurface.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: created the sidecar for the new R11
  progressive-disclosure test — three cases pinning that `CapabilityReason` shows the one-word state
  (optionally `<label> <state>`), keeps the full server reason in the `title` only, and renders nothing
  when supported. Verification pinned to the leaf base (`352d5cd`) because the new test file is
  uncommitted; closeout owns its first source stamp.
</content>
</invoke>
