# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_reconsideration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/rules_reconsideration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:05:38+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R14's guard on `reconsider_on` links, in the validator's one registry (MIK-R22 rule 9).** A `reconsider_on`
link addresses its alternative by position (`alternative`, subject `reconsider:<DEC-ID>#<index>`), so reordering a
decision's alternatives would silently retarget the link, the worklist subject and every history row about it.
Importing the module registers one refusing rule, `R14.1-linked-alternative-order`; `validator.py` imports it next to
the other rule modules, so every place the validator runs (the writer, `validate_tree`, `require_valid_commit`, the
managed sync, `knowledge-validate`) refuses such a reorder. This is L13's carried decision on link stability (ruling
2026-09-30T01:45:56: "refuse a reorder that changes a linked index").

## Code Commentary

### Logic

- `_decisions` reads every decision file under `knowledge/decisions/` as **raw JSON** (`_DECISION_DIRECTORY`), on the
  candidate and on each comparison base, keyed by `id`; a file that is not JSON is skipped, so a base the shape rule
  would not parse is compared as far as it can be read. `_options` lists each alternative's `option` text and
  `_linked` the indexes a `reconsider_on` link addresses.
- `moved_linked_alternatives(before, after)` follows alternatives by their `option` text. A linked index on either
  side (K_B or K_C) whose option appears at another index on the other side has moved; so has an alternative moved
  **into** a linked index (the second loop, over `_linked(after)`, review F6). An option that is not unique on a
  side names no one alternative and is not followed. It returns `(option, index before, index after)` per move.
- `check_linked_alternative_order` runs only when there is a base; for each parsed decision present on the candidate
  and a base, it yields one finding per move at the decision's `alternatives` field: "alternative '…' moved from
  index 1 to 2, and a reconsider_on link addresses an alternative by its index …; keep linked alternatives at their
  index and append new ones after them".

### Conventions

- The rule is refusing and sets no `writer_reports`, so the writer refuses exactly as a commit route does.
- Its `ValidationRule` cites "MIK-R14 rule 3 (L13 carried decision: link stability)".

### Invariants And Boundaries

- **A linked alternative cannot be reordered to another index.** Candidate invariant. Realized by
  `moved_linked_alternatives` and `R14.1-linked-alternative-order`; proved by
  `test_a_reorder_of_linked_alternatives_is_refused` (a swap is refused twice; a reword in place and an append pass;
  an unlinked alternative moved into a linked index is refused; a link only K_C adds, on an alternative moved into
  its index, is refused once) and on real data by `reorder-both-builds.txt`: the lifted D18 with alternatives 1 and 2
  swapped passes on the base build and is refused twice on the L14 build (review F5, re-run on a clean scratch line;
  note R6-4: that base build is the pre-L14 scratch at `31d761a2`).
- **An alternative edited in place keeps its links.** A reworded option stays at its index, so its links still mean
  it; appended alternatives never move a linked one.
- **Nothing changes until decisions are authored on a converted line.** The validator runs only over converted memory
  (MIK-R22 rule 8), and the conversion writes no decisions.

### Todos

- **Recorded limit (ruling 04:37:56 Q4):** the guard follows alternatives by option text. A move combined with a
  reword of the moved option is not caught, and duplicate option texts are not followed. Binding links to a content
  hash would change the L21 link shape and was not taken.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R14@v2` of task
`260928_maintained-invariant-knowledge` and the leaf documents `13_decision-records-with-rejected-alternatives.json`
and `14_reconsideration-surfacing.json`; they live outside the code and memory repositories, so they are named here and
not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: why a reorder would retarget a link, and how an alternative is followed. | "Reordering a decision's alternatives" | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_reconsideration.py:1-17 |
| Options, linked indexes and the raw decision files of a tree. | `_options`; `_linked`; `_decisions` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_reconsideration.py:39-46; mcp/src/agents_remember/memory_quality/knowledge_validator/rules_reconsideration.py:49-57; mcp/src/agents_remember/memory_quality/knowledge_validator/rules_reconsideration.py:60-71 |
| Moves followed from both sides by unique option text. | `moved_linked_alternatives` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_reconsideration.py:74-104 |
| One refusing finding per move, against every base. | `check_linked_alternative_order` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_reconsideration.py:107-129 |
| The rule registered on import. | `RECONSIDERATION_RULES` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_reconsideration.py:132-142 |
| Swap refused twice; reword and append pass; moves into a linked index refused from either side. | `test_a_reorder_of_linked_alternatives_is_refused` | mcp/tests/test_reconsideration_surfacing.py:561-601 |

## Cross-Repo References

No meaningful cross-repo references found: the rule reads the validation context's trees only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:05:38+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): created this card for the new file MIK-R14 adds, recording L13's carried decision (01:45:56), the Q4 recorded limit (04:37:56), review F5 and F6 (05:31:11) and note R6-4 (11:53:13). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
