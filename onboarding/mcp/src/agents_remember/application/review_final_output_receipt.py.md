# mcp/src/agents_remember/application/review_final_output_receipt.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Bind a retained four-tree comparison to the exact code and memory trees a completed closeout or integration delivered. Receipts measure completed transactions and never gate them.

## Code Commentary

### Logic

`select_review_comparison` selects the highest retained tree record, names unreadable or conflicting records, and reports historical dataset generations alone as `legacy-limit`. Recording reads the delivered code and memory-content commit trees from the comparison's own repositories and records their exact match verdicts.

Read-back distinguishes missing, unreadable and recorded phase receipts. A current receipt must describe the retained comparison. Historical v1 receipts remain readable as `legacy-limit`; their recorded source and dataset identities prove no exact reviewed memory tree. Later comparisons label successors without rewriting earlier receipts.

### Invariants And Boundaries

Code agreement alone proves no delivered-pair coverage. Absent or moved memory cannot become conformance. Unknown or corrupt comparisons do not undo a completed transaction. Both transaction result keys remain. No current HEAD, dataset or new comparison substitutes for missing historical proof.

### Todos

None recorded.

## Evidence

### Repo-Internal References

Phase measurement can replace the same phase receipt; retained comparison records are not rewritten. Exact source selection and both delivered trees remain separate from transaction acceptance.

- `select_review_comparison` supplies the current exact-tree receipt boundary described above. [33]
- `record_final_output_receipt` supplies the current exact-tree receipt boundary described above. [34]
- `_read_receipt` supplies the current exact-tree receipt boundary described above. [35]
- `final_output_selection_block` supplies the current exact-tree receipt boundary described above. [36]
- `final_output_result_block` supplies the current exact-tree receipt boundary described above. [37]
- `require_comparison_repositories` supplies the current exact-tree receipt boundary described above. [38]
- `source_comparison_matches` supplies the current exact-tree receipt boundary described above. [39]
- The old canonical published-dataset receipt channel was retired. Separately, ordinary published intent resolves a converted tree and its index; it is not a canonical receipt publication channel. [29]
