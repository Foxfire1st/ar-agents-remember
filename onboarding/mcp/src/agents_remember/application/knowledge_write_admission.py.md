# mcp/src/agents_remember/application/knowledge_write_admission.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The frozen admission value for taskless curator file writes. The setup resolver derives it from the declared repository and its real checkouts; a caller cannot assert admission with a boolean.

## Code Commentary

### Logic

The only admission kind is `repository-bootstrap`. Provenance names the setup authority, exact reference and fact read. The value carries the repository, coordination and worktree roots, exact source commits, work branch, operation scope and source reference. A memory repository path may be absent; the writer requires an admitted memory worktree.

### Invariants And Boundaries

The value decides no destination, identity or authority. Leaf file writes read their enclosure in `cli/knowledge_ingest.py`; this module no longer adapts a leaf contract. Canonical coercion and frozen-database refusal left with the retired database writer. No former database route remains to protect.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; `BOOTSTRAP-HANDOVER.md` is the process authority
this value implements, and it is a task-tree document rather than a configured domain source.

No external documentation is required for the write-admission value.

### Repo-Internal References


- The taskless admission derives real setup authority; canonical enclosure adapters and database refusal were retired. [1]


- The taskless admission value and provenance are the published shapes. [2]


- The one current admission kind is repository-bootstrap. [3]

- **Provenance as a value: what admitted the write, from which document, and the one fact that made it an admission.** [4]

- The taskless operation is bound to its exact code/memory roots and admitted source commits. [5]

- The optional memory repository against the required memory worktree the operation refuses on. [6]

- Provenance carries the exact setup authority and reference rather than a caller boolean. [7]


- The current resolver derives taskless admission from repository setup authority. [11]



### Cross-Repo References

No cross-repository behavior is implemented in this file: it reads no repository at all. The resolved
settings' `crossRepo.allow` is empty, so nothing here names, reads or writes another repository.

No meaningful cross-repo references found.
