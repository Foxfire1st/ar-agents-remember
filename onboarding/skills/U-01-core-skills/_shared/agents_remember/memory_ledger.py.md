# memory_ledger.py

| Field                  | Value                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember-md                                                 |
| path                   | `skills/U-01-core-skills/_shared/agents_remember/memory_ledger.py` |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-05-12T10:59                                                   |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a`                         |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

`memory_ledger.py` is the common parser, validator, and writer for external-memory `memory.md` ledgers.

## Code Commentary

### Logic

The module parses a fenced `json ar-memory-ledger` metadata block, reads the first `Code commit | Memory commit` table after it, validates required fields and top-row consistency, writes canonical branchless ledger text, prepends new mappings, and can locate the Git commit that introduced a ledger row. The current writer emits `ar-memory-ledger/v1`; the parser still accepts legacy `ar-memory-branch-ledger/v1` files so existing ledgers can be migrated by rewriting them.

### Conventions

The helper accepts only strict JSON metadata and a two-column newest-first markdown table. Branch names are not part of the canonical ledger identity; compatibility is represented by code commit to memory commit rows. It exposes dataclasses and raises `LedgerError` for invalid ledgers.

### Invariants And Boundaries

The first table row must match `lastVerifiedCodeCommit` and `lastMemoryContentCommit`. The helper does not create memory repos or perform task closeout; C-09 owns lifecycle work.

### Todos

After the first real external-memory repo is bootstrapped, add fixture coverage for ledger-anchor lookup across actual Git history.

### Docs References

No external documentation is needed; this is repository-local standard-library logic.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                                                    | Citations          | Source Path                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------- |
| The module defines the ledger dataclass and strict `LedgerError` failure type.                                             | L28-L41            | [memory_ledger.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/memory_ledger.py) |
| Parsing requires a fenced JSON metadata block, required metadata fields, supported schema, and a two-column mapping table. | L53-L91; L115-L129 | [memory_ledger.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/memory_ledger.py) |
| Validation requires newest-first ordering and top-row consistency with the metadata's last verified commits.               | L144-L153          | [memory_ledger.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/memory_ledger.py) |
| Writing, prepending, lookup, and initial-ledger helpers provide the common API C-09 and C-10 consume.                      | L156-L224          | [memory_ledger.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/memory_ledger.py) |
| The worktree design spec defines the ledger as the code-to-memory compatibility map.                                       | L451-L557          | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |

## Cross-Repo References

No sibling repository evidence is needed for the helper itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-12T10:59: Updated the ledger contract notes after branch fields were removed from canonical `memory.md` metadata while preserving legacy parse support.
- 2026-05-09T21:59: Created onboarding for the new external memory ledger helper.
- 2026-05-09T22:57: Refreshed verification metadata and added source-level evidence for parser/writer behavior.
