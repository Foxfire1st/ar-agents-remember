# mcp/src/agents_remember/application/task_docs/task_flat_list_edits.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Mutates flat task decisions and keyed questions inside the task owner’s already admitted read/publication operation.

## Code Commentary

TaskMutationEdit is the frozen edit bundle. append_decision requires a nonempty decision object. put_open_question validates the entire nonempty list of dictionaries and all key/text pairs before mutating openQuestions, then replaces the first string beginning with the supplied key or appends. A key must be nonblank and text must begin with that literal key. This ordering prevents an invalid later question from leaving earlier replacements applied.

## Invariants And Boundaries

These are in-memory list edits, not independent publication or lock authority; errors retain TaskDocError and literal prefix addressing.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- Mutates flat task decisions and keyed questions inside the task owner’s already admitted read/publication operation. These are in-memory list edits, not independent publication or lock authority; errors retain TaskDocError and literal prefix addressing. [1]
