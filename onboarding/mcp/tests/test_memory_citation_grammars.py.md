# mcp/tests/test_memory_citation_grammars.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_grammars.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `723fd2f1becc130d85d7a6b285b93115be0df852` |
| lastVerifiedCommitDate | 2026-09-13T02:07:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Language-aware declaration resolution for citation repair.

## Code Commentary

### Logic

With the TypeScript grammar a moved declaration resolves uniquely instead of matching mentions; without it the same move declines as ambiguous. Python extents include decorators, classes and members. TypeScript, TSX and JavaScript constructs bind their own names, quoted URLs retain slashes and pooled interface members repair to one defining file.

The grammar fixtures now prove continuity rather than assuming it. `TypeScriptPureMoveTests.moved()` writes the cited `dashboard/src/rail.tsx` holding the `RailRow` declaration and commits it with `Tree.stamp()`, then writes the moved file, deletes the cited one with `remove_source`, and stamps the card at the commit that held the declaration. `TypeScriptInterfacePoolRepairTests.test_three_interface_members_in_another_file_repair_as_one_claim` does the same for `dashboard/src/panels/gone.ts` holding the `PanelProps` interface. The legitimate kind-preserving relocations therefore still repair because the same extent kind is provable at the recorded stamp; the grammar expectations themselves were not relaxed.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

A parser-supported declaration is stronger evidence than textual similarity. Missing grammar support cannot silently justify a confident move. A unique tree-wide name match is likewise not sufficient by itself: the relocation fixtures must show the same extent kind at the card's recorded stamp.

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
| Cited declaration is written, committed and stamped, then moved and removed. | "    def moved(self) -> None:" | mcp/tests/test_memory_citation_grammars.py:40-62 |
| With the grammar the move is repaired onto the declaration. | `test_with_the_grammar_the_move_is_repaired_onto_the_declaration` | mcp/tests/test_memory_citation_grammars.py:73-80 |
| Without the grammar the same move is declined. | `test_without_the_grammar_the_same_move_is_declined` | mcp/tests/test_memory_citation_grammars.py:82-89 |
| A decorated definition is stamped from its first decorator. | `test_a_decorated_definition_is_stamped_from_its_first_decorator` | mcp/tests/test_memory_citation_grammars.py:104-107 |
| A class and its methods and attributes all bind. | `test_a_class_and_its_methods_and_attributes_all_bind` | mcp/tests/test_memory_citation_grammars.py:109-115 |
| Each declaration form binds its name over its own lines. | `test_each_declaration_form_binds_its_name_over_its_own_lines` | mcp/tests/test_memory_citation_grammars.py:137-140 |
| A tsx component is read by the tsx dialect. | `test_a_tsx_component_is_read_by_the_tsx_dialect` | mcp/tests/test_memory_citation_grammars.py:142-145 |
| A javascript module is read by the javascript grammar. | `test_a_javascript_module_is_read_by_the_javascript_grammar` | mcp/tests/test_memory_citation_grammars.py:147-158 |
| A url does not lose its double slash during quote matching. | `test_a_url_does_not_lose_its_double_slash_during_quote_matching` | mcp/tests/test_memory_citation_grammars.py:195-198 |
| Three interface members in another file repair as one claim. | `test_three_interface_members_in_another_file_repair_as_one_claim` | mcp/tests/test_memory_citation_grammars.py:209-248 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded that the grammar move fixtures now prove continuity — the cited `RailRow` declaration and the pooled `PanelProps` interface are written, committed with `Tree.stamp()`, then moved and deleted with `remove_source`, and the cards are stamped at the commit that held them — so the legitimate kind-preserving relocations still repair and the grammar expectations were not relaxed. Corrected every reference range to the measured source. Verification metadata remains closeout-owned.

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
