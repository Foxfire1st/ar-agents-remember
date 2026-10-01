# dashboard/src/grammar/TaskRequirementLinks.tsx

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured.

No relevant domain documentation was found.

### Repo-Internal References

- The listing client that feeds the context. [1]
- The artifact target the `open` callback lifts. [2]
- The markdown consumer that renders registered addresses as buttons. [3]
- The reader that mounts the provider around task prose. [4]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

No applicable cross-repository source was found.
