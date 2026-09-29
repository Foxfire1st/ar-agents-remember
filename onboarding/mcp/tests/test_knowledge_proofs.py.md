# mcp/tests/test_knowledge_proofs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_proofs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T15:26:13+02:00 |
| lastVerifiedCommitHash | `e49ba07865b3848cd36759cea6b37bba7d0d51c3`|
| lastVerifiedCommitDate | 2026-09-29T15:47:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R28 cases: tests that prove an invariant are first-class proof entries.** The module covers
rule 2 (both evidence forms, the curator's facet, unresolvable evidence reported), rule 4 (the `proofs` of
the `invariant` and `family` views of a converted tree, and none for a database), rule 5 (the index's
"without proof" list and the informational checklist section) and rule 6 (migrated evidence listed, then
turned into a proof by a curator pass through the writer). Rule 3 and the stale-proof clause are not
covered here: by architect ruling they belong to L08 and L03.

## Code Commentary

### Logic

- **Rule 2, the parser.** A parametrized case reads `path::Class::method` as `Class.method`, `path -k name`
  (bare, quoted, backticked, bracketed, parenthesized, double-quoted), `-k` expressions that name only the
  file, a bare test module, helper modules that are never reported, and text with no test. A second case checks that a file
  named with a test anywhere in the evidence is not also reported bare, in both string orders.
- **Rule 2, the writer.** Both forms become `PRF-` proofs with symbol anchors once `proofs` carries a
  facet; an absent `-k` test and a bare file are `unresolvable`, and the rendered report says so. A proof
  waits for the curator's facet: no sidecar is written until it is authored, the report offers the
  statement as a draft, and a blank facet is refused and writes nothing.
- **Rule 4.** A review tree (`write_review_tree`) with a proven and an unproven invariant: the `invariant`
  view carries the proof or `[]`, the `family` view carries every member's proofs, and no pass or result
  key exists. The parity database fixture's `invariant` and `family` reads, and the other views, carry no
  `proofs`. A family whose members have no proof shows `[]`.
- **Rules 5 and 6.** The index lists live invariants without proof and excludes a retired one. The
  checklist renders the section as information: the wire summary is identical with and without the list,
  the count stays 0, and an unconverted checklist has no section. Migrated evidence is listed with its
  named test, the controller hands exactly that list to the checklist (`None` for an unconverted tree), and a
  writer pass with `invariant_id` and `proofs` writes the proof and empties the list. The list reuses the
  cached index and reports a refused cache location as `unreadable` without creating it.

### Conventions

- The writer cases build their worlds with `knowledge_writer_test_support`; the view and list cases use
  `knowledge_index_test_support`'s review tree. Both are catalog rows this module consumes (see
  `evidence-lifecycle.toml`).

### Invariants And Boundaries

- No case runs a test or asserts a pass: a proof is what its test demonstrates, not a result.
- The module is registered in the `unit-regression` lane (`test-evidence-lanes.toml:112`).

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R28@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in `28_first-class-test-proofs.json`);
it lives outside the code and memory repositories, so it is named here and not cited as a row.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The cases, by rule.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's statement of the rules it covers. | "tests that prove an invariant are first-class proof entries" | mcp/tests/test_knowledge_proofs.py:1-11 |
| The writer runs as this leaf's owner. | `OWNER`; `_write` | mcp/tests/test_knowledge_proofs.py:79-79; mcp/tests/test_knowledge_proofs.py:82-92 |
| The parser's forms, expressions and helper modules. | `test_evidence_names_a_test_as_a_test_id_or_as_a_path_plus_symbol` | mcp/tests/test_knowledge_proofs.py:98-146 |
| No bare row for a file named with a test elsewhere. | `test_a_file_named_with_a_test_anywhere_in_the_evidence_is_not_also_reported_bare` | mcp/tests/test_knowledge_proofs.py:149-152 |
| Both forms become proofs once faceted; unresolvable evidence is reported. | `test_both_forms_become_proofs_once_faceted_and_unresolvable_evidence_is_reported` | mcp/tests/test_knowledge_proofs.py:155-200 |
| A proof waits for the curator's facet. | `test_a_proof_waits_for_the_curator_facet_and_is_offered_the_statement_as_a_draft` | mcp/tests/test_knowledge_proofs.py:203-224 |
| The view cases' tree and read helper. | `_review_tree`; `_read` | mcp/tests/test_knowledge_proofs.py:230-235; mcp/tests/test_knowledge_proofs.py:238-242 |
| Invariant and family views carry their proofs. | `test_the_invariant_and_family_views_carry_their_proofs` | mcp/tests/test_knowledge_proofs.py:245-277 |
| A database read and the other views carry none. | `test_a_database_read_and_other_views_carry_no_proofs` | mcp/tests/test_knowledge_proofs.py:280-319 |
| A family with no proof shows `[]`. | `test_a_family_whose_members_have_no_proof_shows_an_empty_list` | mcp/tests/test_knowledge_proofs.py:322-337 |
| Live invariants without proof; a retired one is excluded. | `test_the_index_lists_live_invariants_without_proof` | mcp/tests/test_knowledge_proofs.py:343-356 |
| The checklist section is information that moves no count. | `test_the_checklist_shows_the_list_as_information_that_moves_no_count` | mcp/tests/test_knowledge_proofs.py:398-426 |
| Migrated evidence is listed, then a curator pass writes the proof. | `test_migrated_evidence_is_listed_then_turned_into_a_proof_by_a_curator_pass` | mcp/tests/test_knowledge_proofs.py:429-466 |
| The cached index is reused and an unreadable one reported. | `test_the_list_reuses_the_cached_index_and_reports_an_unreadable_one` | mcp/tests/test_knowledge_proofs.py:469-485 |

## Cross-Repo References

No meaningful cross-repo references found: every case builds its own temporary code and memory
repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): created this card for the new test module MIK-R28 adds (22 cases). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
