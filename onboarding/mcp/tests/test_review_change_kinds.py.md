# mcp/tests/test_review_change_kinds.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

**MIK-R33's primary falsifier on the server: the change-kind facts over a store-authored four-tree comparison.** The
fixture (`build_world`) is a live leaf over a code repository and a converted memory repository, each with a committed
base and the leaf's candidate, resolved and composed exactly as the reviewer does, with one member authored per badge
kind and the review rounds' extra cases. It is the world the dashboard's `triage.*` bodies are captured from
(`triage.capture-provenance.json`).

`test_review_change_kinds.py` proves the MIK-R33 change-kind facts over a live leaf on four real Git trees, one member per badge kind. In W03 it also proves the outline: index-only reads, catalogue preservation, authored membership order, summary cuts, and the unknown/unavailable states. Four further test declarations cover leaf-wide code facts, unavailable code facts, public-gate worklist states and answering witnesses, and held-input validation (six parameterized variants).
## Code Commentary

### Logic

- **The world.** `INV-AAAAAA` (revision 1→2, its realization met by a hunk: `intent` `+impl` `+unknown`), `INV-BBBBBB` (a hunk:
  `implementation`), `INV-CCCCCC` (re-anchored in an unchanged file: `implementation`, definition 7), `INV-DDDDDD` (a
  proof of a changed test: `implementation` `+test` `+unknown`), `INV-EEEEEE` (`unchanged`), `INV-FFFFFF` (shared: `unchanged` in
  `FAM-F00001`, joins `FAM-F00002`: `membership`), `INV-GGGGGG` (recorded at a blob neither side holds: `unknown`),
  `INV-KKKKKK` (carried mechanically: `unchanged`), `INV-HHHHHH` (added, joins `FAM-F00001`: `intent` `+membership`),
  `INV-PPPPPP` (same revision, applicability reworded: `intent` `text_differs`), and `FAM-F00003`'s `INV-MMMMMM` (a
  `file` entry covering the rewritten `pkg/data.bin`), `INV-NNNNNN` (a `line_range` entry there: `unknown`),
  `INV-SSSSSS` (a stale-at-base realization repaired: "re-anchored (stale at base)"), `INV-XXXXXX` (linked plus a
  stale entry in the changed test: `implementation` `+unknown`) and `INV-RRRRRR` (retired at the same revision:
  `intent`). `FAM-F00002`'s guarantee changes; `FAM-F00003`'s revision is bumped for a reorder with the same guarantee.
- **The 12 cases:** every occurrence's kind; the shared member; a partial page describing only its returned members;
  an unreadable sidecar; an unreadable family record (guarantee and membership unknown, the membership reason apart
  from the change-kind reasons); unreadable trees; a changed non-text file; the moved entry, retired record and
  unresolved range in one family; an unread sidecar of a changed file beside an established fact (review R2-1 N5); the
  total unknown only for the family's own records; the facts derived and describing exactly the returned members (both
  validators refused); a dataset review carrying no facts.
- **Review R2-1's N6 (ruling 2026-09-30T18:57:45):** a fixture where rule 6b's conditional `unknown` alone decides the
  primary is not reachable under F1 and F4 (a non-file entry on a changed binary either keeps its anchor, leaving a
  side's range unresolved, or changes it, which is a re-anchor), so the FAM-F00003 case pins it through its own reason
  ("pkg/data.bin changed as a non-text file … RLZ-N00001 is not a file entry") beside the after side's
  unresolved-range reason; mutation N6 is caught.
- Registered in the `unit-regression` lane (`test-evidence-lanes.toml`).

### Conventions

Module-level fixture builders (`_invariant`, `_family`, `_entry`, `_sidecar`, `_memory_base`, `_memory_candidate`,
`build_world`), a `world` fixture over `tmp_path`, and small helpers that read the composed context (`_context`,
`_entry_of`, `_by_invariant`, `_kinds`). The autouse `_no_bound_services` fixture keeps the composition off live
services.

### Invariants And Boundaries

The world is SYNTHETIC store-authored knowledge over real Git trees, not project knowledge. It proves the three
candidate invariants recorded on `application/review_change_kinds.py.md`; the worker's mutation sets (46 of 46 at the
R1 fix round, 4 of 4 at R2, 9 of 9 at the merge round) were run against these cases and the dashboard suites.

### Todos

No additional work is asserted by this card.

`test_the_outline_reads_only_indexes_and_preserves_catalogue_fields` rewrites family membership (a leave-and-join) and an invariant statement, then replaces TreeLane.classify, CodeTrees._blob, KnowledgeIndex.family/invariant and knowledge_review.compose_review with refusing callbacks: the catalogue entries must equal the subject catalogue's, the dump without `outline` must keep its exact fields, and the outline must show added/removed/changed/unchanged with candidate-first member order, `joined`/`left` membership, word-cut summaries and `text_uuid` selector ids — including that a code-changed but meaning-unchanged invariant reads `unchanged`. `test_the_outline_states_unknown_records_and_unavailable_membership_or_indexes` covers corrupt invariant/family records (`unknown` / `unavailable` naming unparseable files), the dataset case (`trees=None`, no converted memory) and a missing index database. The corrupt-family outline detail names `cannot read FAM-F00001`. The leaf-wide agreement case compares the final classified result after its size loop with walked-family implementation, proof and unresolved-range facts; its body does not guard against roster reads. Unreadable code facts are `unavailable` with a detail and no invariant facts. Worklist states equal the public gate result, and a deferred history row supplies the answering witness. Matching readable held inputs agree with ordinary evaluation; mismatched memory, code tree or code root, one-sided held inputs and a failed held code read each yield `undecided` with a reason.
## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References


### Cross-Repo References

No cross-repo boundary is crossed by this file.

- The fixture's members, one per badge kind, and the three families.  Anchor: "one member per badge kind"; "its members are reordered" [1]
- The world: a live leaf over four Git trees. [2]
- Every occurrence's kind from the recorded comparison, and the shared member. [3]
- Returned members only, and the failure states that are unknown, never unchanged. [4]
- Definition 8, the moved entry, the unresolved range and the unread sidecar beside an established fact. [5]
- The total, the derived facts and the dataset review. [6]


> Retained earlier citation wording: - Its lane row.  Anchor: "mcp/tests/test_review_change_kinds.py" [7]


- The outline reads indexes only and keeps catalogue bytes [8]

- Families, membership and summaries match the detail's facts  Anchor: `outline` [9]

- Corrupt invariant records produce unknown outline facts; a corrupt family names cannot read FAM-F00001; dataset and missing-index cases are unavailable. [10]
- The final classified leaf facts agree with walked-family implementation, proof and unresolved-range facts. Unreadable code facts are unavailable rather than an empty successful result. [11]
- Worklist states match public gate verdicts and name the answering history row. Six held-input variants fail closed with reasons; matching readable held inputs match ordinary evaluation. [12]

## Catalogue comparison field

The index-only outline case now includes `comparison` in the exact serialized field sequence checked after excluding `outline`. The forbidden source, roster and per-subject readers remain in place, and catalogue equality, totals, authored membership order and meaning-only facts remain asserted. This extra field-name assertion does not independently validate a numbered comparison's resolved value.

- The index-only outline preserves exact catalogue fields including comparison. [13]

- Its lane row.  Anchor: "mcp/tests/test_review_change_kinds.py" [7]
