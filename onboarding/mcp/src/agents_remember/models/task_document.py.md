# mcp/src/agents_remember/models/task_document.py

## Governing Overview

[models overview](overview.md)

## Purpose

`models/task_document.py` (260731-EFA-L9) is the task-document wire vocabulary shared with the
response models: `StepStatus`/`DocStatus` and the terminal-readiness blocker moved here from the
`tasks` package so response models can import them without reaching up (layering cleanup).

## Code Commentary

### Logic

`CompletionBlocker` (cit:(["class CompletionBlocker"], mcp/src/agents_remember/models/task_document.py:42-42)) models the terminal-readiness blocker a task
document carries; the module exports the status literals the wire layer re-exports.

`CanonicalTaskObservation` freezes the exact task-source digest, authority namespace, validator version, semantic topology and optional intent observed by the task-domain owner. It rejects extra fields and requires a normalized absolute POSIX task root. `MasterExecutionNature` is the closed organizational/atomic vocabulary shared by persistence and projections.

### Invariants And Boundaries

- Models owns the wire vocabulary; task and response modules import it from this layer.
- Canonical observations retain task-domain ownership and exact source/topology identities; they do not grant approval.

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- Response and task modules import the vocabulary from this module. [1]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
