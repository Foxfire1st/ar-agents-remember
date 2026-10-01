# mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py

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

## Evidence

### Docs References

No external Domain Documentation source is configured. The cited behavior is a repository-owned contract, without an external documentation claim.

No configured external domain source.

### Repo-Internal References

The concrete owners and forcing cases below support this file's contract.

- Accepted cells carry optional exact-move projection bindings. [1]
- Cell replacements and generated history compose one final byte sequence. [2]
- Complete original bytes and held source-index identity must still match. [3]
- Every source cell and optional projection binding is checked. [4]
- Validation precedes atomic byte publication and final digest accounting. [5]
- Preview validates the same preconditions without invoking the writer. [6]
- Each accepted projection receives the complete document digest. [7]
- The existing writer uses a unique temporary file, fsync and atomic replacement; it does not lock. [8]

### Cross-Repo References

This file creates no cross-repository protocol. It composes local citation and file-publication owners.

No separate cross-repository authority.
