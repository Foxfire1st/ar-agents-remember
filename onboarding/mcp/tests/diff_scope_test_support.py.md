# mcp/tests/diff_scope_test_support.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Builds the two-snapshot knowledge and Git fixture used by the diff and review readers.

## Code Commentary

`build_diff_fixture` copies the read-scope fixture into before and candidate datasets, then applies named fixture transitions: successor revisions, realization removals/additions, an unrelated revision and the corresponding source-tree changes. The selected source trees and logical dataset identities remain independently observable.

Fixture rows are inserted by RowStore and realization constructors imported from knowledge_rows_test_support. Realization row digests come from knowledge_row_codec_test_support.claim_row_digest, not a production encoder in records.py. Production read/comparison owners consume those index-shaped datasets. The helper provides no canonical writer, lock, label/lineage/duplicate admission guarantee or claim_no_rewrite enforcement. Historical write-shaped helper names describe fixture construction only.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `build_diff_fixture` supplies the current fixture or assertion described above. [40]
- `_author_revised_revision` supplies the current fixture or assertion described above. [41]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [42]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [43]
