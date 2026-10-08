# mcp/tests/test_knowledge_paging.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Pins token-bounded converted-tree leaf/view paging and continuation bindings.

## Code Commentary

Nine test functions cover exact family walks without duplicate/lost rows, randomized page bounds, an oversized row returned alone and flagged, whole multi-seed block bounds, deferred seed queues, view ordering, code-tree-bound resumed leaf/view walks and refusal of an empty ordering. The named code repository and page-one tree remain part of continuation identity.

Fixtures write converted text documents and Git trees through knowledge_index_test_support. Source assertions distinguish page enumeration from full index completeness and refuse invalid or moved continuation inputs without a payload. The retired projection-over-artifact-limit test and former eleven-case account are removed coverage, not a current projection contract.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_a_forty_member_family_pages_from_read_ar_files_through_knowledge_read_exactly_once` supplies the current fixture or assertion described above. [13]
- `test_a_row_larger_than_the_threshold_is_returned_alone_and_flagged` supplies the current fixture or assertion described above. [14]
- `test_the_whole_knowledge_block_of_several_seeds_stays_within_the_threshold` supplies the current fixture or assertion described above. [15]
- `test_a_view_walk_is_bound_to_its_named_code_tree` supplies the current fixture or assertion described above. [16]
