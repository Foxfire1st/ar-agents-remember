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

### Logic

**`memory_repo_path` is optional and `memory_worktree` is not** (`:100-106`): a repository with no
external memory layer has no memory repository to name, while `memory_worktree` is the strictly
stronger requirement the operation itself refuses on, exactly as it did when it read a contract.

### Invariants And Boundaries

- There is no `admitted=True` argument on this path; an admission is built by a resolver, never
  asserted by a caller.
- An admission confers no authority and decides no destination, namespace or identity.
- `memory_repo_path` may be `None`; `memory_worktree` is the requirement the operation refuses on.
- `scope` is the **retry** scope: it is what makes "an exact retry does not duplicate knowledge" true
  without the retry key ever becoming an identity input.

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

### Repo-Internal References

- **The module's own statement of the gap it closes and of why a second write path was refused.** [12]
- **The facts one admitted write is bound to, including the retry scope and the two exact source revisions.** [13]
- Which authority admitted this write, and whether it was derived without an enclosure. [14]
- **The second real admission this value exists to carry, and the resolver that builds it.** [15]
