# mcp/tests/read_scope_test_support.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Constructs an index-shaped dataset and a real Git tree with the topology needed by bounded scope-read tests.

## Code Commentary

The fixture retains exact invariant/family/revision identities, source locators, applicability, conditions, exclusions and memberships. Its topology deliberately distinguishes directly containing families, sibling realizations, an advertised unreached family, absent/unparsed/mismatched sources and explicit stopping boundaries. Callers use the returned identities rather than inferring relationships from names.

RowStore, revision, family, membership and realization constructors are imported from knowledge_rows_test_support and insert test-only rows. Their production-shaped names do not make them shipped authoring operations or establish the retired storage admission rules. The Git source and current read owners are real; dataset construction is a test fixture.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `build_read_scope_fixture` supplies the current fixture or assertion described above. [11]
- `_create_invariant` supplies the current fixture or assertion described above. [12]
- `_create_revision` supplies the current fixture or assertion described above. [13]
- `_create_realization` supplies the current fixture or assertion described above. [14]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [15]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [16]
