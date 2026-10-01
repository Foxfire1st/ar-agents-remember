# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_reconsideration.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R14@v2` of task
`260928_maintained-invariant-knowledge` and the leaf documents `13_decision-records-with-rejected-alternatives.json`
and `14_reconsideration-surfacing.json`; they live outside the code and memory repositories, so they are named here and
not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: why a reorder would retarget a link, and how an alternative is followed. [1]
- Options, linked indexes and the raw decision files of a tree. [2]
- Moves followed from both sides by unique option text. [3]
- One refusing finding per move, against every base. [4]
- The rule registered on import. [5]
- Swap refused twice; reword and append pass; moves into a linked index refused from either side. [6]

### Cross-Repo References

No meaningful cross-repo references found: the rule reads the validation context's trees only.

No cross-repo boundary is crossed by this file.
