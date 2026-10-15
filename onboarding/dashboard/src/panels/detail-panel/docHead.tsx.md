# dashboard/src/panels/detail-panel/docHead.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Render the shared identity/fact/note head and export the bounded ObjectiveLead primitive for form-page composition.

## Code Commentary

DocHead orders form/ID/status, title, labelled facts and notes; it does not render the objective. OverviewTop and TaskReaderPage place ObjectiveLead after the identity head, body notice and ReaderHead series/change-set line; the task direct-grant slot precedes it too. The objective uses shared titled-block spacing and still precedes Now or Steps. The exported objective retains measured-height clamping with line/character fallback without layout. In-place more exposes the bounded text, while a separate counted own-view link preserves long full-text reachability. Waits for and Needed by facts render projected task IDs, titles and served statuses. Missing docPath leaves the reference visible but disables its jump.

The chain and primary-requirement facts are independent strip facts, not extra note rows. At most six remaining header notes are drawn as notes across strip and lines: short values join the fact strip; longer values use `Clip`. A Master/Parent portfolio note already represented by an existing chain, or a Primary requirement note represented by the primary fact, takes none of those six places and calls no all-link by itself. The all-link appears only for notes neither drawn nor already stated; its total includes all document notes. Without the corresponding fact the same labelled note remains eligible as an ordinary note.

The primary requirement displays its ID/version link, not another copy of its requirement text. Consumed metadata is suppressed only when the actual fact exists, preserving older-cache content. Status/type lines retain explicit preview and in-place expansion behavior.

## Boundaries

DependencyFact constructs taskdoc selection keys for projected dependency paths; full-body hydration remains outside this module. Dependency display does not validate waitsFor or grant permission to start. The six-note bound is not a bound on the parent chain or independent primary fact. The full header-notes view can show the complete hydrated note list.

## Evidence


- DocHead draws identity, facts and notes, including projected dependency facts; objective placement belongs to readerTop and taskReader composition. [1]


- Already represented chain/primary metadata is suppressed before the six-note selection; total/more account for all notes. [2]

- ObjectiveLead uses shared block spacing, opens its bounded text in place and retains the counted long-full-text own-view link. [3]
