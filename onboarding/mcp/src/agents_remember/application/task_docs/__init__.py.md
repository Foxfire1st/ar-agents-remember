# mcp/src/agents_remember/application/task_docs/__init__.py

## Governing Overview

[application/task_docs route overview](overview.md)

## Purpose

Package marker for the task-document authoring application modules (260815-DAG master full-gate
repair): a one-line docstring only — the package has no re-export surface.

## Code Commentary

The module is a single docstring (`"""Task-document authoring application modules."""`); the
package's modules are imported by their full paths (`agents_remember.application.task_docs.
task_doc_tools`, etc.), not re-exported here.

### Invariants And Boundaries

- No `__all__` and no re-exports: importers name the module explicitly, so the package cannot
  grow a facade surface.

## Evidence

### Repo-Internal References

- The package marker docstring. [1]

### Cross-Repo References

No cross-repo boundary applies.

No meaningful cross-repo references found.
