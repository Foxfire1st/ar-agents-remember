# mcp/src/agents_remember/models/knowledge_files/reconsideration.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The one spelling of MIK-R14's reconsideration subject, its triggers, its row dispositions and the rule that
answers an item.** The worklist registrant (`application/knowledge_worklist/reconsideration.py`), the history-row
model (`history.ReconsiderationRow`), the writer (`application/knowledge_writer/reconsideration.py`) and the
closeout gate (MIK-R09, L09) all import from here, so an item's subject, the subject of the row that answers it,
the target spelling the writer compares, and the open/satisfied predicate cannot drift apart. The module is pure:
it reads no tree, no Git and no task document.

## Code Commentary

### Logic

- **Kind and dispositions (rule 4).** `RECONSIDERATION_ITEM_KIND` is `reconsideration_candidate`;
  `RECONSIDER_DISPOSITIONS` is `still_rejected` and `raise`, and nothing else.
- **Triggers (rule 1).** `TRIGGERS` names the five: `record_file`, `history_row`, `anchor`, `anchor_stale` and
  `requirement_version`. `anchor_stale` is the review R1 F3 addition (ruling 2026-09-30T05:31:11): a link anchor
  classified `stale_at_base` fires instead of going silent. `TRIGGERING_DISPOSITIONS` lists the history-row
  dispositions that count as a change of the row's subject: `changed`, `moved`, `deleted`, `rerouted`, `retired`.
  `REFRESHED_TRIGGERS` (`anchor`, `anchor_stale`, `requirement_version`) are the triggers a `still_rejected` answer
  refreshes the link for (rulings Q2/Q3, F1, F3); a `record_file` or `history_row` link is never rewritten.
- **Subject (rule 3).** `RECONSIDER_SUBJECT_PATTERN` is `reconsider:<DEC-ID>#<alternative index>`, the decision ID
  taken from the shared `id_pattern` and the index with no leading zero; `reconsider_subject` spells it (the same
  spelling as `decisions.ReconsiderLink.subject`) and `parse_reconsider_subject` reads it back, or `None`.
- **Question key.** `question_key(subject, leaf)` is the prefix `[<subject> raised by <leaf>]` that identifies a
  `raise` row's question in the leaf's `openQuestions`: one question per subject and leaf, so a rerun of the same
  `raise` finds it and appends nothing (ruling Q7).
- **Target key (review R2 N1).** `link_target_key(target)` is the one spelling of a `reconsider_on` target: a
  record ID or `route:` string is itself; an anchor is `<path>@<blob>#<content>`; a requirement is
  `<repository>/<task path>#<id>@<version>`. The worklist fills `facts.changed[].target` with it, and the writer
  compares a K_C link with the fired target through it before any refresh, so a link re-authored after the worklist
  fired is never refreshed onto the wrong target.
- **The predicate (rule 5).** `reconsideration_item_open(item, rows_by_subject)` is open unless the leaf has a row
  with the item's subject. The row kind admits only `still_rejected` and `raise`, so any such row satisfies it.

### Conventions

- `rows_by_subject` maps each history-row subject of the leaf to its row ID: the same shape MIK-R30's and
  MIK-R10's predicates take, for L09's gate.
- No prose is evaluated anywhere: `reconsider_when` is only copied into facts and the question (packet
  Exclusions).

### Invariants And Boundaries

- **The worklist's `satisfiedBy` and the gate's predicate agree by construction.** Realized by the registrant
  calling `reconsideration_item_open` to fill `satisfiedBy`; proved by
  `test_still_rejected_answers_the_candidate_and_the_stored_predicate_agrees` and on every real candidate of the
  worker's and reviewers' runs ("agrees with satisfiedBy: True").
- **A decision target never triggers (one hop).** No trigger here names a decision; the registrant skips a
  `DEC-` target (rule 3).
- **Unconverted memory reads are unchanged.** Nothing reads this module on an unconverted leaf, which gets no
  worklist and no knowledge write.

### Todos

- **L09:** the gate applies `reconsideration_item_open(item, rows_by_subject)`; an unanswered candidate blocks
  closeout (D29).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R14@v2` of task
`260928_maintained-invariant-knowledge` and its leaf document `14_reconsideration-surfacing.json` (rulings
2026-09-30T04:37:56 to 11:53:13); they live outside the code and memory repositories, so they are named here and
not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: the subject, the triggers, the rows and the one satisfying rule. [1]
- The kind and the two row dispositions. [2]
- The history-row dispositions that count as a change of the row's subject. [3]
- The five triggers, and the three a `still_rejected` answer refreshes. [4]
- The subject pattern over the shared decision ID pattern. [5]
- The subject spelled and parsed. [6]
- One question per subject and leaf. [7]
- The one spelling of a link target, compared before a refresh (N1). [8]
- The satisfying rule over a stored item, for the gate. [9]
- The row kind, the subject parser and the item kind are registered with MIK-R14 as owner. [10]
- The stored predicate agrees with `satisfiedBy` on the answered item. [11]

### Cross-Repo References

No meaningful cross-repo references found: the module defines names only.

No cross-repo boundary is crossed by this file.
