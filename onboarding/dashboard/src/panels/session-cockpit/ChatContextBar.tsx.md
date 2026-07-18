# dashboard/src/panels/session-cockpit/ChatContextBar.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ChatContextBar.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T12:43+02:00 |
| lastVerifiedCommitHash | `82f2de40a666ea00754f364cfe764cea9294235f` |
| lastVerifiedCommitDate |  2026-07-18T13:07:00+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit overview](overview.md)

## Purpose

Carries product duties formerly stranded in the retired Chats route into the canonical cockpit:
launch Chat/Terminal, show task/leaf context, route an existing row locally to a lifecycle, and
authoritatively attach or move a running row to a leaf.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

The compact `＋ Chat` control now exposes the accessible name
`New chat — choose Claude, Codex, or Pi`. The visual label remains terse, while assistive and
role-based browser selection identifies that the control opens the one harness chooser. It does not
create direct per-harness buttons or introduce another launch path.

New launches inherit the selected lifecycle through the server route. Existing lifecycle attachment
remains explicitly local because no server endpoint exists. Leaf attach/move calls the daemon first,
patches the registry only on success, broadcasts a `leaf` invalidation, and renders same-role conflict
without changing the row.

## Invariants And Boundaries

Do not present local lifecycle routing as durable server authority. Leaf ownership is authoritative:
no optimistic local mutation and no hidden 409 refusal.

### Logic

The bar combines the sole chooser entrance with current task, lifecycle, leaf, and attachment
context. FEUI-L9R changes only the chooser button's accessible name.

### Conventions

Compact visible labels may use an explicit accessible name when the action's full meaning would not
fit the bar; stable data attributes remain the browser-test seam.

### Invariants And Boundaries

This remains one launch entrance. It does not create harness-specific launch buttons or bypass the
canonical LaunchFlow.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found for this file. | Source discovery checked | — |

## Cross-Repo References

The bar composes repository-local task/session helpers and same-origin terminal routes; no cross-repository implementation governs it.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical host and sole-launch-path composition. | L928-L958 | [SessionsView.tsx](SessionsView.tsx) |
| Session patch/broadcast and server leaf route. | L1-L80 | [../../data/sessions.ts](../../data/sessions.ts) · [../../data/terminal.ts](../../data/terminal.ts) |

## Update History

- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded the chooser entrance's explicit accessible name and
  sole-launch-path boundary; verification metadata remains pinned pending candidate closeout.

- 2026-07-18T07:22+02:00 — Created for the FEUI-L8 legacy-Chats duty transfer; verification metadata
  remains blank until commit.
