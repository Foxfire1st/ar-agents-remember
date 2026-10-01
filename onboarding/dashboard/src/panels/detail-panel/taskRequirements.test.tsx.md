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

`seedRequirementTask` builds a sub-task document with `taskDoc`, seeds it
through `seedTaskDocuments`, and configures `stubNotes` with the notes
listing plus the requirement listing (the stub's third argument). The requirement
packet fixture mirrors the data-route fixture shape (`address/size/sha256`).

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
- seedTaskDocuments seeds the selected task documents into the shared projection fixture. [2]
- stubNotes responds to task-document, notes-list/read and requirements-list requests. [3]
- taskDoc supplies the required generated task-document fields before caller overrides. [4]
- The requirement anchor rendering exercised through Markdown. [5]
- The reference resolution rules under test. [6]

### Cross-Repo References

No cross-repository implementation source governs this test module.

No applicable cross-repository source was found.
