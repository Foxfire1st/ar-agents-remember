# mcp/tests/test_knowledge_validator.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

Representative cases; the full list is in the module.

- The fixture tree passes with only the legacy count, and MIK-R22's report-only set is pinned. [1]
- Merge duplicates are conflicts naming both files; parallel mints merge cleanly. [2]
- The hand-added marker is refused. [3]
- A dot-named card and its sidecar are validated. [4]
- The boundary merge: three rows, passes, three stale reports. [5]
- The retired record the history fixtures keep in every tree (records are never deleted, MIK-R22 rule 3; L09 R2-1). [6]
- A closed history file is frozen. [7]
- MIK-R27: reference-only justifications are refused, real prose is admitted. [8]
- MIK-R27: an existing record whose test was deleted is only reported. [9]
- MIK-R27: exported, retired and merge-parent records are never refused. [10]
- MIK-R27: a forged legacy ID does not make a record exported. [11]
- MIK-R27: the legacy count and the rules' registration flags. [12]
- A later rule runs everywhere; report-only never refuses. [13]

### Cross-Repo References

No meaningful cross-repo references found: the cases run over in-memory trees.

No cross-repo boundary is crossed by this file.
