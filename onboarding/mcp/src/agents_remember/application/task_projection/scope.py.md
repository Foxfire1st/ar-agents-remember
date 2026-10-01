# mcp/src/agents_remember/application/task_projection/scope.py

## Governing Overview

[application overview](../overview.md)

## Purpose

Bind the projection to the **actual** admitted worktree, branch and task document. Every fact here
comes from an existing AR owner, and this module decides nothing those owners already decide.

## Code Commentary

### Logic

Three owners answer, and this module only reconciles their answers:

- **Coordination context** — `resolve_coordination_context` with a `WorktreeContractReader`, i.e. the
  same resolution the `context_packet` MCP tool uses. It answers where the coordination root, the
  task root and the memory worktree are, or refuses.
- **Worktree contract** — `WorktreeContractReader.load_contract` answers which work branch, source
  branch and base commit the admitted worktree actually has, and which task and leaf the enclosure
  belongs to.
- **Task document** — `TaskDocumentTopology` answers whether the admitted task reference resolves to
  exactly one document, at what altitude, and whether the bound role may sit there. The exact
  accepted JSON bytes come from `capture_task_doc_source`, so the reported document digest is the
  bytes the owner read rather than a re-read that could have moved underneath.

`parse_task_reference` accepts exactly `TaskDocumentRef.key` —
`"<repository>/<path-inside-tasks/<repository>>"` — so there is no second identity vocabulary to keep
in step. A reference in another form is `projection-task-reference-invalid`.

**Every disagreement gets its own status and its own remedy.** There is no fallback branch, no
nearest match and no silent widening: `projection-binding-unresolved`,
`projection-contract-unavailable`, `projection-repository-mismatch`,
`projection-branch-mismatch`, `projection-task-unknown`, `projection-task-binding-mismatch`,
`projection-role-altitude-mismatch`, `projection-scope-ambiguous`,
`projection-memory-binding-unavailable`. Where a refusal wraps an existing owner's error, its own
status is preserved in `owner_status` so a caller can branch on the owner's vocabulary instead of
matching prose.

`_parent_of` resolves a leaf's immediate parent **and only a leaf's**. A master's or sprint's own
parent is deliberately not resolved: the only owner that answers it walks the whole repository master
census, and no plan reads that document — paying for it would be cost without a fact.

**`read_documents` is the single enforcement point** for "read only the task altitude and relevant
ancestors the bound role and operation require": a document the plan does not name is not handed to
the projection, so it cannot be injected by accident further down. `referenced_documents` is its
counterpart — the resolved document the plan points at instead of reading.

`_memory_gap` reports an enclosure that records an external memory mode but no memory worktree, so
"memory reads are unbound for this seat" is a visible gap rather than an assumed success.

### Invariants And Boundaries

- The bound task document is **only read**. No task state, memory content or Git ref is written by
  `resolve_task_projection_scope`.
- The admitted repository and work branch are compared against what the enclosure contract declares
  before anything else is read; a projection is never produced for a branch the enclosure does not
  own.
- `read_documents` is the only gate on document visibility. Widening it, or reading a document the
  plan did not name, breaks the altitude contract.
- A refusal keeps the wrapped owner's status in `owner_status`. Do not collapse it into the
  projection's own vocabulary.
- `_parent_of` stays leaf-only. Do not extend it to master/sprint parents without first proving a
  plan reads that document.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking the configured sources.

### Repo-Internal References

The resolution entry point, the three owners it reconciles, and the two gates that make the plan
binding.

- The one resolution call: admitted binding plus hints in, bound scope or refusal out. [1]
- The canonical task reference parser — the admitted identity's only accepted form. [2]
- The two gates that make the read plan binding: read exactly these, reference those. [3]
- The admitted-identity reconciliation against what the enclosure declares. [4]
- The leaf-only parent read, and why a master's or sprint's parent is not resolved. [5]
- The exact accepted task-document bytes this module digests, rather than re-reading the file. [6]
- The topology owner that decides whether a reference resolves and which altitude may carry the seat. [7]
- The enclosure contract and its reader — the owner of branch, base commit and leaf identity. [8]
- The resolution shape this module mirrors rather than reinvents. [9]
- The case that proves every unresolvable input returns its own source-resolution status. [10]
- The case that proves a refused and a successful projection leave the task tree byte-identical. [11]

### Cross-Repo References

No sibling-repository contract consumes this scope resolver.

No meaningful cross-repo references found.
