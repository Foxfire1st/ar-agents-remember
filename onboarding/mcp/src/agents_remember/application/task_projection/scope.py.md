# mcp/src/agents_remember/application/task_projection/scope.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_projection/scope.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T10:30+02:00 |
| lastVerifiedCommitHash | `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| lastVerifiedCommitDate | 2026-09-16T10:52:30+02:00|
| governingOverview      | `../overview.md`                           |

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

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking the configured sources. | N/A | N/A |

## Repo-Internal References

The resolution entry point, the three owners it reconciles, and the two gates that make the plan
binding.

| Finding | Anchor | Source |
| --- | --- | --- |
| The one resolution call: admitted binding plus hints in, bound scope or refusal out. | `resolve_task_projection_scope`; `ProjectionScopeRequest`; `ResolvedProjectionScope` | mcp/src/agents_remember/application/task_projection/scope.py:292-373; mcp/src/agents_remember/application/task_projection/scope.py:94-106; mcp/src/agents_remember/application/task_projection/scope.py:110-121 |
| The canonical task reference parser — the admitted identity's only accepted form. | `parse_task_reference` | mcp/src/agents_remember/application/task_projection/scope.py:63-90 |
| The two gates that make the read plan binding: read exactly these, reference those. | `read_documents`; `referenced_documents` | mcp/src/agents_remember/application/task_projection/scope.py:376-391; mcp/src/agents_remember/application/task_projection/scope.py:394-405 |
| The admitted-identity reconciliation against what the enclosure declares. | `_require_admitted_identity`; `_require_task_ownership`; `_altitude_of` | mcp/src/agents_remember/application/task_projection/scope.py:146-165; mcp/src/agents_remember/application/task_projection/scope.py:195-213; mcp/src/agents_remember/application/task_projection/scope.py:216-234 |
| The leaf-only parent read, and why a master's or sprint's parent is not resolved. | `_parent_of` | mcp/src/agents_remember/application/task_projection/scope.py:237-263 |
| The exact accepted task-document bytes this module digests, rather than re-reading the file. | `capture_task_doc_source`; `TaskDocSourceSnapshot` | mcp/src/agents_remember/tasks/store.py:73-82; mcp/src/agents_remember/tasks/store.py:24-36 |
| The topology owner that decides whether a reference resolves and which altitude may carry the seat. | `TaskDocumentTopology`; `TaskDocumentRefError`; `TaskAltitude` | mcp/src/agents_remember/tasks/document_refs.py:87-634; mcp/src/agents_remember/tasks/document_refs.py:39-44; mcp/src/agents_remember/tasks/document_refs.py:32-32 |
| The enclosure contract and its reader — the owner of branch, base commit and leaf identity. | `WorktreeContract`; `load_contract`; `WorktreeContractReader` | mcp/src/agents_remember/worktrees/worktree_contract.py:229-283; mcp/src/agents_remember/worktrees/worktree_contract.py:432-463; mcp/src/agents_remember/worktrees/modules/contract_reader.py:27-29 |
| The resolution shape this module mirrors rather than reinvents. | `resolve_coordination_context` | mcp/src/agents_remember/kernel/coordination_context_resolver.py:129-143 |
| The case that proves every unresolvable input returns its own source-resolution status. | `test_every_unresolvable_input_returns_its_own_source_resolution_status` | mcp/tests/test_task_projection.py:621-696 |
| The case that proves a refused and a successful projection leave the task tree byte-identical. | `test_a_refused_and_a_successful_projection_leave_the_task_tree_byte_identical` | mcp/tests/test_task_projection.py:699-716 |

## Cross-Repo References

No sibling-repository contract consumes this scope resolver.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: created this card for the branch/worktree binding
  module added by the scoped-task-context leaf (`CAPS-R03@v1`). Records the three owners it
  reconciles rather than reimplements, the nine distinct source-resolution refusals with their
  `owner_status` preservation, the leaf-only parent read and its reason, `read_documents` as the
  single document-visibility gate, and the read-only invariant. Verification metadata is left at the
  leaf base commit because the source is uncommitted — the governed closeout stamps the real code
  commit.
