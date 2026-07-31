# mcp/src/agents_remember/kernel/memory_ledger.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/memory_ledger.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`memory_ledger.py` parses, validates, writes, and updates the external-memory
`memory.md` ledger that maps code commits to memory-content commits.

## Code Commentary

### Logic

The module reads a fenced JSON metadata block plus the first `Code commit |
Memory commit` table, validates that the newest table row matches the metadata,
serializes the canonical ledger format, prepends new mappings, finds existing
mappings, and creates an initial ledger.

### Conventions

The parser deliberately uses the standard library and a small markdown/table
grammar rather than pulling in a general markdown or YAML dependency.

### Invariants And Boundaries

- `sortOrder` must remain `newest-first`.
- The first table row must match `lastVerifiedCodeCommit` and
  `lastMemoryContentCommit`.
- `prepend_mapping()` requires both commits and updates metadata and rows
  together.

### Todos

- `parse_ledger_rows()` is a Phase 06 complexity hotspot candidate.

## Docs References

No external documentation is needed for this repository-local ledger format.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for the local ledger parser. | n/a | n/a |

## Repo-Internal References

Same-repository source is the direct evidence for the external-memory ledger
format.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module defines the canonical ledger schema, row and ledger dataclasses, and validation error type (a subclass of `AgentsRememberError`). | L17-L41 | [memory_ledger.py](agents-remember/mcp/src/agents_remember/kernel/memory_ledger.py) |
| `parse_ledger_text()` requires the fenced JSON metadata block, required metadata fields, supported schema, and a valid mapping table. | L51-L104 | [memory_ledger.py](agents-remember/mcp/src/agents_remember/kernel/memory_ledger.py) |
| `validate_ledger()`, `ledger_to_text()`, and `prepend_mapping()` keep metadata and newest-first rows synchronized. | L142-L179; L193-L204 | [memory_ledger.py](agents-remember/mcp/src/agents_remember/kernel/memory_ledger.py) |

## Cross-Repo References

The ledger records code and memory commits across the source repository and its
external memory repository, but the implementation contract is local to this
file and the `c-09-git-worktree-manager` skill worktree manager.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `c-09-git-worktree-manager` direct closeout imports these ledger helpers, then rewrites the code->memory mapping only when it actually changed before committing `memory.md`. | L9-L14; L523-L534 | [modules/closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py) |
| `c-09-git-worktree-manager` integration imports the same helpers and unconditionally prepends the integrated code->memory mapping. | L10-L15; L251-L257 | [modules/integrate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/integrate.py) |

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the cross-repo citation that broke when
  the worktree manager was split into `worktrees/modules/`. `git_worktree_manager.py` is now a
  195-line pure re-export facade with no ledger call in it at all, so the old `L18-L24; L923-L929;
  L1071-L1078` pointed past the end of the file. Split the row in two and repointed to the real
  call sites, both read back: `modules/closeout.py` L9-L14 (import) + L523-L534 (direct-closeout
  mapping update, which now skips the rewrite when `find_mapping` already matches) and
  `modules/integrate.py` L10-L15 (import) + L251-L257 (integration mapping prepend). Claim text
  rewritten to name the two modules and the conditional-vs-unconditional difference.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/kernel/memory_ledger.py` since the L2 base commit is the whole-tree
  `ruff format` pass in `00e8379`, which re-wrapped 1 line(s) with no token change whatsoever.
  Checked by parsing both revisions and comparing the abstract syntax trees (identical) and the
  comment tokens (identical), so no symbol, signature, default, decorator, control-flow branch,
  docstring, or assertion this card describes has moved, and every claim this card makes about its
  own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-05-31T12:30+02:00 — Removed `find_ledger_anchor_commit()` (and its `subprocess` use) from Logic and references; `LedgerError` now subclasses `AgentsRememberError` (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Extracted `_ledger_rows_from` (inner row loop) from `parse_ledger_rows` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
