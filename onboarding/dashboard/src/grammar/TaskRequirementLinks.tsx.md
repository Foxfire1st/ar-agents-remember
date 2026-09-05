# dashboard/src/grammar/TaskRequirementLinks.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/TaskRequirementLinks.tsx` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-04T01:06+02:00 |
| lastVerifiedCommitHash | `1993dd25bdf8331a2c1e28171dff2bf92ea090e2` |
| lastVerifiedCommitDate | 2026-09-04T00:57:29+02:00 |
| governingOverview      | `overview.md`                              |

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

The requirement-link context (260831-CCR-L23) that lets rendered task prose and
reference lists open task-local requirement packets through the internal reader
instead of treating `requirements/<path>.md` markdown as a dead or external
link. It fetches the registered requirement listing for the viewed task document
once and exposes an `open(path)` callback that lifts a
`{ kind: 'requirements', repo, master, document, path }` target to the cockpit
takeover. `Markdown.tsx` and `TaskNotes.tsx` read the context to render
registered requirement addresses as buttons and refuse unregistered ones.

## Code Commentary

### Logic

`TaskRequirementLinksProvider({ repo, master, document, onOpenArtifact, children })`
holds the fetched `requirements: RequirementEntry[]` in local state. On
`[repo, master, document]` change it clears the list and, when `document` is
defined, calls `listRequirements(repo, master, document)` with the `let live`
cancellation idiom (an unreachable API or a document without a registered root leaves
an empty list — never a crash). The memoized context value supplies the listing and
an `open(path)` that forwards `onOpenArtifact` only when a document is set.

`useTaskRequirementLinks()` reads the context; consumers handle a `null`
value (a reader surface outside any provider) by leaving requirement addresses
unresolved.

### Conventions

Provider/context idiom shared with other grammar modules; the fetch is GET-only and
keyed to the exact task document, matching the reader-scoped lifecycle.

### Invariants And Boundaries

- The provider is mounted per task-document reader (taskReader's
  `TaskRequirementBoundary` wraps `MasterOverview` and `TaskReader`),
  so the listing is scoped to the document being read.
- No document means no fetch and no `open` (an absent `document` is only
  valid on the notes variant of the artifact target).
- Opening is delegated to `onOpenArtifact`; the provider itself never navigates
  or writes.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The listing client that feeds the context. | `listRequirements` | dashboard/src/data/requirements.ts:26-32 |
| The artifact target the `open` callback lifts. | `TaskArtifactReaderTarget` | dashboard/src/data/taskArtifacts.ts:1-14 |
| The markdown consumer that renders registered addresses as buttons. | `requirementAnchor` | dashboard/src/grammar/Markdown.tsx:116-133 |
| The reader that mounts the provider around task prose. | `TaskRequirementBoundary` | dashboard/src/panels/detail-panel/taskReader.tsx:86-104 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: created for the
  requirement-link provider/context that makes registered task-local requirement
  packets openable from task prose and reference lists. Verified at code commit
  1993dd25.
