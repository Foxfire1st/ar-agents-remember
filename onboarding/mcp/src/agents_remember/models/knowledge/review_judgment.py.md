# mcp/src/agents_remember/models/knowledge/review_judgment.py

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Defines pane 3’s history judgments and proof-entry observations for the selected tree-review record, replacing—not renaming—the old evidence/assessment pane.

## Code Commentary

`ReviewJudgmentRow` retains attempt, row/subject identity, disposition, optional effect/revision, reason, typed `because`, covered-entry or examined-member counts, history path and closed flag. `ReviewJudgmentProof` retains the proof entry’s ID, invariant, path, optional symbol, authored facet, and `current`/`stale`/`unverifiable` state with detail. A proof state is measured at the after code tree, not an execution result.

`ReviewJudgmentPane` distinguishes `rows`, `none`, and `unavailable`; its validator requires rows exactly in the `rows` state. `proofs` is independent and may remain present when history is none or unavailable. The producer selects every owner-history row for the subject or `membership:<subject>`, sorts by attempt then row ID, and does not restrict this pane to meaning-changing rows. Family proofs come from after-tree membership, not an invented union of all historical family members.

## Invariants And Boundaries

No source-file change, historical assessment or passing test is converted into a new authored judgment. The schema’s fields do not establish visible disclosure policy or text; those require renderer evidence. This read-only pane supplies neither publication nor acceptance authority.

## Evidence

- History rows retain their authored fields, counts, file path and closed flag. [1]
- Proof entries carry after-code currentness, not run outcomes. [2]
- Rows are present exactly in rows state; proof entries are a separate collection. [3]
- Owner-history filtering includes membership subjects and sorts by attempt and row ID. [4]
- Proofs are observed at the after code tree; family scope is the after-index membership. [5]
