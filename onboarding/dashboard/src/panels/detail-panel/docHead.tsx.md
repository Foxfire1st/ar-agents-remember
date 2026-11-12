# dashboard/src/panels/detail-panel/docHead.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Render the shared identity/fact/note head and export the bounded ObjectiveLead primitive for form-page composition.

## Code Commentary

DocHead takes identity/title/status from TaskEntry and content facts from TaskSummary, ordering form/ID/status, title, labelled facts and notes; it does not render the objective. TaskReader composition places ObjectiveLead after the identity head, body notice and ReaderHead series/change-set line; the task direct-grant slot precedes it too. The objective uses shared titled-block spacing and still precedes Now or Steps. The exported objective retains measured-height clamping with line/character fallback without layout. In-place more exposes the bounded text, while a separate counted own-view link preserves long full-text reachability. Waits for and Needed by resolve exact canonical references in the shared task map and use shared TaskStatusWord. Missing targets remain visible/inert rather than guessing paths.

The chain and primary-requirement facts are independent strip facts, not extra note rows. At most six remaining header notes are drawn as notes across strip and lines: short values join the fact strip; longer values use `Clip`. A Master/Parent portfolio note already represented by an existing chain, or a Primary requirement note represented by the primary fact, takes none of those six places and calls no all-link by itself. The all-link appears only for notes neither drawn nor already stated; its total includes all document notes. Without the corresponding fact the same labelled note remains eligible as an ordinary note.

The primary requirement displays its ID/version link, not another copy of its requirement text. Consumed metadata is suppressed only when the actual fact exists, preserving older-cache content. Status/type lines retain explicit preview and in-place expansion behavior.

The head is the task document's tray collection surface. It adds the shared tray host class and renders one `AddToTray` beside the identity/status line only when `entry.reference` exists. `taskPick` receives that canonical reference with the entry's ID and title. This component supplies the task-document offer; it does not add collection controls to Operations rows, own deduplication, or send a message.

## Boundaries

Dependencies retain their projected id/title. A served gone reference renders the literal gone marker; only a non-gone reference resolving to a canonical entry supplies shared task-state wording and navigation. A dependency without a document reference supplies no TaskStatusWord and no invented destination. The gone marker is not a second authored task stage.

DependencyFact constructs taskdoc selection keys for projected dependency paths; full-body hydration remains outside this module. Dependency display does not validate waitsFor or grant permission to start. The six-note bound is not a bound on the parent chain or independent primary fact. The full header-notes view can show the complete hydrated note list.

## Evidence

- Already represented chain/primary metadata is suppressed before the six-note selection; total/more account for all notes. [2]
- ObjectiveLead uses shared block spacing, opens its bounded text in place and retains the counted long-full-text own-view link. [3]
- Dependency identity remains visible, while gone and entry resolution gate task wording and navigation. [4]
- The canonical task document has one task-reference tray offer in its identity head, and no offer when the entry lacks a document reference. [5]
