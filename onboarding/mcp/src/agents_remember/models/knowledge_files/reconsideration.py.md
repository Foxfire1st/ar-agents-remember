# mcp/src/agents_remember/models/knowledge_files/reconsideration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/reconsideration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:05:38+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R14@v2` of task
`260928_maintained-invariant-knowledge` and its leaf document `14_reconsideration-surfacing.json` (rulings
2026-09-30T04:37:56 to 11:53:13); they live outside the code and memory repositories, so they are named here and
not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: the subject, the triggers, the rows and the one satisfying rule. | "Reconsideration candidates (MIK-R14@v2)" | mcp/src/agents_remember/models/knowledge_files/reconsideration.py:1-24 |
| The kind and the two row dispositions. | `RECONSIDERATION_ITEM_KIND`; `RECONSIDER_DISPOSITIONS` | mcp/src/agents_remember/models/knowledge_files/reconsideration.py:47-50 |
| The history-row dispositions that count as a change of the row's subject. | `TRIGGERING_DISPOSITIONS` | mcp/src/agents_remember/models/knowledge_files/reconsideration.py:53-53 |
| The five triggers, and the three a `still_rejected` answer refreshes. | `TRIGGERS`; `REFRESHED_TRIGGERS` | mcp/src/agents_remember/models/knowledge_files/reconsideration.py:55-62 |
| The subject pattern over the shared decision ID pattern. | `RECONSIDER_SUBJECT_PATTERN` | mcp/src/agents_remember/models/knowledge_files/reconsideration.py:64-67 |
| The subject spelled and parsed. | `reconsider_subject`; `parse_reconsider_subject` | mcp/src/agents_remember/models/knowledge_files/reconsideration.py:70-73; mcp/src/agents_remember/models/knowledge_files/reconsideration.py:76-80 |
| One question per subject and leaf. | `question_key` | mcp/src/agents_remember/models/knowledge_files/reconsideration.py:83-90 |
| The one spelling of a link target, compared before a refresh (N1). | `link_target_key` | mcp/src/agents_remember/models/knowledge_files/reconsideration.py:93-109 |
| The satisfying rule over a stored item, for the gate. | `reconsideration_item_open` | mcp/src/agents_remember/models/knowledge_files/reconsideration.py:112-121 |
| The row kind, the subject parser and the item kind are registered with MIK-R14 as owner. | `test_the_row_kind_and_the_item_kind_are_registered` | mcp/tests/test_reconsideration_surfacing.py:604-611 |
| The stored predicate agrees with `satisfiedBy` on the answered item. | `test_still_rejected_answers_the_candidate_and_the_stored_predicate_agrees` | mcp/tests/test_reconsideration_surfacing.py:417-443 |

## Cross-Repo References

No meaningful cross-repo references found: the module defines names only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:05:38+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): created this card for the new file MIK-R14 adds, recording rulings 04:37:56 (Q7 question key), 05:31:11 (F3 `anchor_stale`, F1 `REFRESHED_TRIGGERS`) and 06:17:11 (N1 `link_target_key`). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
