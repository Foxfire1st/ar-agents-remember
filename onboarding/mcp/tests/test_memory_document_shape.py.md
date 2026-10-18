# mcp/tests/test_memory_document_shape.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Memory table parsing and preservation of legitimate code-example content.

## Code Commentary

### Logic

Windows citation cells keep their three columns and fenced diffs remain valid content. The missing-cell case asserts `table_row_cell_count_mismatch`, `1 cells` and the `Nothing is lost` preservation message; it does not assert that the result returns the complete original row. The retained precision cases do not restore removed timezone sorting or closing-diff timestamp rules.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Existing legitimate examples survive a style scan; malformed table rows retain their original-text message rather than silently losing content.

### Todos

No file-local implementation change is requested by this reconciliation.

The Windows-cell precision case now counts the live cell_spans result rather than the removed stripped-cell wrapper. Its three-column and full-document-clean assertions and inputs are preserved; this is assertion-path maintenance, not a changed table contract.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.


- The same Windows citation cell keeps three columns through live cell spans and a clean full-document check. [1]

- A diff quoted in a fenced block is the document working. [2]
- A missing cell is reported. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
