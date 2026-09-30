# mcp/src/agents_remember/models/knowledge_files/decisions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/decisions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:13:48+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**MIK-R13's content rules for decision records, and the reads they make possible, as pure functions over one
record.** The shape (`ar-decision/v1`, `records.DecisionRecord`) is MIK-R21 rule 4; this module adds what a
well-formed shape can still get wrong. The validator (`memory_quality/knowledge_validator/rules_decisions.py`)
refuses on these functions, and every reader applies the same reading: the reader (MIK-R29, L29) and the
reconsideration surfacing (MIK-R14, L14) take `governs_links`, `reconsider_links`, `superseded_by` and
`derived_status` from here.

## Code Commentary

### Logic

- **Alternatives (rule 1).** `alternative_problems` reports fewer than `MINIMUM_ALTERNATIVES` (2) alternatives and
  any count of `chosen` other than one, naming the chosen indexes ("chosen: none", "chosen: 0, 1").
  `reconsider_when_problems` reports every `rejected` or `deferred` alternative (`RECONSIDERABLE`) whose
  `reconsider_when` is absent, at field `alternatives.<i>.reconsider_when`. A blank value never parses (the model
  refuses it), so only absence is checked here. The prose is **never evaluated**.
- **`reconsider_on` indexes (rule 3).** `reconsider_link_problems` checks each `reconsider_on` link's `alternative`:
  out of range ("the decision has N (indexes 0 to N-1)") or pointing at a `chosen` alternative is a problem, at
  `links.<i>.alternative`. The index is the **authored order** of `alternatives`, which the canonical formatter
  keeps (it does not sort alternatives). Refusing a link to the chosen alternative is ruling 01:45:56 Q2.
- `content_problems` concatenates the three refusing checks; the validator registers each check as its own rule
  instead, so today nothing in the tree calls it.
- **Governs (rule 3).** `GOVERNS_RELATIONS` is `explains`, `constrains` and `motivated_change_to`; `governs_links`
  returns those links: the records, routes, anchors and requirements the decision is read from.
- **`reconsider_links`** returns one `ReconsiderLink` per `reconsider_on` link that names an existing rejected or
  deferred alternative, with the alternative, the link and its index; `subject` is MIK-R14's worklist subject
  `reconsider:<DEC-ID>#<index>`.
- **Superseded is derived (rule 2).** `DecisionStatus` cannot spell `superseded`. `superseded_by(records)` maps each
  decision ID to the sorted IDs of the decisions whose `supersedes` name it; `derived_status(record, superseding)`
  returns `superseded` when that map names the record, else its stored status (`DerivedDecisionStatus`).
  `stored_superseded_fields(document)` reads a **raw** document and names where it stores `superseded` (`status`
  or `alternatives.<i>.status`), because such a document does not parse.

### Conventions

- Problems are `ContentProblem(field, message)`; the validator turns each into a `Finding` at the record's path.
- The module lives in `models` so the validator (`memory_quality`) and readers above it share one reading.

### Invariants And Boundaries

- **A decision has at least two alternatives and exactly one chosen.** Realized by `alternative_problems`
  (refused through `R13.1-alternatives`); proved by `test_alternative_counts_and_the_one_chosen_are_refused_by_rule`.
- **Every rejected or deferred alternative says when to reconsider.** Realized by `reconsider_when_problems`
  (`R13.1-reconsider-when`); proved by `test_a_rejected_or_deferred_alternative_without_reconsider_when_is_refused`.
- **Superseded is derived, never stored.** Realized by the status literal, `stored_superseded_fields`,
  `superseded_by` and `derived_status`; proved by `test_a_stored_superseded_status_is_refused_naming_the_field` and
  `test_superseded_is_derived_and_reconsider_links_carry_their_subject`.
- Every `reconsider_on` subject names a real rejected or deferred alternative (`reconsider_links` skips any other,
  and the validator refuses it).
- `reconsider_when` is prose for people; nothing reads it. A decision comes back up only through its
  `reconsider_on` links (MIK-R14, packet Exclusions).

