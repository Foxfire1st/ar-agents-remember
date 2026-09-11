# dashboard/src/panels/useCollapsedTaskGroups.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/useCollapsedTaskGroups.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-12T12:58+02:00                           |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`       |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Owns the Operations task-group disclosure preference. It keeps groups expanded on first use and
persists collapsed stable task-selection keys across dashboard refreshes or component remounts.

## Code Commentary

### Logic

`useCollapsedTaskGroups` initializes a `Set<string>` from `localStorage` when running in a browser,
otherwise returning an empty set for non-browser rendering. `toggleCollapsed` immutably adds/removes a
typed task selection key, writes the v1 JSON array to `operations.tasks.collapsed.v1`, and returns the
new set to the caller.

### Conventions

The hook follows the dashboard's small persisted-flag pattern: the storage key is versioned, the public
state is a `ReadonlySet`, and the hook returns a stable callback via `useCallback`.

### Invariants And Boundaries

- Unrecorded groups are expanded by default.
- Persistence is keyed by stable typed task-selection keys, never labels or array positions.
- The hook owns presentation preference only; it does not filter BY PHASE, clear selection, or mutate task data.
- The app-written v1 payload is intentionally trusted; no migration or corruption fallback is part of this leaf.

### Todos

None known for this leaf.

## Docs References

No relevant documentation found after checking the resolved `system/sources.md`; it has no configured
Domain Documentation entries. The storage behavior is a local application contract covered by tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain-documentation source was available for this local hook. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The parent list applies the hook only to BY REPO hierarchy visibility and leaves selection/detail separate. | `LifecycleListImpl` | dashboard/src/panels/lifecycle-list/LifecycleList.tsx:224-259 |
| Focused tests verify stable storage keys, remount persistence, independent nested state, and expanded defaults. | "operations.tasks.collapsed.v1" | dashboard/src/panels/lifecycle-list/hierarchy.test.tsx:217-217 |
| The existing persisted-flag pattern was the worker's local implementation reference. | `usePersistedFlag` | dashboard/src/panels/file-viewer/usePersistedFlag.ts:6-25 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The preference is local to the dashboard browser surface and has no cross-repository interface. | — | — |

## Update History

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 3 repository-internal citations for the parent list, focused persistence tests, and persisted-flag reference.
- 2026-07-12T12:58+02:00 — Created for 260712-TRH-L3. Candidate source is uncommitted; verification metadata
  is pinned to the leaf base until closeout stamps the eventual code commit.
