# mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Defines exact final-output receipts for tree-bound comparisons while decoding the historical receipt format separately.

## Code Commentary

FinalOutputReceipt binds the recorded code and knowledge trees and their comparison digest. `tree_match_state` and `tree_output_verdict` compare the actually supplied identities; an unread half is not matching. LegacyFinalOutputReceipt retains the historical code/logical-dataset shape and its validator functions without reopening that dataset. The removed _code_clause/_knowledge_clause helpers are not current rendering owners. A receipt is data about exact compared outputs, never leaf or Git acceptance.

## Evidence

### Repo-Internal References

- `FinalOutputReceipt` owns the current boundary described above. [19]
- `tree_comparison_digest` owns the current boundary described above. [20]
- `tree_output_verdict` owns the current boundary described above. [21]
- `LegacyFinalOutputReceipt` owns the current boundary described above. [22]
