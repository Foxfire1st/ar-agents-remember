# mcp/tests/test_memory_citation_grammars.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_grammars.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Language-aware declaration resolution for citation repair.

## Code Commentary

### Logic

With the TypeScript grammar a moved declaration resolves uniquely instead of matching mentions; without it the same move declines as ambiguous. Python extents include decorators, classes and members. TypeScript, TSX and JavaScript constructs bind their own names, quoted URLs retain slashes and pooled interface members repair to one defining file.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

A parser-supported declaration is stronger evidence than textual similarity. Missing grammar support cannot silently justify a confident move.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| With the grammar the move is repaired onto the declaration. | `test_with_the_grammar_the_move_is_repaired_onto_the_declaration` | mcp/tests/test_memory_citation_grammars.py:61-68 |
| Without the grammar the same move is declined. | `test_without_the_grammar_the_same_move_is_declined` | mcp/tests/test_memory_citation_grammars.py:70-77 |
| A decorated definition is stamped from its first decorator. | `test_a_decorated_definition_is_stamped_from_its_first_decorator` | mcp/tests/test_memory_citation_grammars.py:92-95 |
| A class and its methods and attributes all bind. | `test_a_class_and_its_methods_and_attributes_all_bind` | mcp/tests/test_memory_citation_grammars.py:97-103 |
| Each declaration form binds its name over its own lines. | `test_each_declaration_form_binds_its_name_over_its_own_lines` | mcp/tests/test_memory_citation_grammars.py:125-128 |
| A tsx component is read by the tsx dialect. | `test_a_tsx_component_is_read_by_the_tsx_dialect` | mcp/tests/test_memory_citation_grammars.py:130-133 |
| A javascript module is read by the javascript grammar. | `test_a_javascript_module_is_read_by_the_javascript_grammar` | mcp/tests/test_memory_citation_grammars.py:135-139 |
| A url does not lose its double slash during quote matching. | `test_a_url_does_not_lose_its_double_slash_during_quote_matching` | mcp/tests/test_memory_citation_grammars.py:183-186 |
| Three interface members in another file repair as one claim. | `test_three_interface_members_in_another_file_repair_as_one_claim` | mcp/tests/test_memory_citation_grammars.py:192-215 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
