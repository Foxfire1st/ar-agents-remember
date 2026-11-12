# dashboard/src/panels/detail-panel/taskRequirements.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The detail-panel component suite for task-local requirement navigation
(260831-CCR-L23). It seeds one sub-task whose objective prose and References carry
requirement addresses (`requirements/CCR-R23-v1-...md`), a missing packet, an
external URL, and a section anchor, then asserts the reader opens registered packets
through the internal reader, fails closed on unregistered ones while preserving
external links and anchors, and keeps an explicit `notes/requirements/...`
collision on the Series notes surface.

## Code Commentary

### Logic

seedRequirementTask builds a native TaskEntry with qualified reference and taskSummary objective/References, then seeds it through seedTaskEntries. stubNotes supplies the notes listing and registered requirement listing (its third argument); the requirement fixture retains address/size/sha256. This is fixture adaptation, not a change to requirement routing.

- **prose link** — a registered address in the objective renders as a
  `requirement-link` button (never an `<a>`); clicking it calls
  `onOpenNotes` with the full requirements target
  (`{ kind, repo, master, document, path }`).
- **References resolution** — the reference item matching the registered packet
  renders as `requirement-ref-1` and opens the same target.
- **fail closed** — `requirements/missing.md` renders as
  `requirement-link-refused` plain text (no `<a>`, no navigation), while
  `https://...` and `#anchor` links keep their real `href`.
- **notes collision** — the reference that names `notes/requirements/<packet>`
  is resolved by the notes surface (not the requirement resolver) and opens a
  `kind: 'notes'` target.

### Conventions

Rendering + `fireEvent` click assertions in the shared detail-panel idiom;
fetch is stubbed through the shared `test-utils.stubNotes` (never a live server).

### Invariants And Boundaries

Requirement addresses open only when the fetched listing registers them; an absent
packet is a visible refusal, never a dead hyperlink or a crash. External/anchor links
are untouched by the requirement interceptor.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository-local component suite.

No relevant domain documentation was found.

### Repo-Internal References

- The detail-panel entry under test. [1]
- seedTaskEntries seeds the supplied native TaskEntry list into the shared projection via seedProjection, which calls dashboardStore.applySnapshot(projection(over)); tasks are applied after other caller overrides. The requirement fixture supplies its selected entry through this helper, not seedTaskDocuments. [2]

- stubNotes responds to task-document, notes-list/read and requirements-list requests. [3]

- taskEntry and taskSummary are re-exported from the shared wire fixtures. They supply typed native-entry and reader-content defaults before caller overrides; taskEntry derives a qualified key from an overridden reference unless the caller supplies a key. The requirement fixture composes taskEntry with taskSummary, rather than taskDoc. [4]

- The requirement anchor rendering exercised through Markdown. [5]



- The reference resolution rules under test. [6]

### Cross-Repo References

No cross-repository implementation source governs this test module.

No applicable cross-repository source was found.
