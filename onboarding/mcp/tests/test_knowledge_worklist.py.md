# mcp/tests/test_knowledge_worklist.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_worklist.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T04:44:12+02:00 |
| lastVerifiedCommitHash | `31d761a241055d67b85ef3908033856b78a86a57`|
| lastVerifiedCommitDate | 2026-09-30T05:10:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R08@v2 worklist cases over real Git repositories (21 cases).** Every case builds two real
repositories under `tmp_path`: **code** (a small package `pkg/review.py` with four functions, `pkg/other.py`,
a test module, a ten-line text file and a binary file) and a **converted memory** whose base commit records
realization and proof entries anchored at the code base, two families and their invariants. A case commits a
code candidate C and, where it matters, a memory candidate K_C, then computes the worklist over the four named
sides (`worklist_for_sides`) exactly as the leaf route does.

## Code Commentary

### Logic

- **Fixture.** `ENTRIES` maps eight entries to invariants `INV-AAAAAA` to `INV-FFFFFF` (symbol, line-range
  and file locators, one `proves` entry on `test_refuses_unlisted`); `FAMILIES` groups them. `World` commits
  code and memory, builds anchors and sidecars, and runs `worklist`. `items`, `classes` and `entry_facts`
  index a result. Since MIK-R10, `knowledge_items` (every item but the `UNEXPLAINED_KINDS`) is what the
  "raises nothing" assertions check: an unlinked hunk now raises MIK-R10's `unexplained_hunk`, which is not an
  item about recorded knowledge.
- **Covered obligations:**
  - hunk parsing and line-range mapping arithmetic (definition 2 and 3);
  - the conforming example: a body edit of `_not_listed` raises exactly one `touched_invariant` and its
    `reached_family`, the other entries in the file are `carried`, and siblings are classified; the
    non-conforming "four invariants" case is excluded by the exact item set;
  - the boundary: a comment between functions raises no knowledge item (it is linked to no entry, so it
    raises exactly one `unexplained_hunk`, MIK-R10), a comment inside raises;
  - class precedence: `stale_at_base` first, reaching its families without widening; `moved_or_absent` for
    deletion, rename (with a `mechanical` unique match), ambiguity (no match) and a deleted range;
  - line ranges that map, carry and touch; proof entries in change detection (a changed test body is
    `touched`, a deleted test `moved_or_absent`, on `INV-AAAAAA`);
  - gate linkage: binary changes against a file anchor, text hunks linked by either side's ranges, and a mode
    change with a text change (review R1 F5);
  - maintenance scope; added, retired and re-anchored entries (and new records raising nothing); a
    mechanical carry in K_C is not a change; a re-anchor of a stale entry raises the stale item; a record
    change with both revisions;
  - the registry's four declarations and refused duplicate; item-ID stability and determinism;
  - `incomplete` for an unknown B and an unparseable K_C; no worklist when both memory sides are
    unconverted; the definition-4 ruling (review R1 F3); a partial inventory with a real non-UTF-8 file name
    is `incomplete` (F4).

### Conventions

- Assertions check exact sets and exact classes, not "non-empty".
- The module is registered in the `unit-regression` lane of `test-evidence-lanes.toml`.

### Invariants And Boundaries

- The fixture's `_not_listed`, `test_refuses_unlisted` and `test_accepts_listed` are **fixture source text**
  inside string constants, not test cases of this module.
- Every case runs on real Git trees and real converted memory; nothing is mocked.

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two real repositories each case builds. | "a converted **memory** whose base commit records" | mcp/tests/test_knowledge_worklist.py:1-8 |
| The fixture's entries and locators. | `ENTRIES` | mcp/tests/test_knowledge_worklist.py:85-99 |
| The fixture world and its worklist run. | `World`; `worklist_for_sides` | mcp/tests/test_knowledge_worklist.py:175-251 |
| The knowledge items, without MIK-R10's unexplained kinds. | `UNEXPLAINED_KINDS`; `knowledge_items` | mcp/tests/test_knowledge_worklist.py:287-293 |
| Hunk parsing and mapping. | `test_hunks_parse_and_line_ranges_map_through_the_zero_context_diff` | mcp/tests/test_knowledge_worklist.py:309-328 |
| The conforming body-edit example. | `test_a_body_edit_raises_its_invariant_and_family_and_carries_the_rest_of_the_file` | mcp/tests/test_knowledge_worklist.py:336-361 |
| The comment boundary: no knowledge item between functions, and exactly one unexplained hunk (MIK-R10). | `test_a_comment_between_functions_raises_nothing_and_one_inside_raises` | mcp/tests/test_knowledge_worklist.py:364-379 |
| Proofs in change detection. | `test_proof_entries_take_part_in_change_detection` | mcp/tests/test_knowledge_worklist.py:434-448 |
| Knowledge-side changes. | `test_added_retired_and_reanchored_entries_raise_and_new_records_do_not` | mcp/tests/test_knowledge_worklist.py:488-520 |
| The registry. | `test_the_registry_declares_four_things_per_kind_and_refuses_a_second_registration` | mcp/tests/test_knowledge_worklist.py:559-597 |
| `incomplete` inputs. | `test_unreadable_inputs_make_the_run_incomplete_and_name_them` | mcp/tests/test_knowledge_worklist.py:617-626 |
| Both memory sides unconverted: no worklist. | `test_two_unconverted_memory_sides_get_no_worklist` | mcp/tests/test_knowledge_worklist.py:629-643 |
| The definition-4 ruling. | `test_an_unchanged_blob_is_untouched_whatever_its_recorded_content_says` | mcp/tests/test_knowledge_worklist.py:651-670 |
| A partial inventory. | `test_a_partial_change_inventory_makes_the_run_incomplete_naming_the_paths` | mcp/tests/test_knowledge_worklist.py:673-686 |
| The lane registration. | "mcp/tests/test_knowledge_worklist.py" | mcp/tests/test-evidence-lanes.toml:117-117 |

## Cross-Repo References

No meaningful cross-repo references found: every repository is built under `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): **body updated for MIK-R10.** Recorded the `knowledge_items` helper (three L08 assertions that meant "no knowledge item" now use it) and the comment-between-functions case's new assertion of exactly one `unexplained_hunk`; one row added, the comment-boundary row reworded. Other rows were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-30T02:35:21+00:00: Generated citation repair: `test_unreadable_inputs_make_the_run_incomplete_and_name_them` repointed to mcp/tests/test_knowledge_worklist.py:617-626. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:35:21+00:00: Generated citation repair: "mcp/tests/test_knowledge_worklist.py" repointed to mcp/tests/test-evidence-lanes.toml:117-117. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
