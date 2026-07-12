# dashboard/src/panels/TaskGroupDisclosure.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/TaskGroupDisclosure.tsx`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-12T12:58+02:00                           |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`       |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The native disclosure control for Operations task-group rows. It exposes a compact, keyboard-operable
button for a group with visible descendants without turning disclosure activation into task selection.

## Code Commentary

### Logic

`TaskGroupDisclosure` receives the row label, collapsed state, and a toggle callback. It renders a
native `button` with `type="button"`, an accurate Expand/Collapse accessible name, and
`aria-expanded={ !collapsed }`. Pointer-down, key-down, and click handlers stop propagation so the
button remains an independent navigation control inside the React Aria `ListBoxItem`.

### Conventions

Presentation uses the panels route's co-located Panda `css()` styling, a visible chevron, and the
shared amber focus-visible treatment. The component owns no state and performs no persistence.

### Invariants And Boundaries

- The component does not select a task, mutate task state, or decide which rows have descendants.
- Parent `LifecycleList` supplies the stable key and owns collapse persistence.
- `aria-expanded` always describes the supplied collapsed state.

### Todos

None known for this leaf.

## Docs References

No relevant documentation found after checking the resolved `system/sources.md`; it has no configured
Domain Documentation entries. Accessibility semantics are proved by the native control and focused
repository tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain-documentation source was available for this local UI primitive. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The parent list renders this control only for descendant-bearing BY REPO rows and passes the stable row label/key state. | L281-L318 | [LifecycleList.tsx](LifecycleList.tsx) |
| Focused tests verify native button semantics, accessible names, aria-expanded state, and selection isolation. | L898-L937 | [LifecycleList.test.tsx](LifecycleList.test.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The control is local to the dashboard panels route and has no cross-repository interface. | — | — |

## Update History

- 2026-07-12T12:58+02:00 — Created for 260712-TRH-L3. Candidate source is uncommitted; verification metadata
  is pinned to the leaf base until closeout stamps the eventual code commit.