### Todos

- **L14 (ruling 01:45:56 Q6, review F1): resolved by L14.** An update that reorders `alternatives` would silently
  re-point existing `reconsider_on` indexes; MIK-R14's validator rule `R14.1-linked-alternative-order`
  (`memory_quality/knowledge_validator/rules_reconsideration.py`) now refuses a linked alternative moved to another
  index against every comparison base, following alternatives by option text (a move combined with a reword is a
  recorded limit, ruling 2026-09-30T04:37:56 Q4). L14's worklist and writer read these links through
  `reconsider_links`, `superseded_by` and `derived_status`.
- **L29 (ruling 01:45:56 Q4):** packet rule 6 (reads show the chosen and rejected alternatives with their reasons
  and `reconsider_when`, and a derived `superseded`) is the reader's, using `governs_links`, `superseded_by` and
  `derived_status`.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R13@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`13_decision-records-with-rejected-alternatives.json`), MIK-R21 rules 4 and 6 for the record and requirement-reference
shapes, and the coordination-root note Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`,
section 4.5); they live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The content rules and the derived reads.

| Finding | Anchor | Source |
| --- | --- | --- |
| The governs relations, the reconsiderable statuses and the minimum count. | `GOVERNS_RELATIONS`; `RECONSIDERABLE`; `MINIMUM_ALTERNATIVES` | mcp/src/agents_remember/models/knowledge_files/decisions.py:36-36; mcp/src/agents_remember/models/knowledge_files/decisions.py:38-38; mcp/src/agents_remember/models/knowledge_files/decisions.py:40-40 |
| A `reconsider_on` link with the alternative it reopens and MIK-R14's subject. | `ReconsiderLink` | mcp/src/agents_remember/models/knowledge_files/decisions.py:53-68 |
| At least two alternatives, exactly one chosen. | `alternative_problems` | mcp/src/agents_remember/models/knowledge_files/decisions.py:71-93 |
| Every rejected or deferred alternative carries `reconsider_when`. | `reconsider_when_problems` | mcp/src/agents_remember/models/knowledge_files/decisions.py:96-107 |
| A `reconsider_on` index must exist and name a rejected or deferred alternative. | `reconsider_link_problems` | mcp/src/agents_remember/models/knowledge_files/decisions.py:110-137 |
| The three refusing checks together. | `content_problems` | mcp/src/agents_remember/models/knowledge_files/decisions.py:140-147 |
| The links the decision is read from, and the reconsider links with their subjects. | `governs_links`; `reconsider_links` | mcp/src/agents_remember/models/knowledge_files/decisions.py:150-153; mcp/src/agents_remember/models/knowledge_files/decisions.py:156-167 |
| Superseded is derived from later decisions' `supersedes`. | `superseded_by`; `derived_status` | mcp/src/agents_remember/models/knowledge_files/decisions.py:170-177; mcp/src/agents_remember/models/knowledge_files/decisions.py:180-185 |
| Where a raw document stores `superseded`. | `stored_superseded_fields` | mcp/src/agents_remember/models/knowledge_files/decisions.py:188-196 |
| The shape: the stored status literal and the decision record. | `DecisionStatus`; `DecisionRecord` | mcp/src/agents_remember/models/knowledge_files/records.py:53-53; mcp/src/agents_remember/models/knowledge_files/records.py:172-193 |

## Cross-Repo References

No meaningful cross-repo references found: the functions read one record or one raw document.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): this card's source is unchanged. **A forward reference to L14 is resolved in the Todos:** MIK-R14 adds the validator rule `R14.1-linked-alternative-order` (index stability, L13's carried Q6/F1) and reports `reconsider_on` requirement endpoints in the worklist's `reconsideration.links` summary (Q5/F2, partly: commit routes still resolve none, and the reads stay with L29). The installed fixer only normalised ranges here. No verification stamp was advanced.
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): created this card for the new file MIK-R13 adds, recording rulings 01:45:56 Q2, Q4 and Q6. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
