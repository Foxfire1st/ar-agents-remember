# mcp/src/agents_remember/application/knowledge_writer/worklist_checks.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Keep an ordinary leaf writer's new history judgments consistent with the persisted worklist before anything is published. The module supplies shape checks and same-run refusals; it does not compute a replacement worklist, decide an invariant's meaning, publish questions, or write memory.

## Code Commentary

### Input boundary

`worklist_shape_problem` names a missing worklist and asks for `memory_quality_check`. It rejects an unreadable top-level items population and the consumed malformed item/facts/record/collection shapes. This is a bounded validation of the fields this module consumes, not a claim that it validates every field of the full worklist schema. A present base revision must be an actual integer, not a Boolean.

The writer checks that boundary before virtual authoring for a leaf. `worklist_problems` applies the further checks only to leaf owners; wave/crossing owners are not required to supply a leaf worklist. It derives valid subjects from item subjects, unexplained-row subjects and membership-invariant aliases. It never guesses a subject for an absent item.

### Subject admission

A non-raise `still_rejected`, `planned:` or `hunk:` request must answer an existing worklist subject. An unmatched request names the subject and the recompute-or-correct remedy. Handles authored by the same document are resolved through the authoring operation's handle map.

A genuinely new row about a record whose origin names this leaf is refused when no worklist subject names it. A subject already held in this leaf's trusted pre-authoring history may instead renew its existing row without that worklist subject. `_prior_own_subjects` reads immutable `MemoryState.files`, not the candidate rows already authored into mutable documents; checking the latter would let a new row authorize itself. `raise` rows retain their existing exemption, while their question/publication authority stays with the other owners.

Only exact owner/attempt paths accepted by `owner_history_attempt` are parsed through `parse_history_document`; the parsed history must be a leaf history with the same owner ID. Malformed or undecodable histories grant no exception and remain subject to normal validation. The prior-subject set is collected once outside the row loop. This is neither foreign-history permission nor permission to rewrite the worklist, waive the whole-history after-anchor check, or use candidate source as a live leaf producer. Missing/unreadable worklists still refuse before this eligibility test.

### Governing-row check

Only the history rows produced by this authoring operation are tested here. For each such row, `_hidden_change` walks **all** worklist items with that subject. Touched and stale invariant items use the shared changed-record predicate with their recorded base revision and the virtual candidate record revision. A reached-family item uses the shared family predicate when `reachedBy` includes `guarantee-changed`.

A matching item that supplies no refusing comparison does not terminate the walk. In particular, an earlier stale item without a base revision cannot hide a later touched item's changed-record comparison. The first real violation is returned with the instruction to name the `changed` row again. Row-model validation errors encountered here are left to normal row authoring to report; that catch is not blanket suppression of arbitrary failures.

The public writer gathers these problems after virtual authoring/carry/render checks and before the output is written. These same-run refusals supplement the gate and publication validator; they do not replace their separate comparison and closed-history obligations.

### Boundaries

- Persisted worklist facts are inputs, not permission to run another producer or fabricate item IDs.
- A valid effect/reason must still be authored by the Curator; this module judges neither semantic truth nor family membership.
- Question publication, storage rollback, anchor resolution and requirement endpoints have separate owners.
- The source fixtures below express regression assertions. This card records source inspection, not a new execution result or independent CODE/MEMORY acceptance.

## Evidence

No Domain Documentation entries are configured in `system/sources.md`. These are repository-local implementation and fixture facts; the governing requirement is MIK-R54@v1 rule1.

- Missing or malformed consumed worklist shapes receive a named compute/recompute refusal. [1]
- Item scalar types, actual integer base revisions and consumed collection shapes are checked without claiming full-schema validation. [2]
- Own-origin records need a worklist subject for a genuinely new judgment; trusted pre-operation same-owner history permits existing-row renewal without authorizing candidate-created or foreign rows. [3]

- Renewal eligibility comes from parseable pre-authoring own-leaf history bytes; current-operation rows, foreign history and unreadable documents grant none. [10]

- Only newly authored history rows are passed through the same-run governing-row check. [4]
- Every matching stale/touched/family item is examined until a genuine shared-predicate violation is found. [5]
- The writer performs leaf shape admission and collects worklist problems after virtual authoring, before publication. [6]
- The retained CLI fixture orders both stale/touched items and then reverses them; each refused disposition preserves both current memory bytes and the closed attempt. [7]
- The family fixture requires refusal of no_impact and assigned judgments over a changed guarantee. [8]
- A leaf without a persisted worklist is refused with memory_quality_check guidance. [9]
