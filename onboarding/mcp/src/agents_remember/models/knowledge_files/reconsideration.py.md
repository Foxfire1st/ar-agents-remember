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
- **Triggers (rule 1).** `TRIGGERS` includes `record_file`, `history_row`, `anchor`, `anchor_stale`, `requirement_version`, `route_absent` and `refresh_not_current`. `anchor_stale` is the review R1 F3 addition (ruling 2026-09-30T05:31:11): a link anchor
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
- **The predicate.** `reconsideration_item_open(item, rows_by_subject, superseded=frozenset())` first closes a parsed decision in the supplied superseded set; otherwise a `refresh_not_current` changed fact stays open even with a row, and only the remaining items are answered by matching row presence.
  The row kind still admits only `still_rejected` and `raise`. The default empty set preserves the existing
  two-argument behavior; unknown/malformed subjects and unrelated IDs stay open without a matching row.
  This pure function does not derive supersession or read a knowledge tree.

### Conventions

- `rows_by_subject` maps each history-row subject of the leaf to its row ID: the same shape MIK-R30's and
  MIK-R10's predicates take, for L09's gate.
- No prose is evaluated anywhere: `reconsider_when` is only copied into facts and the question (packet
  Exclusions).

### Invariants And Boundaries

- **Pure helper and production gate are distinct.** Worklist construction derives supersession from K_B and K_C and skips superseded decisions. The pure `reconsideration_item_open` retains its optional empty-set default and two-argument compatibility; it does not derive candidate state. Production registration instead calls `reconsideration_row_open(item, GateContext)`, forwarding candidate knowledge, opened code and the row map to `reconsideration_gate_reason`. That owner derives candidate supersession, closes a superseded decision, and reobserves `refresh_not_current` targets (or accepts exact restoration to the base target) before passing remaining changes and the superseded set to the pure helper. The former no-context-wiring/row-map-only production account is retired. Source-defined tests are evidence of their asserted controls, not a fresh execution grade.
- **A decision target never triggers (one hop).** No trigger here names a decision; the registrant skips a
  `DEC-` target (rule 3).
- **Unconverted memory reads are unchanged.** Nothing reads this module on an unconverted leaf, which gets no
  worklist and no knowledge write.

### Todos

- **Current gate:** `reconsideration_gate_reason` uses candidate knowledge and opened code as well as rows; a still-stale refreshed target remains open despite a row. The historical L09 direct two-argument gate adapter is superseded, not current wiring.

`route_absent` and `refresh_not_current` extend the trigger vocabulary without extending `REFRESHED_TRIGGERS`. The shared `link_target_key` also supplies ordinary link-target subjects. Predicate priority matters: supplied supersession closes first, a remaining `refresh_not_current` fact stays open despite a row, and ordinary matching-row satisfaction applies only afterward.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R14@v2` of task
`260928_maintained-invariant-knowledge` and its leaf document `14_reconsideration-surfacing.json` (rulings
2026-09-30T04:37:56 to 11:53:13); they live outside the code and memory repositories, so they are named here and
not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References













### Cross-Repo References

No meaningful cross-repo references found: the module defines names only.

No cross-repo boundary is crossed by this file.


## Requalified checked-source evidence

- The module docstring: the subject, the triggers, the rows and the one satisfying rule. [1]

- The row kind, the subject parser and the item kind are registered with MIK-R14 as owner. [10]

- The stored predicate agrees with `satisfiedBy` on the answered item. [11]

- The kind and the two row dispositions. [2]

- The history-row dispositions that count as a change of the row's subject. [3]

- The five triggers, and the three a `still_rejected` answer refreshes. [4]

- The subject pattern over the shared decision ID pattern. [5]

- The subject spelled and parsed. [6]

- One question per subject and leaf. [7]

- The one spelling of a link target, compared before a refresh (N1). [8]

- The pure stored-item rule closes matching rows or supplied superseded IDs; empty default preserves two-argument behavior. [9]

- The row kind, the subject parser and the item kind are registered with MIK-R14 as owner. [10]
- The stored predicate agrees with `satisfiedBy` on the answered item. [11]



- A candidate successor suppresses the base decision and lists its ID; the stored rule requires supplied context. [12]

- Without a successor the changed target still raises. [13]

- An unrelated candidate decision suppresses nothing and raises no item itself. [14]



- The closeout gate recomputes its worklist and reads no earlier persisted document. [15]

- Direct landing computes its worklist over exact sides before judging. [16]

- The registered reconsideration gate forwards candidate knowledge, opened code and rows to the candidate-aware owner; only its final remaining-change check uses the pure helper. [17]

### Cross-Repo References

## Candidate-aware succession evidence

Inspected source assertions, not a fresh Curator test run or deployment of the
checked leaf repair to the serving build.

- An explicitly supplied superseded set closes a stored item without a row; the empty default preserves row-based compatibility. [18]

- Supersession, stale refresh and ordinary row satisfaction have explicit priority in the pure predicate. [19]
