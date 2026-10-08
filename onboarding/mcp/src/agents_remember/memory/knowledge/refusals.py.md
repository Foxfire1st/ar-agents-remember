# mcp/src/agents_remember/memory/knowledge/refusals.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Shared typed index-read refusals and the storage-defect exception. A refusal names the exact code, operation, identifying facts and next action; a storage failure with no contract code is a defect rather than an expected outcome.

## Code Commentary

### Logic

KnowledgeStorageError reports an unclassified storage failure. RefusalFacts carries optional table, record_id, expected and observed values. refusal constructs KnowledgeRefusal with those facts and the required next_action.

selected_input_unavailable_refusal refuses an explicitly selected input that is absent or unreadable. A missing selection is an input error, never an empty dataset. Its next action names restoration of the exact recorded memory tree or rebuilding its derived index; no current tree is substituted.

### Invariants And Boundaries

- Expected failures are typed values, so callers branch on a code rather than parsing prose.
- This module neither repairs a selection nor creates a dataset to make a read succeed.
- KnowledgeStorageError identifies a defect that the contract vocabulary does not describe.

### Historical boundary — MIK-R26

Canonical database mutation factories, KnowledgeRefused transaction control flow, lineage and relation factories, SQLite-error mapping, candidate/publication factories and composition factories were retired. Their old mutation guarantees are not current entry points of this module; the retained functions serve index reads.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- A storage failure with no contract code is a defect. [1]


- The identifying facts and generic typed-refusal constructor. [2]


- An absent or unreadable explicit selection is refused without substituting a current tree. [11]


- The retained refusal value and its declared code vocabulary. [14]


### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
