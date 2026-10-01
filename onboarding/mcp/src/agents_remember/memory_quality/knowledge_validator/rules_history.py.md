# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_history.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R09's rule on history rows, in the validator's one registry (MIK-R22 rule 9; carried from the L12 review,
decision 2026-09-29T06:39:28).** The writer (MIK-R12) checks every row of the owner's history file it writes against
the tree it produces, but a row edited by hand, or left behind by a direct sidecar edit, is never seen by the writer.
The same two MIK-R07 writer-support checks therefore also run as validator rules, and so at every commit route: every
row's subject names a record of the candidate (`unknown_subjects`), and every covered entry's `after` anchor equals
that entry's anchor in the candidate (`reanchor_mismatches` over `sidecar_entry_anchors`, MIK-R07 rule 4).
`validator.py` imports the module, which registers `R09-history-rows` (refusing, `writer_reports`) and
`R09-history-rows-merged` (report-only).

## Code Commentary

### Logic

- **Which files (review R1 F1, ruling 16:07:55; review R2-1, ruling 17:59:48):**
  - `unknown_subjects` runs over **every** history file, open or closed, at every route. A retired record still
    resolves (MIK-R22 rule 3: records are never deleted), so no legitimate row names an unknown subject, and a closed
    file committed outside the AR routes cannot carry a ghost subject past a master or checkpoint landing.
  - `checked_history_files(context)` picks the files the re-anchor check reads: every **open** file; and, when
    `context.leaf_publication` is set (closeout, direct landing, a leaf's recorded landing), every file closed in K_C
    but **not closed in any comparison base**. The leaf's own file stays editable until its closeout commit writes
    `closed: true` (MIK-R07 rule 7), so a flag set earlier, by hand or left by a refused attempt, is never a waiver.
  - A file closed in a base is frozen (MIK-R22 rule 7 keeps it byte-identical) and historical: its rows describe the
    tree it closed on, and it is not re-anchor-checked again (a later leaf may re-anchor an entry an earlier row
    covered). This scoping to leaf-publication routes is the architect's F1 ruling.
- **Rows the merge moved (the sync part of ruling 16:07:55).** `_mismatches` yields `(path, row, mismatched entries,
  moved)` for every disagreeing invariant row. With more than one base (a merge), `_BaseRows.agreed` asks each parent,
  lazily, whether it holds the **identical row** at the same path and whether that row agreed with **that parent's**
  entries; if some parent does, the mismatch was caused by the merge (`moved`).
  - `check_history_rows` refuses an unknown subject and an unmoved mismatch ("covered entries … no longer carry its
    'after' anchor … name the row again through the writer").
  - `check_merged_history_rows` reports a moved one ("the merge moved covered entries …; the leaf's next gate checks
    the row against its new base"), and does not refuse the sync. At the leaf's next gate there is one base, so the
    strict rule applies and the curator re-records the row (MIK-R09 Failure and Recovery: after a sync, stale items
    reopen).
- The revision and examined-member bindings are currentness, not validity: a row whose invariant changed revision
  afterwards reopens its item at the gate and is not invalid here.

### Conventions

- `writer_reports=True`: inside the writer these rules only report, because the writer refuses its own owner's rows
  through its whole-file check and a leaf may repair another file before closeout; every commit route refuses.
- `HISTORY_ROWS_RULE` cites "MIK-R09 (carried from MIK-R12)"; `HISTORY_ROWS_MERGED_RULE` "MIK-R09 (sync)".

### Invariants And Boundaries

- **A history file closed in K_B is frozen; at leaf-publication routes every other history file's rows must agree
  with their entries, whatever the file's own closed flag says.** Candidate invariant (not ingested). Realized by
  `checked_history_files` with `ValidationContext.leaf_publication`, set at every leaf route; proved by
  `test_a_hand_closed_leaf_file_is_refused_at_closeout_validation_and_record_landing`,
  `test_a_sibling_s_file_closed_in_the_base_is_not_re_anchor_checked_at_a_leaf_route` (N01),
  `test_the_closeout_s_exact_tree_re_anchor_checks_the_file_it_has_just_closed` (N08) and the direct-landing twin (N09),
  and the renamed `test_the_gate_runs_the_validator_and_its_history_row_rule`.
- **Every subject a history row names resolves in the tree, at every route.** Candidate invariant (not ingested).
  Realized by the first loop of `check_history_rows`; proved by
  `test_a_hand_committed_closed_history_file_with_a_ghost_subject_is_refused_at_master_landing` (the reviewer's R2
  probe, N21). The L22 validator fixtures now keep the retired record `INV-RET1R3` in the tree (`status: retired`),
  per MIK-R22 rule 3, so their assertions are unchanged.
- **A sync merge refuses a row only when the leaf's own side had it wrong.** Proved by
  `test_a_sync_merge_refuses_a_history_row_only_when_the_leaf_s_own_side_had_it_wrong` in
  `test_knowledge_validator_routes.py` ("consistent" syncs; "already wrong" is refused by `R09-history-rows`).
- Note (review R3): the validator itself has no deletion-against-base rule; "records are never deleted" is held by
  the tools, and this rule now enforces it for every record a history row names.

### Todos

- **Accepted note (R2-4):** record landing falls back to the landed commit's parents as bases when
  `memory_base_commit` is empty, which could reach the merge exemption at a leaf route; leaf contracts always carry
  `memory_base_commit`, so it is practically unreachable.
- The byte-for-byte check of a new history file against its leaf's recorded closeout commit was offered by review R2
  and not required (ruling 17:59:48).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R09@v2`, `MIK-R07@v2`, `MIK-R22@v1` and
`09_mandatory-invariant-closeout-gate.json`, outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: the two checks, which files, rows the merge moved. [1]
- The files the re-anchor check reads. [2]
- A merge parent's rows, read only when a row disagrees. [3]
- Every disagreeing row, and whether the merge moved it. [4]
- The refusing check over every file's subjects and the unmoved mismatches. [5]
- The report-only check of rows the merge moved. [6]
- The two rules registered on import. [7]
- The context flag a leaf publication sets. [8]
- A ghost subject in a closed file is refused at master landing. [9]
- The sync merge cases. [10]

### Cross-Repo References

No meaningful cross-repo references found: the rule reads the validation context's trees only.

No cross-repo boundary is crossed by this file.
