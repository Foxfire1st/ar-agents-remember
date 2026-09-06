# mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `b34f4a59562b76a3e2413027468e0f699117b36f` |
| lastVerifiedCommitDate | 2026-09-06T06:31:12+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Area overview](overview.md)

## Purpose

Publishes one accepted citation-document batch after checking its complete original bytes and frozen source authority.

## Code Commentary

### Logic

`Edit` retains a source span, prior/replacement values, accounting class and optional projection. `DocumentTransaction.render` starts from the original UTF-8 bytes, combines accepted cell edits and generated history, and serializes the final bytes once. `unchanged` rereads the complete path and compares the held snapshot ID, then validates every cell and projection's snapshot/was/now/prior digest.

`preview` returns a validated prospective SHA-256 without writing. `publish` renders, checks immediately before calling `atomic_write_bytes`, then returns the final-byte SHA-256. `projections` adds that same complete digest to the accepted projection records. Missing paths or changed preconditions return refusal without publishing; other I/O failures propagate.

### Conventions

The file has one owner and one mirrored card. Source coordinates below include decorators. The source-index lease and application write-scope authorization remain separate contracts.

### Invariants And Boundaries

- A changed title, padding, history, source cell, truncated document or missing document prevents the entire batch from being published.
- The held source-index snapshot is checked by identity. This does not recensus the live source tree.
- Raw UTF-8 plus LF splitting preserves existing CRLF bytes; right-to-left edits preserve multiple-cell offsets.
- Atomic replacement prevents partial-file publication. There is no memory-file mutex or OS compare-and-swap: an uncooperative writer after the final read is outside this detection guarantee.

### Todos

No additional debt is claimed by this card.

## Docs References

No external Domain Documentation source is configured. The cited behavior is a repository-owned contract, without an external documentation claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

The concrete owners and forcing cases below support this file's contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| Accepted cells carry optional exact-move projection bindings. | `Edit` | mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py:19-27 |
| Cell replacements and generated history compose one final byte sequence. | `render` | mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py:40-52 |
| Complete original bytes and held source-index identity must still match. | `unchanged` | mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py:54-67 |
| Every source cell and optional projection binding is checked. | `_cell_unchanged` | mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py:69-79 |
| Validation precedes atomic byte publication and final digest accounting. | `publish` | mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py:81-87 |
| Preview validates the same preconditions without invoking the writer. | `preview` | mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py:89-92 |
| Each accepted projection receives the complete document digest. | `projections` | mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py:94-99 |
| The existing writer uses a unique temporary file, fsync and atomic replacement; it does not lock. | `atomic_write_bytes` | mcp/src/agents_remember/kernel/atomic_write.py:51-70 |

## Cross-Repo References

This file creates no cross-repository protocol. It composes local citation and file-publication owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| No separate cross-repository authority. | N/A | N/A |

## Update History

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Created the transaction-owner card with exact full-byte/cell/lease checks, CRLF composition, preview/publication accounting and the explicit final-read concurrency limit. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

