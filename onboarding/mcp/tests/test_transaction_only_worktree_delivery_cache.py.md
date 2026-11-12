# mcp/tests/test_transaction_only_worktree_delivery_cache.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The memory-cache refresh cases of the transaction-only delivery module (CCR-R12): an existing correct cache is untouched, a missing one is rebuilt, and corrupted or forged data is repaired from Git alone.

## Code Commentary

`_ClosedCacheLeaf` builds one closed external leaf and the disposable cache derived from its Git attribution, and `git_state` fingerprints the repository around each refresh. The first case refreshes a current cache, asserts its bytes and the Git state are unchanged, deletes it, refreshes again, and requires the rebuilt cache to equal the canonical ledger by `load_ledger` and by `ledger_to_text` while the Git state still matches. The second case writes four malformations: text that is not a ledger, forged memory and code mappings, reordered rows, and a header that disagrees with its first row. Each is repaired to the canonical ledger with the Git state unchanged and the worktree content untouched.

## Invariants And Boundaries

The refresh writes no commit object and no ref: every case compares HEAD, the refs and the commit-object inventory before and after, and the payload-byte and status checks hold. The reconstructed attribution comes from Git, not from the cache, so a forged row cannot survive a refresh.

## Evidence

### Repo-Internal References

- A current cache is preserved byte for byte, and a missing one is rebuilt to the canonical ledger. [1]


- Malformed, forged, reordered and wrongly headed caches are repaired with no Git commit object or ref written. [2]

