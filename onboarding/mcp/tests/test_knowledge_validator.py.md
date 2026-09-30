# mcp/tests/test_knowledge_validator.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_validator.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R22 rules 1–9 at unit level, over converted fixture trees.** Each test changes one thing in the fixture tree and checks that exactly the owning rule answers, with its rendered file, field and rule (`_only`). Since leaf 260928-MIK-L27 its last section also proves MIK-R27's admission rules, which that packet adds to the registry (rule 9). Registered in the `unit-regression` lane; 46 collected cases (9 of them MIK-R27's).

## Code Commentary

### Logic

- **Baseline:** the fixture tree passes every rule, MIK-R04's route rules included; the report-only set **owned by MIK-R22** (filtered by `owner.startswith("MIK-R22")` since leaf 260928-MIK-L04) is pinned to `R22.3-sidecar-without-markdown`, `R22.3-unresolved-target` and `R22.6-carried-stale`, so a later packet's report-only rules do not break the pin. Since MIK-R27 the fixture tree's only violation is the one report-only `R27.4-legacy-unassessed` count (`LEGACY_COUNT`: its Doc14 family is an export), and the four report-only pins in the rule 3 and rule 6 cases, plus the standalone conversion's, each gain `LEGACY_COUNT` and stay exact.
- **Rule 1:** a bad field, a non-canonical file (naming the formatter), a file outside the layout, and a misplaced sidecar.
- **Rule 2:** the filename prefix, duplicate IDs after a merge (`merge conflict:` naming both files), the packet's conforming parallel-mint example, and duplicate entry IDs across sidecars.
- **Rule 3:** the packet's non-conforming hand-added `[4]`, an unused reference, Markdown without a sidecar, a file sidecar without Markdown (reported; holds no references), record links, a retired record, an unresolved target (reported), a disallowed relation by field, and a dot-named card with its sidecar.
- **Rules 4 and 5:** an invariant that lists its realizations; a missing family member.
- **Rule 6:** an added anchor at a missing path, a carried anchor at a deleted path (reported stale; with an empty code tree the family's carried routes are reported too, as `R04.1-carried-route-absent`), the packet's boundary merge example, re-anchored and moved entries, locator and content rules, and an unconverted base with the standalone conversion.
- **Rule 7:** a closed history file is frozen (edited, deleted, closed in one merge parent); an open one may change; history is shape-only (the packet's rename boundary example).
- **The retired subject kept in the tree (MIK-R09, L09 review R2-1, ruling 2026-09-30T17:59:48).** The three rule-7 cases use a history file whose subject `INV-RET1R3` stands for "a subject that has since been retired". Since L09, MIK-R09's `R09-history-rows` rule checks every history file's subjects at every route (`unknown_subjects`), so a subject absent from the tree would now refuse. MIK-R22 rule 3 says records are never deleted (retiring sets `status: retired` and keeps the file), so the fixtures now model it faithfully: `RETIRED` adds `INV-RET1R3` with `status: retired` (and an unchecked admission) to each tree, including the left merge parent. The assertions are unchanged, and the packet's boundary example (a renamed `before` path in a closed file) still passes.
- **Rules 8 and 9:** applicability by the marker; a later packet's rule runs everywhere and a report-only rule never refuses.
- **Markers:** the grammar table and the invalid-number message.
- **MIK-R27, the admission rule** (leaf 260928-MIK-L27), with helpers that change one record's admission, drop the proof sidecar's `proves`, leave `INV-7K3F9Q`'s realizations in `integrate.py` only, or add an exported invariant (`_with_export`: its ID is `derived_record_id("invariant", EXPORTED_LEGACY_ID)`, or a forged ID when `identifier` is given):
  - the packet's admitted example passes as a new record;
  - **reference-only justifications are refused**, naming the record, `admission.justification` and the criterion: 20 refused forms (the packet's "introduced by L43", bare IDs, D-IDs and hashes by ruling 22:11:24 Q2, and the provenance phrasings of ruling 23:04:57 F1 such as "Per ruling D14", "Added in commit a4eba7b7", "L43/L44", "Implements R27.2", "ICR L45", "Added on 2026-09-28 in L43"), and 9 admitted ones, including real prose with reference-shaped words ("Deadbeef cafe faced a decade", "Uses D3 to render the chart", "L1 cache and L2 cache"); a new family and a new decision are refused the same way;
  - no criterion is refused by the shape rule `R22.1-shape` (field `admission…criteria`), and `legacy-unassessed` on a new record by `R27.2-new-record`;
  - an unsupported `guarded_by_test` (no proof) and an unsupported `spans_locations` (one file, named) are refused on a new record;
  - **an existing record whose test was deleted is only reported** (the packet's Expected Evidence), with "reported, not refused";
  - exported, retired and merge-parent records are never refused;
  - **a forged legacy ID does not make a record exported** (ruling 23:04:57 F2): the genuine export is only reported, and the same record under `INV-F0RG3D` is refused as new, for the claim and for `legacy-unassessed`;
  - the legacy count names live records by kind and drops assessed and retired (demoted) ones;
  - the three rules are registered, `R27.2-new-record` refusing and the other two report-only, none writer-reported.

### Conventions

- The rule-9 test registers two test rules and removes them from `registry._REGISTRY` in a `finally` block.

### Invariants And Boundaries

- Every packet example (conforming, non-conforming and boundary) is covered at this level.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

Representative cases; the full list is in the module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture tree passes with only the legacy count, and MIK-R22's report-only set is pinned. | `test_converted_fixture_tree_passes_every_rule` | mcp/tests/test_knowledge_validator.py:94-109 |
| Merge duplicates are conflicts naming both files; parallel mints merge cleanly. | `test_duplicate_ids_after_a_merge_are_a_conflict_naming_both_files`; `test_parallel_leaves_minting_different_ids_merge_cleanly` | mcp/tests/test_knowledge_validator.py:160-173; mcp/tests/test_knowledge_validator.py:176-183 |
| The hand-added marker is refused. | `test_a_hand_added_marker_without_a_reference_is_refused` | mcp/tests/test_knowledge_validator.py:203-211 |
| A dot-named card and its sidecar are validated. | `test_a_dot_named_card_and_its_sidecar_are_validated` | mcp/tests/test_knowledge_validator.py:303-323 |
| The boundary merge: three rows, passes, three stale reports. | `test_merge_where_one_parent_deleted_a_file_the_other_parents_card_cites` | mcp/tests/test_knowledge_validator.py:380-396 |
| The retired record the history fixtures keep in every tree (records are never deleted, MIK-R22 rule 3; L09 R2-1). | `RETIRED` | mcp/tests/test_knowledge_validator.py:450-454 |
| A closed history file is frozen. | `test_a_closed_history_file_is_frozen` | mcp/tests/test_knowledge_validator.py:479-494 |
| MIK-R27: reference-only justifications are refused, real prose is admitted. | `test_a_new_record_whose_justification_is_only_a_reference_is_refused` | mcp/tests/test_knowledge_validator.py:667-728 |
| MIK-R27: an existing record whose test was deleted is only reported. | `test_an_existing_record_whose_test_was_deleted_is_only_reported` | mcp/tests/test_knowledge_validator.py:764-773 |
| MIK-R27: exported, retired and merge-parent records are never refused. | `test_exported_retired_and_merged_records_are_never_refused` | mcp/tests/test_knowledge_validator.py:776-795 |
| MIK-R27: a forged legacy ID does not make a record exported. | `test_a_forged_legacy_id_does_not_make_a_record_exported` | mcp/tests/test_knowledge_validator.py:798-813 |
| MIK-R27: the legacy count and the rules' registration flags. | `test_legacy_records_are_counted_until_assessed_or_demoted`; `test_the_rules_are_registered_refusing_new_and_reporting_the_rest` | mcp/tests/test_knowledge_validator.py:816-832; mcp/tests/test_knowledge_validator.py:835-845 |
| A later rule runs everywhere; report-only never refuses. | `test_a_later_packets_rule_runs_everywhere_and_report_only_never_refuses` | mcp/tests/test_knowledge_validator.py:546-563 |

## Cross-Repo References

No meaningful cross-repo references found: the cases run over in-memory trees.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **body updated for MIK-R09 (a fixture change).** A Logic bullet records the `RETIRED` fixture: the rule-7 history cases now keep `INV-RET1R3` in the tree as a retired record, because MIK-R09's history-row rule checks every file's subjects at every route (review R2-1, ruling 17:59:48) and MIK-R22 rule 3 keeps retired records; assertions unchanged. One row added; the rule-7 rows below it were re-pointed or normalised by the installed fixer (its bullet is kept, since no claim was reworded) or by the exact base-to-staged line shift.
- 2026-09-30T18:03:19+00:00: Generated citation repair: `test_an_existing_record_whose_test_was_deleted_is_only_reported` repointed to mcp/tests/test_knowledge_validator.py:764-773. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T00:17:15+02:00 — 260928-MIK-L27 curator (uncommitted change set on `ar/260928-mik-l27`, code base `46ca74302e76cf40fb6370ea9ece16d8fa719f00` plus the staged delta): **body update — the MIK-R27 section (9 cases, 46 collected) and `LEGACY_COUNT` in L22's pins.** Purpose, the Baseline bullet and a new MIK-R27 bullet state it, with rulings Q2, F1 and F2; the baseline row reworded; five rows added; the other rows re-pointed by the exact line shifts. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — two minimal MIK-R04 edits to L22's tests.** The report-only pin is filtered to rules owned by MIK-R22, and the carried-stale case with an empty code tree also expects `R04.1-carried-route-absent`; the Baseline and Rule 6 bullets and the baseline row say so. The other rows were re-pointed by the exact line shift, their claims unchanged. No verification stamp was advanced.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
