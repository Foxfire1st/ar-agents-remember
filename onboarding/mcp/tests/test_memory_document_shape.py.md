# mcp/tests/test_memory_document_shape.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Memory table parsing and history timestamp repair boundaries.

## Code Commentary

### Logic

Windows citation cells keep their three columns and fenced diffs are valid content. Missing cells report their original text. Mixed timezone frames are caught and refused for sorting; newly added naive timestamps fail within the closing diff, while a renamed old document is not treated as newly authored.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

History repair may not guess an offset or reorder incomparable timestamps. Existing examples and source evidence must survive a style check.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- The same windows cell in a three column table keeps its columns. [1]
- A diff quoted in a fenced block is the document working. [2]
- A missing cell is reported. [3]
- The live mixed frame pair is caught instead of passing silently. [4]
- The fixer refuses to sort a section that mixes frames. [5]
- A naive bullet this closeout adds fails. [6]
- A renamed document is not treated as newly written. [7]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
