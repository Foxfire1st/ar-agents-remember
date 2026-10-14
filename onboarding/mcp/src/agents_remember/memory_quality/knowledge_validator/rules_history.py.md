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
`R09-history-rows-merged` (`merge_reports`, not plain report-only).

## Code Commentary

### Logic

- **Which files (review R1 F1, ruling 16:07:55; review R2-1, ruling 17:59:48):**
  - `unknown_subjects` runs over **every** history file, open or closed, at every route. Invariant,
    family and decision/facet `RecordRow` subjects resolve to their candidate record; `MembershipRow`
    resolves the invariant after `membership:`. Other row kinds answer worklist items rather than
    records and are not checked here. A retired record still resolves (MIK-R22 rule 3: records are
    never deleted), so a closed file committed outside AR routes cannot carry a ghost subject past
    master or checkpoint landing. This subject check does not judge revision currentness.
  - `checked_history_files(context)` picks the files the re-anchor check reads: every **open** file; and, when
    `context.leaf_publication` is set (closeout, direct landing, a leaf's recorded landing), every file closed in K_C
    but **not closed in any comparison base or frozen commit** (`context.closed_before`). The leaf's own file stays editable until its closeout commit writes
    `closed: true` (MIK-R07 rule 7), so a flag set earlier, by hand or left by a refused attempt, is never a waiver.
  - A file closed in a base is frozen (MIK-R22 rule 7 keeps it byte-identical) and historical: its rows describe the
    tree it closed on, and it is not re-anchor-checked again (a later leaf may re-anchor an entry an earlier row
    covered). This scoping to leaf-publication routes is the architect's F1 ruling.
- **Rows the merge moved (the sync part of ruling 16:07:55).** `_mismatches` yields `(path, row, mismatched entries,
  moved)` for every disagreeing invariant row. With more than one base (a merge), `_BaseRows.agreed` asks each parent,
  lazily, whether it holds the **identical row** at the same path and whether that row agreed with **that parent's**
  entries; if some parent does, the mismatch was caused by the merge (`moved`).
  - `check_history_rows` refuses unknown subjects and every disagreeing row at a leaf publication, including a mismatch a merge moved. At a merge that is not a leaf publication, an unmoved mismatch still refuses.
  - `check_merged_history_rows` yields moved mismatches only for non-publication merges. Its `merge_reports` registration gives bounded reporting at the sync merge, not permanent immunity. The finding names the deferral reason (the merge cannot judge against its new base) and says the next publication/landing refuses if the row still disagrees. The leaf-publication check still refuses every mismatch, including moved ones.
- The revision and examined-member bindings are currentness, not validity: a row whose invariant changed revision
  afterwards reopens its item at the gate and is not invalid here.
- **A leaf's attempt files are one history (L37, decision record DEC-0AEQ28; INV-MS9BMJ).**
  - A file closed in the commit the candidate sits on (`context.frozen`) is frozen and historical like one closed
    in a base: an earlier, recorded closeout of the same leaf closed it, and the leaf's later rows are in its next
    attempt file.
  - `_governing_attempts` maps each `(owner, subject)` to the attempt of the owner's latest row about it.
    `_mismatches` skips a row that a later attempt of the same owner answers again, whether or not its file is
    frozen. The later row is checked.
- **A change the leaf made stays visible (L37, INV-XN0FG8).** At a commit that publishes a leaf,
  `_unlanded_judgments` lists the invariant and family rows of every history file that no comparison base holds
  closed, each owner's attempts in order. `_hidden_changes` yields a latest row that is neither `changed` nor a
  retiring row (`keeps_change_visible`) when an earlier row about the same subject is a `changed` row.
  `check_history_rows` refuses it under `R09-history-rows`; the message names the row it replaces, with its
  revision and effect for an invariant, and says to name that changed row again through the writer. The rule
  needs no converted base, so it also runs at a leaf's recorded landing. Two limits: a change that has landed on
  the parent line is no longer covered, and a master's landing is not judged by it.

### Conventions

- `R09-history-rows` carries `writer_reports=True`: the writer reports its validator findings while
  independently refusing its own owner's rows through the whole-file check, so another file can be
  repaired before closeout. `R09-history-rows-merged` instead carries `merge_reports=True`; the
  non-publication sync exemption is bounded and leaf publication never inherits it.
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
- Record deletion is independently refused by `rules_admission.check_record_kept` (`R27.4-record-kept`) for every ID a comparison base holds; retirement changes status and retains the file. Subject resolution here is not a substitute for that comparison.

### Todos

- The former missing-memory-base fallback and leaf merged-row exemption are superseded. Recorded leaf landing requires the named memory base and rejudges the exact pair; every master landing authenticates newly closed history against its owner publication. Those are current route obligations, not accepted limits.

## Judging Only Published Rows (MIK-R48)

`check_family_judgments` iterates the shared `checked_history_files` population,
so both history rules agree on what the route publishes: open files are always
judged; at a leaf publication a file not closed in a base is judged whatever its
flag says; closed files are never judged at master or checkpoint landing or in a
validation without a base. Rows unchanged at the same path in a base or frozen
file are exempt inside a judged file.

- Only route-published new or edited rows are judged. [18]

## Evidence



### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R09@v2`, `MIK-R07@v2`, `MIK-R22@v1` and
`09_mandatory-invariant-closeout-gate.json`, outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References


- The module docstring: the two checks, which files, frozen attempts, the governing changed row, rows the merge moved. [1]


- The files the re-anchor check reads. [2]

- A merge parent's rows, read only when a row disagrees. [3]

- Every disagreeing row that no later attempt of its owner answers again, and whether the merge moved it. [4]

- The refusing check rejects all mismatches at a leaf publication and only unmoved mismatches at a non-publication merge. [5]




- The context flag a leaf publication sets. [8]
- A ghost subject in a closed file is refused at master landing. [9]
- The sync merge cases. [10]

- A file closed in a base or in a frozen commit is left out of the re-anchor check. [11]
- Each owner's latest attempt about a subject. [12]
- A row that a later attempt answers again is not re-anchor-checked. [13]
- A later row of another disposition that would replace the leaf's changed row. [14]
- The refusal names the changed row it replaces. [15]


- Changed row remains governing in every attempt. [16]




- Parent-line change may be answered by any later row. [17]



### Cross-Repo References

No meaningful cross-repo references found: the rule reads the validation context's trees only.

No cross-repo boundary is crossed by this file.

- Leaf publication refuses all merged-row mismatches; the `merge_reports` finding defers only at a non-publication sync merge and names the next refusing publication/landing. [19]
- Moved-row findings are bounded `merge_reports` at non-publication sync merges; their messages explain deferral and the next refusing publication/landing. [6]
- The history-row registrations: `R09-history-rows` uses `writer_reports`, while `R09-history-rows-merged` uses `merge_reports`, not plain report-only. [7]
- Current source delta inspected statically: Extend subject resolution and bounded merge reporting; keep R52 leaf refusal, frozen-attempt scope, independent retention and gate-owned currentness. [20]
