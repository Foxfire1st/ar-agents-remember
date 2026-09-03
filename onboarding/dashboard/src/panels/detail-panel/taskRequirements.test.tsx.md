# dashboard/src/panels/detail-panel/taskRequirements.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/detail-panel/taskRequirements.test.tsx` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-04T01:06+02:00 |
| lastVerifiedCommitHash | `1993dd25bdf8331a2c1e28171dff2bf92ea090e2` |
| lastVerifiedCommitDate | 2026-09-04T00:57:29+02:00 |
| governingOverview      | `../overview.md`                            |

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

## Docs References

No Domain Documentation source is configured for this repository-local component suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The detail-panel entry under test. | `DetailPanel` | dashboard/src/panels/detail-panel/DetailPanel.tsx:74-76 |
| The shared seed + notes/requirements stub used by the suite. | `seedTaskDocuments`; `stubNotes`; `taskDoc` | dashboard/src/panels/detail-panel/test-utils.tsx:373-479; dashboard/src/panels/detail-panel/test-utils.tsx:452-495 |
| The requirement anchor rendering exercised through Markdown. | `requirementAnchor` | dashboard/src/grammar/Markdown.tsx:116-133 |
| The reference resolution rules under test. | `resolveRequirementReference` | dashboard/src/data/requirements.ts:64-69 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: created for the
  detail-panel requirement-navigation suite (prose/References opening, missing-packet
  refusal, external/anchor preservation, notes-collision routing). Verified at code
  commit 1993dd25.
