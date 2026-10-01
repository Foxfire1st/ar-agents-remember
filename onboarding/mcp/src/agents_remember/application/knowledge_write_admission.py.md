# mcp/src/agents_remember/application/knowledge_write_admission.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The value the curator's ingest operation is bound to, instead of a document (ICR-R29@v1).** Until
this leaf the operation resolved every tree, identity, retry scope and root it used from a
`WorktreeContract` — a **leaf enclosure contract** — so the operation's own input shape said that a
repository's knowledge can only be written by a task that already has a worktree. A repository's
*first* knowledge has no task and no enclosure, and the bootstrap handover refuses minting one to
satisfy the shape (`BOOTSTRAP-HANDOVER.md` line 11); a second write path is the parallel-store defect
the preservation boundaries name. The honest third option is what this module makes possible: bind the
operation to **the facts it actually reads**, and let a second *real* admission be built for a context
with no enclosure.

`KnowledgeWriteAdmission` (`:79-131`) is exactly that field set, renamed to say what each field is in
*any* admission rather than only inside a leaf: the retry `scope`, the repository name, the
coordination root, the code and memory roots, the exact `code_base_commit`/`memory_base_commit`, the
code work branch, and the `source_ref` document the admission was read from.

**Two admissions, one implementation.** `enclosure_admission` (`:134-165`) derives one from a contract
and `admit_bootstrap_context` derives one from the repository and setup authority. Neither wraps the
other and neither restates a rule: the operation downstream of this value is identical for both, which
is what makes "reuse the namespace, identity allocation, candidate, batch, snapshot and publication
owners" a fact about the call graph rather than a claim in a report.

**Provenance is a value, never a boolean.** `AdmissionProvenance` (`:63-76`) names *what* admitted the
write, the exact document it was read from and the one fact that made it an admission. There is
deliberately no `admitted=True` parameter anywhere on this path: a caller cannot assert an admission,
it can only be handed one a resolver built after its own checks — the handover's "a client-supplied
boolean is not authority" clause, held by the shape of the type rather than by a check.

**What this value is not.** It confers no authority by itself (it is a frozen record of facts a
resolver already established) and it decides nothing about a destination, a namespace or an identity:
those stay with the operation and the shipped owners it calls.

## Code Commentary

### Logic

**The two admissions are a declared vocabulary, not a flag** (`:55-60`). `AdmissionKind` is the
`Literal["leaf-enclosure", "repository-bootstrap"]`; `ENCLOSURE_ADMISSION_KIND` and
`BOOTSTRAP_ADMISSION_KIND` are the constants. The comment states why it is a stored vocabulary: a
reader of a report or a retained progress record branches on the spelling rather than on prose.
`KnowledgeWriteAdmission.kind` (`:121-125`) exposes it and `is_bootstrap` (`:127-131`) is the one
convenience predicate over it.

**`enclosure_admission` derives nothing** (`:134-165`). It reads the cells the operation needs out of
the contract and states in the provenance that a real contract is what admitted the write, with
`detail` naming the enclosure and the code base commit the contract recorded when the enclosure was
cut. No commit, no tree and no identity is computed here.

**One coercion at the operation's front door** (`:168-184`). `as_write_admission` passes a value that
is already a `KnowledgeWriteAdmission` through **untouched** — its provenance is the fact being
carried, and re-deriving it would replace a real authority with a guess — adapts a `WorktreeContract`
through the factory above, and loads a path through the shipped contract loader so the loader's own
refusals are the caller's.

**`memory_repo_path` is optional and `memory_worktree` is not** (`:100-106`): a repository with no
external memory layer has no memory repository to name, while `memory_worktree` is the strictly
stronger requirement the operation itself refuses on, exactly as it did when it read a contract.

### Conventions

The module imports the contract loader and nothing else from the application or kernel planes; it
performs no I/O, reads no Git and holds no state. Its `__all__` (`:45-53`) is the whole published
surface.

### Invariants And Boundaries

- There is no `admitted=True` argument on this path; an admission is built by a resolver, never
  asserted by a caller.
- An admission confers no authority and decides no destination, namespace or identity.
- `enclosure_admission` computes no commit, tree or identity; it reads what the contract recorded.
- `as_write_admission` passes an existing admission through untouched rather than re-deriving it.
- `memory_repo_path` may be `None`; `memory_worktree` is the requirement the operation refuses on.
- `scope` is the **retry** scope: it is what makes "an exact retry does not duplicate knowledge" true
  without the retry key ever becoming an identity input.
- **The frozen database (L37, MIK-R37 rule 3).** `as_write_admission` is the database batch writer's front door:
  after resolving the admission it calls `_require_unfrozen_database`. An admission whose memory worktree holds
  `knowledge/layout.json` raises `KnowledgeDatabaseFrozen`, naming the curator file writer
  (`publication.FILE_WRITER_ROUTE`: `knowledge-ingest`, or `knowledge-bootstrap --wave`); the tree's
  `knowledge.sqlite` stays in place, unwritten, until MIK-R26 removes it. An unconverted tree in a memory
  repository that holds converted memory raises the same class with the cutover lock's refusal (MIK-R09 rule 6).
  An unconverted tree in a repository with no converted memory is admitted as before. `_require_unfrozen_database`
  is a realization of INV-1XKX9ERN.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; `BOOTSTRAP-HANDOVER.md` is the process authority
this value implements, and it is a task-tree document rather than a configured domain source.

No external documentation is required for the write-admission value.

### Repo-Internal References

- **The module's own statement of the gap it closes and of why a second write path was refused.** [1]
- The published surface: the two kind constants, the value, the provenance and the two builders. [2]
- **The two admissions as a declared, stored vocabulary rather than a boolean.** [3]
- **Provenance as a value: what admitted the write, from which document, and the one fact that made it an admission.** [4]
- **The facts one admitted write is bound to, including the retry scope and the two exact source revisions.** [5]
- The optional memory repository against the required memory worktree the operation refuses on. [6]
- Which authority admitted this write, and whether it was derived without an enclosure. [7]
- **The enclosure adapter that derives nothing and states that a real contract admitted the write.** [8]
- **The one coercion at the front door: an existing admission is passed through untouched, never re-derived.** [9]
- The shipped contract loader and the document type the enclosure adapter reads. [10]
- **The second real admission this value exists to carry, and the resolver that builds it.** [11]
- The one operation both admissions reach. [12]

- The front door resolves the admission, then refuses a frozen or locked database. [13]
- The database writer is frozen on a converted tree and names the file writer. [14]

### Cross-Repo References

No cross-repository behavior is implemented in this file: it reads no repository at all. The resolved
settings' `crossRepo.allow` is empty, so nothing here names, reads or writes another repository.

No meaningful cross-repo references found.
