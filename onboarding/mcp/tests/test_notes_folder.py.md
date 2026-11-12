# mcp/tests/test_notes_folder.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Server tests for the one-folder notes answer: one level per request in a stable total order without descending, 200-entry parts with a next-part row, held-descriptor confinement without following symlinks, per-token reference resolution in one request, the removed whole-tree answer, and the unchanged refusal and read wire answers.

## Code Commentary

Fifteen cases pin rule 2 and its edges: stable order with case-fold ties broken identically from any enumeration, parts above the ceiling, tree-size-independent work, live refresh on the next request, single-request reference resolution, the gone whole-tree route, the mid-request directory-swap confinement (L126-CODE-01), the escaping bare-link refusal with in-root alias (L126-CODE-05 area, Parent d388 format), scoped refusals with note reads, the three permission cases (readable-unsearchable 200 without children per INV-413DC8XE, searchable-unreadable and neither keeping baseline 500), and the Parent reference-format case (nested bare stays text, pathed links). Each regression fails on a targeted revert.

## Evidence

- One folder level answers in a stable order and never descends. [1]
- Parts above the ceiling page in order. [2]
- Folder work does not grow with tree size. [3]
- A swapped directory mid-request stays confined. [4]
- Case-fold ties order identically from any enumeration. [5]
- The whole-tree answer is gone with no caller. [6]

- A readable-unsearchable folder answers 200 present with no children. [7]
- A searchable-unreadable folder keeps baseline 500. [8]
- A neither-read-nor-search folder keeps 500. [9]
