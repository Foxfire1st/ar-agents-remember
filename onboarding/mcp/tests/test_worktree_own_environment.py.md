# mcp/tests/test_worktree_own_environment.py

## Governing Overview

[tests overview](overview.md)

## Purpose

Guards the separation between repository-specific candidate environments and generic product
instructions. The canonical worker brief and all nine shipped copies point to the tool notes,
not a concrete interpreter. Candidate checks run in their own code worktree's environment.

## Code Commentary

### Logic

The first case checks all ten template surfaces for the tool-notes pointer, absence of the named
interpreter/source-path tokens, and the requirement to record the interpreter actually used.
The second scans canonical role, operation and template Markdown for those tokens. A discriminator
case shows the predicate rejects the retired interpreter line and accepts the shipped template.

The accounting case calls the product's `changed_worktree_paths` on the repository holding a real
`mcp/.venv` and rejects any returned `.venv` or `node_modules` path. Its precondition refuses a run
without that venv. The Node half is structural when no `dashboard/node_modules` exists; this case
is not an executed sync, closeout, landing or cleanup demonstration.

### Invariants And Boundaries

- Build the worktree environment as `system/tools.md` prescribes and run this candidate test with
  that worktree's interpreter. Editable installation supplies the candidate package.
- The token census covers canonical `roles`, `operations` and `templates`; the ten-copy check is
  for the worker brief, not an assertion that every generated instruction file was scanned.
- The tests do not build an environment, choose a language-server setting, invoke a transaction,
  certify a landing or decide whether instruction-only setup is enough for later tasks.
- Installed AR tools and memory-operation commands remain the landed product.

## Evidence

### Docs References

No Domain Documentation source is configured. These are repository-owned instruction and Git
accounting contracts; no external source is claimed.

### Repo-Internal References

- All shipped worker briefs must delegate environment setup and record the actual interpreter. [1]
- Canonical instruction surfaces contain no named candidate-interpreter tokens. [2]
- The token predicate rejects the retired wording rather than passing vacuously. [3]
- The accounting case requires a built venv and excludes either environment directory from the working inventory; it does not run the lifecycle. [4]

### Cross-Repo References

No sibling-repository boundary is exercised. Assertions and catalog registration do not establish
transaction or language-server execution evidence.
