# dashboard/src/panels/detail-panel/docHead.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Render the one shared identity, objective, fact strip and note head used by sprint, master and task pages.

## Code Commentary

The head orders form/ID/status, title, objective, labelled facts and notes. The objective leads on every form; measured natural height decides whether it is initially clamped, with line/character fallback without layout. In-place more exposes the bounded text, while a separate counted own-view link preserves long full-text reachability.

The chain and primary-requirement facts are independent strip facts, not extra note rows. At most six remaining header notes are drawn as notes across strip and lines: short values join the fact strip; longer values use `Clip`. A Master/Parent portfolio note already represented by an existing chain, or a Primary requirement note represented by the primary fact, takes none of those six places and calls no all-link by itself. The all-link appears only for notes neither drawn nor already stated; its total includes all document notes. Without the corresponding fact the same labelled note remains eligible as an ordinary note.

The primary requirement displays its ID/version link, not another copy of its requirement text. Consumed metadata is suppressed only when the actual fact exists, preserving older-cache content. Status/type lines retain explicit preview and in-place expansion behavior.

## Boundaries

Selection keys and full-body hydration remain outside this module. The six-note bound is not a bound on the parent chain or independent primary fact. The full header-notes view can show the complete hydrated note list.

## Evidence

- Every form shares identity, objective-first placement, independent fact strip and note head. [1]
- Already represented chain/primary metadata is suppressed before the six-note selection; total/more account for all notes. [2]
- The objective exposes bounded text in place and offers its long full text through a counted own view. [3]
