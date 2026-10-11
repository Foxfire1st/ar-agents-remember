# mcp/src/agents_remember/application/review_final_output_receipt.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Bind a retained four-tree comparison to the exact code and memory trees a completed closeout or integration delivered. Receipts measure completed transactions and never gate them.

## Code Commentary

### Logic

`select_review_comparison` selects the highest retained tree record, names unreadable or conflicting records, and reports historical dataset generations alone as `legacy-limit`. Recording reads the delivered code and memory-content commit trees from the comparison's own repositories and records their exact match verdicts. A delivery without a memory commit on a leaf that holds a comparison writes no receipt (ruling 814778): the caller answers not-recorded with that reason.

Read-back distinguishes missing, unreadable and recorded phase receipts. A current receipt must describe the retained comparison. Historical v1 receipts remain readable as `legacy-limit`; their recorded source and dataset identities prove no exact reviewed memory tree. Later comparisons label successors without rewriting earlier receipts.

### Invariants And Boundaries

Code agreement alone proves no delivered-pair coverage. Absent or moved memory cannot become conformance. Unknown or corrupt comparisons do not undo a completed transaction. Both transaction result keys remain. No current HEAD, dataset or new comparison substitutes for missing historical proof.

### Todos

None recorded.

### Logic

**Publication and read-back are the durable-evidence pair.**
`record_final_output_receipt` (`:258-299`) publishes through `publish_durable_evidence` under
`receipt_file_name` (`:252-255`) — `final-output-<leaf>-<generation-id>-<phase>.json` in the shipped
durable reports root — and returns the record beside `read_back_evidence`'s result. A phase measured
twice converges on one file and reports `replaced_existing`, because the record says what that phase
delivered **when it was read**.

### Invariants And Boundaries

- **Nothing here can refuse a transaction.** The recording runs *after* the Git transaction and its
  contract write, inside the result builder; every failure becomes a state in the payload. The one
  raising function is `record_final_output_receipt`, and the transaction owners deliberately call the
  never-raising wrapper instead.
- **A phase that recorded nothing is still reported.** `read_final_output_receipts` returns one entry per
  phase, so "nothing was recorded" and "no phase was asked about" never read the same.
- **One file per (leaf, generation, phase)**, so a leaf accumulates at most two files per generation it
  publishes and a repeated measurement converges on its own location.

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

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads a task root and a repository path the worktree contract names, and it resolves the declared publication location inside the same repository boundary.

### Repo-Internal References

- The one durable file-name prefix, one file per leaf, generation and phase. [40]
- One published receipt: the durable artifact, the record, and the read-back that proves it. [41]
- The one durable destination a phase publishes to. [42]
- **Measuring one phase and publishing it: the owners' values, the read-back, and `replaced_existing` rather than a hidden rewrite.** [43]
- **The prepared-work projection: the one comparison it makes, and `None` rather than `True` when either side is unknown.** [44]
- **The three attachments and the `ok`-plus-a-real-commit gate that keeps a failed transaction from carrying a receipt.** [45]
- **The never-raising entry point and its three states, including `not-applicable` for a series contract.** [46]
- **The three production call sites: closeout preview, closeout apply and integration.** [47]
- **The reopen owner's fourth channel, which is what makes the reader a production consumer.** [48]
- The durable-evidence pair every receipt is published and read back through. [49]
