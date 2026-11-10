# mcp/tests/test_worktree_own_environment.py

## Governing Overview

[overview](overview.md)

## Purpose

Guards the separation between repository-specific candidate environments and generic product
instructions. The canonical Worker role's candidate-environment action and every declared package copy point to the
tool notes, not a concrete interpreter. Candidate checks run in their own code worktree's environment.

## Code Commentary

### Logic

The first case checks `roles/worker.md` in the canonical tree and every declared copy for the tool-notes
pointer, absence of the named interpreter/source-path tokens, and exactly one occurrence each of the four
clauses: build the environment as `system/tools.md` says, run every candidate command in it, report a command
the tool notes lack, and record the interpreter each run used.
The second scans canonical role, operation and template Markdown for those tokens. A discriminator
case shows the predicate rejects the retired interpreter line and accepts the shipped canonical Worker role.

The accounting case initializes a temporary Git repository, copies the product `.gitignore`, builds its own `mcp/.venv` with `venv.EnvBuilder(with_pip=False)`, and populates `dashboard/node_modules` with a fixture file. It calls the product's `changed_worktree_paths` on that repository and rejects any returned `.venv` or `node_modules` path. Both fixture directories are present; it does not depend on a live candidate venv. The copy census is imported from the shared declaration-derived `GENERATED_SKILL_COPIES` registry. These source assertions are not an executed sync, closeout, landing or cleanup demonstration.

### Invariants And Boundaries

- Build the worktree environment as `system/tools.md` prescribes and run this candidate test with
  that worktree's interpreter. Editable installation supplies the candidate package.
- The token census covers canonical `roles`, `operations` and `templates`; the copy check is
  for the Worker role file, not an assertion that every generated instruction file was scanned.
- Only the accounting case builds a temporary no-pip environment fixture. The tests do not provision a real candidate environment, choose a language-server setting, invoke a sync/closeout transaction, certify a landing or decide whether instruction-only setup is enough for later tasks.
- Installed AR tools and memory-operation commands remain the landed product.

## Evidence

- The accounting case creates a temporary Git/venv/node_modules fixture with product ignore rules and checks both environment directories are absent from the changed-worktree inventory. [5]


### Docs References

No Domain Documentation source is configured. These are repository-owned instruction and Git
accounting contracts; no external source is claimed.

### Repo-Internal References

- Every shipped copy of the Worker candidate-environment action must delegate environment setup and record the actual interpreter. [1]

- Canonical instruction surfaces contain no named candidate-interpreter tokens. [2]

- The token predicate rejects the retired wording rather than passing vacuously. [3]

- The accounting case requires a built venv and excludes either environment directory from the working inventory; it does not run the lifecycle. [4]


### Cross-Repo References

No sibling-repository boundary is exercised. Assertions and catalog registration do not establish
transaction or language-server execution evidence.
